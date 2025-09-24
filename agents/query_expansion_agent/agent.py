from .prompt import SYSTEM_PROMPT, EXPERT_USER_PROMPT
from agents.openai_chatComplete import completion_with_backoff, completion_with_log
from agents.utils import fill_in_placeholders, get_error_message, is_run_code_success, print_chat_message


class QueryExpansionAgent():
    def __init__(self, expert_ins, simple_ins,model_type='gpt-4'):
        self.chat_history = []
        self.expert_ins = expert_ins
        self.simple_ins = simple_ins
        self.model_type = model_type

    def run(self, query_type):
        if query_type == 'expert':
            information = {
                'query': self.expert_ins,
            }
        else:
            information = {
                'query': self.simple_ins,
            }

        messages = []
        messages.append({"role": "system", "content": fill_in_placeholders(SYSTEM_PROMPT, information)})
        messages.append({"role": "user", "content": fill_in_placeholders(EXPERT_USER_PROMPT, information)})
        expanded_query_instruction = completion_with_log(messages, self.model_type)

        # Guard: if model call failed and returned an exception object, fall back to original instruction
        if not isinstance(expanded_query_instruction, str):
            # choose appropriate original instruction
            fallback_text = self.expert_ins if query_type == 'expert' else self.simple_ins
            # Make it explicit in logs by appending a note (non-user visible unless later logged)
            return fallback_text
        return expanded_query_instruction
