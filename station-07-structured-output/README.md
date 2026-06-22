# Station 07 - Structured Output (Strict JSON)

> Phase: **Phase 2 — SERVE** | Estimated time: **1 day**

## Objective

Force your fine-tuned model to output strict JSON via outlines / xgrammar / lm-format-enforcer. Compare vs prompt-only JSON.

## What you'll build

Risk-classifier endpoint with grammar-constrained decoding + 100-test validation showing 100% valid JSON.

## What you'll learn

- Grammar-constrained decoding: regex / BNF grammar at sampling time
- Why OpenAI's 'JSON mode' isn't enough (still possible to get invalid schemas)
- outlines vs xgrammar vs lm-format-enforcer: pros/cons
- Performance cost: ~5-10% latency overhead
- When structured output beats fine-tuning for schema compliance

## Resources (only runnable ones)

- [outlines docs](https://outlines-dev.github.io/outlines/)
- [xgrammar README](https://github.com/mlc-ai/xgrammar)
- [lm-format-enforcer README](https://github.com/noamgat/lm-format-enforcer)

## Artifact (the commit)

Risk-classifier endpoint with structured output + before/after CSV (prompt-only JSON vs grammar-constrained).

## Success criteria

- [ ] 100 test prompts -> 100% valid JSON output
- [ ] Before (prompt-only): JSON validity rate recorded
- [ ] Latency overhead measured (should be <10%)
- [ ] Schema validated against Pydantic model

## Files in this folder

- `notebook.ipynb` or `script.py` - the actual build (you create this)
- `what-i-built.md` - 1 paragraph on what you shipped (you create this)
- `what-i-learned.md` - 1 page max on what clicked (you create this)
- `artifact.md` - links to HF Hub models/datasets, screenshots, demo URLs (you create this)
- `assets/` - screenshots, plots, CSVs (you create this)

## When this station is done

Update `../progress.md` to check all boxes. Only then may you open Station 08's resources.
