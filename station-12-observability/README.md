# Station 12 - Observability with Langfuse

> Phase: **Phase 4 — EXPAND** | Estimated time: **2 days**

## Objective

Self-host Langfuse. Instrument every model call in your workbench. Build a dashboard: p95 latency, refusal rate, hallucination rate by category, drift over time.

## What you'll build

Langfuse self-hosted via docker-compose + instrumented workbench + dashboard screenshot + alert config.

## What you'll learn

- Tracing vs metrics vs logs: when each matters
- OpenTelemetry basics: spans, traces, attributes
- Langfuse data model: traces, observations (generations/spans/events), scores
- What to actually monitor in prod: latency, cost, refusal rate, hallucination rate, drift
- Alerting: threshold-based + anomaly-based
- Why JSONL logs (your V1) aren't enough for prod debugging

## Resources (only runnable ones)

- [Langfuse self-host docs](https://langfuse.com/self-hosting)
- [Langfuse Python SDK](https://langfuse.com/docs/sdk/python/decorators)
- [OpenTelemetry primer (skim)](https://opentelemetry.io/docs/what-is-opentelemetry/)

## Artifact (the commit)

Dashboard screenshot showing p95 latency + refusal rate by risk category + alert config for 'refusal rate spiked'.

## Success criteria

- [ ] Langfuse self-hosted via docker-compose on Linux
- [ ] Every model call in workbench instrumented (trace + observation)
- [ ] Dashboard shows: p95 latency, refusal rate, hallucination rate by category
- [ ] Alert config saved for 'refusal rate > 30% in 1-hour window'
- [ ] Screenshot committed to `assets/`

## Files in this folder

- `notebook.ipynb` or `script.py` - the actual build (you create this)
- `what-i-built.md` - 1 paragraph on what you shipped (you create this)
- `what-i-learned.md` - 1 page max on what clicked (you create this)
- `artifact.md` - links to HF Hub models/datasets, screenshots, demo URLs (you create this)
- `assets/` - screenshots, plots, CSVs (you create this)

## When this station is done

Update `../progress.md` to check all boxes. **This is the final station — you're done.**
