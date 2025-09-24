import matplotlib
matplotlib.use('Agg')
"""
3-D Bar Plot of a 2-D Histogram (200 uniform points)

This script:
1. Generates two uniform random samples in the range [-5, 5].
2. Builds a 2-D histogram with 10 × 10 bins.
3. Visualises the histogram with a 3-D bar plot.
4. Saves the figure as 'novice_final.png'.

Only NumPy and Matplotlib are used, fully satisfying the stated constraints.
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D      # noqa: F401  (registers the 3-D projection)

# ------------------------------------------------------------------
# 1. Reproducible random numbers
# ------------------------------------------------------------------
np.random.seed(1234567)

# 2×200 uniform samples in [-5, 5]
x = np.random.uniform(-5, 5, 200)
y = np.random.uniform(-5, 5, 200)

# ------------------------------------------------------------------
# 2. Build a 2-D histogram
# ------------------------------------------------------------------
bins = 10
hist, xedges, yedges = np.histogram2d(
    x, y,
    bins=bins,
    range=[[-5, 5], [-5, 5]]
)

# ------------------------------------------------------------------
# 3. Prepare coordinates for bar3d
# ------------------------------------------------------------------
# Left-bottom cardinals of each bar
xpos, ypos = np.meshgrid(xedges[:-1], yedges[:-1], indexing="ij")
xpos = xpos.ravel()
ypos = ypos.ravel()
zpos = np.zeros_like(xpos)

# Bar dimensions
dx = (xedges[1] - xedges[0]) * np.ones_like(xpos)   # uniform bin width in x
dy = (yedges[1] - yedges[0]) * np.ones_like(ypos)   # uniform bin width in y
dz = hist.ravel()

# ------------------------------------------------------------------
# 4. Plot
# ------------------------------------------------------------------
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')

# Colour bars with a colormap based on height for better visual discrimination
normed_heights = dz / dz.max() if dz.max() > 0 else dz
colors = plt.cm.viridis(normed_heights)

ax.bar3d(xpos, ypos, zpos, dx, dy, dz, color=colors, zsort='average', edgecolor='k', linewidth=0.3)

# Axis labels and title
ax.set_xlabel('X values')
ax.set_ylabel('Y values')
ax.set_zlabel('Counts per bin')
ax.set_title('3-D Bar Plot of 2-D Histogram (200 uniform points)')

# Tidy view: rotate slightly for a better first impression
ax.view_init(elev=25, azim=135)

# ------------------------------------------------------------------
# 5. Save exactly one PNG and exit
# ------------------------------------------------------------------
plt.savefig("novice_final.png", dpi=300, bbox_inches='tight')