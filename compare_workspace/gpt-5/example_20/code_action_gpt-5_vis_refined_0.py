import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 (ensures 3D projection is available)

# Step 1: Set a fixed random state for reproducibility
np.random.seed(42)

# Step 2: Generate data
x = np.arange(30)  # x values from 0 to 29
num_layers = 4
y_values = [np.random.rand(30) for _ in range(num_layers)]  # 4 layers of random heights
layer_colors = ['purple', 'orange', 'grey', 'pink']

# Step 3: Create a 3D subplot
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111, projection='3d')

# Step 4: Plot bars for each layer
for k in range(num_layers):
    # Color all bars in the layer with the specified color, last bar as black
    bar_colors = [layer_colors[k]] * 29 + ['black']
    ax.bar(
        x, y_values[k],
        zs=k, zdir='y',
        color=bar_colors,
        alpha=0.8,
        edgecolor='black',
        linewidth=0.3
    )

# Step 5: Labels and ticks
ax.set_xlabel('X')
ax.set_ylabel('Y (layer k)')
ax.set_zlabel('Values')

# Only show discrete y positions for which data exists
ax.set_yticks(range(num_layers))
ax.set_yticklabels([f'Layer {i}' for i in range(num_layers)])

# Optional improvements: viewing angle and light grid for readability
ax.view_init(elev=20, azim=-60)
ax.grid(True)

# Step 6: Save the plot
plt.savefig('novice_final.png')