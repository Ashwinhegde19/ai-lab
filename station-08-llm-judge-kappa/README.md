# Station 08 - LLM-as-Judge + Cohen's kappa

> Phase: **Phase 3 — EVALUATE** | Estimated time: **3 days**

## Objective

Use GPT-4o-mini as judge on your risk-classifier outputs. Compare judge labels vs ground truth. Compute Cohen's kappa. Document judge biases.

## What you'll build

Judge module + 200-example judge eval + kappa score + `judge_calibration.md` writeup documenting biases.

## What you'll learn

- LLM-as-judge: rubric design, pointwise vs pairwise vs rubric grading
- Judge biases: position bias, length bias, verbosity bias, self-preference
- Cohen's kappa: chance-corrected inter-annotator agreement
- Krippendorff's alpha: when labels are ordinal or missing
- How to mitigate biases: swap positions, average over orderings, use 2 judges
- When judge is right vs when ground truth is right (judges sometimes know better)

## Resources (only runnable ones)

- [DeepLearning.ai - Building and Evaluating Advanced RAG Applications (TruLens)](https://www.deeplearning.ai/short-courses/building-evaluating-advanced-rag/)
- [sklearn.metrics.cohen_kappa_score docs](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.cohen_kappa_score.html)
- [Krippendorff's alpha paper (skim intro only)](https://www.enhd.org/iss4/vol3iss4_article1.pdf)

## Artifact (the commit)

`judge_calibration.md` writeup (1-2 pages) documenting: kappa score, identified biases, mitigation strategies applied.

## Success criteria

- [ ] 200 risk-classifier outputs judged by GPT-4o-mini
- [ ] Cohen's kappa >= 0.6 (substantial agreement) OR honest writeup of why it's lower
- [ ] At least 2 judge biases identified and documented
- [ ] Mitigation strategy applied + kappa improvement measured

## Files in this folder

- `notebook.ipynb` or `script.py` - the actual build (you create this)
- `what-i-built.md` - 1 paragraph on what you shipped (you create this)
- `what-i-learned.md` - 1 page max on what clicked (you create this)
- `artifact.md` - links to HF Hub models/datasets, screenshots, demo URLs (you create this)
- `assets/` - screenshots, plots, CSVs (you create this)

## When this station is done

Update `../progress.md` to check all boxes. Only then may you open Station 09's resources.
