#!/usr/bin/env python3
"""HUD-themed pixel banner for Awesome Craft Jarvis. Original scene, no brand marks."""
import random
from pathlib import Path

random.seed(13)
P = 8
W = 100
H = 34  # 800x272
out = []


def r(x, y, w, h, c, cls=None, extra=""):
    a = f' class="{cls}"' if cls else ""
    out.append(
        f'<rect x="{x*P}" y="{y*P}" width="{w*P}" height="{h*P}" fill="{c}"{a}{extra}/>'
    )


def disc(cx, cy, rad, col, cls=None):
    for dy in range(-rad, rad + 1):
        for dx in range(-rad, rad + 1):
            if dx * dx + dy * dy <= rad * rad:
                r(cx + dx, cy + dy, 1, 1, col, cls)


def ring(cx, cy, rad, col, cls=None):
    lo = (rad - 0.7) ** 2
    hi = (rad + 0.7) ** 2
    for dy in range(-rad - 1, rad + 2):
        for dx in range(-rad - 1, rad + 2):
            d2 = dx * dx + dy * dy
            if lo <= d2 <= hi:
                r(cx + dx, cy + dy, 1, 1, col, cls)


# 3x5 pixel font
F = {
    "A": ["010", "101", "111", "101", "101"],
    "C": ["011", "100", "100", "100", "011"],
    "F": ["111", "100", "110", "100", "100"],
    "I": ["111", "010", "010", "010", "111"],
    "J": ["111", "001", "001", "101", "010"],
    "R": ["110", "101", "110", "101", "101"],
    "S": ["011", "100", "010", "001", "110"],
    "T": ["111", "010", "010", "010", "010"],
    "V": ["101", "101", "101", "101", "010"],
    " ": ["000", "000", "000", "000", "000"],
}

style = """
<style>
.tw{animation:tw 2.4s steps(2) infinite}
.tw2{animation:tw 3.1s steps(2) infinite .8s}
.tw3{animation:tw 1.9s steps(2) infinite 1.4s}
@keyframes tw{0%,100%{opacity:1}50%{opacity:.15}}
.blink{animation:tw 1s steps(1) infinite}
.glow{animation:glow 1.6s steps(3) infinite}
.glow2{animation:glow 1.8s steps(3) infinite .5s}
@keyframes glow{0%,100%{opacity:.3}50%{opacity:1}}
.pulse{animation:pulse 1.4s steps(2) infinite}
@keyframes pulse{0%,100%{opacity:.45}50%{opacity:1}}
.eq{animation:eq .6s steps(2) infinite}
.eq2{animation:eq .7s steps(2) infinite .15s}
.eq3{animation:eq .5s steps(2) infinite .3s}
@keyframes eq{0%,100%{transform:scaleY(1)}50%{transform:scaleY(.35)}}
.scan{animation:scan 3.2s steps(16) infinite}
@keyframes scan{0%{transform:translateY(0);opacity:.2}50%{transform:translateY(64px);opacity:.7}100%{transform:translateY(0);opacity:.2}}
.led{animation:led 1.2s steps(2) infinite}
.led2{animation:led 1.6s steps(2) infinite .4s}
.led3{animation:led 2s steps(2) infinite .8s}
@keyframes led{0%,100%{opacity:1}50%{opacity:.2}}
</style>
"""

# Night operations room
sky = ["#05080f", "#071018", "#0a1520", "#0c1b28", "#0e2130", "#102638", "#122a40"]
for i, c in enumerate(sky):
    r(0, i * 4, W, 4, c)

# Sparse HUD dots, keep the title band clear
for i in range(22):
    while True:
        x = random.randrange(W)
        y = random.randrange(11)
        if not (20 <= x <= 80 and y <= 8):
            break
    r(
        x,
        y,
        1,
        1,
        random.choice(["#67e8f9", "#fff7c2", "#5eead4"]),
        random.choice(["tw", "tw2", "tw3"]),
    )

# Corner viewfinder brackets
r(2, 11, 6, 1, "#155e75")
r(2, 11, 1, 5, "#155e75")
r(92, 11, 6, 1, "#155e75")
r(97, 11, 1, 5, "#155e75")
r(2, 27, 6, 1, "#155e75")
r(2, 23, 1, 5, "#155e75")
r(92, 27, 6, 1, "#155e75")
r(97, 23, 1, 5, "#155e75")

