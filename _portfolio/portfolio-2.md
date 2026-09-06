---
title: "GC-POMO: Group-Aware Deep Reinforcement Learning for Constrained TSPs"
excerpt: "A unified deep reinforcement learning framework that coordinates inter-group transitions with intra-group routing for BWTSP and CTSP-d."
collection: portfolio
header:
  teaser: cover-group-aware-routing.jpg
---

GC-POMO studies group-constrained traveling salesman problems, where route feasibility depends not only on which node is selected next but also on evolving group-level rules. The work covers two complementary settings: BWTSP, with non-contiguous black-white interleaving constraints, and CTSP-d, with priority-constrained cluster sequencing.

**Authors:** Guangyu Zou, Jing Sun, Yuyao Zhang, Jie Gao, Yaoxin Wu, and Jingwen Li  
**My contribution:** Software and Visualization, as recorded in the manuscript's CRediT authorship statement.

## Research Problem

Most neural routing methods make flat node-level decisions. That representation is poorly matched to problems in which group transitions determine which node choices remain feasible. A useful policy must coordinate two coupled decisions:

- which group should be visited next under the current constraint state;
- which node within that group should extend the route.

The research asks whether one model can learn this hierarchy across different group-level routing rules while retaining fast neural construction and useful cross-size generalization.

## Method

GC-POMO extends the POMO construction paradigm with three group-aware components:

1. **Interactive MDP formulation.** The route state tracks how group-level feasibility evolves after every node selection.
2. **Group-aware attention encoder.** Cross-group attention combines node-level spatial embeddings with group-level structural representations.
3. **Interactive dual decoder.** Inter-group and intra-group decoders coordinate group transitions and within-group routing, with problem-specific masks enforcing BWTSP or CTSP-d eligibility rules.

The model is trained with policy-gradient reinforcement learning and POMO-style multi-start rollouts. The shared architecture remains the same across the two problem families; the constraint state and action masks encode their different routing rules.

![GC-POMO group-aware encoder and interactive dual-decoder architecture]({{ base_path }}/images/gc-pomo-framework.png)

## Experimental Results

- **BWTSP solution quality:** With 3,000 rollouts, GC-POMO reached objectives of **6.422** on BWTSP50 and **8.565** on BWTSP100, compared with **6.604** and **8.900** for POMO. Relative to LKH, these correspond to gaps of **-5.8%** and **-10.2%**.
- **CTSP-d solution quality:** Across 20-, 50-, and 100-node instances, GC-POMO achieved objectives of **2.608**, **5.079**, and **8.702**, improving on POMO's **2.623**, **5.162**, and **9.036** under the same 3,000-rollout setting.
- **Cross-size generalization:** Models evaluated on BWTSP200, BWTSP300, and BWTSP500 reduced the gap to LKH from POMO's **7.1%, 14.0%, and 32.7%** to **3.0%, 9.2%, and 18.5%**. On large CTSP-d instances, GC-POMO obtained the best reported feasible objective in each tested size group.
- **Ablation evidence:** Removing either the group-aware encoder or the inter-group decoder degraded performance. The encoder had the larger effect on solution quality, while the decoder introduced more computational cost.

## My Contribution

My contribution focused on **software implementation and research visualization**. This included supporting the experimental software pipeline and producing visual materials that make group-constrained route behavior, model structure, and comparative results easier to inspect and communicate.

## Interpretation and Limitations

The gains are strongest on medium and large instances. On the smallest BWTSP setting, DACT produced the best objective and GC-POMO remained 1.0% above the LKH reference. Runtime also grows with rollout count and model complexity. These results suggest that explicit group awareness improves neural routing substantially, while larger-scale efficiency and richer operational constraints remain open directions.
