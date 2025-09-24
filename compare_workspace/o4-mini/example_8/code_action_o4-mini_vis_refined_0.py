import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors as mcolors

# 1. Set a fixed random state for reproducibility
np.random.seed(42)

# 2. Generate random data
num_points = 200
r = np.random.rand(num_points)                     # radial distances in [0,1)
theta = np.random.rand(num_points) * 2 * np.pi     # angles in [0, 2π)

# 3. Compute sizes and colors
sizes = (r ** 2) * 1000  # point size ∝ r², scaled for visibility
hsv = np.column_stack((theta / (2 * np.pi),       # hue ∈ [0,1)
                       np.ones(num_points),       # saturation = 1
                       np.ones(num_points)))      # value = 1
colors = mcolors.hsv_to_rgb(hsv)                   # convert HSV to RGB

# 4. Create polar scatter plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='polar')
ax.scatter(theta, r, s=sizes, c=colors, alpha=0.75)

# 5. Add title
ax.set_title("200 Random Polar Scatter (size ∝ r², color by angle)", va='bottom')

# 6. Save the figure as a PNG file
plt.savefig("novice_final.png")