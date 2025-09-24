import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt

# Prepare data
data = np.array([[80., 20.], [50., 50.], [40., 60.]])
flat_data = data.flatten()  # [80, 20, 50, 50, 40, 60]
total = flat_data.sum()     # 300

# Normalize data to 2π radians
## Outer ring (sums: [100, 100, 100])
outer_sums = data.sum(axis=1)
cum_outer = np.cumsum(np.append(0, outer_sums)) * 2 * np.pi / total
widths_outer = cum_outer[1:] - cum_outer[:-1]

## Inner ring (flattened data)
cum_inner = np.cumsum(np.append(0, flat_data)) * 2 * np.pi / total
widths_inner = cum_inner[1:] - cum_inner[:-1]

# Radial settings
inner_ring_bottom = 1
inner_ring_height = 1
outer_ring_bottom = 2
outer_ring_height = 1

# Color setup
cmap = plt.get_cmap('viridis', 20)  # 20-color colormap
outer_colors = cmap(np.arange(3) * 4)    # Indices [0, 4, 8]
inner_colors = cmap([1, 2, 5, 6, 9, 10]) # Indices [1, 2, 5, 6, 9, 10]

# Create polar plot
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(projection='polar')

# Outer ring (3 segments)
ax.bar(
    x=cum_outer[:-1],          # Start angles
    width=widths_outer,        # Angular widths
    bottom=outer_ring_bottom,  # Radial start
    height=outer_ring_height,  # Radial thickness
    color=outer_colors,        # Segment colors
    edgecolor='white',         # Edge color
    linewidth=1,               # Edge line width
    align='edge'               # Align bars to start angle
)

# Inner ring (6 segments)
ax.bar(
    x=cum_inner[:-1],          # Start angles
    width=widths_inner,        # Angular widths
    bottom=inner_ring_bottom,  # Radial start
    height=inner_ring_height,  # Radial thickness
    color=inner_colors,        # Segment colors
    edgecolor='white',         # Edge color
    linewidth=1,               # Edge line width
    align='edge'               # Align bars to start angle
)

# Configure plot
ax.set_ylim(0, 3)              # Radial axis limits
plt.title('Pie plot with bar method and polar coordinates', pad=20)
ax.set_axis_off()              # Hide axis

# Save plot
plt.savefig("novice.png", bbox_inches='tight', dpi=100)