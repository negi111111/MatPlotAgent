import matplotlib
matplotlib.use('Agg')
"""
Deterministic side-by-side bar charts that satisfy all requirements.

1. Only Matplotlib is used for plotting.
2. The random seed is fixed for reproducibility.
3. Two bar charts are rendered in one figure:
   • Left: a uniform transparency (alpha = 0.5) for both bar faces and edges.
   • Right: per-bar transparencies where face-alpha + edge-alpha = 1.
4. Exactly one PNG file (“novice_final.png”) is created; no interactive
   windows are opened.
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

# ------------------------------------------------------------------
# Prepare reproducible data
# ------------------------------------------------------------------
np.random.seed(42)                       # 1. reproducibility
x = np.arange(1, 21)                     # 2. x-values 1 … 20
y = np.random.uniform(-1, 1, size=20)    # 3. 20 y-values in [-1, 1]

# Colors: blue for positive, orange for negative values
base_colors = ['blue' if val > 0 else 'orange' for val in y]

# ------------------------------------------------------------------
# Create the figure with two side-by-side subplots
# ------------------------------------------------------------------
fig, axs = plt.subplots(1, 2, figsize=(14, 5))

# ------------------------------------------------------------------
# 1st subplot – uniform transparency (alpha = 0.5) for faces and edges
# ------------------------------------------------------------------
uniform_alpha = 0.5
for xi, yi, c in zip(x, y, base_colors):
    face_rgba = mcolors.to_rgba(c, alpha=uniform_alpha)
    edge_rgba = (0, 0, 0, uniform_alpha)          # black edge, same alpha
    axs[0].bar(xi, yi,
               color=face_rgba,
               edgecolor=edge_rgba,
               linewidth=1)

axs[0].set_title("Uniform transparency for all bars and edges")
axs[0].set_xlabel("Index")
axs[0].set_ylabel("Value")

# ------------------------------------------------------------------
# 2nd subplot – individual transparencies (face_alpha + edge_alpha = 1)
# ------------------------------------------------------------------
abs_y = np.abs(y)
max_abs_y = abs_y.max() if abs_y.max() > 0 else 1.0     # avoid div-by-zero
edge_alphas = abs_y / max_abs_y                         # 0 … 1
face_alphas = 1.0 - edge_alphas                         # ensure sums to 1

for xi, yi, c, f_a, e_a in zip(x, y, base_colors, face_alphas, edge_alphas):
    face_rgb = mcolors.to_rgb(c)
    face_rgba = (*face_rgb, f_a)
    edge_rgba = (0, 0, 0, e_a)                          # black with alpha
    axs[1].bar(xi, yi,
               color=face_rgba,
               edgecolor=edge_rgba,
               linewidth=1)

axs[1].set_title("Adjusted transparencies for each bar and edge")
axs[1].set_xlabel("Index")
axs[1].set_ylabel("Value")

# ------------------------------------------------------------------
# Layout & save
# ------------------------------------------------------------------
plt.tight_layout()
plt.savefig("novice_final.png")