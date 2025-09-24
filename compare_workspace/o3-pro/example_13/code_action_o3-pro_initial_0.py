import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import patches

# 1. Define the subplot layout
mosaic = """
AB
CD
EE
"""
fig, axes = plt.subplot_mosaic(mosaic, figsize=(9, 10))

# 2. Reusable bar-plot data
categories = np.arange(5)
values = np.array([4, 7, 1, 8, 5])
bar_width = 0.6

# 3. Four bar plots with distinct hatch patterns
axes["A"].bar(categories, values, width=bar_width,
              color='skyblue', edgecolor='black', hatch='/')
axes["B"].bar(categories, values, width=bar_width,
              color='skyblue', edgecolor='black', hatch='\\\\')
axes["C"].bar(categories, values, width=bar_width,
              color='coral', edgecolor='black', hatch='x')
axes["D"].bar(categories, values, width=bar_width,
              color='coral', edgecolor='black', hatch='o')

# Common cosmetic tweaks for A–D
for tag in "ABCD":
    axes[tag].set_xticks(categories)
    axes[tag].set_xticklabels([f'Cat {i}' for i in categories])
    axes[tag].set_ylabel('Value')

# 4. Filled area plot in section E
x = np.linspace(0, 2 * np.pi, 400)
y = np.cos(x)
axes["E"].fill_between(x, 0, y,
                       facecolor='magenta', alpha=0.4,
                       hatch='//', edgecolor='black')

# 5. Add an Ellipse and a Polygon
ellipse = patches.Ellipse((np.pi, 0.5), width=2.0, height=0.7,
                          facecolor='yellow', edgecolor='black',
                          hatch='..', linewidth=1.5)
triangle_vertices = [(np.pi - 1, -0.5),
                     (np.pi,       0.8),
                     (np.pi + 1, -0.5)]
polygon = patches.Polygon(triangle_vertices, closed=True,
                          facecolor='cyan', edgecolor='black',
                          hatch='xxx', linewidth=1.5)
axes["E"].add_patch(ellipse)
axes["E"].add_patch(polygon)

# 6. Axis limits and aspect ratio for E
axes["E"].set_aspect('equal', adjustable='box')
axes["E"].set_xlim(0, 2 * np.pi)
axes["E"].set_ylim(-1.5, 1.5)
axes["E"].set_xlabel('x')
axes["E"].set_ylabel('cos(x)')

# 7. Final layout adjustments and save
fig.tight_layout()
plt.savefig("novice.png")