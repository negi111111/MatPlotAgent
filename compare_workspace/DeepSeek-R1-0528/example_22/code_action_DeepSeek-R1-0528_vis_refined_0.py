import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Set random seed for reproducibility
np.random.seed(1234567)

# Generate random data
x = np.random.uniform(-5, 5, 200)
y = np.random.uniform(-5, 5, 200)

# Create 2D histogram
hist, xedges, yedges = np.histogram2d(x, y, bins=10, range=[[-5, 5], [-5, 5]])

# Prepare grid coordinates
xpos, ypos = np.meshgrid(xedges[:-1] + 0.5, yedges[:-1] + 0.5, indexing="ij")
xpos = xpos.ravel()
ypos = ypos.ravel()
zpos = np.zeros_like(xpos)

# Bar dimensions (full bin width)
dx = dy = np.ones_like(zpos)
dz = hist.ravel()

# Create figure and 3D axis
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Custom Matplotlib styling (replicating modern theme)
plt.style.use('default')
plt.rcParams['axes.facecolor'] = 'white'
plt.rcParams['grid.color'] = '#e0e0e0'
plt.rcParams['axes.grid'] = True
plt.rcParams['font.family'] = 'sans-serif'

# Create colored bars (using viridis colormap)
if np.max(dz) > 0:
    colors = plt.cm.viridis(dz / np.max(dz))
else:
    colors = 'cornflowerblue'

# Plot 3D bars
ax.bar3d(xpos, ypos, zpos, dx, dy, dz, color=colors, 
         edgecolor='black', linewidth=0.2, alpha=0.8, shade=True)

# Axis labels and title
ax.set_xlabel('X values', fontsize=12, labelpad=12)
ax.set_ylabel('Y values', fontsize=12, labelpad=12)
ax.set_zlabel('Counts', fontsize=12, labelpad=12)
ax.set_title('3D Histogram of Random Data', fontsize=14, pad=20)

# Axis limits and grid
ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)
ax.grid(True, linestyle='--', alpha=0.7)

# Adjust view angle for better visibility
ax.view_init(elev=30, azim=-45)

# Save as PNG
plt.tight_layout()
plt.savefig('novice_final.png')