---
layout: profile
permalink: /
title: "Yuyao Zhang | Learning-Augmented Optimization"
author_profile: false
redirect_from:
  - /about/
  - /about.html
---

{% include base_path %}

<section class="route-hero" id="home" aria-labelledby="route-hero-title">
  <div class="route-hero__copy">
    <p class="route-kicker"><span>01</span> Learning-Augmented Optimization</p>
    <h1 id="route-hero-title"><span>Yuyao</span><span>Zhang</span></h1>
    <p class="route-hero__cn">张誉耀</p>
    <p class="route-hero__lead">I study how learning can help strong classical optimization solvers make better decisions.</p>
    <div class="route-hero__actions">
      <a class="route-button route-button--primary" href="#research">Explore research <i class="fa-solid fa-arrow-right" aria-hidden="true"></i></a>
      <a class="route-button" href="https://github.com/KennethZhang29"><i class="fab fa-github" aria-hidden="true"></i> GitHub</a>
      <a class="route-button" href="{{ base_path }}/cv/"><i class="fa-solid fa-file-lines" aria-hidden="true"></i> CV</a>
    </div>
  </div>

  <aside class="route-status" aria-label="Current research coordinates">
    <p class="route-status__label">Current coordinates</p>
    <div class="route-status__row">
      <span>Base</span>
      <strong>Guangzhou · Macau · Zhuhai</strong>
    </div>
    <div class="route-status__row">
      <span>Affiliation</span>
      <strong>Faculty of Data Science, City University of Macau</strong>
    </div>
    <div class="route-status__row">
      <span>Research question</span>
      <strong>Can learned structure guide reliable search?</strong>
    </div>
    <div class="route-status__row route-status__row--accent">
      <span>Status</span>
      <strong><i aria-hidden="true"></i> Building, testing, explaining</strong>
    </div>
  </aside>

  <a class="route-scroll" href="#about" aria-label="Continue to about section">
    <span>Scroll to trace the route</span>
    <i class="fa-solid fa-arrow-down" aria-hidden="true"></i>
  </a>
</section>

<section class="route-section route-about" id="about" aria-labelledby="about-title">
  <div class="route-section__index" aria-hidden="true">02 / PROFILE</div>
  <div class="route-about__portrait">
    <img src="{{ base_path }}/images/yuyao-zhang.jpg" alt="Portrait of Yuyao Zhang" />
    <p>Undergraduate researcher<br>City University of Macau</p>
  </div>
  <div class="route-about__copy">
    <p class="route-kicker"><span>About</span> Researcher behind the routes</p>
    <h2 id="about-title">Classical search backbone.<br>Learned structural hints.</h2>
    <p>I am an undergraduate student in the Faculty of Data Science at City University of Macau. My research interests lie at the intersection of machine learning, combinatorial optimization, and intelligent transportation.</p>
    <p>Rather than asking neural networks to construct entire solutions from scratch, I explore how learned information, including promising candidate edges, route-state signals, and feasibility-aware patterns, can guide established methods such as Population-LKH and local search.</p>
    <p>I am particularly interested in routing problems shaped by real-world constraints: customer groups, priority rules, charging stations, battery capacity, and time windows. Beyond model performance, I care about reliable experimentation, interpretable improvements, and understanding why a method works or fails.</p>
    <div class="route-interest-line" aria-label="Research interests">
      <span>Learning-Augmented Optimization</span>
      <span>Evolutionary Computation</span>
      <span>Reinforcement Learning</span>
      <span>Vehicle Routing</span>
      <span>Energy-Constrained Delivery</span>
    </div>
  </div>
</section>

<section class="route-section route-research" id="research" aria-labelledby="research-title">
  <div class="route-section__index" aria-hidden="true">03 / RESEARCH</div>
  <header class="route-section__header">
    <p class="route-kicker"><span>Selected work</span> Problem → Method → Evidence</p>
    <h2 id="research-title">Research is a sequence of decisions.</h2>
    <p>These projects connect one research theme: using learned structure to make constrained search more effective, robust, and explainable.</p>
  </header>

  <article class="route-project">
    <figure class="route-project__visual">
      <img src="{{ base_path }}/images/research-framework.png" alt="Framework for learned structural-prior guided Population-LKH" />
      <figcaption>01 · Learned structural priors guiding Population-LKH</figcaption>
    </figure>
    <div class="route-project__copy">
      <p class="route-project__number">PROJECT 01</p>
      <h3>Learned Structural-Prior Guided Population-LKH for BWTSP</h3>
      <p>A neural-combinatorial framework that learns promising candidate edges, adapts the prior policy, and uses a guarded selector to guide strong finite-L search.</p>
      <dl class="route-project__facts">
        <div><dt>Problem</dt><dd>Budgeted weighted TSP</dd></div>
        <div><dt>Method</dt><dd>Edge priors + adaptive selection</dd></div>
        <div><dt>Evidence</dt><dd>12 / 12 portfolio-best matches</dd></div>
      </dl>
      <a href="{{ base_path }}/portfolio/portfolio-1/">Read the project <i class="fa-solid fa-arrow-right" aria-hidden="true"></i></a>
    </div>
  </article>

  <article class="route-project route-project--reverse">
    <figure class="route-project__visual">
      <img src="{{ base_path }}/images/route-comparison.png" alt="Route comparison for constrained routing experiments" />
      <figcaption>02 · Route-level inspection under practical constraints</figcaption>
    </figure>
    <div class="route-project__copy">
      <p class="route-project__number">PROJECT 02</p>
      <h3>Energy-Constrained Delivery for Drones and Electric Vehicles</h3>
      <p>An ongoing research direction extending static edge guidance toward move- and route-state-aware optimization for payload-dependent energy routing and optional charging stations.</p>
      <dl class="route-project__facts">
        <div><dt>Problem</dt><dd>Energy-aware delivery</dd></div>
        <div><dt>Signals</dt><dd>Edge + move + route state</dd></div>
        <div><dt>Goal</dt><dd>Robust feasibility-aware search</dd></div>
      </dl>
      <a href="{{ base_path }}/portfolio/portfolio-2/">Read the project <i class="fa-solid fa-arrow-right" aria-hidden="true"></i></a>
    </div>
  </article>
