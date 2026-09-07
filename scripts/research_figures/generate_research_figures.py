#!/usr/bin/env python3
"""Generate website-ready research figures from manuscript source tables."""

from __future__ import annotations

import csv
import sys
from pathlib import Path

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle, FancyArrowPatch, FancyBboxPatch


ROOT = Path(__file__).resolve().parents[2]
DATA_DIR = Path(__file__).resolve().parent / "source_data"
QA_DIR = Path(__file__).resolve().parent / "qa"
PNG_DIR = ROOT / "images" / "research-figures"
VECTOR_DIR = ROOT / "assets" / "research-figures" / "vector"
SKILL_SCRIPTS = Path.home() / ".codex" / "skills" / "nature-figure" / "scripts"
sys.path.insert(0, str(SKILL_SCRIPTS))

from audit_panel_alignment import require_matplotlib_panel_alignment  # noqa: E402


COLORS = {
    "navy": "#17243B",
    "blue": "#3488B8",
    "blue_soft": "#B9D8E8",
    "teal": "#279A91",
    "teal_soft": "#C5E7E1",
    "orange": "#D9653B",
    "orange_soft": "#F5D4C5",
    "green": "#6D9147",
    "green_soft": "#DCE8CF",
    "silver": "#AEB8C2",
    "line": "#D8DEE5",
    "muted": "#667085",
    "paper": "#F8FAFC",
    "white": "#FFFFFF",
}


mpl.rcParams.update(
    {
        "font.family": "sans-serif",
        "font.sans-serif": ["Arial", "Helvetica", "DejaVu Sans", "sans-serif"],
        "font.size": 8,
        "axes.titlesize": 10,
        "axes.labelsize": 8,
        "xtick.labelsize": 7,
        "ytick.labelsize": 7,
        "legend.fontsize": 7,
        "svg.fonttype": "none",
        "pdf.fonttype": 42,
        "axes.spines.right": False,
        "axes.spines.top": False,
        "axes.linewidth": 0.8,
        "legend.frameon": False,
        "figure.facecolor": COLORS["paper"],
        "axes.facecolor": COLORS["paper"],
        "text.color": COLORS["navy"],
        "axes.labelcolor": COLORS["navy"],
        "xtick.color": COLORS["muted"],
        "ytick.color": COLORS["muted"],
    }
)


def load_csv(name: str) -> list[dict[str, str]]:
    with (DATA_DIR / name).open(newline="", encoding="utf-8") as stream:
        return list(csv.DictReader(stream))


def export_figure(fig: plt.Figure, stem: str, *, require_labels: bool) -> None:
    QA_DIR.mkdir(parents=True, exist_ok=True)
    PNG_DIR.mkdir(parents=True, exist_ok=True)
    VECTOR_DIR.mkdir(parents=True, exist_ok=True)
    fig.canvas.draw()
    require_matplotlib_panel_alignment(
        fig,
        json_out=QA_DIR / f"{stem}.alignment.json",
        overlay_svg=QA_DIR / f"{stem}.alignment.svg",
        tolerance_pt=1.5,
        gutter_tolerance_pt=1.5,
        require_panel_labels=require_labels,
        strict=True,
    )
    fig.savefig(PNG_DIR / f"{stem}.png", dpi=600, bbox_inches="tight", facecolor=COLORS["paper"])
    fig.savefig(VECTOR_DIR / f"{stem}.svg", bbox_inches="tight", facecolor=COLORS["paper"])
    fig.savefig(VECTOR_DIR / f"{stem}.pdf", bbox_inches="tight", facecolor=COLORS["paper"])
    fig.savefig(
        VECTOR_DIR / f"{stem}.tiff",
        dpi=600,
        bbox_inches="tight",
        facecolor=COLORS["paper"],
        pil_kwargs={"compression": "tiff_lzw"},
    )
    plt.close(fig)


def panel_label(ax: plt.Axes, letter: str) -> None:
    ax.text(
        -0.14,
        1.08,
        letter,
        transform=ax.transAxes,
        fontsize=10,
        fontweight="bold",
        va="top",
        ha="left",
    )


