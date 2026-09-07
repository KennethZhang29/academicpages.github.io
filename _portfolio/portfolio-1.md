---
title: "Cluster-Aware Learned Edge Priors for Guiding LKH Solvers on Constrained Clustered Traveling Salesman Problems"
excerpt: "A learning-enhanced Population-LKH framework for constrained clustered TSPs, combining structural edge priors, adaptive sparsification, and guarded solver selection."
collection: portfolio
header:
  teaser: cover-learned-search.jpg
---

This project studies how machine learning can improve a strong classical optimizer without replacing its search machinery. The framework targets constrained clustered routing problems, with finite-L BWTSP as the main testbed and CTSP-d as a transfer setting.

**Role:** Sole author. I formulated the research problem, designed and implemented the complete learning-and-solver pipeline, built the evaluation protocol, ran the experiments and ablations, analyzed the results, and wrote the manuscript.

## Research Problem

Classical local-search and evolutionary operators are effective at reducing tour length, but they are often blind to non-local structural constraints. In BWTSP, for example, a sequence of individually short edges can still violate limits on the number of ordinary nodes or the cumulative distance between constrained nodes.

The central question is:

> Can a learned, constraint-conditioned structural prior reshape the candidate space explored by LKH while preserving the reliability of the underlying solver?

The study also asks when guidance should be sparse or broad, which guided solver configuration should be used for a given instance, and whether those decisions generalize beyond the training distribution.

## Method

The method is a two-stage learning-enhanced Population-LKH pipeline:

1. **Construct structural candidates.** Local, anchor, bridge, and seed-adjacency edge families combine geometric proximity, constraint-critical transitions, and evidence from Weak-LKH and Population-LKH seed tours.
2. **Learn edge utility.** A Transformer-based edge-prior network jointly encodes coordinates, structural labels, and seed-tour topology to score candidate edges.
3. **Adapt prior density.** An instance-level policy chooses whether to retain all candidates or apply a learned top-k or top-ratio sparsification rule.
4. **Guide classical search.** The sparse prior is injected through LKH's native `EDGE_FILE` interface, leaving the solver's local-search mechanics intact.
5. **Select robustly.** A learned variant selector chooses among guided configurations, while confidence- and sparsity-triggered hedge guards preserve fallback options under prediction error.

![Two-stage cluster-aware edge-prior guided Population-LKH framework]({{ site.baseurl }}/images/research-figures/guided-lkh-method.png)

## Experimental Results

- **Development benchmark:** On 12 archive-calibrated finite-L BWTSP instances, the full development-tuned pipeline reduced aggregate constraint penalty from 35,452 to 1,497 (**95.8%**) and aggregate tour length from 1,102,425 to 1,045,630 (**5.2%**) relative to Population LKH.
- **Held-out generalization:** When all learned components were trained only on generated instances, the selector reduced mean aggregate penalty by **61.4%** and mean tour length by **2.6%**, while increasing the mean number of feasible instances from **4.4 to 7.4**. It won or tied lexicographically on all 12 evaluated instances across the paired comparison.
- **Cross-size behavior:** On unseen generated instances with 600, 800, and 1,000 nodes, the learned-prior oracle reduced aggregate tour length by **3.5%**; the practical guarded selector achieved a **1.0%** reduction.
- **Ablation evidence:** A handcrafted structural prior already reduced penalty by **78.4%**. Learned ranking, sparsification, selection, and hedge guards raised the reduction to **95.8%**, supporting the value of each stage beyond candidate construction alone.

![Results for guided finite-L BWTSP search, including development, holdout, and cross-size evidence]({{ site.baseurl }}/images/research-figures/guided-lkh-results.png)

## Interpretation and Limitations

The strongest 12-instance result uses public-suite fine-tuning and should be read as development-benchmark performance. The generated-only evaluation provides cleaner evidence of transfer but remains limited in scale, and the multi-seed comparison did not support a statistical-significance claim. CTSP-d experiments show useful structural transfer, although the current guided portfolio does not outperform the strongest penalty-transformed LKH baseline.

The main takeaway is therefore measured: learned structural priors can substantially improve a strong solver, but selector calibration and evaluation under distribution shift remain important open problems.
