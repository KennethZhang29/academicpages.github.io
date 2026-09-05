---
title: "Learned Structural-Prior Guided Population-LKH for BWTSP"
excerpt: "A neural-combinatorial optimization framework that guides strong Population-LKH search with learned edge priors, adaptive policies, and a guarded selector."
collection: portfolio
header:
  teaser: research-framework.png
---

This project asks how learning can improve a trusted solver without replacing its search machinery. I designed a framework that uses learned structural priors to choose, prune, and prioritize candidate decisions for Population-LKH on finite-L Budgeted Weighted Traveling Salesman Problem instances.

The key research questions are:

- Can learned edge information improve the quality-cost trade-off of a high-performing classical heuristic?
- When should the solver use an aggressive prior, a conservative prior, or no learned guidance?
- Can a low-cost selector predict the best option in a portfolio of guided search configurations?

Across twelve public finite-L instances, the guarded selector matched the portfolio-best choice in all twelve cases while using about 3.10x less selection cost. The study emphasizes mechanism checks and ablations, not only end metrics.

![Ablation results for guided BWTSP search]({{ base_path }}/images/ablation.png)
