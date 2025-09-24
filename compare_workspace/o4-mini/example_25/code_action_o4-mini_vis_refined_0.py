import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def g(s):
    return np.sin(3 * np.pi * s) * np.exp(-s)

# Generate data for the 1D plot
s = np.linspace(0, 2, 100)
g_s = g(s)
g_s_plus_0_1 = g(s + 0.1)
g_s_plus_0_2 = g(s + 0.2)

# Create figure and subplots
fig = plt.figure(figsize=(12, 6))
ax1 = fig.add_subplot(1, 2, 1)
ax2 = fig.add_subplot(1, 2, 2, projection='3d')

# Plot the 1D functions
ax1.plot(s, g_s, label='g(s)', color='blue')
ax1.plot(s, g_s_plus_0_1, label='g(s + 0.1)', linestyle='--', color='green')
ax1.plot(s, g_s_plus_0_2, label='g(s + 0.2)', linestyle=':', color='red')
ax1.set_title('1D plot of g(s) shifts')
ax1.set_xlabel('s')
ax1.set_ylabel('g(s)')
ax1.legend()

# Generate data for the 3D surface
P = np.linspace(-3, 3, 100)
Q = np.linspace(-3, 3, 100)
P, Q = np.meshgrid(P, Q)
E = np.cos(np.sqrt(P**2 + Q**2))

# Plot the 3D surface
surf = ax2.plot_surface(P, Q, E, cmap='viridis', edgecolor='none')
ax2.set_title('3D surface of cos(sqrt(P^2 + Q^2))')
ax2.set_xlabel('P')
ax2.set_ylabel('Q')
ax2.set_zlabel('E(P, Q)')
fig.colorbar(surf, ax=ax2, shrink=0.5, aspect=5)

# Main title and save
plt.suptitle('A Story of 2 Subplots')
plt.savefig('novice_final.png', bbox_inches='tight')