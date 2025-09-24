import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Step 1: Initialize random number generation with fixed seed for reproducibility
np.random.seed(1234567)

# Step 2: Generate random values
x = np.random.uniform(-5, 5, 200)
y = np.random.uniform(-5, 5, 200)

# Step 3: Create a 2D histogram
hist, xedges, yedges = np.histogram2d(x, y, bins=10, range=[[-5, 5], [-5, 5]])

# Step 4: Construct a 3D bar plot
xpos, ypos = np.meshgrid(xedges[:-1], yedges[:-1], indexing="ij")
xpos = xpos.ravel()
ypos = ypos.ravel()
zpos = 0

dx = dy = 0.5 * np.ones_like(zpos)
dz = hist.ravel()

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Use a colormap for better visualization of bar heights
colors = plt.cm.viridis(dz / dz.max())
ax.bar3d(xpos, ypos, zpos, dx, dy, dz, zsort='average', color=colors, alpha=0.7)

# Step 5: Add labels and title with improved styling
ax.set_xlabel('X', fontsize=12, labelpad=10)
ax.set_ylabel('Y', fontsize=12, labelpad=10)
ax.set_zlabel('Counts', fontsize=12, labelpad=10)
ax.set_title('3D Bar Plot of 2D Histogram', fontsize=14, pad=20)

# Additional Improvements
# Adjust ticks for better readability
ax.set_xticks(np.arange(-5, 6, 1))
ax.set_yticks(np.arange(-5, 6, 1))
ax.set_zticks(np.arange(0, dz.max() + 1, 5))

# Add grid for better depth perception
ax.grid(True, linestyle='--', alpha=0.5)

# Adjust view angle for better visualization
ax.view_init(elev=30, azim=45)

# Step 6: Save the plot to PNG file
plt.savefig('novice_final.png', bbox_inches='tight', dpi=300)