# Title: CRAFT JARVIS
title = "CRAFT JARVIS"
tx = (W - len(title) * 4) // 2
ty = 2
for k, ch in enumerate(title):
    for yy, row in enumerate(F[ch]):
        for xx, b in enumerate(row):
            if b == "1":
                r(tx + k * 4 + xx + 0.25, ty + yy + 0.25, 1, 1, "#000", None, ' opacity=".55"')
                r(tx + k * 4 + xx, ty + yy, 1, 1, "#5eead4")

# Left sidebar: four abstract status cards
for i, (led, cls) in enumerate(
    (("#22c55e", "led"), ("#22c55e", "led2"), ("#fbbf24", "led3"), ("#64748b", "led"))
):
    y = 12 + i * 3
    r(4, y, 14, 2, "#0f172a")
    r(5, y, 12, 2, "#1e293b")
    r(6, y, 8, 1, "#334155")
    r(16, y, 1, 1, led, cls)

# Desk / console surface (behind the ring ticks)
for x in range(W):
    r(x, 28, 1, 1, "#0e7490" if x % 8 == 0 else "#164e63")
    r(x, 29, 1, 1, "#0f172a" if x % 2 else "#1e293b")
    for y in range(30, H):
        r(x, y, 1, 1, "#070b14" if (x + y) % 4 else "#0b1220")

# Horizontal scan line
r(20, 13, 60, 1, "#164e63", "scan")

# Center status ring: concentric pixel rings with tick marks. Original HUD, not a brand mark.
cx, cy = 49, 18
disc(cx, cy, 8, "#06202e")
ring(cx, cy, 8, "#155e75")
ring(cx, cy, 6, "#0e7490", "pulse")
ring(cx, cy, 4, "#22d3ee", "glow")
disc(cx, cy, 1, "#ecfeff", "glow2")
for dx, dy in ((0, -9), (0, 9), (-9, 0), (9, 0)):
    r(cx + dx, cy + dy, 1, 1, "#5eead4", "pulse")
# short axis ticks
for dx, dy in ((0, -7), (0, 7), (-7, 0), (7, 0)):
    r(cx + dx, cy + dy, 1, 1, "#67e8f9")

# Right: voice waveform, scaled from the bottom of each bar
bars = [4, 7, 5, 9, 6, 8, 5, 7, 4, 6]
cls_cycle = ["eq", "eq2", "eq3", "eq2", "eq"]
for i, hgt in enumerate(bars):
    x = 78 + i * 2
    y = 22 - hgt
    out.append(
        f'<rect x="{x*P}" y="{y*P}" width="{P}" height="{hgt*P}" fill="#22d3ee" '
        f'class="{cls_cycle[i % 5]}" style="transform-box:fill-box;transform-origin:center bottom"/>'
    )

# Pixel microphone, left of the ring
r(33, 24, 3, 3, "#334155")
r(34, 25, 1, 2, "#94a3b8")
r(33, 27, 3, 1, "#1e293b")
r(34, 24, 1, 1, "#22d3ee", "led")

# Small speaker grille, right of the ring
r(64, 24, 5, 3, "#1e293b")
r(65, 25, 3, 1, "#334155")
r(66, 24, 1, 1, "#22d3ee", "led2")
r(65, 26, 1, 1, "#64748b")
r(67, 26, 1, 1, "#64748b")

# Status bar
out.append(
    f'<text x="{8}" y="{H*P-8}" font-family="monospace" font-size="12" fill="#5eead4">'
    f"&gt; local assistant ready"
    f'<tspan class="blink">_</tspan></text>'
)

svg = (
    f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W*P} {H*P}" '
    f'width="{W*P}" height="{H*P}" shape-rendering="crispEdges">'
    + style
    + "".join(out)
    + "</svg>"
)

dest = Path(__file__).resolve().parent / "assets" / "craft-jarvis.svg"
dest.write_text(svg)
print(f"wrote {dest} ({dest.stat().st_size} bytes)")
