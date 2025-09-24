import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define the parameter array
t = np.linspace(0, 4 * np.pi + 0.1, 100)

# Define the parametric curve
x = np.cos(t)
y = np.sin(2 * t)
z = np.cos(4 * t)

# Define error bars
error = 0.3
indices = np.where((np.arange(len(t)) % 20 == 0) & ((np.arange(len(t)) // 20) % 3 == 0) | ((np.arange(len(t)) // 20) % 3 == 2))[0]

# Create the 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(x, y, z, label='Parametric Curve', color='blue')

# Add error bars
ax.errorbar(x[indices], y[indices], z[indices], xerr=error, yerr=error, zerr=error, fmt='o', label='Error Bars', color='red')

# Label the axes
ax.set_xlabel('X label')
ax.set_ylabel('Y label')
ax.set_zlabel('Z label')

# Add a legend
ax.legend()

# Save the plot
plt.savefig('novice_final.png')

# Close the figure to prevent display
plt.close()