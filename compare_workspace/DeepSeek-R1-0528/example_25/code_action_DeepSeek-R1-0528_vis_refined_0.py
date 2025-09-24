import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define the function g(s)
def g(s):
    return np.sin(3 * np.pi * s) * np.exp(-s)

# Generate data for 2D plot
s = np.linspace(0, 10, 100)
g_s = g(s)
g_s_plus_0_1 = g(s + 0.1)
g_s_plus_0_2 = g(s + 0.2)

# Create figure with subplots
fig = plt.figure(figsize=(10, 8))
fig.suptitle('A Story of 2 Subplots', fontsize=16)

# First subplot: 2D line plot
ax1 = fig.add_subplot(2, 1, 1)
ax1.plot(s, g_s, label='g(s)', color='blue')
ax1.plot(s, g_s_plus_0_1, label='g(s + 0.1)', linestyle='--', color='red')
ax1.plot(s, g_s_plus_0_2, label='g(s + 0.2)', linestyle=':', color='green')
ax1.set_title('Shifted Decaying Sine Waves')
ax1.set_xlabel('s')
ax1.set_ylabel('g(s)')
ax1.legend()
ax1.grid(True)

# Generate data for 3D surface plot
P = np.linspace(-5, 5, 100)
Q = np.linspace(-5, 5, 100)
P, Q = np.meshgrid(P, Q)
E = np.cos(np.sqrt(P**2 + Q**2))

# Second subplot: 3D surface plot
ax2 = fig.add_subplot(2, 1, 2, projection='3d')
surf = ax2.plot_surface(P, Q, E, cmap='viridis', rstride=1, cstride=1)
ax2.set_title('Cosine of Radial Distance Surface')
ax2.set_xlabel('P')
ax2.set_ylabel('Q')
ax2.set_zlabel('Magnitude')
fig.colorbar(surf, ax=ax2, shrink=0.5, aspect=5)

# Save to PNG without displaying
plt.savefig('novice_final.png', bbox_inches='tight')