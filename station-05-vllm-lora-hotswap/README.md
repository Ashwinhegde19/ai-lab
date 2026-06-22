# Station 05 - vLLM + LoRA Hot-Swap

> Phase: **Phase 2 — SERVE** | Estimated time: **2 days**

## Objective

Serve your base Llama-3-8B + 3 LoRA adapters (SFT, DPO, GRPO) in one vLLM instance. Switch adapters via API param.

## What you'll build

vLLM server with `--enable-lora` flag + 3 LoRA adapters registered + curl test script.

## What you'll learn

- vLLM internals: continuous batching, PagedAttention, prefix cache
- Multi-LoRA serving: how vLLM loads/unloads adapters per request
- Memory math: base model + N adapters x adapter size
- Latency: hot-swap overhead vs separate processes per adapter
- OpenAI-compatible API: chat, streaming, tools, JSON mode

## Resources (only runnable ones)

- [vLLM docs (you took the course - refresh)](https://docs.vllm.ai/)
- [vLLM multi-LoRA serving docs](https://docs.vllm.ai/en/latest/features/lora.html)
- [Unsloth Inference & Deployment](https://unsloth.ai/docs/basics/inference-and-deployment)

## Artifact (the commit)

Running vLLM server + `test_curl.sh` demonstrating all 3 adapters + commit of the launch script.

## Success criteria

- [ ] vLLM server starts with base model + 3 LoRA adapters registered
- [ ] `curl` requests with different `model` params return responses from correct adapter
- [ ] All 3 adapters respond with correct risk classifications
- [ ] p95 latency measured and recorded

## Files in this folder

- `notebook.ipynb` or `script.py` - the actual build (you create this)
- `what-i-built.md` - 1 paragraph on what you shipped (you create this)
- `what-i-learned.md` - 1 page max on what clicked (you create this)
- `artifact.md` - links to HF Hub models/datasets, screenshots, demo URLs (you create this)
- `assets/` - screenshots, plots, CSVs (you create this)

## When this station is done

Update `../progress.md` to check all boxes. Only then may you open Station 06's resources.
