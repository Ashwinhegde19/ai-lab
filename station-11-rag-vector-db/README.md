# Station 11 - RAG with Vector DB

> Phase: **Phase 4 — EXPAND** | Estimated time: **3 days**

## Objective

Replace V1 keyword retrieval with: BGE-M3 embeddings + Chroma DB + bge-reranker. Measure retrieval quality.

## What you'll build

Chroma DB instance + BGE-M3 embedder + bge-reranker + retrieval eval (recall@5, MRR, latency).

## What you'll learn

- Chunking strategies: fixed-size, recursive, semantic, late chunking
- BGE-M3: multilingual, dense + sparse + multi-vector retrieval
- Vector DBs: Chroma (dev) vs Qdrant (prod) vs pgvector (existing Postgres)
- Re-ranking: why BM25 + vector + reranker beats vector alone
- Retrieval eval metrics: recall@k, MRR, nDCG
- Long-context vs RAG tradeoffs

## Resources (only runnable ones)

- [Chroma quickstart](https://docs.trychroma.com/)
- [BGE-M3 HF model card](https://huggingface.co/BAAI/bge-m3)
- [bge-reranker-v2-m3 HF model card](https://huggingface.co/BAAI/bge-reranker-v2-m3)
- [LangChain RAG tutorial (reference)](https://python.langchain.com/docs/tutorials/rag)

## Artifact (the commit)

Retrieval eval CSV + writeup of which chunking strategy worked best for AI safety docs.

## Success criteria

- [ ] Chroma DB populated with 50+ AI safety documents
- [ ] BGE-M3 embeddings + bge-reranker wired in
- [ ] Retrieval eval: recall@5 >= 0.7 on hand-labelled queries
- [ ] Latency: end-to-end retrieval < 500ms

## Files in this folder

- `notebook.ipynb` or `script.py` - the actual build (you create this)
- `what-i-built.md` - 1 paragraph on what you shipped (you create this)
- `what-i-learned.md` - 1 page max on what clicked (you create this)
- `artifact.md` - links to HF Hub models/datasets, screenshots, demo URLs (you create this)
- `assets/` - screenshots, plots, CSVs (you create this)

## When this station is done

Update `../progress.md` to check all boxes. Only then may you open Station 12's resources.
