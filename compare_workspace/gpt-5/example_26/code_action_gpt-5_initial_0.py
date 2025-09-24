import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from matplotlib.colors import Normalize

# 1) Prepare axes data
x = np.linspace(0, 20, 400)          # X: 0 to 20, evenly spaced
mu_values = np.linspace(2, 10, 17)   # Y means: 2 to 10, 17 samples (step 0.5)

# 2) Colormap setup (reversed plasma) with normalization over Y (mu) range
cmap = plt.cm.plasma_r
norm = Normalize(vmin=mu_values.min(), vmax=mu_values.max())

# 3) Create figure and 3D axes
fig = plt.figure(figsize=(11, 8))
ax = fig.add_subplot(111, projection='3d')

z_max_overall = 0.0

# 4) Loop over means to plot lines and filled polygons
for mu in mu_values:
    sigma = 0.5 * mu  # Standard deviation is half the mean (Y value)

    # Gaussian PDF along x for this mean and sigma
    z = (1.0 / (np.sqrt(2 * np.pi) * sigma)) * np.exp(-0.5 * ((x - mu) / sigma) ** 2)

    # Color for this mean using reversed plasma colormap
    color = cmap(norm(mu))

    # Plot the 3D line at constant y=mu
    ax.plot(x, np.full_like(x, mu), z, color=color, linewidth=2.0, alpha=1.0)

    # Build a polygon under the curve down to z=0
    curve_points = list(zip(x.tolist(), [mu] * x.size, z.tolist()))
    base_points = list(zip(x[::-1].tolist(), [mu] * x.size, [0.0] * x.size))
    verts = curve_points + base_points

    poly = Poly3DCollection([verts], facecolors=[color], edgecolors='none', alpha=0.6)
    ax.add_collection3d(poly)

    # Keep track of maximum z for setting z-axis limits
    z_max_overall = max(z_max_overall, float(np.max(z)))

# 5) Set axis limits
ax.set_xlim(0, 20)
ax.set_ylim(mu_values.min(), mu_values.max())
ax.set_zlim(0, z_max_overall * 1.1)

# 6) Labels and title
ax.set_xlabel('X')
ax.set_ylabel('Y (mean μ)')
ax.set_zlabel('Probability density (Gaussian PDF)')
ax.set_title('3D Filled Polygons Under Gaussian PDF Lines')

# 7) Colorbar indicating the mean (μ) mapping to color
sm = plt.cm.ScalarMappable(cmap=cmap, norm=norm)
sm.set_array([])
cbar = plt.colorbar(sm, ax=ax, pad=0.1, fraction=0.035)
cbar.set_label('Mean (μ)')

# 8) View settings and save
ax.view_init(elev=25, azim=-60)
plt.tight_layout()
plt.savefig("novice.png")