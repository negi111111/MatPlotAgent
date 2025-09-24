import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Prepare data for the first subplot (2D plot)
s = np.linspace(0, 2, 100)
g1 = np.sin(3 * np.pi * s) * np.exp(-s)
s_shift1 = s + 0.1
g2 = np.sin(3 * np.pi * s_shift1) * np.exp(-s_shift1)
s_shift2 = s + 0.2
g3 = np.sin(3 * np.pi * s_shift2) * np.exp(-s_shift2)

# Prepare data for the second subplot (3D surface plot)
p = np.linspace(-5, 5, 100)
q = np.linspace(-5, 5, 100)
P, Q = np.meshgrid(p, q)
E = np.cos(np.sqrt(P**2 + Q**2))

# Create the figure and subplots
fig = plt.figure(figsize=(12, 5))
fig.suptitle('A Story of 2 Subplots', fontsize=14)
ax1 = plt.subplot(1, 2, 1)
ax2 = plt.subplot(1, 2, 2, projection='3d')

# Plot data in the first subplot (2D plot)
ax1.plot(s, g1, label='g(s)', color='blue')
ax1.plot(s, g2, label='g(s + 0.1)', color='green')
ax1.plot(s, g3, label='g(s + 0.2)', color='red')
ax1.set_title('2D Plot of g(s)')
ax1.set_xlabel('s')
ax1.set_ylabel('g(s)')
ax1.legend()
ax1.grid(True)

# Plot data in the second subplot (3D surface plot)
surf = ax2.plot_surface(P, Q, E, cmap='viridis')
ax2.set_title('3D Surface Plot of E')
ax2.set_xlabel('P')
ax2.set_ylabel('Q')
ax2.set_zlabel('E')
fig.colorbar(surf, ax=ax2, shrink=0.5, aspect=5)

# Adjust layout to prevent overlap
plt.tight_layout()
fig.subplots_adjust(top=0.85)

# Save the plot as a PNG file
plt.savefig("novice.png")