---
layout: profile
permalink: /
title: "Kenneth Zhang | Learning-Augmented Optimization"
author_profile: false
redirect_from:
  - /about/
  - /about.html
---

{% include base_path %}

<aside class="folio-side folio-side--left" aria-label="Profile links">
  <a href="https://github.com/KennethZhang29" aria-label="GitHub" title="GitHub"><i class="fab fa-github" aria-hidden="true"></i></a>
  <a href="{{ base_path }}/cv/" aria-label="Curriculum vitae" title="CV"><i class="fa-solid fa-file-lines" aria-hidden="true"></i></a>
  <a href="#research" aria-label="Research projects" title="Research"><i class="fa-solid fa-diagram-project" aria-hidden="true"></i></a>
  <span aria-hidden="true"></span>
</aside>

<aside class="folio-side folio-side--right" aria-label="Current locations">
  <p>Guangzhou · Macau · Zhuhai</p>
  <span aria-hidden="true"></span>
</aside>

<section class="folio-hero" id="home" aria-labelledby="folio-hero-title">
  <p class="folio-eyebrow folio-enter folio-enter--1">Hi, my name is</p>
  <h1 id="folio-hero-title" class="folio-enter folio-enter--2">Kenneth Zhang.</h1>
  <h2 class="folio-enter folio-enter--3">I build learning-guided optimization systems.</h2>
  <p class="folio-hero__intro folio-enter folio-enter--4">I am an undergraduate researcher at the Faculty of Data Science, City University of Macau. I study how machine learning can give strong classical solvers better structural hints for constrained routing and intelligent transportation.</p>
  <div class="folio-hero__actions folio-enter folio-enter--5">
    <a class="folio-outline-button" href="#research">Explore my research</a>
    <a class="folio-text-link" href="{{ base_path }}/cv/">View CV <i class="fa-solid fa-arrow-right" aria-hidden="true"></i></a>
  </div>
  <a class="folio-scroll-cue" href="#about" aria-label="Scroll to About Me"><span></span>Scroll</a>
</section>

<section class="folio-section folio-about folio-reveal" id="about" aria-labelledby="about-title">
  <h2 class="folio-numbered-heading" id="about-title"><span>01.</span> About Me</h2>
  <div class="folio-about__inner">
    <div class="folio-about__text">
      <p>Hi! I’m <strong>Kenneth Zhang (张誉耀)</strong>, an undergraduate student at the Faculty of Data Science, City University of Macau. I am interested in the intersection of machine learning, combinatorial optimization, and intelligent transportation.</p>
      <p>My current research explores a simple question: <strong>can learning help strong classical optimization solvers make better decisions?</strong> Instead of asking neural networks to construct an entire route from scratch, I work on learning useful structural hints, such as promising candidate edges, route-state signals, and feasibility-aware patterns, to guide Population-LKH and local search.</p>
      <p>I am especially interested in routing problems with practical constraints: customer groups, priority rules, charging stations, battery limits, and time windows.</p>
      <p>Outside research, I enjoy playing football and tennis, watching films, and playing Counter-Strike 2. I am also a devoted Chelsea supporter.</p>
      <p>Some areas I am currently working with:</p>
      <ul class="folio-skills">
        <li>Learning-Augmented Optimization</li>
        <li>Combinatorial Optimization</li>
        <li>Evolutionary Computation</li>
        <li>Reinforcement Learning</li>
        <li>Vehicle Routing</li>
        <li>Energy-Constrained Delivery</li>
      </ul>
    </div>
    <figure class="folio-portrait">
      <div class="folio-portrait__frame">
        <img src="{{ base_path }}/images/kenneth-zhang.jpg" alt="Portrait of Kenneth Zhang" />
      </div>
      <figcaption>Kenneth Zhang · 张誉耀</figcaption>
    </figure>
  </div>
</section>

<section class="folio-section folio-experience folio-reveal" id="experience" aria-labelledby="experience-title">
  <h2 class="folio-numbered-heading" id="experience-title"><span>02.</span> Where I’ve Studied &amp; Researched</h2>
  <div class="folio-tabs">
    <div class="folio-tabs__list" role="tablist" aria-label="Education and research experience">
      <button class="is-active" id="tab-ilsca" type="button" role="tab" aria-selected="true" aria-controls="panel-ilsca" data-folio-tab="ilsca">iLSCA Lab</button>
      <button id="tab-cityu" type="button" role="tab" aria-selected="false" aria-controls="panel-cityu" tabindex="-1" data-folio-tab="cityu">CityU Macau</button>
    </div>
    <div class="folio-tabs__panels">
      <article class="folio-tab-panel is-active" id="panel-ilsca" role="tabpanel" aria-labelledby="tab-ilsca" data-folio-panel="ilsca">
        <h3>Research Assistant <span>@ iLSCA Lab, HKUST (Guangzhou)</span></h3>
        <p class="folio-tab-panel__date">June 2026 – August 2026 · Guangzhou</p>
        <ul>
          <li>Worked on learning-guided approaches for constrained combinatorial optimization and routing.</li>
          <li>Investigated how learned candidate-edge and route-state signals can support strong search procedures.</li>
          <li>Focused on careful benchmark design, ablation studies, and mechanism-level inspection.</li>
        </ul>
      </article>
      <article class="folio-tab-panel" id="panel-cityu" role="tabpanel" aria-labelledby="tab-cityu" data-folio-panel="cityu" hidden>
        <h3>Undergraduate Student <span>@ City University of Macau</span></h3>
        <p class="folio-tab-panel__date">2023 – 2027 (Expected) · Macau</p>
        <ul>
          <li>Studying in the Faculty of Data Science with a growing focus on optimization and machine learning.</li>
          <li>Building research experience across evolutionary computation, reinforcement learning, and vehicle routing.</li>
          <li>Based across Guangzhou, Macau, and Zhuhai in the Greater Bay Area.</li>
        </ul>
      </article>
    </div>
  </div>
