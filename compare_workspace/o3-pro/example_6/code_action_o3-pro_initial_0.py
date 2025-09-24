import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.cm import get_cmap

# ------------------------------------------------------------------
# 1. Raw data (rows are outer-ring slices, columns are inner slices)
raw = np.array([[80., 20.],
                [50., 50.],
                [40., 60.]])          # shape: (3, 2)

# ------------------------------------------------------------------
# 2. Prepare widths (in radians) for the polar bars
total       = raw.sum()              # 300
inner_vals  = raw.flatten()          # six values
outer_vals  = raw.sum(axis=1)        # three values

inner_w = inner_vals / total * 2 * np.pi
outer_w = outer_vals / total * 2 * np.pi

# ------------------------------------------------------------------
# 3. Convert widths to start angles so the two rings stay aligned
θ_outer = np.concatenate(([0], np.cumsum(outer_w)))[:-1]
θ_inner = np.concatenate(([0], np.cumsum(inner_w)))[:-1]

# ------------------------------------------------------------------
# 4. Colour selection from a discrete colormap
cmap          = get_cmap('tab20')    # 20 categorical colours
outer_colors  = cmap(np.arange(3) * 4)           # indices 0, 4, 8
inner_colors  = cmap([1, 2, 5, 6, 9, 10])        # six specific indices

# ------------------------------------------------------------------
# 5. Create polar axes
fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))

# ------------------------------------------------------------------
# 6. Ring geometry
thickness     = 0.3
outer_bottom  = 1 - thickness        # inner radius of outer ring
inner_bottom  = outer_bottom - thickness  # inner radius of inner ring

# ------------------------------------------------------------------
# 7. Draw the outer ring
ax.bar(θ_outer,
       height=thickness,
       width=outer_w,
       bottom=outer_bottom,
       color=outer_colors,
       edgecolor='white',
       linewidth=1,
       align='edge')

# ------------------------------------------------------------------
# 8. Draw the inner ring
ax.bar(θ_inner,
       height=thickness,
       width=inner_w,
       bottom=inner_bottom,
       color=inner_colors,
       edgecolor='white',
       linewidth=1,
       align='edge')

# ------------------------------------------------------------------
# 9. Decorations
ax.set_title('Pie plot with bar method and polar coordinates', va='bottom')
ax.set_axis_off()
plt.tight_layout()

# ------------------------------------------------------------------
# 10. Save to file
plt.savefig("novice.png")