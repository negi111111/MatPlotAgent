import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Step 1: Set a fixed random state for reproducibility
np.random.seed(42)

# Step 2: Generate data
x = np.arange(30)  # x values from 0 to 29
y_layers = np.array([0, 1, 2, 3])  # y values for different layers (k values)
y = np.random.rand(len(y_layers), len(x)) * 10  # 4 layers of random heights for bars

# Step 3: Define colors for the bars
colors = ['purple', 'orange', 'grey', 'pink']

# Step 4: Create a 3D bar plot
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Step 5: Plot bars with specified opacity
for i in range(len(y_layers)):
    # Use bar3d for 3D bar plotting; set width and depth for bars
    ax.bar3d(x, np.full_like(x, y_layers[i]), 0, dx=0.5, dy=0.5, dz=y[i], 
             color=colors[i] if i < len(y_layers) - 1 else 'black', alpha=0.8)

# Step 6: Set labels and customize axes
ax.set_xlabel('X Axis', fontsize=12)
ax.set_ylabel('Y Axis (Layer)', fontsize=12)
ax.set_zlabel('Z Axis (Height)', fontsize=12)
ax.set_yticks(y_layers)  # Only label the discrete layer values on y-axis

# Add a title for context and aesthetics
ax.set_title('3D Bar Plot of Random Data', fontsize=14)

# Adjust the viewing angle for better visibility
ax.view_init(elev=30, azim=45)

# Step 7: Save the plot to a PNG file
plt.savefig('novice_final.png', bbox_inches='tight', dpi=300)