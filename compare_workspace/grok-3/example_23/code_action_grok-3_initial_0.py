import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define the ranges for alpha and w
alpha = np.linspace(-6 * np.pi, 6 * np.pi, 100)  # 100 points for smooth curve
w = np.linspace(-3, 3, 100)  # 100 points for smooth curve

# Create a mesh grid for alpha and w to compute the curve points
Alpha, W = np.meshgrid(alpha, w)

# Compute p as w cubed plus 2
P = W**3 + 2

# Compute a and b based on p and alpha
A = P * np.sin(Alpha)
B = P * np.cos(Alpha)

# Create a new figure
fig = plt.figure(figsize=(10, 8))

# Add a 3D subplot
ax = fig.add_subplot(111, projection='3d')

# Plot the surface using A, B, and W with a high-contrast colormap
surface = ax.plot_surface(A, B, W, cmap='viridis')

# Add a color bar for better visualization
fig.colorbar(surface, ax=ax, shrink=0.5, aspect=5)

# Set labels for the axes
ax.set_xlabel('A (p * sin(alpha))')
ax.set_ylabel('B (p * cos(alpha))')
ax.set_zlabel('W')

# Set the title of the plot
ax.set_title('3D Parametric Curve')

# Save the plot as a PNG file
plt.savefig("novice.png")
plt.close()