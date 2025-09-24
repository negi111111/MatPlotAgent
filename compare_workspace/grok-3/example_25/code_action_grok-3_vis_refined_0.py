import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define the function g(s)
def g(s):
    return np.sin(3 * np.pi * s) * np.exp(-s)

# Generate data for g(s)
s = np.linspace(0, 2, 100)
g_s = g(s)
g_s_plus_0_1 = g(s + 0.1)
g_s_plus_0_2 = g(s + 0.2)

# Create the figure and subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

# 2D plot of g(s)
ax1.plot(s, g_s, label='g(s)', color='blue')
ax1.plot(s, g_s_plus_0_1, label='g(s + 0.1)', color='green')
ax1.plot(s, g_s_plus_0_2, label='g(s + 0.2)', color='red')
ax1.set_title('2D Plot of g(s)')
ax1.set_xlabel('s')
ax1.set_ylabel('g(s)')
ax1.legend()
ax1.grid(True)

# Define arrays P and Q for 3D plot
P = np.linspace(-5, 5, 100)
Q = np.linspace(-5, 5, 100)
P, Q = np.meshgrid(P, Q)

# Define the function E
E = np.cos(np.sqrt(P**2 + Q**2))

# 3D surface plot of E
ax2 = fig.add_subplot(122, projection='3d')
surf = ax2.plot_surface(P, Q, E, cmap='viridis')
fig.colorbar(surf, ax=ax2, shrink=0.5, aspect=5)
ax2.set_title('3D Surface Plot of E')
ax2.set_xlabel('P')
ax2.set_ylabel('Q')
ax2.set_zlabel('E')

# Set overall title
plt.suptitle('A Story of 2 Subplots')

# Save the plot as a PNG file
plt.savefig('novice_final.png')