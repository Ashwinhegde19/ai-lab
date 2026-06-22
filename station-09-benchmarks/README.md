# Station 09 - Public Benchmark Integration

> Phase: **Phase 3 — EVALUATE** | Estimated time: **2 days**

## Objective

Run your fine-tuned model on a slice of HarmBench + TruthfulQA + BBQ. Get real benchmark numbers, not just your custom prompts.

## What you'll build

`benchmarks.md` table: model x benchmark x score. Run base + SFT + (optional) DPO for comparison.

## What you'll learn

- How public benchmarks are structured (prompt set + scoring function)
- HarmBench: adversarial prompt + classifier scoring (harmful vs refused)
- TruthfulQA: factual prompts where models often mimic misconceptions
- BBQ: bias benchmark - ambiguous + disambiguated scenarios
- Cost-efficient subsampling: 100-200 examples per benchmark is enough for trends
- Why public benchmarks matter for credibility (founders + customers recognize them)

## Resources (only runnable ones)

- [HarmBench repo](https://github.com/centerforaisafety/HarmBench)
- [TruthfulQA repo](https://github.com/sylinrl/TruthfulQA)
- [BBQ repo](https://github.com/nyu-mll/BBQ)
- [lm-evaluation-harness (EleutherAI)](https://github.com/EleutherAI/lm-evaluation-harness)

## Artifact (the commit)

`benchmarks.md` table + raw outputs CSV + 1-paragraph interpretation of what the numbers mean.

## Success criteria

- [ ] All 3 benchmarks run on your fine-tuned model
- [ ] Numbers in `benchmarks.md` table
- [ ] Interpretation paragraph explains: does fine-tuning help or hurt on each benchmark?
- [ ] At least 1 interesting finding documented

## Files in this folder

- `notebook.ipynb` or `script.py` - the actual build (you create this)
- `what-i-built.md` - 1 paragraph on what you shipped (you create this)
- `what-i-learned.md` - 1 page max on what clicked (you create this)
- `artifact.md` - links to HF Hub models/datasets, screenshots, demo URLs (you create this)
- `assets/` - screenshots, plots, CSVs (you create this)

## When this station is done

Update `../progress.md` to check all boxes. Only then may you open Station 10's resources.
