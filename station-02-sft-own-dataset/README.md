# Station 02 - SFT on Your Own Dataset

> Phase: **Phase 1 — TRAIN** | Estimated time: **5-7 days**

## Objective

Build a 1000-example AI risk-classification dataset and fine-tune Llama-3-8B on it via QLoRA. This becomes Workbench V2's Assistant #3.

## What you'll build

Three deliverables: (1) `data/risk_dataset.jsonl` with 1000 examples in ChatML format, (2) a fine-tuned LoRA adapter on HF Hub, (3) `eval/results.csv` with precision/recall/F1 vs base model.

## What you'll learn

- ChatML template format and why strict formatting matters
- Dataset schema design: instruction + input + structured JSON output
- Train/val split (80/20) and why you need a held-out eval set
- Catastrophic forgetting: the fine-tuned model forgets how to be helpful
- Mixing in general data (10% ShareGPT) to prevent forgetting
- Eval during training: held-out set, loss-vs-quality gap
- When to stop training (eval loss plateau, not training loss)

## Resources (only runnable ones)

- [Unsloth Datasets Guide](https://unsloth.ai/docs/get-started/fine-tuning-llms-guide)
- [RLHF Book Ch.2 - Instruction Fine-Tuning (skim, 45 min)](https://rlhfbook.com/c/instruction-fine-tuning.html)
- [HuggingFaceH4/ultrachat_200k format reference](https://huggingface.co/datasets/HuggingFaceH4/ultrachat_200k)

## Artifact (the commit)

LoRA adapter on HF Hub + dataset on HF Hub + eval CSV. **This is the V2 deliverable for the Ollive workbench.**

## Success criteria

- [ ] Dataset has 1000+ examples covering 6 risk categories (hallucination, bias, jailbreak, harmful, unsafe compliance, PII)
- [ ] Fine-tuned model outputs valid JSON 95%+ of the time on held-out set
- [ ] Precision >= 0.85 vs base model's ~0.6
- [ ] F1 >= 0.80
- [ ] Adapter is the one you'll deploy in Station 05

## Files in this folder

- `notebook.ipynb` or `script.py` - the actual build (you create this)
- `what-i-built.md` - 1 paragraph on what you shipped (you create this)
- `what-i-learned.md` - 1 page max on what clicked (you create this)
- `artifact.md` - links to HF Hub models/datasets, screenshots, demo URLs (you create this)
- `assets/` - screenshots, plots, CSVs (you create this)

## When this station is done

Update `../progress.md` to check all boxes. Only then may you open Station 03's resources.
