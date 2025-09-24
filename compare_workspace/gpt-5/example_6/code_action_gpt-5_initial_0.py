import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt

# 1) Import and setup
# (Using numpy and matplotlib; selecting a discrete 20-color colormap)
cmap = plt.get_cmap('tab20')

# 2) Prepare the input data
data = np.array([[80., 20.],
                 [50., 50.],
                 [40., 60.]], dtype=float)

total = data.sum()

# 3) Normalize the data to 2π
normalized = data / total * (2 * np.pi)

# 4) Build color arrays from a 20-color colormap (select specific indices)
tab20_colors = np.array(cmap.colors)  # 20 distinct RGBA colors
outer_colors = tab20_colors[np.arange(3) * 4]        # indices [0, 4, 8]
inner_colors = tab20_colors[[1, 2, 5, 6, 9, 10]]     # six specific color indices

# 5) Compute bar widths for both rings
outer_widths = normalized.sum(axis=1)     # three outer widths
inner_widths = normalized.flatten()       # six inner widths

# 6) Compute starting angles (theta) for each bar segment
# Outer ring starts: cumulative starts from 0
outer_theta = np.cumsum(np.concatenate(([0.0], outer_widths[:-1])))

# Inner ring starts: aligned to the outer segment's start per row
inner_theta_list = []
for row_idx, row_widths in enumerate(normalized):
    start = outer_theta[row_idx]
    row_starts = start + np.cumsum(np.concatenate(([0.0], row_widths[:-1])))
    inner_theta_list.extend(row_starts)
inner_theta = np.array(inner_theta_list)

# 7) Set up the polar plot
fig, ax = plt.subplots(figsize=(6, 6), subplot_kw={'projection': 'polar'})
ax.axis('off')

r0 = 0.5            # radius of the blank center
ring_thickness = 0.4
ax.set_ylim(0, r0 + 2 * ring_thickness)

# 8) Draw the bars for both rings
# Outer ring
ax.bar(outer_theta,
       height=ring_thickness,
       width=outer_widths,
       bottom=r0 + ring_thickness,
       color=outer_colors,
       edgecolor='white',
       linewidth=1,
       align='edge')

# Inner ring
ax.bar(inner_theta,
       height=ring_thickness,
       width=inner_widths,
       bottom=r0,
       color=inner_colors,
       edgecolor='white',
       linewidth=1,
       align='edge')

# 9) Add the title
ax.set_title('Pie plot with bar method and polar coordinates')

# Save the figure
plt.savefig("novice.png")