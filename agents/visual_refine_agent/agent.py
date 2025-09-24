import os
import base64
import re


from .prompt import SYSTEM_PROMPT, USER_PROMPT, ERROR_PROMPT
from agents.openai_chatComplete import  completion_for_4v
from agents.utils import fill_in_placeholders
EVAL_VISION_MODEL = os.getenv("EVAL_VISION_MODEL", "gpt-4o-mini")



def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')


def get_code(response):

    all_python_code_blocks_pattern = re.compile(r'```python\s*([\s\S]+?)\s*```', re.MULTILINE)


    all_code_blocks = all_python_code_blocks_pattern.findall(response)
    all_code_blocks_combined = '\n'.join(all_code_blocks)
    return all_code_blocks_combined


class VisualRefineAgent:
    def __init__(self, plot_file, config, code, query):
        self.chat_history = []
        self.plot_file = plot_file
        self.code = code
        self.query = query
        self.workspace = config['workspace']

    def _supports_vision(self, model_name: str) -> bool:
        if not model_name:
            return False
        m = model_name.strip().lower()
        # Heuristics: 4o family and omni/vision-capable models
        return (
            '4o' in m or
            'omni' in m or
            'vision' in m or
            m.startswith('gpt-4.1')
        )

    def run(self, model_type, query_type, file_name):
        plot = os.path.join(self.workspace, self.plot_file)
        base64_image1 = encode_image(f"{plot}")

        information = {
            'query': self.query,
            'file_name': file_name,
            'code': self.code
        }

        messages = []
        messages.append({"role": "system", "content": fill_in_placeholders(SYSTEM_PROMPT, information)})
        messages.append({
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": fill_in_placeholders(USER_PROMPT, information),
                },
                {
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:image/jpeg;base64,{base64_image1}"
                    }
                },
            ]
        })
        # Use model if it supports vision; otherwise fall back to EVAL_VISION_MODEL
        chosen_model = model_type if self._supports_vision(model_type) else EVAL_VISION_MODEL
        visual_feedback = completion_for_4v(messages, chosen_model)
        return visual_feedback