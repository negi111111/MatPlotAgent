import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import matplotlib.cm as cm

# Prepare data
x = np.linspace(0, 20, 100)
y_values = np.arange(2, 11, 2)  # y = 2, 4, 6, 8, 10
z_data = []
for y in y_values:
    mean = y
    std = y / 2
    z = (1 / (std * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - mean) / std) ** 2)
    z_data.append(z)
z_data = np.array(z_data)

# Set up 3D plot
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')
ax.set_xlim(0, 20)
ax.set_ylim(2, 10)
ax.set_zlim(0, np.max(z_data) * 1.1)

# Plot lines and fill polygons with reversed plasma colormap
colormap = cm.plasma.reversed()
colors = colormap(np.linspace(0, 1, len(y_values)))
for i, y_val in enumerate(y_values):
    # Plot the line graph
    ax.plot(x, np.full_like(x, y_val), z_data[i], color=colors[i], label=f'y={y_val}')
    # Fill under the curve using Poly3DCollection
    verts = [(x[j], y_val, 0) for j in range(len(x))] + [(x[j], y_val, z_data[i][j]) for j in range(len(x)-1, -1, -1)]
    poly = ax.add_collection3d(Poly3DCollection([verts], color=colors[i], alpha=0.5))

# Add labels and title
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Probability (Z-axis)')
ax.set_title('3D Plot of Gaussian Distributions with Filled Polygons')

# Add legend
ax.legend()

# Save the plot as a PNG file
plt.savefig("novice.png")