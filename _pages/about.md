---
permalink: /
title: "Kenneth Zhang"
author_profile: true
redirect_from:
  - /about/
  - /about.html
---

{% include base_path %}

<p class="research-eyebrow">Research portfolio · HKUST(GZ) Red Bird MPhil applicant</p>

<p class="research-lead">I study learning-guided combinatorial optimization for constrained routing, where strong solvers, learned priors, and careful evidence meet.</p>

<p class="research-copy">My current work asks a practical question: how can learning improve a trusted heuristic without hiding the mechanism that makes it reliable? I build hybrid optimization systems for intelligent logistics, then test not only whether they work, but why they work and when they fail.</p>

<div class="signal-row" aria-label="Research highlights">
  <div class="signal">
    <span class="signal__value">12 / 12</span>
    <span class="signal__label">portfolio-best matches on public finite-L BWTSP instances</span>
  </div>
  <div class="signal">
    <span class="signal__value">3.10x</span>
    <span class="signal__label">lower selection cost with guarded configuration choice</span>
  </div>
  <div class="signal">
    <span class="signal__value">2</span>
    <span class="signal__label">connected research lines in constrained routing</span>
  </div>
</div>

## Research interests

<div class="research-grid">
  <article class="research-card">
    <span class="research-card__tag">Optimization</span>
    <h3>Learning-guided search</h3>
    <p>Combining learned structural signals with large-neighborhood and local-search heuristics.</p>
  </article>
  <article class="research-card">
    <span class="research-card__tag">Routing</span>
    <h3>Constrained decision systems</h3>
    <p>Budgeted, energy-aware, and payload-dependent routing for intelligent logistics.</p>
  </article>
  <article class="research-card">
    <span class="research-card__tag">Methodology</span>
    <h3>Reliable empirical claims</h3>
    <p>Benchmark design, ablation studies, route diagnostics, and evaluation under distribution shift.</p>
  </article>
  <article class="research-card">
    <span class="research-card__tag">Research direction</span>
    <h3>Interpretable hybrid solvers</h3>
    <p>Optimization systems whose learned components are useful, inspectable, and anchored in dependable search.</p>
  </article>
</div>

## Current focus

I am developing a learned structural-prior guided Population-LKH framework for the Budgeted Weighted Traveling Salesman Problem (BWTSP). The framework combines learned edge priors, adaptive prior policies, and a guarded selector to guide strong local search under finite-L constraints.

<figure>
  <img src="{{ base_path }}/images/research-framework.png" alt="Learning-guided Population-LKH research framework" />
  <figcaption>Research framework: learned structural priors guide classical combinatorial search while retaining the solver's search backbone.</figcaption>
</figure>

The next research step is energy-constrained drone delivery with payload-dependent energy consumption and optional charging stations. I am exploring when edge-level information is sufficient, when move- and route-state-aware guidance becomes necessary, and how hybrid methods behave at scale.

<div class="evidence-note">
  <p><strong>Selected result.</strong> On twelve public finite-L BWTSP instances, the guarded selector matched the portfolio-best configuration in all twelve cases while reducing selection cost by approximately 3.10x.</p>
</div>

## Explore the work

Read the two project narratives in [Research Projects]({{ base_path }}/portfolio/) or follow the ongoing code and experiment trail on [GitHub](https://github.com/KennethZhang29).
