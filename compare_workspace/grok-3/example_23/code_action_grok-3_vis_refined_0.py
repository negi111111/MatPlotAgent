import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define the parameters
alpha = np.linspace(-6 * np.pi, 6 * np.pi, 100)  # Range for alpha
w = np.linspace(-3, 3, 100)                       # Range for w
p = w**3 + 2                                      # p as the cube of w plus 2

# Calculate 'a' and 'b'
a = p * np.sin(alpha[:, np.newaxis])  # Broadcasting to match dimensions
b = p * np.cos(alpha[:, np.newaxis])  # Broadcasting to match dimensions

# Create the 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(a.flatten(), b.flatten(), np.tile(w, len(alpha)), label='Parametric Curve', color='b')

# Label the axes
ax.set_xlabel('A (p * sin(alpha))')
ax.set_ylabel('B (p * cos(alpha))')
ax.set_zlabel('W')
ax.set_title('3D Parametric Curve')

# Add a legend
ax.legend()

# Save the plot to a PNG file
plt.savefig('novice_final.png')

# Do not show the plot or open interactive windows