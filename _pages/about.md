---
permalink: /
title: "Kenneth Zhang"
author_profile: true
redirect_from:
  - /about/
  - /about.html
---

{% include base_path %}

I am an early-career researcher interested in **learning-guided combinatorial optimization**: methods that combine the reliability of strong classical heuristics with learned structural signals.

My current work studies constrained routing problems where feasibility, route structure, and computational budget must be considered together. I am especially interested in intelligent logistics, neural-combinatorial optimization, and evaluation practices that turn experimental results into credible scientific claims.

## Research interests

- Learning-guided heuristic search and large-neighborhood optimization
- Constrained routing, including budgeted and energy-aware variants
- Intelligent logistics and decision systems
- Benchmark design, ablation studies, and robust evaluation

## Current focus

I am developing a learned structural-prior guided Population-LKH framework for the Budgeted Weighted Traveling Salesman Problem (BWTSP). The project uses learned edge priors, adaptive prior policies, and a guarded selector to guide strong local search under finite-L constraints.

The next step is to extend these ideas to payload-dependent, energy-constrained drone delivery with optional charging stations. I want to understand when edge-level information is enough, when move- and state-aware guidance is necessary, and how hybrid methods hold up under scale and distribution shift.

<figure>
  <img src="{{ base_path }}/images/research-framework.png" alt="Learning-guided Population-LKH research framework" />
  <figcaption>Research framework: learned structural priors guide classical combinatorial search.</figcaption>
</figure>

## Selected evidence

On twelve public finite-L BWTSP instances, the guarded selector matched the portfolio-best configuration on all twelve cases while reducing selection cost by approximately 3.10x. The project includes benchmark tables, route visualizations, ablation studies, and a research proposal for the next application domain.

## Contact

My code and ongoing project work are available on [GitHub](https://github.com/KennethZhang29). I welcome conversations about research collaboration, MPhil supervision fit, and intelligent logistics.
