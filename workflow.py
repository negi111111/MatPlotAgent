import argparse
import json

from tqdm import tqdm
import logging
import os
from agents.query_expansion_agent import QueryExpansionAgent
from agents.plot_agent import PlotAgent
from agents.visual_refine_agent import VisualRefineAgent
from agents.utils import is_run_code_success, run_code

def mainworkflow(expert_ins, simple_ins, workspace, model_type='gpt-4o-mini', visual_refine=True):
    # Query expanding
    logging.info('=========Query Expansion AGENT=========')
    config = {'workspace': workspace}
    query_expansion_agent = QueryExpansionAgent(expert_ins, simple_ins, model_type=model_type)
    expanded_simple_instruction = query_expansion_agent.run('simple')
    logging.info('=========Expanded Simple Instruction=========')
    logging.info(expanded_simple_instruction)
    logging.info('=========Plotting=========')

    # GPT-4 Plot Agent
    # Initial plotting
    action_agent = PlotAgent(config, expanded_simple_instruction)
    logging.info('=========Novice 4 Plotting=========')
    novice_log, novice_code = action_agent.run_initial(model_type, 'novice.png')
    logging.info(novice_log)
    logging.info('=========Original Code=========')
    logging.info(novice_code)
    # Code refinement
    # code_refine_agent = CodeRefineAgent(expanded_simple_instruction, novice_4_code)
    # refined_response = code_refine_agent.run()
    # logging.info('=========Refined Code=========')
    # logging.info(refined_response)

    # Visual refinement
    # if True:
    #     # refined_code = get_code(refined_response)
    #     # if refined_code == '':
    #     #    refined_code = refined_response.strip('"""')
    #     # else:
    #     #    pass
    #     refined_code = 'print(json.load())'
    #     if check_refined_code_executable(refined_code, 'gpt-4', 'novice', config['workspace']):
    #         print('Use refined code for visual feedback')
    #         visual_refine_agent = VisualRefineAgent('novice_4.png', config, refined_code, simple_instruction)
    #         visual_feedback = visual_refine_agent.run('gpt-4', 'novice', 'novice_4_final.png')
    #         logging.info('=========Visual Feedback=========')
    #         logging.info(visual_feedback)
    #         final_instruction = refined_code + '\n\n' + visual_feedback
    #         action_agent = PlotAgent(config, final_instruction)
    #         novice_4_log, novice_4_code = action_agent.run_vis('gpt-4', 'novice_4_final.png')
    #         logging.info(novice_4_log)
    #     else:
    if visual_refine and os.path.exists(f'{workspace}/novice.png'):
        print('Use original code for visual feedback')
        visual_refine_agent = VisualRefineAgent('novice.png', config, '', simple_ins)
        visual_feedback = visual_refine_agent.run(model_type, 'novice', 'novice_final.png')
        logging.info('=========Visual Feedback=========')
        logging.info(visual_feedback)
        final_instruction = '' + '\n\n' + visual_feedback
        action_agent = PlotAgent(config, final_instruction)
        novice_log, novice_code = action_agent.run_vis(model_type, 'novice_final.png')
        logging.info(novice_log)
        # Force creation of novice_final.png even if no new image was produced
        final_path = os.path.join(workspace, 'novice_final.png')
        original_path = os.path.join(workspace, 'novice.png')
        if not os.path.exists(final_path) and os.path.exists(original_path):
            try:
                import shutil
                shutil.copy2(original_path, final_path)
                logging.info('novice_final.png was missing; copied from novice.png to ensure output consistency.')
            except OSError as e:
                logging.warning('Failed to force-generate novice_final.png: %s', e)

    # (legacy GPT-3.5-turbo path removed)


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
    parser.add_argument('--visual_refine', type=bool, default=True)
    parser.add_argument('--only_id', type=int, default=None, help='Process only the given example id')
    parser.add_argument('--limit', type=int, default=None, help='Process at most N new examples for quick runs')
    args = parser.parse_args()

    workspace_base = args.workspace
    # Resolve benchmark_data directory relative to this file
    script_dir = os.path.dirname(os.path.abspath(__file__))
    data_path = os.path.join(script_dir, 'benchmark_data')
    # open the json file
    with open(os.path.join(data_path, 'benchmark_instructions.json'), 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # Filter by only_id if specified
    if args.only_id is not None:
        data = [d for d in data if d.get('id') == args.only_id]

    processed = 0
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
            processed += 1
            logging.basicConfig(level=logging.INFO, filename=f'{directory_path}/workflow.log', filemode='w', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            mainworkflow(expert_instruction, novice_instruction, workspace=directory_path, model_type=args.model_type, visual_refine=args.visual_refine)
            if args.limit is not None and processed >= args.limit:
                print(f"Reached processing limit: {args.limit}")
                break
        else:
            print(f"Directory '{directory_path}' already exists.")
            continue
