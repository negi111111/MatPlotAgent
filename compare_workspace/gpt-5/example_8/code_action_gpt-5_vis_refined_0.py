import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
import matplotlib.colors as mcolors

# Set a fixed random state
np.random.seed(42)

# Generate random data
num_points = 200
r = np.random.rand(num_points)  # Random radial distances
theta = np.random.rand(num_points) * 2 * np.pi  # Random angles in radians

# Calculate sizes proportional to r^2
sizes = (r ** 2) * 1000  # Scale for visibility

# Normalize theta for HSV colormap and colorbar
norm = mcolors.Normalize(vmin=0, vmax=2 * np.pi)

# Create polar plot
fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})

# Plot the data with colors determined by angle in HSV
scatter = ax.scatter(theta, r, s=sizes, c=theta, cmap='hsv', norm=norm, alpha=0.75)

# Add colorbar representing angle in radians
cbar = plt.colorbar(cm.ScalarMappable(norm=norm, cmap='hsv'), ax=ax)
cbar.set_label('Angle (radians)')
cbar.set_ticks([0, np.pi / 2, np.pi, 3 * np.pi / 2, 2 * np.pi])
cbar.set_ticklabels(['0', 'π/2', 'π', '3π/2', '2π'])

# Set title
ax.set_title('Polar Scatter: Positions Random, Size ∝ r², Color by Angle (HSV)', va='bottom')

# Save the plot
plt.savefig("novice_final.png", bbox_inches='tight')