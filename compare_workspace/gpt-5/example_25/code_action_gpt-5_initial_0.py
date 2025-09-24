import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # optional; ensures 3D plotting support

# 1) Prepare the 1D domain for s
s = np.linspace(0.0, 2.0, 800)  # start=0.0, stop=2.0, num=800 points

# 2) Define g(s) = sin(3*pi*s) * exp(-s)
def g(x):
    return np.sin(3 * np.pi * x) * np.exp(-x)

# 3) Compute three datasets: g(s), g(s + 0.1), g(s + 0.2)
g0 = g(s)
g1 = g(s + 0.1)
g2 = g(s + 0.2)

# 4) Prepare 3D surface data: P, Q, and E = cos(sqrt(P^2 + Q^2))
p = np.linspace(-5.0, 5.0, 250)  # 1D array for P-axis
q = np.linspace(-5.0, 5.0, 250)  # 1D array for Q-axis
P, Q = np.meshgrid(p, q, indexing='xy')  # 2D coordinate grids
E = np.cos(np.sqrt(P**2 + Q**2))        # surface values

# 5) Create figure and subplots
fig = plt.figure(figsize=(12, 5))
fig.suptitle('A Story of 2 Subplots', fontsize=16)

ax1 = fig.add_subplot(1, 2, 1)                     # first subplot: 2D
ax2 = fig.add_subplot(1, 2, 2, projection='3d')    # second subplot: 3D

# 6) Plot the 2D lines
ax1.plot(s, g0, label='g(s)', color='tab:blue', linewidth=2)
ax1.plot(s, g1, label='g(s + 0.1)', color='tab:orange', linewidth=2)
ax1.plot(s, g2, label='g(s + 0.2)', color='tab:green', linewidth=2)
ax1.set_xlabel('s')
ax1.set_ylabel('g(s)')
ax1.set_title('2D plot of g(s) with shifts')
ax1.legend()
ax1.grid(True, linestyle='--', alpha=0.5)

# 7) Plot the 3D surface
surf = ax2.plot_surface(P, Q, E, cmap='viridis', edgecolor='none', linewidth=0, antialiased=True)
ax2.set_xlabel('P')
ax2.set_ylabel('Q')
ax2.set_zlabel('E = cos(sqrt(P^2 + Q^2))')
ax2.set_title('3D surface')
fig.colorbar(surf, ax=ax2, shrink=0.6, pad=0.1)

# 8) Layout and save
plt.tight_layout(rect=[0, 0, 1, 0.95])  # leave space for suptitle
plt.savefig("novice.png", dpi=150, bbox_inches='tight')