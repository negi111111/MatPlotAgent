import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define the parameters
alpha = np.linspace(-6 * np.pi, 6 * np.pi, 1000)
w = np.linspace(-3, 3, 1000)
p = w**3 + 2

# Calculate 'a' and 'b'
a = p * np.sin(alpha)
b = p * np.cos(alpha)

# Create the 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the parametric curve
ax.plot(a, b, w, label='parametric curve', color='blue')

# Label the axes
ax.set_xlabel('a = p * sin(alpha)')
ax.set_ylabel('b = p * cos(alpha)')
ax.set_zlabel('w')

# Add a legend
ax.legend()

# Enhance visualization
ax.grid(True)
ax.view_init(elev=20, azim=30)

# Save the plot
plt.savefig("novice_final.png")