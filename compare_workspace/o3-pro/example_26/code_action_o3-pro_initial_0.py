import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

# 1. Prepare x-axis values
x = np.linspace(0.0, 20.0, 200)

# 2. Means along the y-axis (from 2 to 10, inclusive)
y_means = np.arange(2, 11)

# 3. Compute one Gaussian curve for each mean value
gaussians = []
for mu in y_means:
    sigma = 0.5 * mu
    z = (1.0 / (sigma * np.sqrt(2.0 * np.pi))) * np.exp(-0.5 * ((x - mu) / sigma) ** 2)
    gaussians.append(z)

# 4. Build 3-D polygon vertices (top edge = curve, bottom edge = baseline at z=0)
polys = []
for idx, mu in enumerate(y_means):
    z = gaussians[idx]
    verts_top    = [(xi, mu, zi) for xi, zi in zip(x, z)]
    verts_bottom = [(xi, mu, 0.0) for xi in x[::-1]]
    polys.append(verts_top + verts_bottom)

# 5. Map colours to polygons using reversed plasma colormap
y_min, y_max = y_means.min(), y_means.max()
colours = cm.plasma_r((y_means - y_min) / (y_max - y_min))

# 6. Create figure and 3-D axes
fig = plt.figure(figsize=(10, 7))
ax  = fig.add_subplot(111, projection='3d')

# 7. Add filled polygons
poly_collection = Poly3DCollection(polys, facecolors=colours, edgecolor='k', alpha=0.7)
ax.add_collection3d(poly_collection)

# 8. (Optional) Plot the outline curves for context
for idx, mu in enumerate(y_means):
    ax.plot(x, np.full_like(x, mu), gaussians[idx],
            color=colours[idx], linewidth=2.0)

# 9. Axis labels, limits, and viewing angle
ax.set_xlabel('X (Position)')
ax.set_ylabel('Y (Mean of Gaussian)')
ax.set_zlabel('Probability Density')

ax.set_xlim(0, 20)
ax.set_ylim(2, 10)
ax.set_zlim(0, 0.45)

ax.set_title('3D Gaussian Curves with Filled Polygons')
ax.view_init(elev=25, azim=-60)

plt.tight_layout()
plt.savefig("novice.png")  # required by task