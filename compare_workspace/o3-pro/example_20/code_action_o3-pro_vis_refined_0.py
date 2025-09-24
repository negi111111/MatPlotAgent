"""
Deterministic 3-D bar chart using only NumPy and Matplotlib.

The script
1. Fixes the random seed for repeatability.
2. Generates four layers of random data (30 values each).
3. Draws a semi-transparent 3-D bar chart where every layer has its own colour
   and the last bar in each layer is highlighted in black.
4. Labels all axes clearly and writes the figure to the required PNG file.

The resulting image is saved as: novice_final.png
"""

import numpy as np
import matplotlib
matplotlib.use("Agg")        # ensure non-interactive backend
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # needed for 3-D plotting

# ------------------------------------------------------------------
# 1. Reproducible random data
# ------------------------------------------------------------------
np.random.seed(42)

# x-coordinates (0 … 29) for each bar
x = np.arange(30)

# Four layers (k = 0, 1, 2, 3) of y-values
y_layers = np.random.rand(4, 30)

# Colours for the four layers
layer_colours = ["purple", "orange", "grey", "pink"]

# ------------------------------------------------------------------
# 2. Create 3-D bar plot
# ------------------------------------------------------------------
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111, projection="3d")

# Fixed bar footprint (width along x and y)
dx = 0.8
dy = 0.8

for k in range(4):
    # All bars for this layer share the same y-position (the layer index)
    xs = x                           # x-positions of bars
    ys = np.full_like(x, k)          # constant y for the layer
    zs = np.zeros_like(x)            # bars start at z = 0
    dz = y_layers[k]                 # heights of the bars

    # Main bars with layer colour
    ax.bar3d(xs, ys, zs, dx, dy, dz, color=layer_colours[k], alpha=0.8, shade=True)

    # Last bar in the layer, coloured black and fully opaque
    ax.bar3d(x[-1], k, 0, dx, dy, y_layers[k, -1], color="black", alpha=1.0, shade=True)

# ------------------------------------------------------------------
# 3. Axis labelling
# ------------------------------------------------------------------
ax.set_xlabel("X-axis (Index)")
ax.set_ylabel("Y-axis (Layer)")
ax.set_zlabel("Z-axis (Value)")

ax.set_yticks(np.arange(4))
ax.set_yticklabels([f"Layer {i}" for i in range(4)])

# ------------------------------------------------------------------
# 4. Save exactly one PNG file
# ------------------------------------------------------------------
plt.tight_layout()
plt.savefig("novice_final.png")