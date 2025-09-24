import os
import logging
import openai  # needed for exception classes

try:
    # optional: load .env if python-dotenv is installed
    from dotenv import load_dotenv  # type: ignore
    load_dotenv()
except ImportError:
    # dotenv is optional; ignore if not installed
    pass

# Temperature used across calls
temperature = float(os.getenv("OPENAI_TEMPERATURE", "0"))

# Plain OpenAI (api.openai.com) fallback
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_BASE_URL = os.getenv("OPENAI_BASE_URL", "https://api.openai.com/v1")

# Azure OpenAI settings
AZURE_OPENAI_ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT")
AZURE_OPENAI_API_KEY = os.getenv("AZURE_OPENAI_API_KEY")
AZURE_OPENAI_API_VERSION = os.getenv("AZURE_OPENAI_API_VERSION", "2024-10-01-preview")

# Azure AI Inference (serverless) settings for multi-provider models
AZURE_INFERENCE_ENDPOINT = os.getenv("AZURE_INFERENCE_ENDPOINT")
AZURE_INFERENCE_API_KEY = os.getenv("AZURE_INFERENCE_API_KEY")


def is_azure_configured() -> bool:
    return bool(AZURE_OPENAI_ENDPOINT and AZURE_OPENAI_API_KEY)


def is_azure_inference_configured() -> bool:
    return bool(AZURE_INFERENCE_ENDPOINT and AZURE_INFERENCE_API_KEY)


def create_client():
    """
    Return a configured OpenAI client instance.

    - If Azure env vars are present, returns AzureOpenAI client.
    - Else if OPENAI_API_KEY is present, returns vanilla OpenAI client (with optional OPENAI_BASE_URL).
    - Else raises RuntimeError.
    """
    # Deferred import to avoid hard dependency during analysis
    if is_azure_inference_configured():
        # Azure AI Inference serverless, supports many models (o-series, DeepSeek, Grok, etc.)
        from openai import OpenAI  # type: ignore
        return OpenAI(
            api_key=AZURE_INFERENCE_API_KEY,
            base_url=AZURE_INFERENCE_ENDPOINT,
        )
    elif is_azure_configured():
        from openai import AzureOpenAI  # type: ignore
        return AzureOpenAI(
            azure_endpoint=AZURE_OPENAI_ENDPOINT,
            api_key=AZURE_OPENAI_API_KEY,
            api_version=AZURE_OPENAI_API_VERSION,
        )
    else:
        from openai import OpenAI  # type: ignore
        if not OPENAI_API_KEY:
            raise RuntimeError(
                "No credentials found. Set AZURE_OPENAI_* for Azure or OPENAI_API_KEY for OpenAI.")
        return OpenAI(api_key=OPENAI_API_KEY, base_url=OPENAI_BASE_URL)


# Backward-compat exports (kept to avoid widespread refactor)
# For legacy code paths that set globals on the SDK
API_KEY = OPENAI_API_KEY if OPENAI_API_KEY else (AZURE_OPENAI_API_KEY or "")
BASE_URL = OPENAI_BASE_URL if OPENAI_API_KEY else (AZURE_OPENAI_ENDPOINT or "")


def _uses_max_completion_tokens(model_name: str) -> bool:
    """Return True if the model likely expects 'max_completion_tokens' instead of 'max_tokens'.

    Azure/OpenAI o-series (o3, o4, o4-mini, etc.) require 'max_completion_tokens'.
    """
    if not model_name:
        return False
    m = model_name.strip().lower()
    return m.startswith("o3") or m.startswith("o4") or m == "o3" or m == "o4"


def _omit_temperature(model_name: str) -> bool:
    """Some reasoning-centric models either ignore or reject temperature.

    Omit temperature for:
    - o-series (o3, o4, o4-mini, etc.)
    - DeepSeek R1 family (e.g., deepseek-r1-0528)
    - Grok family (e.g., grok-3, grok-3-mini)
    """
    if not model_name:
        return False
    m = model_name.strip().lower()
    return (
        m.startswith("o3")
        or m.startswith("o4")
        or m.startswith("gpt-5")
        or m.startswith("deepseek")
        or m.startswith("grok")
    )


