"""
Deterministic 3-D parametric curve with custom “error bars”.

Requirements satisfied:
1. Uses ONLY Matplotlib (no seaborn/plotly/etc.).
2. Saves exactly one PNG called “novice_final.png”.
3. Does NOT call or open an interactive window.
"""

import numpy as np
import matplotlib
matplotlib.use("Agg")                 # non-interactive backend (keeps things headless)
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # registers the 3-D projection

# ------------------------------------------------------------------
# 1. Parameter array: 0 … 4π + 0.1  (1000 points, deterministic)
# ------------------------------------------------------------------
t = np.linspace(0.0, 4.0 * np.pi + 0.1, 1000)

# ------------------------------------------------------------------
# 2. Parametric curve coordinates
#    x = cos(t)
#    y = sin(2t)
#    z = cos(4t)
# ------------------------------------------------------------------
x = np.cos(t)
y = np.sin(2.0 * t)
z = np.cos(4.0 * t)

# ------------------------------------------------------------------
# 3. Select indices for “error bars” using the Boolean rule:
#    * every 20th point AND
#    * the integer group number (idx // 20) is 0 or 2 modulo 3
# ------------------------------------------------------------------
indices = np.arange(len(t))
mask = (indices % 20 == 0) & (((indices // 20) % 3 == 0) | ((indices // 20) % 3 == 2))
err_idx = np.where(mask)[0]

# Constant symmetric error length
err = 0.3

# ------------------------------------------------------------------
# 4. Build the figure
# ------------------------------------------------------------------
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection="3d")

# 4a. Main parametric curve
ax.plot(x, y, z, color="steelblue", linewidth=1.5, label="Parametric Curve")

# 4b. Manual 3-D “error bars”
for i in err_idx:
    # X-direction bar
    ax.plot([x[i] - err, x[i] + err], [y[i], y[i]], [z[i], z[i]],
            color="crimson", linewidth=0.8)
    # Y-direction bar
    ax.plot([x[i], x[i]], [y[i] - err, y[i] + err], [z[i], z[i]],
            color="crimson", linewidth=0.8)
    # Z-direction bar
    ax.plot([x[i], x[i]], [y[i], y[i]], [z[i] - err, z[i] + err],
            color="crimson", linewidth=0.8)

# 4c. Highlight the points where errors were placed
ax.scatter(x[err_idx], y[err_idx], z[err_idx],
           color="crimson", s=10, label="Error sample points")

# ------------------------------------------------------------------
# 5. Axis labels & legend
# ------------------------------------------------------------------
ax.set_xlabel("X label")
ax.set_ylabel("Y label")
ax.set_zlabel("Z label")
ax.legend(loc="upper left")

# ------------------------------------------------------------------
# 6. Save to disk (exactly one PNG file)
# ------------------------------------------------------------------
plt.savefig("novice_final.png", dpi=300)