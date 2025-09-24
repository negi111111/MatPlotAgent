import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D   # noqa: F401  (imported for the 3-D side-effects)

# 1. Reproducible random numbers
np.random.seed(42)

# 2. Layer setup
y_layers      = [0, 1, 2, 3]                       # four y-planes
layer_colours = ['purple', 'orange', 'grey', 'pink']  # matching colours

# 3. Common x-coordinates and random heights
x = np.arange(30)                                  # 0 … 29
heights_per_layer = [np.random.rand(30) for _ in y_layers]

# 4. Create 3-D figure
fig = plt.figure(figsize=(10, 6))
ax  = fig.add_subplot(111, projection='3d')

# 5. Draw each layer
dx, dy = 0.8, 0.5
for i, k in enumerate(y_layers):
    z = np.zeros_like(x)                           # all bars start at z = 0
    dz = heights_per_layer[i]                      # unique heights this layer
    y_array = np.full_like(x, k)                   # constant y for this layer
    colours = [layer_colours[i]]*29 + ['black']    # last bar in black

    ax.bar3d(x, y_array, z,
             dx, dy, dz,
             color=colours,
             alpha=0.8,
             shade=True)

# 6. Axis labelling and ticks
ax.set_xlabel('X-axis (index)')
ax.set_ylabel('Y-axis (layer)')
ax.set_zlabel('Z-axis (value)')
ax.set_yticks(y_layers)
ax.set_yticklabels([f'Layer {k}' for k in y_layers])

# 7. Adjust view and layout
ax.view_init(elev=20, azim=-45)
plt.tight_layout()

# 8. Save to file
plt.savefig("novice.png", dpi=300)