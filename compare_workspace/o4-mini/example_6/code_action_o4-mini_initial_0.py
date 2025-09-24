import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt

# 1. Define the raw data (3 rows, 2 columns)
data = np.array([
    [80., 20.],
    [50., 50.],
    [40., 60.]
])

# 2. Normalize data so the total sums to 2π radians
total = data.sum()                       # 300.0
norm_data = data / total * 2 * np.pi     # Now sums to 2π

# 3. Prepare angular widths for outer and inner rings
outer_widths = norm_data.sum(axis=1)     # 3 slices (one per row)
inner_widths = norm_data.flatten()       # 6 slices (one per cell)

# 4. Compute start angles so slices butt up against each other
outer_starts = np.concatenate(([0], np.cumsum(outer_widths)[:-1]))
inner_starts = np.concatenate(([0], np.cumsum(inner_widths)[:-1]))

# 5. Pick colors from the 'tab20' colormap
cmap = plt.get_cmap('tab20')
outer_colors = cmap(np.arange(3) * 4)        # 3 distinct colors
inner_colors = cmap([1, 2, 5, 6, 9, 10])     # 6 distinct colors

# 6. Define ring radii and thickness
r_inner = 1.0
thickness = 0.3
r_outer = r_inner + thickness

# 7. Create the figure and a polar subplot
fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))

# 8. Plot the inner ring
ax.bar(
    inner_starts,      # start angles
    thickness,         # radial height
    width=inner_widths,# angular widths
    bottom=r_inner,    # inner radius
    color=inner_colors,
    edgecolor='white',
    linewidth=1
)

# 9. Plot the outer ring
ax.bar(
    outer_starts,
    thickness,
    width=outer_widths,
    bottom=r_outer,
    color=outer_colors,
    edgecolor='white',
    linewidth=1
)

# 10. Clean up and title
ax.set_axis_off()
ax.set_title('Pie plot with bar method and polar coordinates', y=1.08)

# 11. Save to PNG
plt.savefig("novice.png")