"""Restyle the generated 3D contribution SVG: GitHub-like font and a Tokyo Night pie palette.

The action hardcodes the font and takes pie colors from each repo's language color,
so both are rewritten here after generation.
"""
import re
import sys

FONT = '-apple-system, "Segoe UI", "Noto Sans", Helvetica, Arial, sans-serif'
PALETTE = ["#7aa2f7", "#bb9af7", "#7dcfff", "#9ece6a", "#e0af68", "#f7768e", "#ff9e64"]
OTHER = "#565f89"

path = sys.argv[1]
svg = open(path, encoding="utf-8").read()
svg = svg.replace('"Ubuntu", "Helvetica", "Arial", sans-serif', FONT, 1)

# Pie slices look like: <path d=".." style="fill: #3572A5;" class="stroke-bg" ...><title>Python 120</title>
slices = re.findall(r'style="fill: (#[0-9A-Fa-f]{3,6});" class="stroke-bg"[^>]*><title>([^<]*?) \d+</title>', svg)
mapping, i = {}, 0
for color, lang in slices:
    if color.lower() in mapping:
        continue
    mapping[color.lower()] = OTHER if lang == "other" else PALETTE[i % len(PALETTE)]
    if lang != "other":
        i += 1

def recolor(m):
    return m.group(1) + mapping.get(m.group(2).lower(), m.group(2))

# legend squares use fill="#..", slices use style="fill: #..;"
svg = re.sub(r'(fill="|fill: )(#[0-9A-Fa-f]{6}|#[0-9A-Fa-f]{3})\b', recolor, svg)
assert slices, "no pie slices found; the action's SVG format may have changed"
open(path, "w", encoding="utf-8").write(svg)
print(f"restyled {len(mapping)} pie colors in {path}")
