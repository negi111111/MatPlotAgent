import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 (kept for compatibility as requested)
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

# Define the axes
x = np.linspace(0, 20, 100)   # x values from 0 to 20
y = np.linspace(2, 10, 5)     # y values from 2 to 10 (5 different means)

# Calculate the Gaussian distribution
X, Y = np.meshgrid(x, y)
sigma = Y / 2.0
Z = (1.0 / (np.sqrt(2.0 * np.pi) * sigma)) * np.exp(-0.5 * ((X - Y) / sigma) ** 2)

# Create the 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the filled polygons under each Gaussian curve using Poly3DCollection
for i, yi in enumerate(y):
    # Top boundary along the Gaussian curve at fixed y=yi
    top_vertices = np.column_stack([x, np.full_like(x, yi), Z[i]])
    # Bottom boundary at Z=0 to close the polygon
    bottom_vertices = np.column_stack([x[::-1], np.full_like(x, yi), np.zeros_like(x)])
    verts = np.vstack([top_vertices, bottom_vertices])
    poly = Poly3DCollection([verts], facecolors=plt.cm.plasma(1 - (i / len(y))), alpha=0.5, edgecolors='none')
    ax.add_collection3d(poly)

# Overlay the Gaussian surface
ax.plot_surface(X, Y, Z, alpha=0.3, cmap='plasma', edgecolor='none')

# Label the axes
ax.set_xlabel('X')
ax.set_ylabel('Y (mean μ)')
ax.set_zlabel('Probability density (Gaussian PDF)')

# Set axis limits
ax.set_xlim(0, 20)
ax.set_ylim(2, 10)
ax.set_zlim(0, np.max(Z))

# Add a title
ax.set_title('3D Filled Polygons Under Gaussian PDF Lines')

# Save the plot
plt.savefig('novice_final.png')