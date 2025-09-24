import matplotlib
matplotlib.use('Agg')
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.colors import to_rgba

# 1) Reproducible random numbers
np.random.seed(42)

# 2) Data
x = np.arange(1, 21)           # x values: 1..20
y = np.random.randn(20)        # 20 random y values (positive and negative)

# 3) Face colors based on sign of y
base_colors = ['blue' if yi > 0 else 'orange' for yi in y]

# 4) Set up the figure with two side-by-side charts
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(14, 6), sharey=True)

# 5) First chart: uniform transparency for all bars and edges
uniform_alpha = 0.6
axes[0].bar(
    x, y,
    color=base_colors,        # per-bar face color: blue if y>0 else orange
    edgecolor='black',        # black edges
    linewidth=1.0,
    width=0.8,
    alpha=uniform_alpha       # same alpha applied to faces and edges
)
axes[0].set_title("Uniform transparency value for all bars and edges")
axes[0].axhline(0, color='grey', linewidth=0.8)

# 6) Second chart: adjusted transparencies per bar and per edge
abs_y = np.abs(y)
max_abs = abs_y.max()

if max_abs == 0:
    # All values are zero; choose a neutral alpha (e.g., 0.5) for faces
    face_alphas = np.full_like(abs_y, 0.5, dtype=float)
else:
    # Normalize absolute y values to [0, 1] for face alphas
    face_alphas = abs_y / max_abs

# Edge alphas complement face alphas so each bar's face_alpha + edge_alpha == 1
edge_alphas = 1.0 - face_alphas

# Build RGBA colors with distinct alpha per bar
face_rgba = [to_rgba(c, a) for c, a in zip(base_colors, face_alphas)]
edge_rgba = [to_rgba('black', a) for a in edge_alphas]

axes[1].bar(
    x, y,
    color=face_rgba,          # per-bar face RGBA (unique alpha per bar)
    edgecolor=edge_rgba,      # per-bar edge RGBA (alpha complements face alpha)
    linewidth=1.0,
    width=0.8                 # do not pass alpha here; use RGBA lists instead
)
axes[1].set_title("Adjusted transparencies for each bar and each edge")
axes[1].axhline(0, color='grey', linewidth=0.8)

# 7) Render
fig.tight_layout()
plt.savefig("novice.png")