import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.lines import Line2D

# Generate data
x = np.linspace(0, 4 * np.pi, 100)
y1 = np.sin(x) - (np.pi / 4)
y2 = np.cos(x) - (np.pi / 4)

# Create 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot stems and points
for xi, yi1, yi2 in zip(x, y1, y2):
    # Sine stems and points
    ax.plot([xi, xi], [0, yi1], [0, 0], color='b')
    ax.scatter(xi, yi1, 0, color='b')
    # Cosine stems and points
    ax.plot([xi, xi], [0, yi2], [0, 0], color='r')
    ax.scatter(xi, yi2, 0, color='r')

# Customize labels and title
ax.set_xlabel('X values (0 to 4π)')
ax.set_ylabel('Y values (Sine and Cosine)')
ax.set_zlabel('Z values (0)')
ax.set_title('3D Stem Plot of Sine and Cosine Functions')

# Create custom legend
legend_elements = [
    Line2D([0], [0], color='b', marker='o', linestyle='', label='Sine'),
    Line2D([0], [0], color='r', marker='o', linestyle='', label='Cosine')
]
ax.legend(handles=legend_elements)

# Save the plot
plt.savefig("novice_final.png")