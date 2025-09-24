import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define the axes
x = np.linspace(0, 20, 100)  # 100 points from 0 to 20
y_values = np.array([2, 4, 6, 8, 10])  # y-values for the mean

# Calculate the Gaussian distribution
z_values = []
for y in y_values:
    mean = y
    std_dev = y / 2
    z = (1/(std_dev * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - mean) / std_dev) ** 2)
    z_values.append(z)

# Create the 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Define colors using reversed plasma colormap
colors = plt.cm.plasma(np.linspace(1, 0, len(y_values)))

# Create a mesh grid for surface plotting
X, Y = np.meshgrid(x, y_values)

# Create Z values for the surface (each row corresponds to a y-value's Gaussian)
Z = np.array(z_values)

# Since Z shape must match X and Y for surface plot, transpose if necessary
Z = Z.T  # Adjust dimensions if needed, but here it's already aligned

# Plot each Gaussian as a line at the corresponding y-value depth
for i, (y_val, z_val) in enumerate(zip(y_values, z_values)):
    # Plot the line for the Gaussian distribution at this y-value
    ax.plot(x, np.full_like(x, y_val), z_val, color=colors[i], label=f'y={y_val}')
    # Simulate the "fill" by plotting a surface from z=0 to z_val at this y-value
    y_grid = np.full_like(X, y_val)
    z_grid = np.tile(z_val, (len(y_values), 1))  # Repeat z_val for surface-like effect
    # However, since surface plot needs a proper grid, plot a ribbon-like surface
    for j in range(len(x)-1):
        verts = [
            (x[j], y_val, 0),
            (x[j+1], y_val, 0),
            (x[j+1], y_val, z_val[j+1]),
            (x[j], y_val, z_val[j])
        ]
        ax.add_collection3d(plt.Poly3DCollection([verts], color=colors[i], alpha=0.5))

# Label the axes
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Probability (Z-axis)')
ax.set_title('3D Plot of Gaussian Distributions with Filled Polygons')

# Set axis limits
ax.set_xlim(0, 20)
ax.set_ylim(2, 10)
ax.set_zlim(0, np.max(z_values) * 1.1)  # Slightly above the max z value for better visibility

# Add a legend
ax.legend()

# Save the plot to a PNG file
plt.savefig('novice_final.png')