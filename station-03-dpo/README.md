# Station 03 - DPO (Preference Optimization)

> Phase: **Phase 1 — TRAIN** | Estimated time: **3 days**

## Objective

Take your Station 02 SFT model. Label 200 prompts with preferred vs rejected responses. Run DPO. Compare SFT vs SFT+DPO on the same eval set.

## What you'll build

200-example preference dataset + DPO training run + side-by-side eval CSV (SFT vs SFT+DPO).

## What you'll learn

- Why DPO replaced PPO for 95% of preference-tuning use cases
- Preference data collection: how to label preferred/rejected without bias
- DPO loss intuition: pull preferred closer, push rejected farther - no reward model needed
- When DPO beats SFT alone (consistency, tone, refusal quality)
- When DPO hurts (over-optimization, mode collapse)
- How to detect DPO failure: KL divergence from SFT model

## Resources (only runnable ones)

- [Unsloth DPO notebook (Llama-3 8B DPO)](https://github.com/unslothai/unsloth)
- [RLHF Book Ch.6 - Direct Alignment (skim)](https://rlhfbook.com/c/direct-alignment.html)
- [TRL DPOTrainer docs](https://huggingface.co/docs/trl/dpo_trainer)

## Artifact (the commit)

SFT+DPO adapter on HF Hub + 1-page writeup comparing SFT vs SFT+DPO eval numbers.

## Success criteria

- [ ] 200 preference pairs labelled with rationale
- [ ] DPO training run completes without NaN
- [ ] Eval shows DPO model >= SFT model on F1 + 'response quality' judge score
- [ ] If DPO hurts: document why (over-optimization, bad labels, etc.)

## Files in this folder

- `notebook.ipynb` or `script.py` - the actual build (you create this)
- `what-i-built.md` - 1 paragraph on what you shipped (you create this)
- `what-i-learned.md` - 1 page max on what clicked (you create this)
- `artifact.md` - links to HF Hub models/datasets, screenshots, demo URLs (you create this)
- `assets/` - screenshots, plots, CSVs (you create this)

## When this station is done

Update `../progress.md` to check all boxes. Only then may you open Station 04's resources.
