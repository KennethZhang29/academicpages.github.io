---
permalink: /
title: "Yuyao Zhang (张誉耀)"
author_profile: true
redirect_from:
  - /about/
  - /about.html
---

{% include base_path %}

<p class="research-eyebrow">Undergraduate researcher · City University of Macau</p>

<p class="research-lead">My research interests lie at the intersection of machine learning, combinatorial optimization, and intelligent transportation.</p>

<p class="research-copy">My current work centers on a simple question: <strong>How can learning help strong classical optimization solvers make better decisions?</strong> Rather than relying on neural networks to construct complete solutions from scratch, I explore how learned structural information can guide established optimization methods.</p>

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

## About me

I am an undergraduate student in the Faculty of Data Science at City University of Macau. My work explores how structural information, such as promising candidate edges, route-state signals, and feasibility-aware patterns, can guide solvers including Population-LKH and local search.

I am particularly interested in routing problems shaped by real-world constraints, including customer groups, priority rules, charging stations, battery capacity, and time windows. My recent work includes learning-guided approaches for constrained clustered traveling salesman problems, as well as ongoing research on energy-constrained delivery planning for drones and electric vehicles.

Beyond model performance, I care about reliable experimentation, interpretable improvements, and understanding why an optimization method works or fails. When I am not debugging a routing instance or investigating a suspiciously good result, I enjoy thinking about how machine learning and optimization can work together to solve practical operational problems.

## Education & experience

<div class="profile-timeline">
  <article class="timeline-entry">
    <span class="timeline-entry__icon" aria-hidden="true"><i class="fa-solid fa-flask"></i></span>
    <div>
      <span class="timeline-entry__date">Jun 2026 – Aug 2026</span>
      <h3>Research Assistant</h3>
      <p>iLSCA Lab, The Hong Kong University of Science and Technology (Guangzhou)</p>
    </div>
  </article>
  <article class="timeline-entry">
    <span class="timeline-entry__icon" aria-hidden="true"><i class="fa-solid fa-graduation-cap"></i></span>
    <div>
      <span class="timeline-entry__date">2023 – 2027 (expected)</span>
      <h3>Undergraduate Study</h3>
      <p>Faculty of Data Science, City University of Macau</p>
    </div>
  </article>
</div>

## Research interests

<div class="research-grid">
  <article class="research-card">
    <span class="research-card__icon" aria-hidden="true"><i class="fa-solid fa-brain"></i></span>
    <span class="research-card__tag">Optimization</span>
    <h3>Learning-guided search</h3>
    <p>Combining learned structural signals with large-neighborhood and local-search heuristics.</p>
  </article>
  <article class="research-card">
    <span class="research-card__icon" aria-hidden="true"><i class="fa-solid fa-route"></i></span>
    <span class="research-card__tag">Routing</span>
    <h3>Constrained decision systems</h3>
    <p>Budgeted, energy-aware, and payload-dependent routing for intelligent logistics.</p>
  </article>
  <article class="research-card">
    <span class="research-card__icon" aria-hidden="true"><i class="fa-solid fa-chart-line"></i></span>
    <span class="research-card__tag">Methodology</span>
    <h3>Reliable empirical claims</h3>
    <p>Benchmark design, ablation studies, route diagnostics, and evaluation under distribution shift.</p>
  </article>
  <article class="research-card">
    <span class="research-card__icon" aria-hidden="true"><i class="fa-solid fa-diagram-project"></i></span>
    <span class="research-card__tag">Research direction</span>
    <h3>Interpretable hybrid solvers</h3>
    <p>Optimization systems whose learned components are useful, inspectable, and anchored in dependable search.</p>
  </article>
</div>

## Methods & tools

<div class="method-strip" aria-label="Methods and tools">
  <span><i class="fa-solid fa-code" aria-hidden="true"></i>Python research engineering</span>
  <span><i class="fa-solid fa-gears" aria-hidden="true"></i>Heuristic search</span>
  <span><i class="fa-solid fa-layer-group" aria-hidden="true"></i>Learning-guided optimization</span>
  <span><i class="fa-solid fa-flask" aria-hidden="true"></i>Reproducible experiments</span>
  <span><i class="fa-solid fa-database" aria-hidden="true"></i>Benchmark analysis</span>
  <span><i class="fa-solid fa-battery-half" aria-hidden="true"></i>Energy-aware routing</span>
</div>

## Current focus

I am developing a learned structural-prior guided Population-LKH framework for the Budgeted Weighted Traveling Salesman Problem (BWTSP). The framework combines learned edge priors, adaptive prior policies, and a guarded selector to guide strong local search under finite-L constraints.

<figure>
  <img src="{{ base_path }}/images/research-framework.png" alt="Learning-guided Population-LKH research framework" />
  <figcaption>Research framework: learned structural priors guide classical combinatorial search while retaining the solver's search backbone.</figcaption>
</figure>

The next research step is energy-constrained drone delivery with payload-dependent energy consumption and optional charging stations. I am exploring when edge-level information is sufficient, when move- and route-state-aware guidance becomes necessary, and how hybrid methods behave at scale.

## Research snapshots

<div class="snapshot-grid">
  <figure>
    <img src="{{ base_path }}/images/route-comparison.png" alt="Route comparison from constrained routing experiments" />
    <figcaption>Route-level comparison: inspecting how learned guidance changes feasible search behavior.</figcaption>
  </figure>
  <figure>
    <img src="{{ base_path }}/images/ablation.png" alt="Ablation results for learning-guided search" />
    <figcaption>Ablation view: separating the contribution of guidance, adaptation, and selection.</figcaption>
  </figure>
</div>

<div class="evidence-note">
  <p><strong>Selected result.</strong> On twelve public finite-L BWTSP instances, the guarded selector matched the portfolio-best configuration in all twelve cases while reducing selection cost by approximately 3.10x.</p>
</div>

## Explore the work

Read the two project narratives in [Research Projects]({{ base_path }}/portfolio/) or follow the ongoing code and experiment trail on [GitHub](https://github.com/KennethZhang29).
