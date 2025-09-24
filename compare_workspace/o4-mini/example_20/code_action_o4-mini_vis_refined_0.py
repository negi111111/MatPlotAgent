import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Step 1: Set a fixed random state
np.random.seed(42)

# Step 2: Generate data
x = np.arange(30)  # x values from 0 to 29
y_values = [np.random.rand(30) for _ in range(4)]  # 4 layers of random y values

# Step 3: Create a 3D subplot
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111, projection='3d')

# Step 4: Define colors
colors = ['purple', 'orange', 'grey', 'pink']
for layer_index, layer_data in enumerate(y_values):
    # Plot the bars for this layer
    ax.bar(x, layer_data, zs=layer_index, zdir='y',
           color=colors[layer_index], alpha=0.8, width=0.8)
    # Color the last bar black with full opacity
    ax.bar(x[-1], layer_data[-1], zs=layer_index, zdir='y',
           color='black', alpha=1.0, width=0.8)

# Step 6: Label axes
ax.set_xlabel('X', fontsize=12)
ax.set_ylabel('Layer (k)', fontsize=12)
ax.set_zlabel('Value', fontsize=12)

# Set y-ticks to only show the discrete layer indices
ax.set_yticks(range(len(y_values)))

# Improve viewing angle and add a title
ax.view_init(elev=25, azim=-60)
ax.set_title('3D Bar Plot of Random Values Across Layers', fontsize=14)

# Step 7: Save the plot
plt.savefig('novice_final.png')