def call_chat_completions(client, *, model: str, messages, temperature: float | None = None,
                          max_new_tokens: int | None = None, extra: dict | None = None):
    """
    Thin wrapper to call chat.completions.create with model-specific params.

    - For o-series models, uses 'max_completion_tokens' when max_new_tokens is provided.
    - For others, uses 'max_tokens'.
    """
    kwargs = {
        "model": model,
        "messages": messages,
    }
    # o-seriesはtemperature未対応のため送らない
    if temperature is not None and not _omit_temperature(model):
        kwargs["temperature"] = temperature
    if max_new_tokens is not None:
        if _uses_max_completion_tokens(model):
            kwargs["max_completion_tokens"] = max_new_tokens
        else:
            kwargs["max_tokens"] = max_new_tokens
    if extra:
        kwargs.update(extra)
    return client.chat.completions.create(**kwargs)


def _use_responses_api(model_name: str) -> bool:
    """Return True if the model should be called via the Responses API.

    o-series (o3/o4/mini/pro) and gpt-5 are typically exposed via Responses API on Azure AI Inference.
    """
    if not model_name:
        return False
    m = model_name.strip().lower()
    return m.startswith("o3") or m.startswith("o4") or m.startswith("gpt-5")


def _messages_to_responses_input(messages):
    """Convert chat messages to Responses API 'input' format.

    - If content is a string, wrap as input_text
    - If content is a list with typed items, map 'text'->input_text and 'image_url'->input_image
    """
    input_items = []
    for msg in messages:
        role = msg.get("role", "user")
        content = msg.get("content", "")
        parts = []
        if isinstance(content, str):
            parts.append({"type": "input_text", "text": content})
        elif isinstance(content, list):
            for item in content:
                itype = item.get("type")
                if itype == "text":
                    parts.append({"type": "input_text", "text": item.get("text", "")})
                elif itype == "image_url":
                    image = item.get("image_url", {})
                    url = image.get("url") if isinstance(image, dict) else None
                    if url:
                        parts.append({"type": "input_image", "image_url": {"url": url}})
        else:
            parts.append({"type": "input_text", "text": str(content)})
        input_items.append({"role": role, "content": parts})
    return input_items


def complete_text(client, *, model: str, messages, temperature: float | None = None,
                  max_new_tokens: int | None = None, extra: dict | None = None) -> str:
    """Unified text generation wrapper.

    - Uses Responses API for o3/o4/gpt-5 models (max_output_tokens)
    - Uses Chat Completions for others (max_tokens or max_completion_tokens)
    Returns the primary text output as a string.
    """
    if _use_responses_api(model):
        kwargs = {"model": model, "input": _messages_to_responses_input(messages)}
        if temperature is not None and not _omit_temperature(model):
            kwargs["temperature"] = temperature
        if max_new_tokens is not None:
            kwargs["max_output_tokens"] = max_new_tokens
        if extra:
            kwargs.update(extra)
        try:
            resp = client.responses.create(**kwargs)
        except openai.BadRequestError as e:  # type: ignore[name-defined]
            # Reasoningモデル(o3/o4/gpt-5)は chat にフォールバックしない: 研究純度維持のため
            logging.error("Responses API BadRequest for %s: %s", model, e)
            return ""  # 上流で空文字扱い / 失敗判定
        except Exception as e:
            logging.error("Responses API unexpected error for %s: %s", model, e)
            return ""
        text = getattr(resp, "output_text", None)
        if text is None:
            try:
                text = resp.output[0].content[0].text  # type: ignore[attr-defined]
            except Exception:
                text = ""
        if not text:
            logging.debug("Responses API returned empty text for model %s (treated as failure)", model)
        return text if text is not None else ""
    else:
        resp = call_chat_completions(
            client,
            model=model,
            messages=messages,
            temperature=temperature,
            max_new_tokens=max_new_tokens,
            extra=extra,
        )
        return resp.choices[0].message.content