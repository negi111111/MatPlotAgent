import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm

# 1. Define the data
data = np.array([
    [80., 20.],
    [50., 50.],
    [40., 60.]
])

# 2. Compute outer wedge angles (row sums relative to total)
row_sums = data.sum(axis=1)                # [100., 100., 100.]
total_sum = row_sums.sum()                 # 300.
outer_angles = row_sums / total_sum * 2 * np.pi

# 3. Compute starting angles for each outer wedge
outer_starts = np.concatenate([[0], np.cumsum(outer_angles)[:-1]])

# 4. Compute inner wedge angles and their start positions
inner_angles = []
inner_starts = []
for i, row in enumerate(data):
    # angles for each slice in this row
    angles = row / row.sum() * outer_angles[i]
    # cumulative starts within this outer wedge
    cum_angles = np.concatenate([[0], np.cumsum(angles)[:-1]])
    for ca, ang in zip(cum_angles, angles):
        inner_starts.append(outer_starts[i] + ca)
        inner_angles.append(ang)

# 5. Choose colors from the 'tab20' colormap
cmap = cm.get_cmap('tab20', 20)
outer_colors = cmap(np.arange(3) * 4)      # three colors spaced by 4
inner_color_indices = [1, 2, 5, 6, 9, 10]
inner_colors = cmap(inner_color_indices)

# 6. Create the plot in polar coordinates
fig, ax = plt.subplots(figsize=(6, 6),
                       subplot_kw=dict(polar=True))

# Parameters for the two rings
inner_radius = 0.7
outer_radius = 1.0
ring_thickness = 0.3

# 7. Draw the inner ring
for start, angle, color in zip(inner_starts, inner_angles, inner_colors):
    ax.bar(
        start,                   # theta start
        ring_thickness,          # radial thickness
        width=angle,             # angular width
        bottom=inner_radius,     # radial position
        color=color,
        edgecolor='white',
        linewidth=1
    )

# 8. Draw the outer ring
for start, angle, color in zip(outer_starts, outer_angles, outer_colors):
    ax.bar(
        start,
        ring_thickness,
        width=angle,
        bottom=outer_radius,
        color=color,
        edgecolor='white',
        linewidth=1
    )

# 9. Aesthetics
ax.set_title('Pie plot with bar method and polar coordinates', va='bottom')
ax.axis('off')

# 10. Save to a single PNG file
plt.savefig('novice_final.png', bbox_inches='tight')