import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Set fixed random state for reproducibility
np.random.seed(42)

# Generate data
x = np.arange(30)  # 30 positions on x-axis
y = np.array([0, 1, 2, 3])  # 4 layers on y-axis
z = np.random.rand(4, 30)  # Random heights for 4 layers × 30 positions

# Define color palette
colors = ['purple', 'orange', 'grey', 'pink']

# Create figure and 3D axis
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Plot each layer
for i, layer in enumerate(y):
    # Create color array: all bars in layer use base color except last one (black)
    bar_colors = [colors[i]] * 30
    bar_colors[-1] = 'black'
    
    # Plot bars for current layer
    ax.bar(x, z[i], zs=layer, zdir='y', color=bar_colors, alpha=0.8)

# Configure axis labels and ticks
ax.set_xlabel('X Axis', labelpad=10)
ax.set_ylabel('Y Axis (k)', labelpad=15)
ax.set_zlabel('Z Axis (Height)', labelpad=10)
ax.set_yticks(y)  # Only show layer positions

# Adjust viewing angle for better visibility
ax.view_init(elev=25, azim=-45)

# Save as PNG without displaying
plt.savefig('novice_final.png', dpi=100, bbox_inches='tight')