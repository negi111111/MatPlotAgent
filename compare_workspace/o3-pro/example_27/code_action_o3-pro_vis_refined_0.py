import matplotlib
matplotlib.use('Agg')
"""
3-D Stem Plot of sin(x) − π/4 and cos(x) − π/4 from 0 to 4π
This script satisfies the following constraints:
1. Uses only NumPy and Matplotlib (no seaborn/plotly/etc.).
2. Creates a 3-D stem plot with two discrete data “rails”.
3. Saves exactly one PNG file called “novice_final.png”.
4. Does NOT call or open any interactive window.
The code is fully deterministic.
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 (imported for 3-D projection)
from matplotlib.lines import Line2D

# ----------------------------------------------------------------------
# Generate data
# ----------------------------------------------------------------------
x = np.linspace(0, 4 * np.pi, 100)          # 100 points from 0 to 4π
y_sin = np.sin(x) - (np.pi / 4)             # sin(x) − π/4
y_cos = np.cos(x) - (np.pi / 4)             # cos(x) − π/4

# ----------------------------------------------------------------------
# Create 3-D figure and axes
# ----------------------------------------------------------------------
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111, projection='3d')

# ----------------------------------------------------------------------
# Stem plot for sin rail (rail index 0 on the Y-axis)
# ----------------------------------------------------------------------
ax.stem(
    x,                            # X-coordinates
    np.zeros_like(x),             # Y-coordinates (rail at y = 0)
    y_sin,                        # Z-coordinates (amplitude)
    linefmt='b-', markerfmt='bo', basefmt=' '
)

# ----------------------------------------------------------------------
# Stem plot for cos rail (rail index 1 on the Y-axis)
# ----------------------------------------------------------------------
ax.stem(
    x,                            # X-coordinates
    np.ones_like(x),              # Y-coordinates (rail at y = 1)
    y_cos,                        # Z-coordinates (amplitude)
    linefmt='r-', markerfmt='ro', basefmt=' '
)

# ----------------------------------------------------------------------
# Axis labels, title, grid, and legend
# ----------------------------------------------------------------------
ax.set_xlabel('x')
ax.set_ylabel('Dataset Rail\n(0 = sin(x) − π/4, 1 = cos(x) − π/4)')
ax.set_zlabel('Amplitude')
ax.set_title('3-D Stem Plot of sin(x) − π/4 and cos(x) − π/4 from 0 to 4π')
ax.view_init(elev=20, azim=30)   # Adjust the view for clarity
ax.grid(True)

# Custom legend handles (one for each dataset)
legend_handles = [
    Line2D([0], [0], color='b', marker='o', linestyle='-', label='sin(x) − π/4'),
    Line2D([0], [0], color='r', marker='o', linestyle='-', label='cos(x) − π/4')
]
ax.legend(handles=legend_handles, loc='upper right')

# ----------------------------------------------------------------------
# Save the figure (exactly one PNG file)
# ----------------------------------------------------------------------
plt.tight_layout()
plt.savefig("novice_final.png")