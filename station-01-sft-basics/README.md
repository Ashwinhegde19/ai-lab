# Station 01 - SFT Basics

> Phase: **Phase 1 — TRAIN** | Estimated time: **1 day**

## Objective

Run Unsloth's Llama-3.1-8B Alpaca notebook end-to-end on free Colab. Save a working LoRA adapter to Hugging Face Hub. Take a screenshot of the loss curve.

## What you'll build

The Unsloth `Llama3.1_(8B)-Alpaca.ipynb` notebook, unchanged. Run it top to bottom. Save the LoRA adapter in three formats: 16-bit merged, 4-bit quantized, GGUF Q4_K_M.

## What you'll learn

- What LoRA actually does (add thin matrices A and B to each weight — 1% of params)
- QLoRA = LoRA on a 4-bit quantized base model
- What a training loop looks like: forward -> loss -> backward -> optimizer step
- Loss curves: training loss vs eval loss, what overfitting looks like
- Completion-only loss masking: why we don't compute loss on the prompt

## Resources (only runnable ones)

- [Unsloth Fine-tuning LLMs Guide](https://unsloth.ai/docs/get-started/fine-tuning-llms-guide)
- [Unsloth Llama-3.1 (8B) Alpaca notebook](https://github.com/unslothai/unsloth/blob/main/README.md)
- [Unsloth Inference & Deployment](https://unsloth.ai/docs/basics/inference-and-deployment)

## Artifact (the commit)

LoRA adapter on HF Hub + 3 screenshots (loss curve, sample outputs, save confirmation). Push the notebook to this folder with your outputs preserved.

## Success criteria

- [ ] Notebook runs without errors on Colab free T4
- [ ] LoRA adapter uploaded to HF Hub under your username
- [ ] Sample inference on the fine-tuned model produces coherent Alpaca-style answers
- [ ] Loss curve shows clean downward trend, no NaNs

## Files in this folder

- `notebook.ipynb` or `script.py` - the actual build (you create this)
- `what-i-built.md` - 1 paragraph on what you shipped (you create this)
- `what-i-learned.md` - 1 page max on what clicked (you create this)
- `artifact.md` - links to HF Hub models/datasets, screenshots, demo URLs (you create this)
- `assets/` - screenshots, plots, CSVs (you create this)

## When this station is done

Update `../progress.md` to check all boxes. Only then may you open Station 02's resources.
