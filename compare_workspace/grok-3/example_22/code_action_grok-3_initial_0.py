import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Set the random seed to 1234567 for reproducibility
np.random.seed(1234567)

# Generate two sets of 200 random values between -5 and 5
x = np.random.uniform(low=-5, high=5, size=200)
y = np.random.uniform(low=-5, high=5, size=200)

# Create a 2D histogram with 10 bins in each dimension over the range -5 to 5
hist, xedges, yedges = np.histogram2d(x, y, bins=10, range=[[-5, 5], [-5, 5]])

# Prepare data for 3D bar plot
xpos, ypos = np.meshgrid(xedges[:-1] + 0.25, yedges[:-1] + 0.25)
xpos = xpos.flatten()
ypos = ypos.flatten()
zpos = np.zeros_like(xpos)  # Starting height of bars (at z=0)
dx = dy = 0.5  # Width of bars in x and y directions
dz = hist.flatten()  # Heights of bars (histogram values)

# Create a 3D plot
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Plot the 3D bars with a clear, high-contrast color
ax.bar3d(xpos, ypos, zpos, dx, dy, dz, color='#1f77b4', alpha=0.6)

# Set labels for axes
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Frequency')

# Set title
ax.set_title('3D Bar Plot of 2D Histogram')

# Save the plot as a PNG file
plt.savefig("novice.png", dpi=300, bbox_inches='tight')
plt.close()