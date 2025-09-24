import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Set random seed for reproducibility
np.random.seed(42)

# Data setup
x = np.arange(30)  # 30 x-values [0-29]
k_values = [0, 1, 2, 3]  # y=k layers
base_colors = ['purple', 'orange', 'grey', 'pink']  # Layer colors

# Create figure and 3D subplot
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Plot each layer with custom styling
dx, dy = 0.8, 0.8  # Bar dimensions
for idx, k in enumerate(k_values):
    # Generate random heights for bars
    z_heights = np.random.rand(30)
    
    # Position bars centered at integer coordinates
    x_pos = x - dx/2
    y_pos = np.full(30, k - dy/2)
    
    # Assign colors (last bar in each layer is black)
    colors = [base_colors[idx]] * 30
    colors[-1] = 'black'
    
    # Create 3D bars
    ax.bar3d(
        x_pos, y_pos, np.zeros(30),  # Base positions
        dx, dy, z_heights,           # Dimensions
        color=colors, 
        alpha=0.8,                   # 80% opacity
        shade=True                   # 3D shading
    )

# Configure axes
ax.set_xlabel('X Axis', fontsize=12)
ax.set_ylabel('Y Axis (k)', fontsize=12)
ax.set_zlabel('Z Axis (Height)', fontsize=12)
ax.set_yticks(k_values)  # Discrete layer indicators

# Finalize and save
plt.tight_layout()
plt.savefig("novice.png")