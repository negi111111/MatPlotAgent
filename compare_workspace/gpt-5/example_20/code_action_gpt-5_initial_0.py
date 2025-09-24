import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # Registers 3D projection

# 1) Fixed random state for reproducibility
rng = np.random.default_rng(seed=42)

# 2) Prepare data
x = np.arange(30)                      # X positions: 0 to 29
zbase = np.zeros_like(x, dtype=float)  # Bars start at z = 0
dx = np.full_like(x, 0.9, dtype=float) # Bar width along X
dy = 0.8                               # Bar width along Y (constant for all bars)

# Define layers and their colors at y = k planes
layers = [
    {'k': 0, 'color': 'purple'},
    {'k': 1, 'color': 'orange'},
    {'k': 2, 'color': 'grey'},
    {'k': 3, 'color': 'pink'},
]

# 3) Create figure and 3D subplot
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111, projection='3d')

# 4) Plot each layer on plane y = k
for layer in layers:
    k = layer['k']
    layer_color = layer['color']

    # y positions fixed at k for this layer
    y = np.full_like(x, k, dtype=float)

    # Generate 30 random numbers for bar heights (dz)
    dz = rng.random(30)  # values in [0, 1)

    # Per-bar colors: all layer_color except last bar is black
    colors = [layer_color] * len(x)
    colors[-1] = 'black'

    # Plot bars for this layer
    ax.bar3d(
        x,           # x base positions
        y,           # y base positions (constant k)
        zbase,       # z base positions (0)
        dx,          # width along x
        dy,          # width along y
        dz,          # bar heights along z
        color=colors,
        alpha=0.8,   # 80% opacity
        shade=True
    )

# 5) Axis labels
ax.set_xlabel('X')
ax.set_ylabel('Y (layer k)')
ax.set_zlabel('Value')

# 6) Y-axis ticks only at layers with data
ax.set_yticks([layer['k'] for layer in layers])
ax.set_yticklabels([str(layer['k']) for layer in layers])

# Optional: adjust X ticks and viewing angle
ax.set_xticks(np.arange(0, 30, 5))
ax.view_init(elev=20, azim=-60)

plt.tight_layout()
plt.savefig("novice.png", dpi=150, bbox_inches='tight')