def clean_axis(ax: plt.Axes, *, grid: bool = False) -> None:
    ax.spines["left"].set_color(COLORS["silver"])
    ax.spines["bottom"].set_color(COLORS["silver"])
    ax.tick_params(length=3, width=0.7)
    if grid:
        ax.grid(axis="y", color=COLORS["line"], linewidth=0.6, alpha=0.75)
        ax.set_axisbelow(True)


def add_box(
    ax: plt.Axes,
    xy: tuple[float, float],
    width: float,
    height: float,
    title: str,
    lines: list[str],
    *,
    facecolor: str,
    edgecolor: str,
) -> None:
    x, y = xy
    patch = FancyBboxPatch(
        (x, y),
        width,
        height,
        boxstyle="round,pad=0.012,rounding_size=0.018",
        linewidth=1.2,
        edgecolor=edgecolor,
        facecolor=facecolor,
    )
    ax.add_patch(patch)
    ax.text(x + width / 2, y + height * 0.73, title, ha="center", va="center", fontsize=9, fontweight="bold")
    ax.text(
        x + width / 2,
        y + height * 0.38,
        "\n".join(lines),
        ha="center",
        va="center",
        fontsize=7,
        color=COLORS["muted"],
        linespacing=1.45,
    )


def connect(ax: plt.Axes, start: tuple[float, float], end: tuple[float, float], color: str = "#60758A") -> None:
    ax.add_patch(
        FancyArrowPatch(
            start,
            end,
            arrowstyle="-|>",
            mutation_scale=11,
            linewidth=1.25,
            color=color,
            connectionstyle="arc3,rad=0",
        )
    )


def draw_network(ax: plt.Axes, center: tuple[float, float], scale: float, *, grouped: bool = False) -> None:
    cx, cy = center
    points = np.array(
        [
            [-0.85, 0.20],
            [-0.45, 0.75],
            [0.05, 0.52],
            [0.72, 0.82],
            [0.88, 0.05],
            [0.30, -0.55],
            [-0.50, -0.62],
        ]
    )
    points = points * scale + np.array([cx, cy])
    order = [0, 1, 3, 4, 5, 6, 2, 0]
    for a, b in zip(order[:-1], order[1:]):
        ax.plot(points[[a, b], 0], points[[a, b], 1], color=COLORS["teal"], lw=1.7, zorder=2)
    for idx, (x, y) in enumerate(points):
        if grouped:
            color = [COLORS["blue"], COLORS["teal"], COLORS["orange"]][idx % 3]
        else:
            color = COLORS["orange"] if idx in {1, 5} else COLORS["white"]
        ax.add_patch(Circle((x, y), scale * 0.16, facecolor=color, edgecolor=COLORS["navy"], lw=0.9, zorder=3))


def title_block(fig: plt.Figure, title: str, subtitle: str, tag: str) -> None:
    fig.text(0.055, 0.955, tag, fontsize=7, fontweight="bold", color=COLORS["teal"], va="top")
    fig.text(0.055, 0.915, title, fontsize=15, fontweight="bold", color=COLORS["navy"], va="top")
    fig.text(0.055, 0.865, subtitle, fontsize=8, color=COLORS["muted"], va="top")


