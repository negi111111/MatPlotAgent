import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors as mcolors

# Set a fixed random state for reproducibility
np.random.seed(42)

# Generate random data
num_points = 200
r = np.random.rand(num_points)  # Random radial distances
theta = np.random.rand(num_points) * 2 * np.pi  # Random angles

# Calculate area of each point
area = (r ** 2) * 1000  # Scale the area for better visibility

# Determine colors in HSV color space
colors = plt.cm.hsv((theta + np.pi) / (2 * np.pi))  # Normalize angle to [0, 1]

# Create the polar scatter plot
fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, projection='polar')
scatter = ax.scatter(theta, r, s=area, c=colors, alpha=0.75, edgecolors='w')

# Add title
ax.set_title("Polar Scatter Plot with Random Points", va='bottom')

# Save the plot
plt.savefig("novice_final.png", bbox_inches='tight')