</section>

<section class="folio-section folio-research folio-reveal" id="research" aria-labelledby="research-title">
  <h2 class="folio-numbered-heading" id="research-title"><span>03.</span> Selected Research</h2>
  <div class="folio-projects">
    <article class="folio-project">
      <div class="folio-project__content">
        <p class="folio-project__overline">Featured Research</p>
        <h3>Learned Structural-Prior Guided Population-LKH</h3>
        <div class="folio-project__description"><p>A neural-combinatorial framework for BWTSP that learns promising candidate edges, adapts its prior policy, and uses guarded selection to guide finite-L search.</p></div>
        <ul class="folio-project__tech"><li>Population-LKH</li><li>Edge Priors</li><li>Adaptive Selection</li></ul>
        <div class="folio-project__links">
          <a href="{{ base_path }}/portfolio/portfolio-1/" aria-label="Read BWTSP project" title="Read project"><i class="fa-solid fa-arrow-up-right-from-square" aria-hidden="true"></i></a>
          <a href="https://github.com/KennethZhang29" aria-label="View GitHub" title="GitHub"><i class="fab fa-github" aria-hidden="true"></i></a>
        </div>
      </div>
      <a class="folio-project__image" href="{{ base_path }}/portfolio/portfolio-1/" aria-label="Read Learned Structural-Prior Guided Population-LKH project"><img src="{{ base_path }}/images/cover-learned-search.jpg" alt="Learning-guided search network illustration" /></a>
    </article>

    <article class="folio-project">
      <div class="folio-project__content">
        <p class="folio-project__overline">Ongoing Research</p>
        <h3>Energy-Constrained Delivery</h3>
        <div class="folio-project__description"><p>Extending static edge guidance toward move- and route-state-aware optimization for drones and electric vehicles under battery, payload, and charging constraints.</p></div>
        <ul class="folio-project__tech"><li>Vehicle Routing</li><li>Energy Models</li><li>Feasibility-Aware Search</li></ul>
        <div class="folio-project__links"><a href="{{ base_path }}/portfolio/portfolio-2/" aria-label="Read energy-constrained delivery project" title="Read project"><i class="fa-solid fa-arrow-up-right-from-square" aria-hidden="true"></i></a></div>
      </div>
      <a class="folio-project__image" href="{{ base_path }}/portfolio/portfolio-2/" aria-label="Read energy-constrained delivery project"><img src="{{ base_path }}/images/cover-energy-routing.jpg" alt="Energy routing map for drones and electric vehicles" /></a>
    </article>

    <article class="folio-project">
      <div class="folio-project__content">
        <p class="folio-project__overline">Research Practice</p>
        <h3>Evidence Before Claims</h3>
        <div class="folio-project__description"><p>I use ablations, route visualization, portfolio comparisons, and mechanism-level diagnostics to understand whether an improvement is real and why it happens.</p></div>
        <ul class="folio-project__tech"><li>Ablation Studies</li><li>Diagnostics</li><li>Reproducibility</li></ul>
      </div>
      <div class="folio-project__image"><img src="{{ base_path }}/images/cover-evidence-first.jpg" alt="Evidence-first ablation and diagnostics illustration" /></div>
    </article>
  </div>
</section>

<section class="folio-section folio-methods folio-reveal" aria-labelledby="methods-title">
  <h2 class="folio-standalone-heading" id="methods-title">Other Things I Care About</h2>
  <div class="folio-methods__grid">
    <article><i class="fa-solid fa-code" aria-hidden="true"></i><h3>Build</h3><p>Python research engineering and solver integration.</p></article>
    <article><i class="fa-solid fa-brain" aria-hidden="true"></i><h3>Learn</h3><p>Structural priors, route signals, and reinforcement learning.</p></article>
    <article><i class="fa-solid fa-flask" aria-hidden="true"></i><h3>Test</h3><p>Benchmarks, controlled ablations, and reproducible runs.</p></article>
    <article><i class="fa-solid fa-chart-line" aria-hidden="true"></i><h3>Explain</h3><p>Route diagnostics and mechanism-level interpretation.</p></article>
  </div>
</section>

<section class="folio-section folio-contact folio-reveal" id="contact" aria-labelledby="contact-title">
  <p class="folio-eyebrow">04. What’s Next?</p>
  <h2 id="contact-title">Let’s solve a hard routing problem.</h2>
  <p>I am interested in research opportunities and conversations around learning-augmented optimization, intelligent transportation, and reliable combinatorial search.</p>
  <a class="folio-outline-button" href="https://github.com/KennethZhang29">Find me on GitHub</a>
  <p class="folio-credit">Design direction inspired by <a href="https://brittanychiang.com">Brittany Chiang</a>.</p>
</section>
