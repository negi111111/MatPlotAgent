import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Set random state for reproducibility
np.random.seed(42)

# Prepare data
x = np.arange(30)  # X values from 0 to 29
y_layers = [0, 1, 2, 3]  # Y layers for 4 sets of data
z_data = [np.random.rand(30) * 10 for _ in range(4)]  # Random heights for bars

# Create a 3D subplot
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Define colors for each layer
colors = ['purple', 'orange', 'grey', 'pink']

# Plot bars for each y layer
for i, y_val in enumerate(y_layers):
    bar_colors = [colors[i]] * 29 + ['black']  # Last bar is black
    ax.bar3d(x, [y_val] * len(x), np.zeros_like(x),  # x, y, z (bottom)
             1, 1, z_data[i],                        # dx, dy, dz (width, depth, height)
             color=bar_colors, alpha=0.8)            # color and opacity

# Set labels for axes
ax.set_xlabel('X Axis')
ax.set_ylabel('Y Axis (Layer)')
ax.set_zlabel('Z Axis (Height)')

# Set y-axis ticks to only show discrete layers
ax.set_yticks(y_layers)

# Save the plot as a PNG file
plt.savefig("novice.png")