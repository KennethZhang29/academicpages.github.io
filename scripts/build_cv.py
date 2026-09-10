#!/usr/bin/env python3
"""Build Kenneth Zhang's one-page academic CV."""

from pathlib import Path

from reportlab.lib.colors import HexColor
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase.pdfmetrics import stringWidth
from reportlab.pdfgen import canvas


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "files" / "Kenneth_Zhang_CV.pdf"

PAGE_W, PAGE_H = A4
MARGIN_X = 42
TOP = PAGE_H - 42
NAVY = HexColor("#102A43")
TEAL = HexColor("#2F8F9D")
ORANGE = HexColor("#D96A4A")
INK = HexColor("#243B53")
MUTED = HexColor("#627D98")
RULE = HexColor("#D9E2EC")
PALE = HexColor("#F0F7F8")


def wrap(text, font, size, width):
    words = text.split()
    lines = []
    current = ""
    for word in words:
        candidate = f"{current} {word}".strip()
        if not current or stringWidth(candidate, font, size) <= width:
            current = candidate
        else:
            lines.append(current)
            current = word
    if current:
        lines.append(current)
    return lines


def paragraph(c, text, x, y, width, size=8.6, leading=11.2, color=INK, font="Helvetica"):
    c.setFont(font, size)
    c.setFillColor(color)
    for line in wrap(text, font, size, width):
        c.drawString(x, y, line)
        y -= leading
    return y


def bullet(c, text, x, y, width, size=8.35, leading=10.7, color=INK):
    c.setFillColor(TEAL)
    c.circle(x + 2.2, y + 2.4, 1.35, fill=1, stroke=0)
    return paragraph(c, text, x + 9, y, width - 9, size, leading, color)


def section(c, title, x, y, width):
    c.setFillColor(NAVY)
    c.setFont("Helvetica-Bold", 9.3)
    c.drawString(x, y, title.upper())
    c.setStrokeColor(TEAL)
    c.setLineWidth(1.2)
    c.line(x, y - 4.5, x + width, y - 4.5)
    return y - 17


def role(c, title, meta, x, y, width):
    c.setFillColor(INK)
    c.setFont("Helvetica-Bold", 9.2)
    c.drawString(x, y, title)
    meta_w = stringWidth(meta, "Helvetica-Bold", 7.7)
    c.setFillColor(MUTED)
    c.setFont("Helvetica-Bold", 7.7)
    c.drawRightString(x + width, y + 0.5, meta)
    return y - 12


def label_block(c, label, lines, x, y, width):
    c.setFillColor(NAVY)
    c.setFont("Helvetica-Bold", 8.7)
    c.drawString(x, y, label)
    y -= 11
    for text in lines:
        y = paragraph(c, text, x, y, width, 8.15, 10.2, INK)
        y -= 2
    return y


