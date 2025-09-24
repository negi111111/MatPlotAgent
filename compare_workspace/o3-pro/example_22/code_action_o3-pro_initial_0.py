import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D   # registers the 3-D projection inside Matplotlib

# ------------------------------------------------------------------
# 1. Reproducibility
# ------------------------------------------------------------------
np.random.seed(1234567)

# ------------------------------------------------------------------
# 2. Generate data
# ------------------------------------------------------------------
n_points = 200
low, high = -5, 5
x_vals = np.random.uniform(low, high, n_points)
y_vals = np.random.uniform(low, high, n_points)

# ------------------------------------------------------------------
# 3. Two-dimensional histogram
# ------------------------------------------------------------------
n_bins = 10
hist, x_edges, y_edges = np.histogram2d(
    x_vals, y_vals,
    bins=n_bins,
    range=[[low, high], [low, high]]
)

# ------------------------------------------------------------------
# 4. Prepare inputs for bar3d
# ------------------------------------------------------------------
# Lower-left corners of the bars
xpos, ypos = np.meshgrid(x_edges[:-1], y_edges[:-1], indexing='ij')
xpos, ypos = xpos.ravel(), ypos.ravel()

# All bars start at z == 0
zpos = np.zeros_like(xpos)

# Bar “footprint” (uniform because bins are equal size)
dx = np.full_like(xpos, x_edges[1] - x_edges[0])
dy = np.full_like(ypos, y_edges[1] - y_edges[0])

# Heights of the bars
dz = hist.ravel()

# ------------------------------------------------------------------
# 5. Plotting
# ------------------------------------------------------------------
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')

# Colour map scaled to bar heights
max_count = dz.max() if dz.max() > 0 else 1
colors = plt.cm.viridis(dz / max_count)

ax.bar3d(xpos, ypos, zpos, dx, dy, dz,
         color=colors,
         shade=True,
         zsort='average')

# Labelling and limits
ax.set_xlabel('X values')
ax.set_ylabel('Y values')
ax.set_zlabel('Counts per bin')
ax.set_title('3-D Bar Plot of 2-D Histogram (200 uniform points)')
ax.set_xlim(low, high)
ax.set_ylim(low, high)

plt.tight_layout()

# ------------------------------------------------------------------
# 6. Save the figure
# ------------------------------------------------------------------
plt.savefig("novice.png")