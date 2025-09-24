import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 (ensures 3D projection is registered)
from mpl_toolkits.mplot3d.art3d import Line3DCollection
from matplotlib.lines import Line2D

# Generate data
x = np.linspace(0, 4 * np.pi, 100)
y1 = np.sin(x) - (np.pi / 4)
y2 = np.cos(x) - (np.pi / 4)

# Create figure and 3D axes
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111, projection='3d')

def add_3d_stems(ax, x_vals, z_vals, y_const, color, marker_size=20, line_width=1.5):
    # Create line segments for stems: from (x, y_const, 0) to (x, y_const, z)
    segments = [np.array([[xi, y_const, 0.0], [xi, y_const, zi]]) for xi, zi in zip(x_vals, z_vals)]
    lc = Line3DCollection(segments, colors=[color], linewidths=line_width)
    ax.add_collection3d(lc)
    # Add markers at the tips
    ax.scatter(x_vals, np.full_like(x_vals, y_const), z_vals, color=color, s=marker_size, depthshade=True)

# Add stems for Sine at y=0 and Cosine at y=1
add_3d_stems(ax, x, y1, y_const=0.0, color='tab:blue')
add_3d_stems(ax, x, y2, y_const=1.0, color='tab:red')

# Baseline reference lines at z=0 for each series
ax.plot([x.min(), x.max()], [0.0, 0.0], [0.0, 0.0], color='tab:blue', linestyle='--', linewidth=1.0, alpha=0.6)
ax.plot([x.min(), x.max()], [1.0, 1.0], [0.0, 0.0], color='tab:red', linestyle='--', linewidth=1.0, alpha=0.6)

# Labels, ticks, and title
ax.set_xlabel('X values (0 to 4π)')
ax.set_ylabel('Function Type')
ax.set_zlabel('Function Value')
ax.set_title('3D Stem Plot of Sine and Cosine Functions')

ax.set_yticks([0, 1])
ax.set_yticklabels(['Sine', 'Cosine'])

# Adjust viewing angle for clarity
ax.view_init(elev=25, azim=-60)

# Light grid for readability
ax.grid(True, linestyle=':', linewidth=0.6, alpha=0.7)

# Legend using proxy artists
legend_handles = [
    Line2D([0], [0], color='tab:blue', marker='o', linestyle='-', label='Sine'),
    Line2D([0], [0], color='tab:red', marker='o', linestyle='-', label='Cosine')
]
ax.legend(handles=legend_handles, loc='upper left')

# Tight layout and save exactly one PNG
plt.tight_layout()
plt.savefig('novice_final.png')