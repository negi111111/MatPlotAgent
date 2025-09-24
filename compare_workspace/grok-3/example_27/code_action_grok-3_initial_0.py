import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Generate the data
x = np.linspace(0, 4 * np.pi, 50)  # 50 points between 0 and 4π
y_sin = np.sin(x - np.pi / 4)  # Sine with phase shift
y_cos = np.cos(x - np.pi / 4)  # Cosine with phase shift

# Set up the 3D plot
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Create the 3D stem plot
for i in range(len(x)):
    # Stems from z=0 to the data point
    ax.plot([x[i], x[i]], [y_sin[i], y_sin[i]], [0, y_cos[i]], 'b-', alpha=0.6, linewidth=1.5)  # Blue stems
    # Base lines on the xy-plane for clarity
    ax.plot([x[i], x[i]], [0, y_sin[i]], [0, 0], 'r-', alpha=0.4, linewidth=1)  # Red base lines

# Plot the data points as markers
ax.scatter(x, y_sin, y_cos, color='navy', s=60, label='Data Points', edgecolor='black')  # Navy markers with black edge

# Customize the plot
ax.set_xlabel('X (0 to 4π)', fontsize=12, labelpad=10)
ax.set_ylabel('Y (sin(x - π/4))', fontsize=12, labelpad=10)
ax.set_zlabel('Z (cos(x - π/4))', fontsize=12, labelpad=10)
ax.set_title('3D Stem Plot of Sine and Cosine Data', fontsize=14, pad=15)
ax.legend(fontsize=10)

# Save the plot as a PNG file
plt.savefig("novice.png", dpi=300, bbox_inches='tight')
plt.close()