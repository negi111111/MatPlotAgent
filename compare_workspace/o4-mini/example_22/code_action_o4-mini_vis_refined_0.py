import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# 1. Initialize random number generation for reproducibility
np.random.seed(1234567)

# 2. Generate two sets of 200 random values in the range [-5, 5]
x = np.random.uniform(-5, 5, 200)
y = np.random.uniform(-5, 5, 200)

# 3. Compute a 2D histogram with 10 bins in each dimension
hist, xedges, yedges = np.histogram2d(
    x, y,
    bins=10,
    range=[[-5, 5], [-5, 5]]
)

# 4. Set up the 3D bar plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Compute the positions and sizes of the bars
# Center the bars in each bin
x_centers = (xedges[:-1] + xedges[1:]) / 2
y_centers = (yedges[:-1] + yedges[1:]) / 2
xpos, ypos = np.meshgrid(x_centers, y_centers, indexing='ij')
xpos = xpos.ravel()
ypos = ypos.ravel()
zpos = np.zeros_like(xpos)

# All bars have the same footprint (width & depth)
dx = dy = 0.5 * np.ones_like(zpos)

# Heights from the histogram counts
dz = hist.ravel()

# Plot the bars
ax.bar3d(
    xpos, ypos, zpos,
    dx, dy, dz,
    zsort='average',
    color='skyblue',
    edgecolor='gray'
)

# 5. Label axes
ax.set_xlabel('X value')
ax.set_ylabel('Y value')
ax.set_zlabel('Count')

# 6. Add a title
ax.set_title('3D Histogram of Random Values')

# Adjust viewing angle for better perspective
ax.view_init(elev=30, azim=45)

# 7. Save the figure
plt.savefig('novice_final.png')