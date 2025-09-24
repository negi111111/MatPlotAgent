import logging
import openai
from agents.config.openai import temperature, create_client, call_chat_completions, complete_text
from tenacity import (
    retry,
    stop_after_attempt,
    wait_random_exponential, stop_after_delay,
)
from models.model_config import MODEL_CONFIG


def print_chat_message(messages):
    for message in messages:
        logging.info(f"{message['role']}: {message['content']}")

@retry(wait=wait_random_exponential(min=0.02, max=1), stop=(stop_after_delay(10) | stop_after_attempt(100)))
def completion_with_backoff(messages, model_type):

    if model_type in MODEL_CONFIG.keys():

        port = MODEL_CONFIG[model_type]['port']
        model_full_path= MODEL_CONFIG[model_type]['model']
        
        # Local vLLM endpoint
        openai_api_key = "EMPTY"
        openai_api_base = f"http://localhost:{port}/v1"

        client = openai.OpenAI(
            api_key=openai_api_key,
            base_url=openai_api_base,
        )
        try:
            response = call_chat_completions(
                client,
                model=model_full_path,
                messages=messages,
                temperature=temperature,
                max_new_tokens=4096,
                extra={"timeout": 30*60},
            )
            result = response.choices[0].message
            answer = result.content
            return answer
        except KeyError:

            return None
        except openai.BadRequestError as e:

            return e

            

    else:
        # Azure/OpenAI client from config
        client = create_client()
        try:
            answer = complete_text(
                client,
                model=model_type,
                messages=messages,
                temperature=temperature,
            )
            return answer
        except KeyError:
            return None
        except openai.BadRequestError as e:
            # フォールバックは排除: BadRequest (OperationNotSupported 等) の場合は None を返し、上流で graceful fallback.
            logging.error("Model %s bad request / not supported: %s", model_type, e)
            return None


def completion_with_log(messages, model_type, enable_log=False):
    if enable_log:
        logging.info('========CHAT HISTORY========')
        print_chat_message(messages)
    response = completion_with_backoff(messages, model_type)
    if enable_log:
        logging.info('========RESPONSE========')
        logging.info(response)
        logging.info('========RESPONSE END========')
    return response


def completion_for_4v(messages, model_type):
    client = create_client()
    return complete_text(
        client,
        model=model_type,
        messages=messages,
        temperature=temperature,
    )
