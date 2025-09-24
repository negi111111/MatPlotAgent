import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define the function g(s)
def g(s):
    return np.sin(3 * np.pi * s) * np.exp(-s)

# Generate data for 2D plot
s = np.linspace(0, 10, 200)
g_s = g(s)
g_s_shift1 = g(s + 0.1)
g_s_shift2 = g(s + 0.2)

# Create figure with subplots
fig = plt.figure(figsize=(10, 8))
fig.suptitle('A Story of 2 Subplots', fontsize=16)

# First subplot: 2D lines
ax1 = fig.add_subplot(2, 1, 1)
ax1.plot(s, g_s, 'b-', linewidth=2, label='g(s)')
ax1.plot(s, g_s_shift1, 'r--', linewidth=2, label='g(s + 0.1)')
ax1.plot(s, g_s_shift2, 'g:', linewidth=2, label='g(s + 0.2)')
ax1.set_xlabel('s', fontsize=12)
ax1.set_ylabel('g(s)', fontsize=12)
ax1.set_title('Shifted Decaying Sine Waves', fontsize=14)
ax1.legend(loc='upper right')
ax1.grid(True, alpha=0.7)

# Second subplot: 3D surface
ax2 = fig.add_subplot(2, 1, 2, projection='3d')

# Generate grid data
P = np.linspace(-5, 5, 50)
Q = np.linspace(-5, 5, 50)
P_grid, Q_grid = np.meshgrid(P, Q)
R = np.sqrt(P_grid**2 + Q_grid**2)
E = np.cos(R)

# Plot surface with viridis colormap
surf = ax2.plot_surface(
    P_grid, Q_grid, E,
    cmap='viridis',
    edgecolor='none',
    rstride=1,
    cstride=1,
    alpha=0.9
)
ax2.set_xlabel('P', fontsize=12, labelpad=10)
ax2.set_ylabel('Q', fontsize=12, labelpad=10)
ax2.set_zlabel('E(P, Q)', fontsize=12, labelpad=10)
ax2.set_title('Cosine of Radial Distance Surface', fontsize=14)

# Add colorbar
cbar = fig.colorbar(surf, ax=ax2, shrink=0.6, aspect=10)
cbar.set_label('Magnitude', rotation=270, labelpad=15)

# Adjust layout and save
plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.savefig("novice.png")