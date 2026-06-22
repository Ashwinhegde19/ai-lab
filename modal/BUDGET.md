# Modal Compute Budget

> You have **$250 of Modal credits** = roughly **250 A100-hours**.
> This file tracks how you'll spend them across all 12 stations.

## Cost math (Modal pricing, approximate)

| GPU | $/hr | Your budget hours |
|---|---|---|
| T4 (16GB) | $0.40 | 625 hrs |
| A10G (24GB) | $1.10 | 227 hrs |
| **A100-40GB** | **$1.39** | **~180 hrs** |
| A100-80GB | $2.10 | ~119 hrs |
| H100-80GB | $3.50 | ~71 hrs |

**Rule of thumb:** Default to **A100-40GB at $1.39/hr** for fine-tuning. Drop to T4 for inference benchmarks. Use H100 only for GRPO.

## Per-station allocation

| Station | Task | GPU | Est. hours | Cost |
|---|---|---|---|---|
| 01 | SFT basics (do on Colab free first!) | A100-40 | 2 | $2.78 |
| 02 | SFT on risk dataset (1000 examples, 3 epochs) | A100-40 | 8 | $11.12 |
| 02 | Eval + benchmark runs | T4 | 3 | $1.20 |
| 03 | DPO (200 pairs, 1 epoch) | A100-40 | 4 | $5.56 |
| 04 | GRPO (finicky — multiple runs) | H100-80 | 20 | $70.00 |
| 05 | vLLM serving + benchmarks | A100-40 | 6 | $8.34 |
| 06 | Quantization (5 variants) | T4 + A100 | 4 | $4.00 |
| 07 | Structured output eval | T4 | 2 | $0.80 |
| 08 | LLM-judge (uses OpenAI API, not Modal) | — | 0 | $0.00 |
| 09 | Public benchmarks (subsample 150 each) | T4 | 6 | $2.40 |
| 10 | Llama Guard 3 + Prompt Guard serving | T4 | 4 | $1.60 |
| 11 | RAG (mostly CPU + small embedder) | T4 | 3 | $1.20 |
| 12 | Langfuse (CPU only, self-hosted) | — | 0 | $0.00 |
| **Buffer** | Re-runs, debugging, mistakes | — | 30 | $41.70 |
| **TOTAL** | | | **~92 hrs** | **~$151** |

**Headroom: ~$99 spare.** That's enough for 2-3 re-runs of GRPO if needed.

## Cost-saving rules

1. **Colab free is your first run for everything.** Don't burn Modal credits until Colab free fails.
2. **Snapshot LoRA adapters.** Re-running Station 02 from scratch costs $11; loading a saved adapter costs $0.
3. **Use T4 for inference benchmarks.** A100 is overkill for testing quant variants.
4. **Modal's serverless model means you only pay for compute time.** No idle charges. Use `modal.App()` properly so containers spin down.
5. **For development, use `modal serve` (interactive) — for production runs, `modal run`.**
6. **H100 only for GRPO.** Everything else A100-40 or smaller.

## Modal scaffold template

See `modal/serve_lora.py` for a starter Modal endpoint that serves your Station 02 fine-tuned LoRA adapter.

## What to do if you're running low

If budget drops below $50:

1. Stop GRPO iterations. Use the best checkpoint you have.
2. Skip Station 09 (public benchmarks) — your custom eval suite is enough for the founder pitch.
3. Do Stations 10-12 on local Linux CPU/MPS instead of Modal (slower but free).
