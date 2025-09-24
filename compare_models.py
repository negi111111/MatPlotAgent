import os
import json
import argparse
from PIL import Image
import shutil

from workflow import mainworkflow  # reuse pipeline for each model

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(SCRIPT_DIR, "benchmark_data")

# The five required models in column order (default comparison order)
DEFAULT_MODELS = [
    "gpt-5",
    "o3-pro",
    "o4-mini",
    "grok-3",
    "DeepSeek-R1-0528",
]


def run_one_example(example_id: int, workspace: str, models: list[str]):
    # Load instructions
    with open(
        os.path.join(DATA_PATH, "benchmark_instructions.json"), "r", encoding="utf-8"
    ) as f:
        data = json.load(f)
    item = next(d for d in data if d["id"] == example_id)
    novice_instruction = item["simple_instruction"]
    expert_instruction = item["expert_instruction"]

    # Ensure ground truth path
    gt_path = os.path.join(DATA_PATH, "ground_truth", f"example_{example_id}.png")
    if not os.path.exists(gt_path):
        raise FileNotFoundError(gt_path)

    # Per model, run pipeline and collect image paths
    results = []  # each element: {model, novice, final}
    for model in models:
        model_workspace = os.path.join(workspace, f"{model}", f"example_{example_id}")
        os.makedirs(model_workspace, exist_ok=True)
        # Copy example input files into workspace (if present)
        input_path = os.path.join(DATA_PATH, "data", str(example_id))
        if os.path.exists(input_path):
            for name in os.listdir(input_path):
                src = os.path.join(input_path, name)
                dst = os.path.join(model_workspace, name)
                if os.path.isdir(src):
                    if not os.path.exists(dst):
                        shutil.copytree(src, dst)
                else:
                    if not os.path.exists(dst):
                        shutil.copy2(src, dst)
        # Run one example via mainworkflow with specified model (produces novice.png, novice_final.png)
        try:
            mainworkflow(
                expert_instruction,
                novice_instruction,
                workspace=model_workspace,
                model_type=model,
                visual_refine=True,
            )
        except (RuntimeError, OSError) as e:
            print(f"[WARN] model {model} failed: {e}")
        novice_img = os.path.join(model_workspace, "novice.png")
        final_img = os.path.join(model_workspace, "novice_final.png")
        results.append(
            {
                "model": model,
                "novice": novice_img if os.path.exists(novice_img) else None,
                "final": final_img if os.path.exists(final_img) else None,
            }
        )
    return results, gt_path


def compose_grid(results, out_path):
    # rows: [no visual feedback, with visual feedback]
    # cols: models
    cols = len(results)
    rows = 2

    # Load images; fallback to blank if missing
    def load_or_blank(path, size=None):
        if path and os.path.exists(path):
            img = Image.open(path).convert("RGBA")
            if size is not None:
                img = img.resize(size, Image.BILINEAR)
            return img
        else:
            return Image.new("RGBA", size if size else (512, 384), (255, 255, 255, 255))

    # Determine target tile size from the first available image
    sample = None
    for r in results:
        if r["novice"] and os.path.exists(r["novice"]):
            sample = Image.open(r["novice"]).convert("RGBA")
            break
        if r["final"] and os.path.exists(r["final"]):
            sample = Image.open(r["final"]).convert("RGBA")
            break
    if sample is None:
        # Fallback to a default tile size if no images are available
        sample = Image.new("RGBA", (512, 384), (255, 255, 255, 255))
    tile_w, tile_h = sample.size

    canvas_w = cols * tile_w
    canvas_h = rows * tile_h
    canvas = Image.new("RGBA", (canvas_w, canvas_h), (255, 255, 255, 255))

    # Row 0: novice
    for c, r in enumerate(results):
        img = load_or_blank(r["novice"], (tile_w, tile_h))
        canvas.paste(img, (c * tile_w, 0))

    # Row 1: final
    for c, r in enumerate(results):
        img = load_or_blank(r["final"], (tile_w, tile_h))
        canvas.paste(img, (c * tile_w, tile_h))

    # No ground-truth row per request

    # Save as PNG
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    canvas.convert("RGB").save(out_path, format="PNG")


def main():
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group(required=False)
    group.add_argument("--example_id", type=int, help="Single example id to process")
    group.add_argument(
        "--example_ids", type=int, nargs="+", help="Multiple example ids to process"
    )
    parser.add_argument(
        "--exclude_ids", type=int, nargs="+", default=None,
        help="Exclude these example ids; if neither --example_id nor --example_ids specified, process all minus excluded"
    )
    parser.add_argument("--workspace", type=str, default="./compare_workspace")
    parser.add_argument(
        "--models",
        type=str,
        nargs="*",
        default=DEFAULT_MODELS,
        help="Override models list; default 5 models required by spec",
    )
    parser.add_argument(
        "--output",
        type=str,
        default=None,
        help="Output composite path; default: <workspace>/example_<id>_compare.png",
    )
    parser.add_argument(
        "--dry_run", action="store_true", help="List target example ids and exit without running"
    )
    args = parser.parse_args()

    # Load all benchmark ids
    with open(os.path.join(DATA_PATH, "benchmark_instructions.json"), "r", encoding="utf-8") as f:
        all_data = json.load(f)
    all_ids = [d["id"] for d in all_data]

    if args.example_id is not None:
        targets = [args.example_id]
    elif args.example_ids is not None:
        targets = args.example_ids
    else:
        # No explicit targets: use all ids minus excluded
        targets = all_ids
    if args.exclude_ids:
        exclude_set = set(args.exclude_ids)
        targets = [i for i in targets if i not in exclude_set]
    targets = sorted(set(targets))

    if args.dry_run:
        print("Target example ids:", targets)
        return

    for ex_id in targets:
        results, _ = run_one_example(ex_id, args.workspace, args.models)
        out_path = args.output or os.path.join(
            args.workspace, f"example_{ex_id}_compare.png"
        )
        compose_grid(results, out_path)
        print(f"Composite saved to: {out_path}")


if __name__ == "__main__":
    main()
