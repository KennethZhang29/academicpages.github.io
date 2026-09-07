# Research Figure Contract

## Guided Population-LKH

- Core conclusion: Constraint-conditioned edge priors improve feasibility first and route length second while retaining a classical solver backbone.
- Results-level question: Does the complete pipeline add value beyond handcrafted candidate shaping, and does any benefit survive held-out and larger-instance evaluation?
- Method archetype: Single-panel workflow schematic.
- Results archetype: Three-panel quantitative grid.
- Evidence chain: development decomposition -> objective improvement -> held-out and cross-size boundary.
- Statistics: Aggregate benchmark values only; no invented uncertainty intervals.
- Reviewer risk: The 95.8% result is development-tuned and must not be presented as held-out generalization.

## GC-POMO

- Core conclusion: Explicit group-aware representation and hierarchical decoding improve neural construction on medium, large, and cross-size group-constrained routing instances.
- Results-level question: Are gains consistent across BWTSP, CTSP-d, larger sizes, and architectural ablations?
- Method archetype: Single-panel workflow schematic.
- Results archetype: Four-panel quantitative grid.
- Evidence chain: BWTSP comparison -> CTSP-d improvement -> cross-size stress test -> component ablation.
- Statistics: Mean objectives over 10,000 generated test instances as reported in the manuscript; no uncertainty intervals were available.
- Reviewer risk: GC-POMO is not best on the smallest BWTSP setting, and 3K rollouts cost more runtime than 1K.

## Export

- Backend: Python / Matplotlib only.
- Website preview: 200 dpi PNG.
- Editable outputs: SVG and PDF.
- Final figure text floor: 7 pt or larger.
- Palette: deep navy, sky blue, teal, terracotta orange, leaf green, and silver grey on an off-white background.
