#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Board DSL Transpiler: Reads from a local .md file and outputs an SVG beside it.
KISS Principle: Minimal file I/O and direct string manipulation.
"""

import re
import html
from pathlib import Path

def compile_board_dsl(dsl_text: str, scale: float = 6.0, margin: float = 30.0) -> str:
    raw_lines = dsl_text.strip().splitlines()
    clean_lines = []
    for line in raw_lines:
        line_no_comment = re.sub(r'%.*$', '', line).strip()
        if line_no_comment:
            clean_lines.append(line_no_comment)

    if not clean_lines:
        raise ValueError("فایل مورد نظر خالی است یا دستور معتبری ندارد.")

    header_match = re.fullmatch(r'board\s*\(\s*(\d+)\s*,\s*(\d+)\s*\)\s*\{', clean_lines[0])
    if not header_match or clean_lines[-1] != '}':
        raise ValueError("خطای سینتکس: فرمت تعریف board(W, H) { ... } اشتباه است.")
    
    board_w, board_h = map(int, header_match.groups())
    points = {}
    edges = []

    for line in clean_lines[1:-1]:
        pt_match = re.fullmatch(r'([A-Za-z_]\w*)\s*=\s*\(\s*(-?[\d.]+)\s*,\s*(-?[\d.]+)\s*\)', line)
        edge_match = re.fullmatch(r'([A-Za-z_]\w*)\s*(--|~\(([+-])\)~)\s*([A-Za-z_]\w*)', line)

        if pt_match:
            name, x, y = pt_match.groups()
            points[name] = (float(x), float(y))
        elif edge_match:
            a, _, sign, b = edge_match.groups()
            edges.append((a, b, sign))
        else:
            raise ValueError(f"دستور ناشناخته: {line}")

    def to_svg_coords(pt):
        x, y = pt
        return (margin + x * scale, margin + (board_h - y) * scale)

    svg_w = board_w * scale + 2 * margin
    svg_h = board_h * scale + 2 * margin

    svg_elements = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {svg_w} {svg_h}" width="100%">',
        '  <style>',
        '    rect.board { fill: #1e1e1e; stroke: #444; stroke-width: 2; rx: 6; }',
        '    line.grid { stroke: #2a2a2a; stroke-width: 1; stroke-dasharray: 4; }',
        '    path.edge { fill: none; stroke: #4ea8de; stroke-width: 2.5; stroke-linecap: round; }',
        '    circle.node { fill: #f72585; stroke: #fff; stroke-width: 1.5; }',
        '    text.label { font-family: monospace; font-size: 13px; fill: #f1f5f9; font-weight: bold; }',
        '  </style>',
        f'  <rect class="board" x="{margin}" y="{margin}" width="{board_w * scale}" height="{board_h * scale}"/>'
    ]

    # رسم خطوط شبکه (Grid)
    step_x = max(1, board_w // 10)
    for x in range(0, board_w + 1, step_x):
        sx1, sy1 = to_svg_coords((x, 0))
        sx2, sy2 = to_svg_coords((x, board_h))
        svg_elements.append(f'  <line class="grid" x1="{sx1:g}" y1="{sy1:g}" x2="{sx2:g}" y2="{sy2:g}"/>')

    step_y = max(1, board_h // 10)
    for y in range(0, board_h + 1, step_y):
        sx1, sy1 = to_svg_coords((0, y))
        sx2, sy2 = to_svg_coords((board_w, y))
        svg_elements.append(f'  <line class="grid" x1="{sx1:g}" y1="{sy1:g}" x2="{sx2:g}" y2="{sy2:g}"/>')

    # رسم یال‌ها
    for a, b, sign in edges:
        if a not in points or b not in points:
            raise KeyError(f"نقطه نامعتبر در یال: {a} یا {b} تعریف نشده‌اند.")
        
        x1, y1 = to_svg_coords(points[a])
        x2, y2 = to_svg_coords(points[b])

        if sign is None:
            svg_elements.append(f'  <path class="edge" d="M {x1:g},{y1:g} L {x2:g},{y2:g}"/>')
        else:
            dx, dy = x2 - x1, y2 - y1
            length = (dx**2 + dy**2) ** 0.5
            if length == 0:
                continue

            # ارتفاع انحنا متناسب با طول خط، با حد بالا
            rise = min(length * 0.2, 20 * scale)
            # '+' یعنی سهمی رو به بالای صفحه (در مختصات SVG یعنی y کمتر)
            direction = -1 if sign == '+' else 1

            c1x = x1 + dx / 3
            c1y = y1 + direction * rise
            c2x = x1 + 2 * dx / 3
            c2y = y2 + direction * rise

            svg_elements.append(
                f'  <path class="edge" d="M {x1:g},{y1:g} '
                f'C {c1x:g},{c1y:g} {c2x:g},{c2y:g} {x2:g},{y2:g}"/>'
            )

    # رسم نودها و لیبل‌ها
    for name, pt in points.items():
        sx, sy = to_svg_coords(pt)
        svg_elements.append(f'  <circle class="node" cx="{sx:g}" cy="{sy:g}" r="4.5"/>')
        svg_elements.append(f'  <text class="label" x="{sx + 8:g}" y="{sy - 6:g}">{html.escape(name)}</text>')

    svg_elements.append('</svg>')
    return '\n'.join(svg_elements)


def process_markdown_file(md_path: Path):
    if not md_path.exists():
        print(f"فایل {md_path} پیدا نشد!")
        return
    
    content = md_path.read_text(encoding="utf-8")
    match = re.search(r'```(?:board)?\s*(board\s*\(.*?\)\s*\{.*?\})\s*```', content, re.DOTALL)
    
    if match:
        dsl_code = match.group(1)
    else:
        dsl_code = content

    svg_data = compile_board_dsl(dsl_code)
    out_path = md_path.with_suffix('.svg')
    out_path.write_text(svg_data, encoding="utf-8")
    print(f"موفق! فایل SVG در اینجا ذخیره شد: {out_path.resolve()}")


if __name__ == "__main__":
    script_dir = Path(__file__).resolve().parent
    target_md = script_dir / "board_input.md"
    process_markdown_file(target_md)
