## 📚 目次 (Table of Contents)

-   [📝 最近の更新サマリ](#-最近の更新サマリ-日本語)
-   [🛠 最近の技術的変更点](#-最近の技術的変更点-研究用途向け)
-   [🧪 実験プロトコル](#-実験プロトコル推奨フロー)
    -   [環境構築](#1-環境構築)
    -   [ベンチマーク指示セット](#2-ベンチマーク指示セット)
    -   [単一モデル実行](#3-単一モデル単一例)
    -   [複数モデル比較](#4-複数モデル比較パネル)
    -   [自動評価](#5-自動評価任意)
    -   [整合性 / 失敗時挙動](#6-整合性--失敗時挙動)
    -   [推奨実行順](#7-推奨実行順)
    -   [再現性メモ](#8-再現性メモ)
    -   [モデル追加手順](#9-モデル追加手順)
    -   [トラブルシューティング](#10-トラブルシューティング早見表)
-   [`simple_instruction` と `expert_instruction`](#-simple_instruction-と-expert_instruction-の違い)
-   [今後の拡張予定](#-今後追加を検討している拡張)
-   [� Introduction](#-introduction)
-   [🎉 News](#-news)
-   [✨ MatPlotAgent](#-matplotagent)
-   [🎖 MatPlotBench](#-matplotbench)
-   [⚡️ Getting Started](#️-getting-started)
-   [Evaluation Pipeline](#evaluation-pipeline)
-   [📊 Experiment Results](#-experiment-results)
-   [📈 Ablation and Case Study](#-ablation-and-case-study)
-   [🔎 Citation](#-citation)

---

## 📝 最近の更新サマリ (日本語)

本リポジトリでは、実験再現性とマルチモデル比較の厳密性を高めるため、以下の主な改善を行いました。差分だけをここに要約しています。

### コアアーキテクチャ / API 周り

-   Azure AI Inference / Azure OpenAI / Public OpenAI を環境変数だけで自動判別するクライアントファクトリを導入
-   推論系 (o3 / o4 / gpt‑5 / DeepSeek R1 / Grok など) は Responses API にルーティングし、従来チャット API との混在を解消
-   モデルごとの許容パラメータ差異に対応（`temperature` を拒否するモデルでは自動的に除去、`max_completion_tokens` / `max_output_tokens` / `max_tokens` を適切に切替）

### 可視化パイプライン / 画像生成

-   Matplotlib のみを許可：Seaborn / Plotly 等のインポートが生成コードに含まれる場合は再プロンプト＆クリーン
-   強制的に headless (`Agg`) + `plt.show()` 除去 + `savefig` 挿入でバッチ再現性を確保
-   リファイン段階で画像が生成されなかった場合、自動的に `novice.png` を `novice_final.png` として複製しダウンストリームを安定化

### 失敗ハンドリング / フォールバックポリシー

-   モデル自動フォールバック機構を完全廃止（以前存在した環境変数トグルも削除）
-   Responses API 呼び出し失敗時は空文字または None を返し、上流でオリジナル指示へフォールバック（別モデル差し替えはしない）
-   例外オブジェクトやエラーメッセージがプロンプト連鎖に混入しないようガード追加

### バッチ / 比較実験支援

-   `compare_models.py` に `--exclude_ids` と `--dry_run` を追加し長時間バッチの部分再実行を容易化
-   比較コンポジット画像は 2 行構成（novice / final）のみに簡素化し、不要なラベルと ground truth 行を削除

### その他

-   Responses API のスキーマ変更に追随 (`input_text` / `input_image`) し 400 エラーを解消
-   `simple_instruction` と `expert_instruction` の概念差を README 末尾に解説
-   追加予定（未実装）：失敗プレースホルダ画像、JSONL ログ、統計集計スクリプト

これらは論文の再現実験やモデル間比較の「透明性確保（No Silent Fallback）」を最優先にした調整です。詳細な英語の技術的説明は下部 “Recent Architectural / Behavioral Changes” セクションを参照してください。

---

## �🛠 最近の技術的変更点 (研究用途向け)

マルチモデル評価、Azure 連携、実験の厳密性向上のために行った主な変更点一覧です（旧バージョンとの差分把握用）。

| 領域                   | 変更内容                                                                                                 | 狙い / 効果                    |
| ---------------------- | -------------------------------------------------------------------------------------------------------- | ------------------------------ |
| クライアント選択       | Azure AI Inference → Azure OpenAI → Public OpenAI の優先順位で自動生成                                   | 環境変数設定のみで切替         |
| Responses API          | o 系 / gpt‑5 系を Responses API に統一。その他は Chat API                                                | エンドポイントと機能の整合性   |
| パラメータ整形         | reasoning 系は `temperature` 自動除去。`max_completion_tokens` / `max_output_tokens` / `max_tokens` 切替 | API リジェクト回避・決定性確保 |
| トークン指定           | モデル種別ごとに適正キーへマッピング                                                                     | 仕様遵守                       |
| ビジョン対応           | 選択モデルが画像非対応ならリファインでビジョン対応代替へ（静的条件内）                                   | クラッシュ防止                 |
| プロット制約           | Matplotlib 限定 + 禁止ライブラリ検出再生成ループ                                                         | 余計な依存とスタイル揺れ抑制   |
| ヘッドレス実行         | `Agg` 強制・`plt.show()` 削除・`savefig` 保証                                                            | バッチ安定化                   |
| novice_final 生成保証  | refine 失敗時に `novice.png` をコピー                                                                    | 後続処理の欠損防止             |
| 比較グリッド           | 3 行 (novice/refined/GT) → 2 行 (novice/final) に簡素化                                                  | 視認性向上・冗長排除           |
| モデルフォールバック   | サイレント自動フォールバックを完全削除                                                                   | 実験の透明性                   |
| 例外伝播制御           | 例外/エラー文字列が次プロンプトに混入しないガード                                                        | 汚染防止                       |
| バッチ除外             | `--exclude_ids` / `--dry_run` を追加                                                                     | 再実行効率改善                 |
| Responses 入力スキーマ | `input_text` / `input_image` へ修正                                                                      | 400 エラー解消                 |

## 🧪 実験プロトコル（推奨フロー）

### 1. 環境構築

```bash
pip install -r requirements.txt
```

ルート直下にある `.env.example` をコピーして自分の秘密情報を記入してください:

```bash
cp .env.example .env
```

`.env` に Azure / OpenAI 系認証情報を設定し、ネットワーク到達性を確認します。`/Users/<あなたのユーザ名>/...` のような絶対パスは **共有用ドキュメントには記載せず**、以下のいずれかの汎用表現を推奨します。

| ローカル固有記述例 | 推奨する汎用化表現 | 備考 |
| ------------------ | ------------------ | ---- |
| `/Users/yourname/projects/MatPlotAgent` | `$(pwd)` または `<project-root>` | ルートディレクトリ参照 |
| `/Users/yourname/.pyenv/versions/...` | `$HOME/.pyenv/versions/...` | ユーザ名秘匿 |
| 結果出力先: `/Users/yourname/tmp/runs` | `./runs` | 相対パスで再現性向上 |

> NOTE: ログ出力等に実行環境のフルパスが埋め込まれる場合、公開前にパス名に個人名や社名が含まれていないか確認してください。

### 2. ベンチマーク指示セット

`benchmark_data/benchmark_instructions.json` には 100 件のケースがあり、各ケースは `simple_instruction`（簡潔・曖昧）と `expert_instruction`（工程列挙・決定的）を保持します。現行パイプラインでは主に simple を novice 生成に利用し、必要に応じ expert を補助コンテキストとして使用します。

### 3. 単一モデル・単一例

```bash
python workflow.py --only_id 10 --model_type o4-mini --workspace ./runs/o4m_ex10
```

成果物: `novice.png`, `novice_final.png`, 生成コード、`workflow.log`。

### 4. 複数モデル比較パネル

```bash
python compare_models.py \
  --example_id 10 \
  --workspace ./compare_workspace
```

出力: `compare_workspace/example_10_compare.png`（行: novice / final × 列: 各モデル）。

モデルセットを上書き:

```bash
python compare_models.py --example_id 10 \
  --models gpt-5 o3-pro o4-mini grok-3 DeepSeek-R1-0528 \
  --workspace ./compare_workspace
```

多数例 + 一部除外:

```bash
python compare_models.py --exclude_ids 1 10 16 17 66 77 82 94 96 98 \
  --workspace ./compare_workspace
```

対象一覧のみ確認 (dry run):

```bash
python compare_models.py --dry_run --workspace ./compare_workspace
```

### 5. 自動評価（任意）

生成後に評価スクリプトを実行しスコア算出。`novice_final.png` は常に存在する設計。

### 6. 整合性 / 失敗時挙動

| シナリオ                                 | 現在の挙動                                                          |
| ---------------------------------------- | ------------------------------------------------------------------- |
| reasoning モデルを誤って Chat API で呼ぶ | エラーで失敗。別モデル代替なし                                      |
| Responses 400 (スキーマ/Operation)       | 空文字戻り → 上流がオリジナル指示へフォールバック（代替モデルなし） |
| refined 画像欠損                         | `novice.png` をコピーして補填                                       |
| 禁止ライブラリ検出                       | 再プロンプト＋再生成ループ                                          |

### 7. 推奨実行順

1. スモーク (1–2 ID, 1 モデル)
2. 少数サブセット (5–10 ID) で挙動/順位確認
3. 全体 100 ID バッチ（必要なら `--exclude_ids` で再実行短縮）
4. novice→final の改善量を統計集計

### 8. 再現性メモ

- 乱数: 指示によっては seed 指定を促し安定性確保
- Temperature: グローバル 0（非対応モデルは送信自体を除外）
- サイレントフォールバック禁止: 失敗は失敗として可視化（空白タイル等）
- 画像サイズ/配置一定: モザイクレイアウト安定

### 9. モデル追加手順

1. OpenAI 互換エンドポイントなら `models/model_config.py` に追記
2. Responses API 必要性を確認（必要なら wrapper 側で自動判定される範囲に命名）
3. 大規模比較に含めたい場合は `compare_models.py` のデフォルト候補へ追加

### 10. トラブルシューティング早見表

| 症状                                         | 原因候補                          | 対処                                              |
| -------------------------------------------- | --------------------------------- | ------------------------------------------------- |
| 400 invalid_value `input_text`/`input_image` | SDK / キャッシュ不整合            | 再インストール・再起動                            |
| コンポジット内が空白タイル                   | モデル出力空/実行失敗             | `<workspace>/<model>/example_X/workflow.log` 確認 |
| `novice_final.png` が過去バージョンで欠損    | refine 途中中断                   | 最新版で自動補填動作を利用                        |
| 禁止ライブラリが残る                         | 検出正規表現がマッチせず          | パターンを再確認（import 行修正）                 |
| OperationNotSupported (o3-pro)               | エンドポイント/デプロイ設定不整合 | Azure Inference 側設定確認                        |

## 🔬 `simple_instruction` と `expert_instruction` の違い

`simple_instruction` はコンパクトで曖昧さを含む目標、`expert_instruction` は手順を段階列挙した決定的ゴール記述です。両者を使い分けることで創造性要求と指示忠実度の差分評価が可能です。現状パイプラインでは主に simple を novice 生成に用い、将来的な忠実度検証のため expert を保持しています。

## 🔮 今後追加を検討している拡張

- 失敗時プレースホルダ PNG（モデル名＋エラー短縮表示）
- 実行ログ JSONL (`model, example_id, phase, status, error`)
- 同一失敗パターン連続時の早期打ち切りヒューリスティック
-   改善量集計と成功率を一括算出するスクリプト

---

新しいモデルファミリを統合する際は、Responses / Chat API の対応関係と「サイレントフォールバック禁止」方針を維持してください。透明性保持が比較実験の信頼性に直結します。

# 📖 Introduction

Scientific data visualization is crucial for conveying complex information in research, aiding in the identification of implicit patterns. Despite the potential, the use of Large Language Models (LLMs) for this purpose remains underexplored. **MatPlotAgent** introduces an innovative, model-agnostic LLM agent framework designed to automate scientific data visualization tasks, harnessing the power of both code LLMs and multi-modal LLMs.

Integrating LLMs into scientific data visualization represents a new frontier in technology that supports research. Existing tools, such as Matplotlib and Origin, are challenging for many people and learning these tools is time-consuming. **MatPlotAgent** is conceived to bridge this gap, leveraging LLM capabilities to enhance human efficiency significantly. **MatPlotBench** is curated to further traction the field of AI-automated scientific data visualization by providing a comprehensive benchmark and trustworthy automatic evaluation method.

# 🎉 News

- March 7, 2024: Releasing the MatPlotAgent, an innovative and model-agnostic framework designed to revolutionize scientific data visualization by automating tasks with advanced LLMs. 🎊
- March 7, 2024: Releasing MatPlotBench, a comprehensive and meticulously curated benchmark that sets a new standard for evaluating AI-driven visualization tools. 🌟

# ✨ MatPlotAgent

1. **Query Expansion**: Thoroughly interprets user requirements and transform them into LLM-friendly instructions
2. **Code Generation with Iterative Debugging**: Uses code to preprocess data and generate figures, with self-debugging capabilities.
3. **Visual Feedback Mechanism**: Employs visual perceptual abilities for error identification and correction.
4. **Generalizability**: Demonstrated effectiveness with various LLMs, including commercial and open-source models.

<div align="center">
  <img src="assets/workflow.png" alt="matplotagent framework">
</div>

# 🎖 MatPlotBench

A high-quality benchmark of 100 human-verified test cases alongside a scoring approach utilizing GPT-4V for automatic evaluation, demonstrating strong correlation with human-annotated scores.

<div align="center">
  <img src="assets/example.png" alt="some examples of MatPlotBench">
</div>

# ⚡️ Getting Started

This project opensources the following components to foster further research and development in the field of scientific data visualization:

- **Benchmark Data (MatPlotBench)**: A meticulously crafted benchmark to quantitatively evaluate data visualization approaches.
- **Evaluation Pipeline**: Utilizes GPT-4V for automatic evaluation, offering a reliable metric that correlates strongly with human judgment.
- **MatPlotAgent Framework**: The entire codebase for the MatPlotAgent framework is available, encouraging adaptation and improvement by the community.

<!-- #TODO
[Instructions on how to access and use the benchmark data, evaluation pipeline, and the MatPlotAgent framework.] -->

Benchmark Data (MatPlotBench) can be found in the `./benchmark_data` folder.

The code requires some dependencies as specified in requirements.txt. Please follow the relevant libraries to install or run:

```bash
pip install -r requirements.txt
```

## MatPlotAgent Framework

### Configuration

If you're using the open-source model, please download the model to your local machine first and adjust the location of the corresponding model in `models/model_config.py`.

If you're using GPT-3.5 or GPT-4, please update your `API_KEY` in `agents/config/openai.py`.

## Use with Azure (OpenAI / AI Inference)

This repository is now configurable to run with Azure-hosted models without changing code.

1. Put your credentials in `.env` at repo root (python-dotenv is used automatically):

- For Azure OpenAI (deployment-based):

  - `AZURE_OPENAI_ENDPOINT=https://<your-resource>.openai.azure.com/`
  - `AZURE_OPENAI_API_KEY=***`
    -   `AZURE_OPENAI_API_VERSION=2025-04-01-preview` (or your supported version)

-   For Azure AI Inference (serverless, multi-provider models like o3, DeepSeek, Grok, etc.):
    -   `AZURE_INFERENCE_ENDPOINT=https://<your-endpoint>/openai/deployments/<deployment>/extensions`
    -   `AZURE_INFERENCE_API_KEY=***`

The code auto-detects in this order:

1. `AZURE_INFERENCE_*` (AI Inference)
2. `AZURE_OPENAI_*` (Azure OpenAI)
3. `OPENAI_API_KEY` + optional `OPENAI_BASE_URL` (api.openai.com)

4. Model names

-   For Azure OpenAI, pass the deployment name as `model_type` (e.g., `--model_type o4-mini` if your deployment is named `o4-mini`).
-   For Azure AI Inference, pass the model id. Confirm the model is enabled on your endpoint. Verified families include:
    -   OpenAI: `gpt-5`, `gpt-5-mini`, `gpt-5-nano`, `gpt-4o`, `gpt-4o-mini`
    -   o-series: `o3`, `o3-mini`, `o3-pro`, `o4-mini`
    -   DeepSeek: `DeepSeek-R1-0528`
    -   Grok: `grok-3`, `grok-3-mini`

3. Vision models

-   By default, evaluation uses `EVAL_TEXT_MODEL=gpt-4` and `EVAL_VISION_MODEL=gpt-4-vision-preview`.
-   Override via `.env` if needed, e.g., `EVAL_TEXT_MODEL=o3`, `EVAL_VISION_MODEL=gpt-4o`.

No code changes are required once `.env` is configured; the client is created dynamically.

Notes:

-   Some reasoning models (o-series, DeepSeek R1, Grok) do not accept `temperature`. The framework automatically omits it for those models and uses the right token parameter (`max_completion_tokens` for o-series).

### Running OpenAI-Compatible Server

If you're utilizing GPT-3.5 or GPT-4, you can skip this section.

We use vLLM to deploy the open-source model as a server, implementing the OpenAI API protocol. This enables vLLM to seamlessly replace applications using the OpenAI API.

Ensure you have vLLM installed and configured on your local machine.

We provide scripts to deploy the API server. For instance, to deploy `CodeLlama-34b-Instruct`, you can execute:

```
bash models/scripts/CodeLlama-34b-Instruct-hf.sh
```

If you need to modify the script's content, please refer to the [vLLM documentation](https://docs.vllm.ai/en/latest/index.html).

### Running MatPlotAgent Framework

To execute the MatPlotAgent framework, use the following script:

```bash
python workflow.py \
    --model_type=MODEL \
    --workspace=path/to/result
```

Replace `MODEL` with the desired model. All available `model_type` options can be found in `models/model_config.py`.

Replace `path/to/result` with the desired path to save the results.

For direct decoding, use:

```bash
python one_time_generate.py \
  --model_type=MODEL \
  --workspace=path/to/result
```

For chain-of-thought variant:

```bash
python one_time_generate_COT.py \
  --model_type=MODEL \
  --workspace=path/to/result
```

## Evaluation Pipeline

After running the MatPlotAgent Framework, you can utilize the Evaluation Pipeline to obtain automatic evaluation scores.

First, replace `directory_path` with `path/to/result` in `evaluation/api_eval.py` and `evaluation/average_score_calc.py`.

Run the evaluation shell script:

```bash
bash evaluation/eval.sh
```

Then (if needed) change into the evaluation directory for manual scripts:

```bash
cd evaluation
```

# 📊 Experiment Results

Our experiments showcase MatPlotAgent's ability to improve LLM performance across a variety of aspects, with notable enhancements in plot quality and correctness, supported by both quantitative scores and qualitative assessments.

Performance of different LLMs on MatPlotBench. For each model, improvements over the direct decoding are highlighted in **bold**.

| Model                                                                              | Direct Decod. | Zero-Shot CoT     | MatPlotAgent w/ GPT-4V |
| ---------------------------------------------------------------------------------- | ------------- | ----------------- | ---------------------- |
| **GPT-4**                                                                          | 48.86         | 45.42 (-3.44)     | 61.16 (**+12.30**)     |
| **GPT-3.5**                                                                        | 38.03         | 37.14 (-0.89)     | 47.51 (**+9.48**)      |
| **Magicoder-S-DS-6.7B** ([Wei et al.,](https://arxiv.org/abs/2312.02120))          | 38.49         | 37.95 (-0.54)     | 51.70 (**+13.21**)     |
| **Deepseek-coder-6.7B-instruct** ([Guo et al.,](https://arxiv.org/abs/2401.14196)) | 31.53         | 29.16 (-2.37)     | 39.45 (**+7.92**)      |
| **CodeLlama-34B-Instruct** ([Rozière et al.,](https://arxiv.org/abs/2308.12950))   | 16.54         | 12.40 (-4.14)     | 14.18 (-2.36)          |
| **Deepseek-coder-33B-instruct** ([Guo et al.,](https://arxiv.org/abs/2401.14196))  | 30.88         | 36.10 (**+5.22**) | 32.18 (**+1.30**)      |
| **WizardCoder-Python-33B-V1.1** ([Luo et al.,](https://arxiv.org/abs/2306.08568))  | 36.94         | 35.81 (-1.13)     | 45.96 (**+9.02**)      |

Additionally, we present the results of using Gemini Pro Vision as the visual agent on GPT-4 and GPT-3.5, showcasing a considerable improvement of 7.87 and 5.45, respectively, over the direct decoding baseline. This evidence further demonstrates our method's model-agnostic characteristics by using various multimodal LLMs to achieve improved performance.

| Model   | Direct Decod. | MatPlotAgent w/ Gemini Pro Vision |
| ------- | ------------- | --------------------------------- |
| GPT-4   | 48.86         | 56.73 (**+7.87**)                 |
| GPT-3.5 | 38.03         | 43.48 (**+5.45**)                 |

We assessed MatPlotAgent's performance on the visualization subset of the Code Interpreter Benchmark, which was released alongside Qwen-agent, witnessing notable improvements over GPT-4. These results underscore the efficacy of our approach in enhancing visualization capabilities.

<table>
  <thead>
    <tr>
      <th rowspan="2"><strong>Model</strong></th>
      <th colspan="3" align="center"><strong>Accuracy of Code Execution Results (%)</strong></th>
    </tr>
    <tr>
      <th align="center"><strong>Visualization-Hard</strong></th>
      <th align="center"><strong>Visualization-Easy</strong></th>
      <th align="center"><strong>Average</strong></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>GPT-4</td>
      <td align="center">66.7</td>
      <td align="center">60.8</td>
      <td align="center">63.8</td>
    </tr>
    <tr>
      <td><strong>+ MatPlotAgent</strong></td>
      <td align="center"><strong>72.6</strong></td>
      <td align="center"><strong>68.4</strong></td>
      <td align="center"><strong>70.5</strong></td>
    </tr>
    <tr>
       <td><em>w/o Visual Feedback</em></td>
      <td align="center">66.7</td>
      <td align="center">65.8</td>
      <td align="center">66.3</td>
    </tr>
  </tbody>
</table>

## 📈 Ablation and Case Study

Examples to illustrate the effect of visual feedback. To investigate the effect of the visual feedback mechanism on different models, we display the outputs of two representative LLMs. Case A, B, and C are generated by GPT-4. Case D is generated by Magicoder-S-DS-6.7B.

<div align="center">
  <img src="assets/ablation.png" alt="Examples to illustrate the effect of visual feedback. To investigate the effect of the visual feedback mechanism on different models, we display the outputs of two representative LLMs. Case A, B, and C are generated by GPT-4. Case D is generated by Magicoder-S-DS-6.7B.">
</div>

Case study of different models

<div align="center">
  <img src="assets/case.png" alt="Case study of different models">
</div>

# 🔎 Citation

Feel free to cite the paper if you think MatPlotAgent is useful.

```bibtex
@misc{yang2024matplotagent,
      title={MatPlotAgent: Method and Evaluation for LLM-Based Agentic Scientific Data Visualization},
      author={Zhiyu Yang and Zihan Zhou and Shuo Wang and Xin Cong and Xu Han and Yukun Yan and Zhenghao Liu and Zhixing Tan and Pengyuan Liu and Dong Yu and Zhiyuan Liu and Xiaodong Shi and Maosong Sun},
      year={2024},
      eprint={2402.11453},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
```

---
