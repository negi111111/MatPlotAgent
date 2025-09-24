import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# 1. Fix random seed
np.random.seed(42)

# 2. Prepare x and layer definitions
x = np.arange(30)
n_layers = 4
base_colors = ['purple', 'orange', 'grey', 'pink']
y_positions = np.arange(n_layers)

# 3. Create figure and 3D axes
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')

# 4. Plot each layer
for k in y_positions:
    heights = np.random.rand(30)
    colors = [base_colors[k]] * 29 + ['black']

    xx = x
    yy = np.full_like(x, fill_value=k, dtype=float)
    zz = np.zeros_like(x, dtype=float)
    dx = np.ones_like(x, dtype=float)
    dy = np.ones_like(x, dtype=float)
    dz = heights

    ax.bar3d(xx, yy, zz, dx, dy, dz, color=colors, alpha=0.8)

# 5. Label axes and set ticks
ax.set_xlabel('X')
ax.set_ylabel('Layer (k)')
ax.set_zlabel('Value')
ax.set_yticks(y_positions)

# 6. Adjust view
ax.view_init(elev=20, azim=30)

plt.tight_layout()
plt.savefig("novice.png")