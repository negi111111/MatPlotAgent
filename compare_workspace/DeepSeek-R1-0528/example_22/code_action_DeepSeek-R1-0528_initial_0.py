import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Initialize random seed for reproducibility
np.random.seed(1234567)

# Generate random data
x = np.random.uniform(low=-5, high=5, size=200)
y = np.random.uniform(low=-5, high=5, size=200)

# Compute 2D histogram
hist, x_edges, y_edges = np.histogram2d(
    x, y, 
    bins=10, 
    range=[[-5, 5], [-5, 5]]
)

# Prepare data for 3D bar plot
x_centers = (x_edges[:-1] + x_edges[1:]) / 2
y_centers = (y_edges[:-1] + y_edges[1:]) / 2
X, Y = np.meshgrid(x_centers, y_centers, indexing='ij')
x_pos = X.flatten()
y_pos = Y.flatten()
z_pos = np.zeros_like(x_pos)
dx = (x_edges[1] - x_edges[0]) * np.ones_like(x_pos)
dy = (y_edges[1] - y_edges[0]) * np.ones_like(y_pos)
dz = hist.flatten()

# Create 3D plot
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

# Plot 3D bars with custom styling
ax.bar3d(
    x_pos, y_pos, z_pos,
    dx, dy, dz,
    color='#1f77b4',  # Matplotlib default blue
    edgecolor='black',
    linewidth=0.5,
    alpha=0.8
)

# Add labels and title
ax.set_xlabel('X values', fontsize=12)
ax.set_ylabel('Y values', fontsize=12)
ax.set_zlabel('Frequency', fontsize=12)
ax.set_title('3D Histogram of Random Data', fontsize=14, pad=20)

# Adjust viewing angle for better visibility
ax.view_init(elev=30, azim=-45)

# Save as PNG file
plt.savefig("novice.png", dpi=100, bbox_inches='tight')