def build():
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    c = canvas.Canvas(str(OUTPUT), pagesize=A4)
    c.setTitle("Kenneth Zhang - Academic CV")
    c.setAuthor("Kenneth Zhang")

    # Header
    c.setFillColor(NAVY)
    c.setFont("Helvetica-Bold", 24)
    c.drawString(MARGIN_X, TOP, "Kenneth Zhang")
    c.setFillColor(TEAL)
    c.setFont("Helvetica-Bold", 10.2)
    c.drawString(MARGIN_X, TOP - 20, "UNDERGRADUATE RESEARCHER | LEARNING-AUGMENTED OPTIMIZATION")
    c.setFillColor(MUTED)
    c.setFont("Helvetica", 8.3)
    c.drawString(MARGIN_X, TOP - 36, "kennethzhang29@outlook.com")
    c.drawString(MARGIN_X + 151, TOP - 36, "github.com/KennethZhang29")
    c.drawRightString(PAGE_W - MARGIN_X, TOP - 36, "Guangzhou | Macau | Zhuhai")
    c.setStrokeColor(NAVY)
    c.setLineWidth(1.6)
    c.line(MARGIN_X, TOP - 46, PAGE_W - MARGIN_X, TOP - 46)

    # Profile and evidence strip
    y = TOP - 63
    y = section(c, "Profile", MARGIN_X, y, PAGE_W - 2 * MARGIN_X)
    profile = (
        "Undergraduate researcher at the Faculty of Data Science, City University of Macau. "
        "I study how learned structural priors and group-aware policies can guide classical "
        "optimization solvers for constrained routing and intelligent transportation."
    )
    y = paragraph(c, profile, MARGIN_X, y, PAGE_W - 2 * MARGIN_X, 9.0, 11.6)
    y -= 6
    strip_h = 36
    c.setFillColor(PALE)
    c.roundRect(MARGIN_X, y - strip_h + 7, PAGE_W - 2 * MARGIN_X, strip_h, 4, fill=1, stroke=0)
    metrics = [
        ("12 / 12", "portfolio-best matches"),
        ("3.10x", "lower selection cost"),
        ("2026", "iLSCA Lab research assistant"),
    ]
    col_w = (PAGE_W - 2 * MARGIN_X) / 3
    for i, (value, caption) in enumerate(metrics):
        cx = MARGIN_X + i * col_w + col_w / 2
        c.setFillColor(TEAL if i != 1 else ORANGE)
        c.setFont("Helvetica-Bold", 12.5)
        c.drawCentredString(cx, y - 7, value)
        c.setFillColor(MUTED)
        c.setFont("Helvetica", 7.5)
        c.drawCentredString(cx, y - 19, caption)
    y -= strip_h + 2

    gutter = 24
    right_w = 163
    left_w = PAGE_W - 2 * MARGIN_X - right_w - gutter
    left_x = MARGIN_X
    right_x = left_x + left_w + gutter
    y_left = y
    y_right = y

    # Left column
    y_left = section(c, "Research Experience", left_x, y_left, left_w)
    y_left = role(c, "Research Assistant, iLSCA Lab", "JUN-AUG 2026", left_x, y_left, left_w)
    y_left = paragraph(
        c,
        "The Hong Kong University of Science and Technology (Guangzhou)",
        left_x,
        y_left,
        left_w,
        8.2,
        10.2,
        MUTED,
        "Helvetica-Oblique",
    )
    y_left -= 2
    y_left = bullet(c, "Developed and evaluated learning-guided methods for constrained routing, connecting neural structural signals with LKH-style heuristic search.", left_x, y_left, left_w)
    y_left = bullet(c, "Built reproducible benchmark, ablation, diagnostic, and scientific-visualization workflows.", left_x, y_left - 2, left_w)
    y_left -= 7

    y_left = section(c, "Selected Research", left_x, y_left, left_w)
    y_left = role(c, "Learned Edge Priors for Population-LKH", "FIRST-AUTHOR PROJECT", left_x, y_left, left_w)
    y_left = bullet(c, "Designed a two-stage framework with cluster-aware candidate construction, Transformer edge priors, adaptive sparsification, and guarded solver selection.", left_x, y_left, left_w)
    y_left = bullet(c, "On 12 finite-L BWTSP instances, matched the portfolio-best choice on 12/12 cases while reducing selection cost by about 3.10x.", left_x, y_left - 2, left_w)
    y_left -= 6

    y_left = role(c, "GC-POMO for Group-Constrained TSPs", "CO-AUTHOR", left_x, y_left, left_w)
    y_left = bullet(c, "Contributed software and research visualization for a group-aware attention encoder and interactive dual-decoder spanning BWTSP and CTSP-d.", left_x, y_left, left_w)
    y_left = bullet(c, "The 3,000-rollout model improved over POMO on BWTSP50/100 and CTSP-d20/50/100, with stronger cross-size generalization.", left_x, y_left - 2, left_w)
    y_left -= 6

    y_left = role(c, "Energy-Constrained Delivery", "ONGOING", left_x, y_left, left_w)
    y_left = bullet(c, "Exploring payload-dependent routing, optional charging stations, battery limits, and feasibility-aware guidance for drone and electric-vehicle delivery.", left_x, y_left, left_w)
    y_left -= 9

    y_left = section(c, "Research Workflow", left_x, y_left, left_w)
    y_left = bullet(c, "Formulate operational constraints and construct reproducible benchmark instances.", left_x, y_left, left_w)
    y_left = bullet(c, "Learn edge, group, move, or route-state signals without replacing reliable solver mechanics.", left_x, y_left - 2, left_w)
    y_left = bullet(c, "Integrate guidance through native solver interfaces and feasibility-aware action masks.", left_x, y_left - 2, left_w)
    y_left = bullet(c, "Audit claims with strong baselines, ablations, multi-seed tests, and route-level diagnostics.", left_x, y_left - 2, left_w)

    # Right column
    y_right = section(c, "Education", right_x, y_right, right_w)
    c.setFillColor(INK)
    c.setFont("Helvetica-Bold", 9.1)
    c.drawString(right_x, y_right, "City University of Macau")
    y_right -= 11
    y_right = paragraph(c, "Faculty of Data Science", right_x, y_right, right_w, 8.2, 10.3, MUTED, "Helvetica-Oblique")
    y_right -= 1
    y_right = paragraph(c, "B.Eng. in Computer Science and Technology", right_x, y_right, right_w, 8.25, 10.4)
    y_right = paragraph(c, "2023-2027 (expected)", right_x, y_right - 1, right_w, 8.15, 10.2, MUTED)
    y_right -= 8

    y_right = section(c, "Technical Skills", right_x, y_right, right_w)
    y_right = label_block(c, "OPTIMIZATION", ["LKH3, Gurobi, ALNS, local search"], right_x, y_right, right_w)
    y_right = label_block(c, "LEARNING", ["PyTorch, Transformer, attention, GNN, policy gradient, POMO"], right_x, y_right, right_w)
    y_right = label_block(c, "ENGINEERING", ["Python, C++, Linux, Git, CUDA"], right_x, y_right, right_w)
    y_right = label_block(c, "RESEARCH", ["Baseline reproduction, ablation, benchmarking, scientific visualization"], right_x, y_right, right_w)
    y_right -= 4

    y_right = section(c, "Research Interests", right_x, y_right, right_w)
    y_right = paragraph(c, "Learning-Augmented Optimization", right_x, y_right, right_w, 8.15, 10.2)
    y_right = paragraph(c, "Combinatorial Optimization", right_x, y_right, right_w, 8.15, 10.2)
    y_right = paragraph(c, "Evolutionary Computation", right_x, y_right, right_w, 8.15, 10.2)
    y_right = paragraph(c, "Reinforcement Learning", right_x, y_right, right_w, 8.15, 10.2)
    y_right = paragraph(c, "Vehicle Routing and Energy Delivery", right_x, y_right, right_w, 8.15, 10.2)
    y_right -= 7

    y_right = section(c, "Languages", right_x, y_right, right_w)
    y_right = paragraph(c, "Mandarin and Cantonese: Native", right_x, y_right, right_w, 8.1, 10.2)
    y_right = paragraph(c, "English: Professional working proficiency", right_x, y_right, right_w, 8.1, 10.2)
    y_right -= 7

    y_right = section(c, "Beyond Research", right_x, y_right, right_w)
    y_right = paragraph(c, "Football, tennis, film, and CS2. Chelsea supporter.", right_x, y_right, right_w, 8.1, 10.2)
    y_right -= 9

    y_right = section(c, "Selected Coursework", right_x, y_right, right_w)
    y_right = paragraph(c, "Data Structures and Algorithms", right_x, y_right, right_w, 8.1, 10.2)
    y_right = paragraph(c, "Optimization Theory", right_x, y_right, right_w, 8.1, 10.2)
    y_right = paragraph(c, "Probability and Statistics", right_x, y_right, right_w, 8.1, 10.2)
    y_right = paragraph(c, "Reinforcement Learning", right_x, y_right, right_w, 8.1, 10.2)
    y_right = paragraph(c, "Deep Learning", right_x, y_right, right_w, 8.1, 10.2)

    # Footer
    footer_y = 30
    c.setStrokeColor(RULE)
    c.setLineWidth(0.7)
    c.line(MARGIN_X, footer_y + 10, PAGE_W - MARGIN_X, footer_y + 10)
    c.setFillColor(MUTED)
    c.setFont("Helvetica", 7.4)
    c.drawString(MARGIN_X, footer_y, "Academic portfolio: kennethzhang29.github.io/academicpages.github.io")
    c.drawRightString(PAGE_W - MARGIN_X, footer_y, "Last updated September 2026")

    if min(y_left, y_right) < footer_y + 18:
        raise RuntimeError(f"Content overflow: lowest y={min(y_left, y_right):.1f}")

    c.showPage()
    c.save()


if __name__ == "__main__":
    build()