def guided_lkh_method() -> None:
    fig, ax = plt.subplots(figsize=(7.2, 4.05))
    fig.subplots_adjust(left=0.04, right=0.97, top=0.78, bottom=0.10)
    title_block(
        fig,
        "Learning augments search without replacing it",
        "Constraint-conditioned edge priors reshape the candidate space explored by Population-LKH.",
        "GUIDED POPULATION-LKH  /  METHOD",
    )
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    ax.add_patch(FancyBboxPatch((0.015, 0.15), 0.60, 0.74, boxstyle="round,pad=0.006", facecolor="#EFF7F7", edgecolor="none"))
    ax.add_patch(FancyBboxPatch((0.63, 0.15), 0.355, 0.74, boxstyle="round,pad=0.006", facecolor="#F3F5F8", edgecolor="none"))
    ax.text(0.03, 0.845, "STAGE 1  LEARNED STRUCTURAL PRIOR", fontsize=7, fontweight="bold", color=COLORS["teal"])
    ax.text(0.65, 0.845, "STAGE 2  GUARDED CLASSICAL SEARCH", fontsize=7, fontweight="bold", color=COLORS["blue"])

    boxes = [
        (0.03, 0.30, 0.125, "Instance", ["geometry", "labels", "Q and finite-L"], COLORS["white"], COLORS["silver"]),
        (0.185, 0.30, 0.135, "Seed tours", ["Weak-LKH", "Population-LKH", "topological context"], COLORS["blue_soft"], COLORS["blue"]),
        (0.35, 0.30, 0.145, "Edge pool", ["local + anchor", "bridge + seed", "candidate families"], COLORS["teal_soft"], COLORS["teal"]),
        (0.525, 0.30, 0.135, "Edge prior", ["Transformer", "utility ranking", "adaptive density"], COLORS["green_soft"], COLORS["green"]),
        (0.69, 0.30, 0.125, "EDGE_FILE", ["native injection", "guided variants", "GPX2 + LK"], COLORS["orange_soft"], COLORS["orange"]),
        (0.845, 0.30, 0.125, "Selector", ["portfolio ranking", "confidence guard", "fallback search"], COLORS["blue_soft"], COLORS["blue"]),
    ]
    for x, y, width, title, lines, face, edge in boxes:
        add_box(ax, (x, y), width, 0.40, title, lines, facecolor=face, edgecolor=edge)
    for left, right in zip(boxes[:-1], boxes[1:]):
        connect(ax, (left[0] + left[2], 0.50), (right[0] - 0.008, 0.50))

    draw_network(ax, (0.092, 0.245), 0.026)
    draw_network(ax, (0.922, 0.245), 0.026)
    ax.text(0.50, 0.085, "Learning decides where to search; Population-LKH still decides the tour.", ha="center", fontsize=8, fontweight="bold")
    ax.text(0.50, 0.035, "Sole-author pipeline  |  BWTSP main testbed  |  CTSP-d transfer setting", ha="center", fontsize=7, color=COLORS["muted"])
    export_figure(fig, "guided-lkh-method", require_labels=False)


