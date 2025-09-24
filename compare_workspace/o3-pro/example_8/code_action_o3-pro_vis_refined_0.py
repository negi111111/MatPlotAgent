import matplotlib
matplotlib.use('Agg')
"""
Deterministic polar scatter plot.

Requirements satisfied:
1. Only uses NumPy and Matplotlib (no seaborn/plotly/etc.).
2. Sets a fixed random seed for reproducibility.
3. Saves exactly one PNG file named 'novice_final.png'.
4. Does NOT call or open any interactive windows.
"""

import numpy as np
import matplotlib.pyplot as plt

# ------------------------------------------------------------------
# 1. Deterministic random data generation
# ------------------------------------------------------------------
np.random.seed(42)          # Fixed seed for reproducibility
num_points = 200

# Radial distances (r) ∈ [0, 1], angles (θ) ∈ [0, 2π)
r = np.random.rand(num_points)
theta = np.random.rand(num_points) * 2 * np.pi

# ------------------------------------------------------------------
# 2. Visual encodings
# ------------------------------------------------------------------
#   • Area ∝ r² so that points farther from origin appear larger.
#   • Hue ∝ θ using the HSV colormap for a smooth color wheel effect.
area   = (r ** 2) * 1000           # Scale factor for visibility
colors = plt.cm.hsv(theta / (2 * np.pi))   # Normalize θ to [0,1]

# ------------------------------------------------------------------
# 3. Plot construction
# ------------------------------------------------------------------
fig = plt.figure(figsize=(8, 8))
ax  = fig.add_subplot(111, polar=True)

ax.scatter(theta,
           r,
           s=area,
           c=colors,
           alpha=0.75,
           edgecolors='w',
           linewidths=0.5)

# Title (use a newline to keep it compact inside the figure)
ax.set_title("Random Polar Scatter (200 points)\nArea ∝ r², Hue ∝ θ", va='bottom')

# Optional axis labels; harmless in a polar projection
ax.set_xlabel("Angle (radians)")
ax.set_ylabel("Radius")

# ------------------------------------------------------------------
# 4. Finalize and save
# ------------------------------------------------------------------
plt.savefig("novice_final.png", bbox_inches='tight')
# Do NOT call  ensures non-interactive, file-only output