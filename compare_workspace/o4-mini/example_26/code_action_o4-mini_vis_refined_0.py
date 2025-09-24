import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define the axes
x = np.linspace(0, 20, 100)        # 100 points from 0 to 20
y_values = np.arange(2, 11)        # mean values from 2 to 10

# Calculate the Z values for each Gaussian
z_values = []
for mean in y_values:
    std_dev = mean / 2.0
    coeff = 1.0 / (std_dev * np.sqrt(2 * np.pi))
    exponent = -0.5 * ((x - mean) / std_dev) ** 2
    z = coeff * np.exp(exponent)
    z_values.append(z)
z_values = np.array(z_values)

# Create the 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot filled polygons under each Gaussian curve
# We use a reversed plasma colormap for the fills
n = len(y_values)
for i, y in enumerate(y_values):
    color = plt.cm.plasma(1.0 - i / float(n - 1))
    ax.fill_between(
        x,
        z_values[i],
        0,               # fill down to z=0
        zs=y,            # at this y-plane
        zdir='y',        # the axis to treat as depth
        color=color,
        alpha=0.5
    )

# Set axis limits
ax.set_xlim(0, 20)
ax.set_ylim(2, 10)
ax.set_zlim(0, np.max(z_values))

# Label the axes
ax.set_xlabel('X')
ax.set_ylabel('Mean (Y)')
ax.set_zlabel('Probability Density (Z)')

# Save the figure
plt.savefig('novice_final.png')