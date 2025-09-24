import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # registers the 3D projection
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import matplotlib.cm as cm

# Prepare the x-axis data
x = np.linspace(0, 20, 100)

# Define the set of y-values to use as means for the Gaussians
y_means = np.linspace(2, 10, 9)

# Create the 3D figure and axes
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

# Choose a reversed plasma colormap and prepare a color for each polygon
cmap = cm.get_cmap('plasma_r', len(y_means))

# Loop over each y-mean, compute the Gaussian PDF along x, build the polygon, and add it
for i, y in enumerate(y_means):
    mu = y
    sigma = y / 2.0
    # Gaussian PDF
    z = (1.0 / (sigma * np.sqrt(2 * np.pi))) * np.exp(-((x - mu) ** 2) / (2 * sigma ** 2))
    
    # Build vertices for the filled polygon
    verts = [(xi, y, zi) for xi, zi in zip(x, z)]
    verts += [(xi, y, 0) for xi in x[::-1]]
    
    # Create and style the polygon
    poly = Poly3DCollection([verts],
                            facecolors=cmap(i),
                            edgecolors='k',
                            alpha=0.7)
    ax.add_collection3d(poly)

# Label axes and set axis limits
ax.set_xlim(0, 20)
ax.set_ylim(2, 10)
ax.set_zlim(0, 0.5)
ax.set_xlabel('X')
ax.set_ylabel('Mean (Y)')
ax.set_zlabel('Probability Density (Z)')

# Adjust the viewing angle for clarity
ax.view_init(elev=30, azim=-60)

plt.tight_layout()
plt.savefig("novice.png")