</section>

<section class="route-evidence" aria-labelledby="evidence-title">
  <div class="route-evidence__copy">
    <p class="route-kicker"><span>Evidence</span> Not just a final score</p>
    <h2 id="evidence-title">I want results that survive inspection.</h2>
    <p>My workflow combines benchmark design, route visualization, ablation studies, and mechanism-level diagnostics. A suspiciously good result is the beginning of the investigation, not the end.</p>
    <div class="route-metrics">
      <div><strong>12 / 12</strong><span>portfolio-best matches</span></div>
      <div><strong>3.10×</strong><span>lower selection cost</span></div>
      <div><strong>2</strong><span>connected routing research lines</span></div>
    </div>
  </div>
  <figure class="route-evidence__visual">
    <img src="{{ base_path }}/images/ablation.png" alt="Ablation results for learning-guided BWTSP search" />
    <figcaption>Ablation view · isolating the contribution of guidance, adaptation, and selection</figcaption>
  </figure>
</section>

<section class="route-section route-journey" id="journey" aria-labelledby="journey-title">
  <div class="route-section__index" aria-hidden="true">04 / JOURNEY</div>
  <header class="route-section__header">
    <p class="route-kicker"><span>Trajectory</span> Three cities, one research direction</p>
    <h2 id="journey-title">Macau → Guangzhou → the next problem.</h2>
  </header>

  <div class="route-journey__line" aria-label="Education and research experience">
    <article>
      <span class="route-journey__node" aria-hidden="true">MO</span>
      <p class="route-journey__date">2023–2027</p>
      <h3>Undergraduate Study</h3>
      <p>Faculty of Data Science<br>City University of Macau</p>
    </article>
    <article>
      <span class="route-journey__node" aria-hidden="true">GZ</span>
      <p class="route-journey__date">Jun–Aug 2026</p>
      <h3>Research Assistant</h3>
      <p>iLSCA Lab<br>HKUST (Guangzhou)</p>
    </article>
    <article>
      <span class="route-journey__node" aria-hidden="true">ZH</span>
      <p class="route-journey__date">Current network</p>
      <h3>Greater Bay Area</h3>
      <p>Guangzhou · Macau · Zhuhai<br>Research without a single coordinate</p>
    </article>
  </div>
</section>

<section class="route-section route-methods" aria-labelledby="methods-title">
  <div class="route-section__index" aria-hidden="true">05 / METHODS</div>
  <header class="route-section__header">
    <p class="route-kicker"><span>Working style</span> Build, test, inspect, explain</p>
    <h2 id="methods-title">A practical research loop.</h2>
  </header>
  <div class="route-methods__grid">
    <div><i class="fa-solid fa-code" aria-hidden="true"></i><strong>Build</strong><span>Python research engineering</span></div>
    <div><i class="fa-solid fa-gears" aria-hidden="true"></i><strong>Search</strong><span>Heuristics and evolutionary methods</span></div>
    <div><i class="fa-solid fa-brain" aria-hidden="true"></i><strong>Learn</strong><span>Structural priors and reinforcement learning</span></div>
    <div><i class="fa-solid fa-flask" aria-hidden="true"></i><strong>Test</strong><span>Reproducible experiments and ablations</span></div>
    <div><i class="fa-solid fa-chart-line" aria-hidden="true"></i><strong>Inspect</strong><span>Benchmark and route diagnostics</span></div>
    <div><i class="fa-solid fa-file-lines" aria-hidden="true"></i><strong>Explain</strong><span>Clear claims and research narratives</span></div>
  </div>
</section>

<section class="route-contact" aria-labelledby="contact-title">
  <p class="route-kicker"><span>06</span> Keep the route open</p>
  <h2 id="contact-title">Interested in optimization that works in the real world.</h2>
  <div class="route-contact__links">
    <a href="https://github.com/KennethZhang29"><i class="fab fa-github" aria-hidden="true"></i> GitHub</a>
    <a href="{{ base_path }}/cv/"><i class="fa-solid fa-file-lines" aria-hidden="true"></i> Curriculum Vitae</a>
    <a href="{{ base_path }}/portfolio/"><i class="fa-solid fa-diagram-project" aria-hidden="true"></i> Research Projects</a>
  </div>
</section>
