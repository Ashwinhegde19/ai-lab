# Station 04 - GRPO (RL with Reward Functions)

> Phase: **Phase 1 — TRAIN** | Estimated time: **5-7 days**

## Objective

Define a reward function (valid JSON + correct risk class). Run GRPO on your SFT model. Earn the 'trained with RL' badge.

## What you'll build

Reward function module + GRPO training run + writeup of what worked and what didn't.

## What you'll learn

- What GRPO actually does (Group Relative Policy Optimization - DeepSeek-R1's trick)
- Reward function design: discrete (valid JSON?) + continuous (correct class?) components
- Why 'Luck + Patience' is Unsloth's honest warning
- RLVR vs RLHF: when you have a verifiable reward vs when you need a human
- When GRPO beats DPO (verifiable tasks) vs when it doesn't (subjective tasks)
- Reward hacking: model finds a way to maximize reward without doing the task

## Resources (only runnable ones)

- [Unsloth Reinforcement Learning Guide](https://unsloth.ai/docs/get-started/reinforcement-learning-rl-guide)
- [Unsloth GRPO tutorial notebook](https://github.com/unslothai/unsloth)
- [DeepSeek-R1 paper (skim Section 3 only)](https://arxiv.org/abs/2501.12948)

## Artifact (the commit)

SFT+GRPO adapter on HF Hub + 'trained with RL' badge on model card + honest writeup.

## Success criteria

- [ ] Reward function defined and unit-tested
- [ ] GRPO training run completes (at least 100 steps)
- [ ] Model's JSON-validity rate improves vs SFT baseline
- [ ] Writeup documents at least one reward-hacking attempt

## Files in this folder

- `notebook.ipynb` or `script.py` - the actual build (you create this)
- `what-i-built.md` - 1 paragraph on what you shipped (you create this)
- `what-i-learned.md` - 1 page max on what clicked (you create this)
- `artifact.md` - links to HF Hub models/datasets, screenshots, demo URLs (you create this)
- `assets/` - screenshots, plots, CSVs (you create this)

## When this station is done

Update `../progress.md` to check all boxes. Only then may you open Station 05's resources.