def guided_lkh_results() -> None:
    rows = load_csv("guided_lkh_summary.csv")
    dev = [row for row in rows if row["section"] == "development" and row["variant"] != "Population LKH"]
    labels = ["Handcrafted prior", "Prior + oracle", "Learned selector", "Full policy + hedges"]
    penalty_reduction = np.array([float(row["penalty_reduction_pct"]) for row in dev])
    objective_reduction = np.array([float(row["objective_reduction_pct"]) for row in dev])

    fig, axes = plt.subplots(2, 2, figsize=(7.2, 5.25))
    fig.subplots_adjust(left=0.19, right=0.975, bottom=0.10, top=0.78, wspace=0.48, hspace=0.54)
    title_block(
        fig,
        "Structural priors improve feasibility first, then distance",
        "Development decomposition is separated from generated-only holdout and cross-size evidence.",
        "GUIDED POPULATION-LKH  /  RESULTS",
    )

    colors = [COLORS["blue_soft"], COLORS["blue"], COLORS["teal"], COLORS["orange"]]

    ax = axes[0, 0]
    panel_label(ax, "a")
    y = np.arange(len(labels))
    bars = ax.barh(y, penalty_reduction, color=colors, height=0.58, edgecolor="none")
    ax.set_title("Constraint penalty reduction", loc="left", fontweight="bold")
    ax.set_xlabel("Reduction vs Population LKH (%)")
    ax.set_yticks(y, labels)
    ax.invert_yaxis()
    ax.set_xlim(0, 106)
    ax.set_xticks([0, 25, 50, 75, 100])
    clean_axis(ax)
    ax.tick_params(length=0)
    for index, (bar, value) in enumerate(zip(bars, penalty_reduction)):
        label_color = COLORS["navy"] if index == 0 else COLORS["white"]
        ax.text(value - 2.0, bar.get_y() + bar.get_height() / 2, f"{value:.1f}%", ha="right", va="center", fontsize=7, fontweight="bold", color=label_color)

    ax = axes[0, 1]
    panel_label(ax, "b")
    bars = ax.barh(y, objective_reduction, color=colors, height=0.58, edgecolor="none")
    ax.set_title("Tour-length reduction", loc="left", fontweight="bold")
    ax.set_xlabel("Reduction vs Population LKH (%)")
    ax.set_yticks(y, labels)
    ax.invert_yaxis()
    ax.set_xlim(0, 6.25)
    ax.set_xticks([0, 2, 4, 6])
    clean_axis(ax)
    ax.tick_params(length=0)
    for bar, value in zip(bars, objective_reduction):
        ax.text(value + 0.12, bar.get_y() + bar.get_height() / 2, f"{value:.1f}%", ha="left", va="center", fontsize=7, fontweight="bold")

    ax = axes[1, 0]
    panel_label(ax, "c")
    ax.set_title("Generated-only holdout", loc="left", fontweight="bold")
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")
    evidence = [
        (0.69, "61.4%", "lower penalty", COLORS["teal"]),
        (0.40, "2.6%", "shorter tours", COLORS["blue"]),
        (0.11, "4.4 → 7.4", "feasible instances", COLORS["orange"]),
    ]
    for y0, value, metric, color in evidence:
        ax.add_patch(FancyBboxPatch((0.03, y0), 0.94, 0.22, boxstyle="round,pad=0.012,rounding_size=0.022", facecolor=COLORS["white"], edgecolor=COLORS["line"], lw=0.9))
        ax.add_patch(FancyBboxPatch((0.03, y0), 0.022, 0.22, boxstyle="round,pad=0.002,rounding_size=0.007", facecolor=color, edgecolor=color, lw=0))
        ax.text(0.09, y0 + 0.11, value, fontsize=12, fontweight="bold", color=color, va="center")
        ax.text(0.53, y0 + 0.11, metric, fontsize=7.2, fontweight="bold", va="center")
    ax.text(0.03, 0.01, "Fresh instances only; no validation-set reuse", fontsize=6.5, color=COLORS["muted"])

    ax = axes[1, 1]
    panel_label(ax, "d")
    xl_labels = ["Prior oracle", "Guarded selector"]
    xl_values = np.array([3.5, 1.0])
    xl_colors = [COLORS["green"], COLORS["orange"]]
    y_xl = np.arange(2)
    bars = ax.barh(y_xl, xl_values, color=xl_colors, height=0.48, edgecolor="none")
    ax.set_title("Unseen 600–1,000-node instances", loc="left", fontweight="bold")
    ax.set_xlabel("Tour-length reduction (%)")
    ax.set_yticks(y_xl, xl_labels)
    ax.invert_yaxis()
    ax.set_xlim(0, 4.25)
    ax.set_xticks([0, 1, 2, 3, 4])
    clean_axis(ax)
    ax.tick_params(length=0)
    for bar, value in zip(bars, xl_values):
        ax.text(value + 0.09, bar.get_y() + bar.get_height() / 2, f"{value:.1f}%", ha="left", va="center", fontsize=7, fontweight="bold")
    export_figure(fig, "guided-lkh-results", require_labels=True)


