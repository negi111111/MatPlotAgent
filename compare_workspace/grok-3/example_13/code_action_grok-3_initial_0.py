import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

# Data for bar plots (same for all four bar plots)
bar_x = [1, 2, 3, 4, 5]
bar_heights = [5, 3, 7, 2, 6]

# Data for cosine curve
x_cos = np.linspace(-2 * np.pi, 2 * np.pi, 100)
y_cos = np.cos(x_cos)

# Define the mosaic layout: 3 rows, with the last row spanning both columns
mosaic = [['bar1', 'bar2'],
          ['bar3', 'bar4'],
          ['cosine', 'cosine']]

# Create the subplot mosaic
fig, axs = plt.subplot_mosaic(mosaic, figsize=(10, 8))

# First row, first bar plot
axs['bar1'].bar(x=bar_x, height=bar_heights, hatch='/', color='blue')
axs['bar1'].set_title('Bar Plot 1 (Hatch: /)')

# First row, second bar plot
axs['bar2'].bar(x=bar_x, height=bar_heights, hatch='\\', color='blue')
axs['bar2'].set_title('Bar Plot 2 (Hatch: \\)')

# Second row, third bar plot
axs['bar3'].bar(x=bar_x, height=bar_heights, hatch='*', color='green')
axs['bar3'].set_title('Bar Plot 3 (Hatch: *)')

# Second row, fourth bar plot
axs['bar4'].bar(x=bar_x, height=bar_heights, hatch='o', color='green')
axs['bar4'].set_title('Bar Plot 4 (Hatch: o)')

# Third row, cosine plot with filled area
ax_cosine = axs['cosine']
ax_cosine.plot(x_cos, y_cos, color='black', label='cos(x)')
ax_cosine.fill_between(x_cos, y_cos, 0, hatch='.', color='magenta', alpha=0.5)
ax_cosine.set_title('Cosine Curve with Filled Area')
ax_cosine.legend()

# Add Ellipse to the cosine plot
ellipse = patches.Ellipse(xy=(0, 0), width=2, height=0.5, hatch='x', color='red', fill=False)
ax_cosine.add_patch(ellipse)

# Add Polygon (triangle) to the cosine plot
polygon = patches.Polygon(xy=[[0, 0], [-0.5, 0.5], [0.5, 0.5]], hatch='+', color='yellow', fill=False)
ax_cosine.add_patch(polygon)

# Adjust aspect ratio and set limits for cosine plot
ax_cosine.set_aspect('auto')
ax_cosine.set_xlim(-2 * np.pi, 2 * np.pi)
ax_cosine.set_ylim(-1.5, 1.5)

# Adjust layout and save the plot
plt.tight_layout()
plt.savefig("novice.png")