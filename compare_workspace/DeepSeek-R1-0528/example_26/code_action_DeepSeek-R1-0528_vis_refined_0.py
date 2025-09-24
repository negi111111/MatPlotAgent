import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define axes and parameters
x = np.linspace(0, 20, 100)  # X-axis values
y_values = np.arange(2, 11)   # Y-axis values (means)
z = np.zeros((len(y_values), len(x)))  # Z-axis storage

# Calculate Gaussian distributions
for i, mean in enumerate(y_values):
    std_dev = mean / 2
    z[i] = (1 / (std_dev * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - mean) / std_dev)**2)

# Create 3D plot
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

# Generate polygons with color gradient
for i in range(len(y_values)):
    # Create polygon vertices
    verts = [(x[0], y_values[i], 0)] + \
            [(x[j], y_values[i], z[i, j]) for j in range(len(x))] + \
            [(x[-1], y_values[i], 0)]
    
    # Convert to polygon format and add to plot
    poly = plt.Polygon([(v[0], v[2]) for v in verts], closed=True, alpha=0.5,
                      color=plt.cm.plasma(1 - i/len(y_values)))
    ax.add_patch(poly)
    
    # Position polygon in 3D space
    art3d.pathpatch_2d_to_3d(poly, z=y_values[i], zdir='y')

# Configure plot appearance
ax.set_xlabel('X-axis', fontsize=12)
ax.set_ylabel('Y-axis (Mean)', fontsize=12)
ax.set_zlabel('Probability Density', fontsize=12)
ax.set_xlim(0, 20)
ax.set_ylim(2, 10)
ax.set_zlim(0, 0.5)
ax.set_title('3D Gaussian Distribution with Polygons', fontsize=14)
ax.view_init(elev=25, azim=-45)  # Set viewing angle

# Save output without displaying
plt.tight_layout()
plt.savefig('novice_final.png')