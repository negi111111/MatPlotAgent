import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 (ensures 3D support in some environments)

# Define the function g(s)
def g(s):
    return np.sin(3 * np.pi * s) * np.exp(-s)

# Generate data for g(s)
s = np.linspace(0, 2, 100)
g_s = g(s)
g_s_plus_0_1 = g(s + 0.1)
g_s_plus_0_2 = g(s + 0.2)

# Create the figure and subplots (2D and 3D)
fig = plt.figure(figsize=(15, 6))

# 2D subplot
ax1 = fig.add_subplot(1, 2, 1)
ax1.plot(s, g_s, label='g(s)', color='blue', linewidth=2)
ax1.plot(s, g_s_plus_0_1, label='g(s + 0.1)', color='orange', linewidth=2)
ax1.plot(s, g_s_plus_0_2, label='g(s + 0.2)', color='green', linewidth=2)
ax1.set_title('2D plot of g(s) with shifts')
ax1.set_xlabel('s')
ax1.set_ylabel('g(s)')
ax1.minorticks_on()
ax1.grid(True, which='both', linestyle='--', alpha=0.4)
ax1.legend(frameon=False)

# Generate data for the 3D surface plot
P = np.linspace(-5, 5, 100)
Q = np.linspace(-5, 5, 100)
P, Q = np.meshgrid(P, Q)
E = np.cos(np.sqrt(P**2 + Q**2))

# 3D subplot
ax2 = fig.add_subplot(1, 2, 2, projection='3d')
surf = ax2.plot_surface(P, Q, E, cmap='viridis', linewidth=0, antialiased=True)
ax2.set_title('3D surface')
ax2.set_xlabel('P')
ax2.set_ylabel('Q')
ax2.set_zlabel('E = cos(sqrt(P^2 + Q^2))')
ax2.grid(True)
# Improve aspect ratio for readability (requires Matplotlib >= 3.3)
try:
    ax2.set_box_aspect((1, 1, 0.5))
except Exception:
    pass
fig.colorbar(surf, ax=ax2, shrink=0.6, aspect=18, pad=0.08)

# Overall title and layout adjustments
plt.suptitle('A Story of 2 Subplots')
fig.tight_layout(rect=[0, 0, 1, 0.96])

# Save the figure as a single PNG
plt.savefig('novice_final.png', bbox_inches='tight')