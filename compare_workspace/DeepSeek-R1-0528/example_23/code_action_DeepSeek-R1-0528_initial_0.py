import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # Required for 3D projection

# Generate parameter array t (1000 points between 0 and 1)
t = np.linspace(0, 1, 1000)

# Compute alpha and w using linear transformations
alpha = -6 * np.pi + t * 12 * np.pi  # Range: [-6π, 6π]
w = -3 + t * 6                       # Range: [-3, 3]

# Calculate p = w^3 + 2
p = w**3 + 2

# Compute coordinates a and b
a = p * np.sin(alpha)
b = p * np.cos(alpha)

# Create 3D plot
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Plot curve with custom styling
ax.plot(a, b, w, 
        color='royalblue',   # High-contrast color
        linewidth=1.5, 
        label='parametric curve')

# Add labels and legend
ax.set_xlabel('a', fontsize=12)
ax.set_ylabel('b', fontsize=12)
ax.set_zlabel('w', fontsize=12)
ax.legend(fontsize=10)

# Set viewing angle for better visualization
ax.view_init(elev=25, azim=-60)

# Save as PNG without displaying
plt.savefig("novice.png", dpi=150, bbox_inches='tight')