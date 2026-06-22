# Station 06 - Quantization Benchmark

> Phase: **Phase 2 — SERVE** | Estimated time: **2 days**

## Objective

Take your SFT model. Quantize to FP16 -> BF16 -> AWQ-4bit -> GPTQ-4bit -> GGUF-Q4_K_M. Benchmark each on latency, memory, quality.

## What you'll build

5 model variants + benchmark CSV + plot showing latency/memory/quality tradeoff.

## What you'll learn

- What 4-bit quantization actually does to model weights
- AWQ vs GPTQ vs GGUF: when to use each
- k-quants (Q4_K_M, Q5_K_M, Q8_0) - llama.cpp's naming
- Quality cliff: how much accuracy you lose per bit
- Memory math: 8B FP16 = 16GB, 4-bit = ~5GB
- When quantization breaks LoRA (and how to fix)

## Resources (only runnable ones)

- [HF AutoAWQ docs](https://github.com/casper-hansen/AutoAWQ)
- [AutoGPTQ docs](https://github.com/AutoGPTQ/AutoGPTQ)
- [llama.cpp README (GGUF + k-quants)](https://github.com/ggerganov/llama.cpp)
- [Unsloth Dynamic GGUF](https://unsloth.ai/docs/basics/dynamic-2-0-ggufs)

## Artifact (the commit)

Benchmark CSV + plot in `assets/` + writeup of which quant is best for your use case.

## Success criteria

- [ ] All 5 quant variants generated and loadable
- [ ] Benchmark CSV has 5 rows with latency (p50/p95), VRAM, F1
- [ ] Plot committed in `assets/quant_tradeoff.png`
- [ ] Winner recommended for production (likely AWQ-4bit)

## Files in this folder

- `notebook.ipynb` or `script.py` - the actual build (you create this)
- `what-i-built.md` - 1 paragraph on what you shipped (you create this)
- `what-i-learned.md` - 1 page max on what clicked (you create this)
- `artifact.md` - links to HF Hub models/datasets, screenshots, demo URLs (you create this)
- `assets/` - screenshots, plots, CSVs (you create this)

## When this station is done

Update `../progress.md` to check all boxes. Only then may you open Station 07's resources.
