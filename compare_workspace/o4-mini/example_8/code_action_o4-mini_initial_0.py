import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import hsv_to_rgb

# 1. Fix random seed for reproducibility
rng = np.random.RandomState(42)

# 2. Number of points
N = 200

# 3. Generate random polar coordinates
r = rng.rand(N)
theta = rng.rand(N) * 2 * np.pi

# 4. Compute marker sizes (area ∝ r^2)
sizes = 100 * r**2

# 5. Build HSV colors from angle
h = theta / (2 * np.pi)
s = np.ones(N)
v = np.ones(N)
hsv = np.column_stack((h, s, v))   # shape (N, 3)

# 6. Convert HSV to RGB
colors = hsv_to_rgb(hsv)

# 7. Create polar scatter plot
fig = plt.figure(figsize=(6, 6))
ax = fig.add_subplot(1, 1, 1, projection='polar')
ax.scatter(
    theta,    # angles
    r,        # radii
    c=colors, # RGB colors
    s=sizes,  # marker areas
    alpha=0.8
)

# 8. Optional styling
ax.set_title("200 Random Polar Scatter (size ∝ r², color by angle)", va='bottom')

# 9. Save the plot to a PNG file
plt.savefig("novice.png")