def gc_pomo_method() -> None:
    fig, ax = plt.subplots(figsize=(7.2, 4.05))
    fig.subplots_adjust(left=0.04, right=0.97, top=0.78, bottom=0.09)
    title_block(
        fig,
        "One policy coordinates group and node decisions",
        "GC-POMO couples group-aware representation with interactive inter- and intra-group decoding.",
        "GC-POMO  /  METHOD",
    )
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    add_box(ax, (0.035, 0.29), 0.16, 0.43, "Grouped instance", ["node coordinates", "group labels", "current route state"], facecolor=COLORS["white"], edgecolor=COLORS["silver"])
    draw_network(ax, (0.115, 0.245), 0.035, grouped=True)
    add_box(ax, (0.245, 0.29), 0.18, 0.43, "Group-aware encoder", ["node self-attention", "group embeddings", "cross-group attention"], facecolor=COLORS["blue_soft"], edgecolor=COLORS["blue"])

    ax.add_patch(FancyBboxPatch((0.47, 0.18), 0.29, 0.65, boxstyle="round,pad=0.012,rounding_size=0.025", facecolor="#EFF7F7", edgecolor=COLORS["teal"], lw=1.2))
    ax.text(0.615, 0.77, "INTERACTIVE DUAL DECODER", ha="center", fontsize=8, fontweight="bold", color=COLORS["teal"])
    add_box(ax, (0.495, 0.49), 0.24, 0.18, "Inter-group decision", ["select an eligible next group"], facecolor=COLORS["teal_soft"], edgecolor=COLORS["teal"])
    add_box(ax, (0.495, 0.25), 0.24, 0.18, "Intra-group decision", ["select the next feasible node"], facecolor=COLORS["green_soft"], edgecolor=COLORS["green"])
    connect(ax, (0.615, 0.49), (0.615, 0.44), COLORS["teal"])

    add_box(ax, (0.80, 0.49), 0.16, 0.22, "Constraint mask", ["BWTSP spacing", "CTSP-d priority"], facecolor=COLORS["orange_soft"], edgecolor=COLORS["orange"])
    add_box(ax, (0.80, 0.20), 0.16, 0.22, "Node action", ["feasible extension", "POMO rollout"], facecolor=COLORS["white"], edgecolor=COLORS["navy"])

    connect(ax, (0.195, 0.505), (0.237, 0.505))
    connect(ax, (0.425, 0.505), (0.462, 0.505))
    connect(ax, (0.76, 0.60), (0.792, 0.60), COLORS["orange"])
    connect(ax, (0.88, 0.49), (0.88, 0.43), COLORS["orange"])
    connect(ax, (0.76, 0.34), (0.792, 0.31), COLORS["teal"])

    ax.annotate("state update", xy=(0.81, 0.20), xytext=(0.37, 0.12), fontsize=7, color=COLORS["muted"], ha="center", arrowprops=dict(arrowstyle="-|>", lw=1.0, color=COLORS["muted"], connectionstyle="arc3,rad=-0.18"))
    ax.text(0.50, 0.045, "Shared architecture  |  Problem-specific state and masks  |  Software + visualization contribution", ha="center", fontsize=7, color=COLORS["muted"])
    export_figure(fig, "gc-pomo-method", require_labels=False)


