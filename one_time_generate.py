import json

from tqdm import tqdm
from agents.plot_agent import PlotAgent
import logging
import os
from agents.utils import is_run_code_success, run_code
import argparse


def mainworkflow(_expert_unused, simple_instruction, workspace='./workspace', model_type='gpt-3.5-turbo', no_sysprompt=False):

    
    config = {'workspace': workspace}
    # GPT-3.5-turbo Plot Agent
    # Initial plotting
    action_agent = PlotAgent(config, simple_instruction)
    logging.info('=========Plotting=========')
    novice_35_log, novice_35_code = action_agent.run_one_time(model_type, 'novice.png',no_sysprompt=no_sysprompt)
    logging.info(novice_35_log)
    logging.info('=========Original Code=========')
    logging.info(novice_35_code)
    


def check_refined_code_executable(refined_code, model_type, query_type, workspace):
    file_name = f'code_action_{model_type}_{query_type}_refined.py'
    with open(os.path.join(workspace, file_name), 'w', encoding='utf-8') as f1:
        f1.write(refined_code)
    log = run_code(workspace, file_name)

    return is_run_code_success(log)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--workspace', type=str, default='./workspace')
    parser.add_argument('--model_type', type=str, default='gpt-4o-mini')
    parser.add_argument('--no_sysprompt',action='store_true')
    args = parser.parse_args()

    workspace_base = args.workspace
    # Resolve benchmark_data directory relative to this file
    script_dir = os.path.dirname(os.path.abspath(__file__))
    data_path = os.path.join(script_dir, 'benchmark_data')
    # open the json file
    with open(os.path.join(data_path, 'benchmark_instructions.json'), 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    for item in tqdm(data):
        novice_instruction = item['simple_instruction']
        expert_instruction = item['expert_instruction']
        example_id = item['id']
        directory_path = f'{workspace_base}/example_{example_id}'

        # Check if the directory already exists
        if not os.path.exists(directory_path):
            # If it doesn't exist, create the directory (including parent workspace folder)
            os.makedirs(directory_path, exist_ok=True)
            print(f"Directory '{directory_path}' created successfully.")
            input_path = os.path.join(data_path, 'data', str(example_id))
            if os.path.exists(input_path):
                #全部copy到f"Directory '{directory_path}'
                os.system(f'cp -r {input_path}/* {directory_path}')
        else:
            print(f"Directory '{directory_path}' already exists.")
            continue

        logging.basicConfig(level=logging.INFO, filename=f'{directory_path}/workflow.log', filemode='w', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        mainworkflow(expert_instruction,novice_instruction, workspace=directory_path,model_type=args.model_type,no_sysprompt=args.no_sysprompt)
