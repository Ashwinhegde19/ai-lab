# Station 10 - Guardrails Upgrade

> Phase: **Phase 3 — EVALUATE** | Estimated time: **2 days**

## Objective

Replace V1 rule-based guardrails with Llama Guard 3 (output classifier) + Prompt Guard (input classifier). Wire into vLLM. Re-run eval.

## What you'll build

Updated guardrail module in the workbench + before/after eval CSV.

## What you'll learn

- Llama Guard 3: taxonomy of safety categories, how it scores
- Prompt Guard: prompt injection + jailbreak detection
- Classifier-based vs rule-based guardrails: pros/cons
- Latency cost of running 2 extra models per request
- False positive patterns: what triggers Llama Guard 3 wrongly
- How to compose input + output guardrails (block early, sanitize late)

## Resources (only runnable ones)

- [Llama Guard 3 HF model card](https://huggingface.co/meta-llama/LlamaGuard3-8B)
- [Prompt Guard 86M HF model card](https://huggingface.co/meta-llama/Prompt-Guard-86M)
- [Llama Guard 3 paper (skim)](https://arxiv.org/abs/2406.12931)

## Artifact (the commit)

Before/after eval CSV in workbench showing: rule-based vs classifier-based guardrails on the same prompt set.

## Success criteria

- [ ] Llama Guard 3 wired as output classifier in vLLM pipeline
- [ ] Prompt Guard wired as input classifier
- [ ] Eval CSV shows: false-positive rate, catch rate, latency overhead
- [ ] Documented at least 1 case where Llama Guard 3 catches what rules missed (and vice versa)

## Files in this folder

- `notebook.ipynb` or `script.py` - the actual build (you create this)
- `what-i-built.md` - 1 paragraph on what you shipped (you create this)
- `what-i-learned.md` - 1 page max on what clicked (you create this)
- `artifact.md` - links to HF Hub models/datasets, screenshots, demo URLs (you create this)
- `assets/` - screenshots, plots, CSVs (you create this)

## When this station is done

Update `../progress.md` to check all boxes. Only then may you open Station 11's resources.
