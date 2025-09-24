import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # registers the 3D projection

# 1) Seed RNG for reproducibility
np.random.seed(1234567)

# 2) Generate two sets of 200 uniform random numbers in [-5, 5]
n_samples = 200
x = np.random.uniform(-5, 5, size=n_samples)
y = np.random.uniform(-5, 5, size=n_samples)

# 3) Compute the 2D histogram with 10×10 bins over [-5, 5]×[-5, 5]
n_bins = 10
range_xy = [[-5, 5], [-5, 5]]
H, x_edges, y_edges = np.histogram2d(x, y,
                                     bins=n_bins,
                                     range=range_xy)

# 4) Compute bin centers so bars are centered
x_centers = (x_edges[:-1] + x_edges[1:]) / 2
y_centers = (y_edges[:-1] + y_edges[1:]) / 2

# 5) Create a meshgrid of bin centers and flatten to 1D
xpos, ypos = np.meshgrid(x_centers, y_centers, indexing="ij")
xpos = xpos.ravel()
ypos = ypos.ravel()

# 6) Prepare bar heights and dimensions
zpos = np.zeros_like(xpos)                               # all bars start at z=0
dx = (x_edges[1] - x_edges[0]) * np.ones_like(zpos)     # constant bin width in x
dy = (y_edges[1] - y_edges[0]) * np.ones_like(zpos)     # constant bin width in y
dz = H.ravel()                                          # bar heights = counts

# 7) Create the 3D bar plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.bar3d(xpos, ypos, zpos,
         dx, dy, dz,
         shade=True)

# 8) Label axes
ax.set_xlabel('X value')
ax.set_ylabel('Y value')
ax.set_zlabel('Count')

# 9) Save the figure to a PNG file
plt.savefig("novice.png")