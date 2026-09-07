# Research Figure QA Notes

All four figures were regenerated from the manuscript summary tables and inspected at final export size.

| Figure | Panel review | Alignment | PDF text | Collision audit |
| --- | --- | --- | --- | --- |
| Guided-LKH method | Process stages, arrows, labels, and callout are legible | Pass | Pass | Pass |
| Guided-LKH results | All four evidence panels are legible; values remain distinct from axes and neighboring panels | Pass | Pass | Pass |
| GC-POMO method | Encoder, dual-decoder, masks, state update, and contribution note are legible | Pass | Pass | Pass |
| GC-POMO results | Curves, direct series labels, value labels, and ablation comparisons are legible | Pass | Pass | Review required: two `text-fill-edge` warnings correspond to direct `GC-POMO` labels placed beside filled endpoint markers. Visual inspection confirms that the labels are not obscured and retain clear separation at final size. |

The generated PNG and TIFF files use 600 dpi. SVG and PDF exports preserve editable text. No uncertainty interval is shown because the manuscript tables used here report deterministic aggregate objectives and gaps rather than seed-level dispersion.
