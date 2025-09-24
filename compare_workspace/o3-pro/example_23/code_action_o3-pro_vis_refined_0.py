"""
Deterministic generation of a 3-D parametric curve and saving it to
'novice_final.png' using only NumPy and Matplotlib.
"""

import numpy as np

# Use a non-interactive backend to guarantee no GUI is opened.
import matplotlib
matplotlib.use("Agg")          # noqa: E402
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401  (needed for 3-D projection)

# ------------------------------------------------------------------
# 1. Create the parameter grids
# ------------------------------------------------------------------
alpha = np.linspace(-6 * np.pi, 6 * np.pi, 1000)  # 1000 points from -6π to 6π
w = np.linspace(-3, 3, 1000)                      # 1000 points from -3 to 3

# ------------------------------------------------------------------
# 2. Compute p, a, and b according to the specification
# ------------------------------------------------------------------
p = w**3 + 2               # p = w³ + 2
a = p * np.sin(alpha)      # a = p · sin(α)
b = p * np.cos(alpha)      # b = p · cos(α)

# ------------------------------------------------------------------
# 3. Build the 3-D plot
# ------------------------------------------------------------------
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')

ax.plot(a, b, w, color='tab:blue', label='parametric curve', linewidth=1.5)

# Axis labels and title
ax.set_xlabel('a')
ax.set_ylabel('b')
ax.set_zlabel('w')
ax.set_title('Parametric Curve')
ax.legend()

# ------------------------------------------------------------------
# 4. Save the figure (exactly one PNG file)
# ------------------------------------------------------------------
plt.savefig("novice_final.png", dpi=300, bbox_inches='tight')