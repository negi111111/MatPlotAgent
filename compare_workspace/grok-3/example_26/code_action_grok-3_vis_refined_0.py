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

for i, z in enumerate(z_values):
    ax.fill_between(x, z, color=colors[i], alpha=0.5, label=f'y={y_values[i]}')
    ax.plot(x, z, color=colors[i])  # Optional: to show the line on top of the filled area

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