import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 (ensures 3D projection is registered)

# Step 1: Initialize random number generation
np.random.seed(1234567)

# Step 2: Generate random values
data1 = np.random.uniform(-5, 5, 200)
data2 = np.random.uniform(-5, 5, 200)

# Step 3: Create a 2D histogram
hist, xedges, yedges = np.histogram2d(data1, data2, bins=10, range=[[-5, 5], [-5, 5]])

# Step 4: Construct a 3D bar plot
xpos, ypos = np.meshgrid(xedges[:-1], yedges[:-1], indexing="ij")
xpos = xpos.ravel()
ypos = ypos.ravel()
zpos = np.zeros_like(xpos, dtype=float)

# Bin widths (uniform because of fixed range and bins)
xwidth = np.diff(xedges)[0]
ywidth = np.diff(yedges)[0]
dx = np.full_like(xpos, xwidth, dtype=float)
dy = np.full_like(ypos, ywidth, dtype=float)
dz = hist.ravel()

fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')

# Color bars by count using a Matplotlib colormap
norm = plt.Normalize(dz.min(), dz.max())
colors = plt.cm.viridis(norm(dz))

ax.bar3d(xpos, ypos, zpos, dx, dy, dz, color=colors, edgecolor='k', shade=True, zsort='average')

# Step 5: Enhance plot aesthetics
ax.set_xlabel('X values')
ax.set_ylabel('Y values')
ax.set_zlabel('Counts')
ax.set_title('3D Histogram of Random Values')

# Optional: set viewing angle for clarity and limit axes to the histogram range
ax.view_init(elev=25, azim=35)
ax.set_xlim(xedges[0], xedges[-1])
ax.set_ylim(yedges[0], yedges[-1])

# Step 6: Save the plot
plt.savefig('novice_final.png')