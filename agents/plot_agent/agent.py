import os
import re


from .prompt import ERROR_PROMPT, INITIAL_SYSTEM_PROMPT, INITIAL_USER_PROMPT, VIS_SYSTEM_PROMPT, VIS_USER_PROMPT, ZERO_SHOT_COT_PROMPT
from agents.openai_chatComplete import completion_with_backoff
from agents.utils import fill_in_placeholders, get_error_message, is_run_code_success, run_code
from agents.utils import print_filesys_struture
from agents.utils import change_directory


class PlotAgent():


    def __init__(self, config, query, data_information=None):
        self.chat_history = []
        self.workspace = config['workspace']
        self.query = query
        self.data_information = data_information

    def generate(self, user_prompt, model_type, query_type, file_name):

        workspace_structure = print_filesys_struture(self.workspace)
        
        information = {
            'workspace_structure': workspace_structure,
            'file_name': file_name,
            'query': user_prompt
        }

        if query_type == 'initial':
            messages = []
            messages.append({"role": "system", "content": fill_in_placeholders(INITIAL_SYSTEM_PROMPT, information)})
            messages.append({"role": "user", "content": fill_in_placeholders(INITIAL_USER_PROMPT, information)})
            print(messages)
        else:
            messages = []
            messages.append({"role": "system", "content": fill_in_placeholders(VIS_SYSTEM_PROMPT, information)})
            messages.append({"role": "user", "content": fill_in_placeholders(VIS_USER_PROMPT, information)})
            print(messages)

        self.chat_history = self.chat_history + messages
        return completion_with_backoff(messages, model_type)

    def get_code(self, response):

        all_python_code_blocks_pattern = re.compile(r'```python\s*([\s\S]+?)\s*```', re.MULTILINE)


        all_code_blocks = all_python_code_blocks_pattern.findall(response)
        all_code_blocks_combined = '\n'.join(all_code_blocks)
        return all_code_blocks_combined
    def get_code2(self, response,file_name):

        all_python_code_blocks_pattern = re.compile(r'```\s*([\s\S]+?)\s*```', re.MULTILINE)


        all_code_blocks = all_python_code_blocks_pattern.findall(response)
        all_code_blocks_combined = '\n'.join(all_code_blocks)
        if all_code_blocks_combined == '':

            response_lines = response.split('\n')
            code_lines = []
            code_start = False
            for line in response_lines:
                if line.find('import') == 0 or code_start:
                    code_lines.append(line)
                    code_start = True
                if code_start and line.find(file_name)!=-1 and line.find('(') !=-1 and line.find(')')!=-1 and line.find('(') < line.find(file_name)< line.find(')'): #要有文件名，同时要有函数调用

                    return '\n'.join(code_lines)
        return all_code_blocks_combined


    def run(self, query, model_type, query_type, file_name):
        try_count = 0
        image_file = file_name
        result = self.generate(query, model_type=model_type, query_type=query_type, file_name=file_name)
        while try_count < 4:
            
            if not isinstance(result, str):  # モデル失敗 (None など)
                safe_code = ''
                return 'MODEL CALL FAILED', safe_code
            if model_type != 'gpt-4':
                code = self.get_code(result)
                if code.strip() == '':
                    code = self.get_code2(result,image_file) #第二次尝试获得代码
                    if code.strip() == '':
                        code = result  #只能用原始回答
                        if code.strip() == '' and try_count == 0: #有可能是因为没有extend query写好了代码，所以他不写代码
                            code = self.get_code(query)
            else:
                code = self.get_code(result)
            self.chat_history.append({"role": "assistant", "content": result if result.strip() != '' else ''})

            # Banned library detection: if code uses disallowed libs, request regeneration
            banned_patterns = [
                r"import\s+seaborn",
                r"from\s+seaborn\s+import",
                r"import\s+plotly",
                r"from\s+plotly\s+import",
                r"import\s+altair",
                r"from\s+altair\s+import",
                r"import\s+bokeh",
                r"from\s+bokeh\s+import",
                r"hvplot",
                r"holoviews",
                r"pandas\.DataFrame\.plot\(",
            ]
            banned_hit = False
            for pat in banned_patterns:
                if re.search(pat, code):
                    banned_hit = True
                    break
            if banned_hit:
                reinforce_msg = (
                    "前回のコードに禁止ライブラリ (seaborn/plotly/bokeh/altair/hvplot/holoviews/DataFrame.plot) が含まれていました。"
                    "Matplotlib のみを使用し、スタイルや色設定も Matplotlib の API だけで再実装してください。"
                    "plt.show() は使わず、必ず plt.savefig('" + image_file + "') を最後に呼び出してください。"
                    "完全な修正版コードのみを再掲してください。"
                )
                self.chat_history.append({
                    "role": "user",
                    "content": reinforce_msg,
                })
                try_count += 1
                result = completion_with_backoff(self.chat_history, model_type=model_type)
                continue

            # sanitize code for headless execution: no interactive windows, ensure backend and save
            code = self._sanitize_code_for_headless(code, image_file)


            file_name = f'code_action_{model_type}_{query_type}_{try_count}.py'
            with open(os.path.join(self.workspace, file_name), 'w') as f:
                f.write(code)
            error = None
            log = run_code(self.workspace, file_name)

            if is_run_code_success(log):
                if print_filesys_struture(self.workspace).find('.png') == -1:
                    log = log + '\n' + 'No plot generated.'
                    
                    self.chat_history.append({"role": "user", "content": fill_in_placeholders(ERROR_PROMPT,
                                                                                          {'error_message': f'No plot generated. When you complete a plot, remember to save it to a png file. The file name should be """{image_file}""".',
                                                                                           'data_information': self.data_information})})
                    try_count += 1
                    result = completion_with_backoff(self.chat_history, model_type=model_type)


                else:
                    return log, code

            else:
                error = get_error_message(log) if error is None else error
                # TODO error prompt
                self.chat_history.append({"role": "user", "content": fill_in_placeholders(ERROR_PROMPT,
                                                                                          {'error_message': error,
                                                                                           'data_information': self.data_information})})
                try_count += 1
                result = completion_with_backoff(self.chat_history, model_type=model_type)
                print(result)

        return log, ''

    def run_initial(self, model_type, file_name):
        print('========Plot AGENT Expert RUN========')
        self.chat_history = []
        log, code = self.run(self.query, model_type, 'initial', file_name)
        return log, code

    def run_vis(self, model_type, file_name):
        print('========Plot AGENT Novice RUN========')
        self.chat_history = []
        log, code = self.run(self.query, model_type, 'vis_refined', file_name)
        return log, code

    def run_one_time(self, model_type, file_name,query_type='novice',no_sysprompt=False):
        
        print('========Plot AGENT Novice RUN========')
        message = []
        workspace_structure = print_filesys_struture(self.workspace)
        
        information = {
            'workspace_structure': workspace_structure,
            'file_name': file_name,
            'query': self.query
        }
        if no_sysprompt:
            message.append({"role": "system", "content": ''''''})
        message.append({"role": "user", "content": fill_in_placeholders(INITIAL_USER_PROMPT, information)})
        result = completion_with_backoff(message, model_type)
        if model_type != 'gpt-4':
            code = self.get_code(result)
            if code == '':
                code = self.get_code2(result,file_name)
                if code == '':
                    code = result
        else:
            code = self.get_code(result)


        # sanitize code and write
        code = self._sanitize_code_for_headless(code, file_name)
        file_name = f'code_action_{model_type}_{query_type}_0.py'
        with open(os.path.join(self.workspace, file_name), 'w') as f:
            f.write(code)
        log = run_code(self.workspace, file_name)
        return log, code
    def run_one_time_zero_shot_COT(self, model_type, file_name,query_type='novice',no_sysprompt=False):
        
        print('========Plot AGENT Novice RUN========')
        message = []
        workspace_structure = print_filesys_struture(self.workspace)
        
        information = {
            'workspace_structure': workspace_structure,
            'file_name': file_name,
            'query': self.query
        }
        message.append({"role": "system", "content": ''''''})
        message.append({"role": "user", "content": fill_in_placeholders(ZERO_SHOT_COT_PROMPT, information)})
        result = completion_with_backoff(message, model_type)
        if model_type != 'gpt-4':
            code = self.get_code(result)
            if code == '':
                code = self.get_code2(result,file_name)
                if code == '':
                    code = result
        else:
            code = self.get_code(result)

        # sanitize code and write
        code = self._sanitize_code_for_headless(code, file_name)
        file_name = f'code_action_{model_type}_{query_type}_0.py'
        with open(os.path.join(self.workspace, file_name), 'w') as f:
            f.write(code)
        log = run_code(self.workspace, file_name)
        return log, code

    def _sanitize_code_for_headless(self, code: str, image_file: str) -> str:
        """Ensure generated code does not attempt to open GUI windows and saves output.

        - Force non-interactive backend (Agg)
        - Remove plt.show()/figure.show() calls
        - If no savefig present, append a savefig with the target image file
        """
        try:
            # ensure backend before pyplot import if possible
            if 'matplotlib.use(' not in code:
                code = "import matplotlib\nmatplotlib.use('Agg')\n" + code

            # comment out any lingering forbidden plotting imports (defensive)
            code = re.sub(r'^(from|import)\s+seaborn.*$', r'# \g<0>  # removed (seaborn forbidden)', code, flags=re.MULTILINE)
            code = re.sub(r'^(from|import)\s+plotly.*$', r'# \g<0>  # removed (plotly forbidden)', code, flags=re.MULTILINE)
            code = re.sub(r'^(from|import)\s+altair.*$', r'# \g<0>  # removed (altair forbidden)', code, flags=re.MULTILINE)
            code = re.sub(r'^(from|import)\s+bokeh.*$', r'# \g<0>  # removed (bokeh forbidden)', code, flags=re.MULTILINE)
            code = re.sub(r'^.*hvplot.*$', r'# \g<0>  # removed (hvplot forbidden)', code, flags=re.MULTILINE)
            code = re.sub(r'^.*holoviews.*$', r'# \g<0>  # removed (holoviews forbidden)', code, flags=re.MULTILINE)
            code = re.sub(r'pandas\.DataFrame\.plot\(', '# DataFrame.plot removed; rewrite below with pure Matplotlib\n# pandas.DataFrame.plot(', code)

            # strip plt.show(...) and any fig.show(...)
            code = re.sub(r"plt\s*\.\s*show\s*\([^)]*\)\s*;?", "", code)
            code = re.sub(r"([A-Za-z_][A-Za-z0-9_]*)\s*\.\s*show\s*\([^)]*\)\s*;?", "", code)
            code = re.sub(r"plt\s*\.\s*pause\s*\([^)]*\)\s*;?", "", code)
            # Turn off interactive mode if turned on
            code = re.sub(r"plt\s*\.\s*ion\s*\(\s*\)\s*", "plt.ioff()\n", code)

            # ensure savefig
            if image_file and 'savefig' not in code:
                if 'import matplotlib.pyplot as plt' not in code:
                    code += "\nimport matplotlib.pyplot as plt"
                code += f"\nplt.savefig('{image_file}')\n"
        except Exception:
            # Fail-safe: return original code if anything goes wrong
            return code
        return code
