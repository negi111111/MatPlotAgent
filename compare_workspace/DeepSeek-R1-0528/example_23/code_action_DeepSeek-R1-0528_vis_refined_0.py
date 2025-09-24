import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define parameter ranges deterministically
alpha = np.linspace(-6 * np.pi, 6 * np.pi, 1000)
w = np.linspace(-3, 3, 1000)
p = w**3 + 2  # p = w^3 + 2

# Calculate coordinates
a = p * np.sin(alpha)
b = p * np.cos(alpha)

# Create 3D plot using Matplotlib primitives
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')
ax.plot(a, b, w, color='royalblue', linewidth=1.5)

# Configure plot aesthetics
ax.set_xlabel('a', fontsize=12, labelpad=10)
ax.set_ylabel('b', fontsize=12, labelpad=10)
ax.set_zlabel('w', fontsize=12, labelpad=10)
ax.set_title('3D Parametric Curve: a = p·sin(α), b = p·cos(α), p = w³+2', 
             fontsize=14, pad=20)

# Set viewing angle for better visualization
ax.view_init(elev=25, azim=-45)

# Configure grid and background
ax.xaxis.pane.fill = False
ax.yaxis.pane.fill = False
ax.zaxis.pane.fill = False
ax.xaxis.pane.set_edgecolor('w')
ax.yaxis.pane.set_edgecolor('w')
ax.zaxis.pane.set_edgecolor('w')
ax.grid(True, linestyle='--', alpha=0.7)

# Save as PNG without displaying
plt.savefig('novice_final.png', dpi=150, bbox_inches='tight')