import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# 1D data for subplot 1
s  = np.linspace(0.0, 2.0, 400)
g1 = np.sin(3 * np.pi * s) * np.exp(-s)
g2 = np.sin(3 * np.pi * (s + 0.1)) * np.exp(-(s + 0.1))
g3 = np.sin(3 * np.pi * (s + 0.2)) * np.exp(-(s + 0.2))

# Create figure
fig = plt.figure(figsize=(12, 6))

# First subplot: 2D line plots
ax1 = fig.add_subplot(1, 2, 1)
ax1.plot(s, g1, label='g(s)',       color='blue',  linewidth=2)
ax1.plot(s, g2, label='g(s + 0.1)', color='green', linestyle='--', linewidth=2)
ax1.plot(s, g3, label='g(s + 0.2)', color='red',   linestyle=':',  linewidth=2)
ax1.set_xlabel('s')
ax1.set_ylabel('g(s)')
ax1.set_title('1D plot of g(s) shifts')
ax1.legend(loc='upper right')

# Prepare 3D data for subplot 2
p  = np.linspace(-3.0, 3.0, 100)
q  = np.linspace(-3.0, 3.0, 100)
P, Q = np.meshgrid(p, q)
E    = np.cos(np.sqrt(P**2 + Q**2))

# Second subplot: 3D surface
ax2 = fig.add_subplot(1, 2, 2, projection='3d')
surf = ax2.plot_surface(
    P, Q, E,
    rstride=1,
    cstride=1,
    cmap='viridis',
    edgecolor='none',
    antialiased=True
)
ax2.set_xlabel('P')
ax2.set_ylabel('Q')
ax2.set_zlabel('E(P, Q)')
ax2.set_title('3D surface of cos(sqrt(P²+Q²))')
fig.colorbar(surf, ax=ax2, shrink=0.5, aspect=10, pad=0.1)

# Final touches
fig.suptitle('A Story of 2 Subplots', fontsize=16, y=1.02)
plt.tight_layout()

# Save the figure
plt.savefig('novice.png', dpi=300, bbox_inches='tight')