# Progress Tracker

> Update this file every time you commit a station. The satisfaction of marking a station `[x]` is real — use it.

## Phase A — 7-day MVP (prove it works)

- [ ] **Repo foundation**
  - [ ] `git init` done
  - [ ] GitHub repo created (`ai-lab`)
  - [ ] First commit pushed
  - [ ] `modal/BUDGET.md` reviewed

- [ ] **Station 01 — SFT Basics** (1 day max, don't polish)
  - [ ] Unsloth Alpaca notebook runs end-to-end on Colab free
  - [ ] LoRA adapter saved (1 format is enough for MVP)
  - [ ] Loss curve screenshot in `station-01-sft-basics/assets/`
  - [ ] `what-i-learned.md` written (1 paragraph)
  - [ ] Committed to GitHub

- [ ] **Station 02-lite — SFT on 20-example seed** (2-3 days)
  - [ ] Run `validate_dataset.py` on `data/risk_dataset.jsonl` → 0 errors
  - [ ] `station-02-sft-own-dataset/notebook.ipynb` runs end-to-end
  - [ ] Eval CSV produced (`eval/results.csv`) — even if numbers are bad
  - [ ] LoRA adapter saved to HF Hub
  - [ ] `what-i-built.md` + `what-i-learned.md` written
  - [ ] Committed to GitHub

**Phase A exit:** Working SFT loop on your own data. Don't optimize. Move to Phase B.

---

## Phase B — Portfolio quality (the V2 spine, ships by early August)

- [ ] **Station 02 (full) — Scale dataset to 1000 examples** (5-7 days)
  - [ ] 200 examples reached (across all 6 categories)
  - [ ] `harmful` category populated (currently 0 in seed)
  - [ ] 500 examples reached
  - [ ] 1000 examples reached
  - [ ] Train/val split (80/20)
  - [ ] Fine-tune Llama-3-8B via QLoRA on Modal A100
  - [ ] Eval CSV: precision >= 0.85, F1 >= 0.80
  - [ ] Adapter + dataset pushed to HF Hub
  - [ ] Committed to GitHub

- [ ] **Station 07 — Structured Output** (1 day)
  - [ ] outlines/xgrammar wired into the classifier
  - [ ] 100% valid JSON on 100 test prompts
  - [ ] Before/after CSV
  - [ ] Committed to GitHub

- [ ] **Station 08 — LLM-as-Judge + Cohen's kappa** (3 days)
  - [ ] GPT-4o-mini judge runs on classifier outputs
  - [ ] Cohen's kappa computed
  - [ ] Judge bias analysis documented in `judge_calibration.md`
  - [ ] Committed to GitHub

- [ ] **Station 05 — vLLM + LoRA Hot-Swap** (2 days)
  - [ ] vLLM server with base + SFT adapter (skip DPO/GRPO for now)
  - [ ] `test_curl.sh` works
  - [ ] p95 latency measured
  - [ ] Committed to GitHub

- [ ] **Station 10 — Guardrails Upgrade** (2 days)
  - [ ] Llama Guard 3 wired as output classifier
  - [ ] Prompt Guard wired as input classifier
  - [ ] Before/after eval CSV
  - [ ] Committed to GitHub

- [ ] **August V2 email sent** to `work@ollive.ai`
  - [ ] 1-page eval PDF generated
  - [ ] 5-min Loom demo recorded
  - [ ] Email sent with repo link + PDF + Loom

**Phase B exit:** V2 deliverable shipped to Ollive founder.

---

## Phase C — Advanced (after August, for parallel applications)

- [ ] **Station 06 — Quantization Benchmark** (2 days)
- [ ] **Station 09 — Public Benchmarks** (2 days)
- [ ] **Station 12 — Observability with Langfuse** (2 days)
- [ ] **Station 11 — RAG with Vector DB** (3 days)
- [ ] **Station 03 — DPO** (3 days, only if SFT+eval+serving are solid)
- [ ] **Station 04 — GRPO** (5-7 days, only if 2+ weeks spare — it's a time sink)

---

## Founder emails (the August goal)

- [ ] **July (~3-week mark)**: Send lightweight check-in email (1 small artifact)
- [ ] **Early August**: Send V2 email with repo link + 1-page PDF + 5-min Loom demo

## Parallel applications (start in Week 2, not after)

- [ ] Repello AI (Bengaluru) — applied
- [ ] Patronus AI (SF, remote) — applied
- [ ] Lakera (Zurich, remote) — applied
- [ ] Protect AI — applied
- [ ] Cranium / HiddenLayer / AIShield — applied
- [ ] Scale AI eval team — applied
- [ ] Robust Intelligence (Cisco) — applied

## Anti-procrastination log

Whenever you catch yourself opening a "new thing to learn" before finishing the current station, log it here. Patterns will emerge.

| Date | What I almost opened | What I did instead |
|---|---|---|
| | | |
