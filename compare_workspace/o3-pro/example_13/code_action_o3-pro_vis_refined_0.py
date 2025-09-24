import matplotlib
matplotlib.use('Agg')
"""
Deterministic plotting script that builds:
1. Four bar charts with different hatch patterns
2. A cosine curve with a hatched, magenta filled area underneath
3. An ellipse and a triangle overlaid on the cosine plot

The figure is arranged in a 3 × 2 mosaic.  
Only Matplotlib (plus NumPy for data) is used, satisfying the strict
library constraints.  Exactly one PNG file is written.
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse, Polygon

# ---------------------------------------------------------------------
# 1. Data for bar plots
categories = ['Cat 0', 'Cat 1', 'Cat 2', 'Cat 3', 'Cat 4']
values = [5, 7, 3, 8, 6]

# ---------------------------------------------------------------------
# 2. Create a 3x2 subplot grid
fig, axs = plt.subplots(3, 2, figsize=(10, 10))

# ---------------------------------------------------------------------
# 3. First row – bar plots with forward and backward slashes
axs[0, 0].bar(categories, values, color='cyan', hatch='/', edgecolor='black')
axs[0, 1].bar(categories, values, color='cyan', hatch='\\', edgecolor='black')
for ax in axs[0]:
    ax.set_ylabel('Value')
    ax.set_ylim(0, max(values) + 2)

# ---------------------------------------------------------------------
# 4. Second row – bar plots with 'x' and 'o' hatch patterns
axs[1, 0].bar(categories, values, color='orange', hatch='x', edgecolor='black')
axs[1, 1].bar(categories, values, color='orange', hatch='o', edgecolor='black')
for ax in axs[1]:
    ax.set_ylabel('Value')
    ax.set_ylim(0, max(values) + 2)

# ---------------------------------------------------------------------
# 5. Third row, left cell – cosine curve with filled area
x = np.linspace(0, 2 * np.pi, 400)
y = np.cos(x)
axs[2, 0].plot(x, y, color='black', linewidth=1)
axs[2, 0].fill_between(x, y, 0, color='magenta', hatch='/', alpha=0.5)

# Axes formatting
axs[2, 0].set_xlim(0, 2 * np.pi)
axs[2, 0].set_ylim(-1.5, 1.5)
axs[2, 0].set_xlabel('x')
axs[2, 0].set_ylabel('cos(x)')
axs[2, 0].set_aspect('equal', adjustable='box')

# ---------------------------------------------------------------------
# 6. Add geometric shapes – an ellipse and a triangle
ellipse = Ellipse(xy=(np.pi, 0), width=2, height=1,
                  edgecolor='black', facecolor='yellow', hatch='x')
triangle = Polygon([[np.pi - 0.5, 0],
                    [np.pi + 0.5, 0],
                    [np.pi, 0.5]],
                   closed=True, edgecolor='black',
                   facecolor='cyan', hatch='\\')
axs[2, 0].add_patch(ellipse)
axs[2, 0].add_patch(triangle)

# ---------------------------------------------------------------------
# 7. Remove the unused subplot (bottom-right)
fig.delaxes(axs[2, 1])

# ---------------------------------------------------------------------
# 8. Final layout adjustments and save
plt.tight_layout()
plt.savefig("novice_final.png")  # Exactly one PNG file as required