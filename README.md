# Personal AI Lab

> **Commit before you consume.**
> 12 stations across the LLM engineer stack — train, serve, evaluate, expand.
> Each station ends with a committed artifact. No artifact, no next station.

## What this is

A single GitHub repo, structured as 12 stations, that proves you can do every layer of the LLM engineering stack end-to-end. Not a course. Not a portfolio site. A working notebook of builds.

Each station folder contains:
- `notebook.ipynb` or `script.py` — the build
- `what-i-built.md` — what you shipped (1 paragraph)
- `what-i-learned.md` — what clicked (1 page max)
- `artifact.md` — links to the artifact (HF model, dataset, screenshot, demo URL)
- `assets/` — screenshots, plots, CSVs

## The phased approach (don't try to do all 12 linearly)

This is the most important update to the plan. 12 stations is a **roadmap**, not a 10-week sprint. Run it in 3 phases:

### Phase A — 7-day MVP (the "prove it works" sprint)
Goal: a working fine-tuned risk classifier, end-to-end, on a small dataset.

1. `git init` + first commit
2. **Station 01** — Run Unsloth Alpaca notebook once, prove LoRA mechanics (1 day max, don't polish)
3. **Station 02-lite** — Use the 20-example seed dataset in `station-02-sft-own-dataset/data/risk_dataset.jsonl`. Run the notebook. Get a working SFT model + eval CSV. Don't scale to 1000 yet.

**Exit criteria:** A committed notebook showing precision/recall/F1 on the val set. Even if numbers are bad, the loop works.

### Phase B — Portfolio quality (the workbench V2 spine)
Goal: the artifact you email to the Ollive founder in early August.

4. **Station 02** (full) — Scale dataset to 1000 examples across 6 risk categories
5. **Station 07** — Structured output (force 100% valid JSON)
6. **Station 08** — LLM-as-judge + Cohen's kappa (real eval, not just heuristic)
7. **Station 05** — vLLM + LoRA hot-swap (serve the model behind an API)
8. **Station 10** — Guardrails upgrade (Llama Guard 3 + Prompt Guard)

**Exit criteria:** The August V2 email sent to `work@ollive.ai` with repo + 1-page PDF + Loom demo.

### Phase C — Advanced (if time allows, after August)
Goal: deepen the portfolio for parallel applications and future roles.

9. **Station 06** — Quantization benchmark
10. **Station 09** — Public benchmarks (HarmBench, TruthfulQA, BBQ)
11. **Station 12** — Observability with Langfuse
12. **Station 11** — RAG with vector DB
13. **Station 03** — DPO (only if SFT + serving + eval are solid)
14. **Station 04** — GRPO (only if you have 2+ weeks spare; it's a time sink)

## Why this order (not the original numbering)

The original plan had DPO and GRPO right after SFT. That's wrong — you'd be optimizing a model you haven't even served or evaluated yet. The correct dependency order is:

```
SFT (02) → structured output (07) → eval/judge (08) → serving (05) → guardrails (10)
                                              ↓
                                    [V2 email sent]
                                              ↓
                       quant (06) → benchmarks (09) → observability (12)
                                              ↓
                                    RAG (11) → DPO (03) → GRPO (04) [optional]
```

**Highest-value spine:** Station 02 + 07 + 08 + 05 + 10 = the workbench V2.

## The 12 stations (full roadmap)

### Phase 1 — TRAIN (where models learn)
- **Station 01** — SFT basics (Unsloth Alpaca notebook end-to-end)
- **Station 02** — SFT on your own dataset (1000-example AI risk dataset → Llama-3-8B) ⭐ **V2 deliverable**
- **Station 03** — DPO (preference optimization on your SFT model) — *Phase C, optional*
- **Station 04** — GRPO (RL with reward functions) — *Phase C, only if time*

### Phase 2 — SERVE (where models meet users)
- **Station 05** — vLLM + LoRA hot-swap (one server, three adapters) ⭐ **V2 deliverable**
- **Station 06** — Quantization benchmark (FP16 → AWQ → GPTQ → GGUF)
- **Station 07** — Structured output (grammar-constrained JSON) ⭐ **V2 deliverable**

### Phase 3 — EVALUATE (where you measure reality)
- **Station 08** — LLM-as-judge + Cohen's kappa ⭐ **V2 deliverable**
- **Station 09** — Public benchmark integration (HarmBench, TruthfulQA, BBQ)
- **Station 10** — Guardrails upgrade (Llama Guard 3 + Prompt Guard) ⭐ **V2 deliverable**

### Phase 4 — EXPAND (the wider stack)
- **Station 11** — RAG with vector DB (BGE-M3 + Chroma + reranker)
- **Station 12** — Observability with Langfuse (self-hosted, dashboard, alerts)

⭐ = the 5 stations that form the V2 deliverable spine

## Profile (this is YOUR lab, calibrated)

- **Time budget:** 8–12 hrs/week → ~10–12 weeks for all 12 stations
- **Compute:** Modal.com ($250 credits ≈ 180 A100-hours) + Colab free for first runs
- **Stack comfort:** Intermediate Python + PyTorch + HF Transformers
- **Dev setup:** Linux (native CUDA + Docker + vLLM all easy)
- **Dataset focus:** AI safety — hallucination, bias, jailbreak, harmful, unsafe compliance, PII
- **Math comfort:** Basic — focus on intuition + code, skip PPO derivations
- **Output language:** English

## The 5 rules (read every Monday)

1. **Build → commit → browse.** You cannot open the next station's resources until the current one has a committed artifact on GitHub.
2. **No new tab until previous station is committed.** No new videos, no new docs, no new courses.
3. **If a resource has no notebook/Colab in the first 10 minutes, drop it.** Includes most "intro to LLMs" courses.
4. **Always serve what you build on vLLM.** You already know it — reuse it as your playground.
5. **One pet project.** The AI safety risk classifier routes every new skill through it. Courses in isolation fade; courses applied to your project stick.

## Anti-topics (do NOT learn these — theory traps)

| Skip | Why |
|---|---|
| Transformer from scratch in PyTorch | Already-built models work fine; you're not Meta |
| PPO/GAE math derivations | DPO/KTO replaced PPO for 95% of use cases; TRL handles it |
| CUDA kernel writing | Unless you join vLLM core team, no |
| Pretraining a model from scratch | Way out of scope; you'll fine-tune, not pretrain |
| Full RLHF book front-to-back | Ch. 2 (SFT) + Ch. 6 (DPO) + Ch. 11 (eval) only |
| Research-paper deep-dives on attention variants | Architectural FOMO; doesn't help ship |
| "Intro to LLMs" generic courses | You're past intro |

## Quick links

- [Progress tracker](progress.md) — checklist, update every commit
- [Modal compute budget](modal/BUDGET.md) — how to spend your $250
- [Reference PDF (print this)](docs/ai-lab-reference.pdf) — 20-page reference card
- [Founder email templates](docs/founder-emails.md) — July check-in + August V2 ship
- [Parallel companies to apply to](docs/parallel-companies.md) — 8 target companies

## Connect to your existing workbench

This lab is not a replacement for [ai-risk-evaluation-workbench](https://github.com/Ashwinhegde19/ai-risk-evaluation-workbench). It's the **upskill pipeline** that feeds V2 of the workbench.

| Lab station | Feeds into workbench V2 as... |
|---|---|
| Station 02 (SFT own dataset) | Assistant #3 — the fine-tuned risk classifier |
| Station 05 (vLLM LoRA hot-swap) | Replaces HF Transformers backend with vLLM |
| Station 07 (structured output) | Forces 100% valid JSON from the classifier |
| Station 08 (LLM-as-judge + kappa) | Replaces heuristic scorer with calibrated judge |
| Station 10 (guardrails upgrade) | Replaces rule-based v1 guardrails with Llama Guard 3 |
| Station 12 (Langfuse) | Replaces JSONL viewer with real observability |

## License

Personal learning repo. MIT for any reusable code you extract.