def gc_pomo_results() -> None:
    rows = load_csv("gc_pomo_results.csv")
    fig, axes = plt.subplots(2, 2, figsize=(7.2, 5.2))
    fig.subplots_adjust(left=0.09, right=0.985, bottom=0.10, top=0.77, wspace=0.34, hspace=0.48)
    title_block(
        fig,
        "Group awareness matters more as routing structure grows",
        "GC-POMO is compared with POMO under matched rollout budgets; lower objective or gap is better.",
        "GC-POMO  /  RESULTS",
    )
    for letter, ax in zip("abcd", axes.flat):
        panel_label(ax, letter)

    ax = axes[0, 0]
    main_bw = [row for row in rows if row["section"] == "main" and row["problem"] == "BWTSP"]
    sizes = np.array([20, 50, 100])
    for method, color, marker in [("POMO (3K)", COLORS["silver"], "o"), ("GC-POMO (3K)", COLORS["teal"], "s")]:
        values = [float(row["gap_pct"]) for row in main_bw if row["method"] == method]
        ax.plot(sizes, values, marker=marker, ms=5, lw=2, color=color)
    ax.axhline(0, color=COLORS["navy"], lw=0.8, ls="--")
    ax.set_title("BWTSP: gap to LKH", loc="left", fontweight="bold")
    ax.set_xlabel("Number of nodes")
    ax.set_ylabel("Objective gap (%)")
    ax.set_xticks(sizes)
    ax.set_xlim(18, 134)
    ax.text(118, -6.6, "POMO", color=COLORS["silver"], fontsize=6.5, va="center", fontweight="bold")
    ax.text(118, -10.2, "GC-POMO", color=COLORS["teal"], fontsize=6.5, va="center", fontweight="bold")
    clean_axis(ax)
    ax.tick_params(length=0)

    ax = axes[0, 1]
    main_ctsp = [row for row in rows if row["section"] == "main" and row["problem"] == "CTSP-d"]
    gains = []
    for size in sizes:
        pomo = next(float(row["objective"]) for row in main_ctsp if int(row["size"]) == size and row["method"] == "POMO (3K)")
        gc = next(float(row["objective"]) for row in main_ctsp if int(row["size"]) == size and row["method"] == "GC-POMO (3K)")
        gains.append(100.0 * (pomo - gc) / pomo)
    ax.plot(sizes, gains, color=COLORS["orange"], marker="o", ms=5, lw=2.2)
    ax.fill_between(sizes, 0, gains, color=COLORS["orange_soft"], alpha=0.75)
    ax.set_title("CTSP-d: gain over POMO", loc="left", fontweight="bold")
    ax.set_xlabel("Number of nodes")
    ax.set_ylabel("Objective reduction (%)")
    ax.set_xticks(sizes)
    ax.set_ylim(0, 4.75)
    clean_axis(ax)
    ax.tick_params(length=0)
    for x, value in zip(sizes, gains):
        if x == 20:
            ax.text(x + 4, 0.20, f"{value:.1f}%", ha="left", fontsize=7, fontweight="bold")
        else:
            ax.text(x, value + 0.55, f"{value:.1f}%", ha="center", fontsize=7, fontweight="bold")

    ax = axes[1, 0]
    gen = [row for row in rows if row["section"] == "generalization"]
    large_sizes = np.array([200, 300, 500])
    for method, color, marker in [("POMO (3K)", COLORS["silver"], "o"), ("GC-POMO (3K)", COLORS["blue"], "s")]:
        values = [float(row["gap_pct"]) for row in gen if row["method"] == method]
        ax.plot(large_sizes, values, marker=marker, ms=5, lw=2, color=color)
    ax.set_title("Cross-size BWTSP generalization", loc="left", fontweight="bold")
    ax.set_xlabel("Number of nodes")
    ax.set_ylabel("Gap to LKH (%)")
    ax.set_xticks(large_sizes)
    ax.set_xlim(185, 640)
    ax.text(570, 32.7, "POMO", color=COLORS["silver"], fontsize=6.5, va="center", fontweight="bold")
    ax.text(570, 18.5, "GC-POMO", color=COLORS["blue"], fontsize=6.5, va="center", fontweight="bold")
    clean_axis(ax)
    ax.tick_params(length=0)
    ax.tick_params(axis="y", pad=8)

    ax = axes[1, 1]
    ablation = [row for row in rows if row["section"] == "ablation"]
    ablation_labels = ["POMO", "No group encoder", "No group decoder", "Full GC-POMO"]
    values = np.array([float(row["objective"]) for row in ablation])
    colors = [COLORS["silver"], COLORS["blue_soft"], COLORS["blue"], COLORS["teal"]]
    y = np.arange(len(values))
    bars = ax.barh(y, values, color=colors, edgecolor="none", height=0.58)
    ax.set_title("CTSP-d100 component ablation", loc="left", fontweight="bold")
    ax.set_xlabel("Objective value")
    ax.set_yticks(y, ablation_labels)
    ax.invert_yaxis()
    ax.set_xlim(8.55, 9.24)
    clean_axis(ax)
    ax.tick_params(length=0)
    for bar, value in zip(bars, values):
        ax.text(value + 0.045, bar.get_y() + bar.get_height() / 2, f"{value:.3f}", ha="left", va="center", fontsize=7, fontweight="bold")
    export_figure(fig, "gc-pomo-results", require_labels=True)


def main() -> None:
    guided_lkh_method()
    guided_lkh_results()
    gc_pomo_method()
    gc_pomo_results()
    print("generated: guided-lkh-method, guided-lkh-results, gc-pomo-method, gc-pomo-results")


if __name__ == "__main__":
    main()
