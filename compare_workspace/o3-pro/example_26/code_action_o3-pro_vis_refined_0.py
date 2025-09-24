import matplotlib
matplotlib.use('Agg')
"""
Deterministic 3-D visualisation of several Gaussian probability-density curves.
The area beneath every curve is rendered as a filled polygon that sits in the
x–z plane at a different, constant y-coordinate (the mean of the Gaussian).
Exactly one PNG file called ``novice_final.png`` will be written and no
interactive window will be opened.

Strictly uses Matplotlib (no seaborn/plotly/…).
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D        # required for 3-D projection
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from matplotlib import patches  # proxy artists for the legend

# --------------------------------------------------------------------------- #
# 1. Axes (x) and Gaussian means (y) ---------------------------------------- #
# --------------------------------------------------------------------------- #
x = np.linspace(0.0, 20.0, 200)        # position axis
y_means = np.linspace(2.0, 10.0, 5)    # five different Gaussian means (y-axis)

# --------------------------------------------------------------------------- #
# 2. Compute Gaussian probability densities (z) ----------------------------- #
# --------------------------------------------------------------------------- #
def gaussian(x_vals: np.ndarray, mu: float, sigma: float) -> np.ndarray:
    """Return a 1-D Gaussian PDF evaluated at *x_vals*."""
    coeff = 1.0 / (sigma * np.sqrt(2.0 * np.pi))
    exponent = -0.5 * ((x_vals - mu) / sigma) ** 2
    return coeff * np.exp(exponent)

z = np.array([gaussian(x, mu, mu / 2.0) for mu in y_means])  # shape (N_means, N_x)

# --------------------------------------------------------------------------- #
# 3. Create figure & 3-D axes ------------------------------------------------ #
# --------------------------------------------------------------------------- #
fig = plt.figure(figsize=(9, 6))
ax = fig.add_subplot(111, projection='3d')

# --------------------------------------------------------------------------- #
# 4. Draw filled polygons + their outline curves ---------------------------- #
# --------------------------------------------------------------------------- #
proxy_patches = []  # for the legend

for idx, (mu, z_vals) in enumerate(zip(y_means, z)):
    # Color from the Plasma colormap (high contrast & perceptually uniform)
    colour = plt.cm.plasma(1.0 - idx / (len(y_means) - 1)) if len(y_means) > 1 else plt.cm.plasma(0.5)

    # Build vertices of the polygon that fills the area under the curve.
    # Forward part: (x, const. y, z).  Return path: (x reversed, const. y, 0)
    verts = [
        *zip(x, np.full_like(x, mu), z_vals),
        *zip(x[::-1], np.full_like(x, mu), np.zeros_like(z_vals))
    ]

    # Add filled surface
    poly = Poly3DCollection([verts], facecolor=colour, alpha=0.5, edgecolor='none')
    ax.add_collection3d(poly)

    # Plot the outline of the curve on top of the fill for clarity
    ax.plot(x, np.full_like(x, mu), z_vals, color=colour, lw=1.5)

    # Collect a proxy artist so the legend shows a coloured square for each mean
    proxy_patches.append(patches.Patch(facecolor=colour, label=f"Mean = {mu:.1f}", alpha=0.5))

# --------------------------------------------------------------------------- #
# 5. Axis limits, labels, title, legend ------------------------------------- #
# --------------------------------------------------------------------------- #
ax.set_xlim(0, 20)
ax.set_ylim(y_means.min(), y_means.max())
ax.set_zlim(0, z.max() * 1.1)

ax.set_xlabel('X (Position)')
ax.set_ylabel('Y (Mean of Gaussian)')
ax.set_zlabel('Probability Density')
ax.set_title('3-D Gaussian Curves with Filled Polygons')

ax.legend(handles=proxy_patches, loc='upper right')

# --------------------------------------------------------------------------- #
# 6. Save PNG and finish ----------------------------------------------------- #
# --------------------------------------------------------------------------- #
plt.tight_layout()
plt.savefig("novice_final.png", dpi=300)