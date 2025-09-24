import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import PolyCollection
from mpl_toolkits.mplot3d import Axes3D

# Generate data
x = np.linspace(0, 20, 200)
y_means = np.linspace(2, 10, 9)
z_values = []

# Calculate Gaussian probabilities
for mean in y_means:
    std_dev = mean / 2
    z = (1 / (std_dev * np.sqrt(2 * np.pi))) * \
        np.exp(-0.5 * ((x - mean) / std_dev) ** 2)
    z_values.append(z)

# Create polygon vertices
vertices = []
for i, mean in enumerate(y_means):
    top = np.column_stack([x, np.full_like(x, mean), z_values[i]])
    bottom = np.column_stack([x[::-1], np.full_like(x, mean), np.zeros_like(x)])
    vertices.append(np.vstack([top, bottom]))

# Initialize plot
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')
ax.set_xlabel('X-axis', fontsize=12)
ax.set_ylabel('Y-axis (Mean)', fontsize=12)
ax.set_zlabel('Probability Density', fontsize=12)
ax.set_xlim(0, 20)
ax.set_ylim(2, 10)
ax.set_zlim(0, 0.5)

# Add polygons with reversed plasma colormap
poly_collection = PolyCollection(
    vertices,
    facecolors=plt.cm.plasma_r(np.linspace(0, 1, len(y_means))),
    alpha=0.7,
    edgecolors='k',
    linewidths=0.5
)
ax.add_collection3d(poly_collection)

# Add line plots
for i, mean in enumerate(y_means):
    ax.plot(x, [mean] * len(x), z_values[i], color='k', linewidth=1.5)

plt.tight_layout()
plt.savefig("novice.png")  # Save as PNG without displaying