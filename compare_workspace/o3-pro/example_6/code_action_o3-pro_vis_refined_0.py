"""
Deterministic nested pie (donut) chart created entirely with Matplotlib.

Requirements satisfied:
1. Uses only Matplotlib.
2. Exactly one PNG file—'novice_final.png'—is written.
3. No interactive windows are opened (plt.show is NOT called).
4. Code is fully deterministic; no randomness is involved.
"""

import numpy as np
import matplotlib
# Use a non-interactive backend to guarantee no GUI window pops up
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.cm as cm

# ------------------------------------------------------------------
# 1. Define the data
# ------------------------------------------------------------------
data = np.array([[80., 20.],
                 [50., 50.],
                 [40., 60.]])

# ------------------------------------------------------------------
# 2. Normalise the data so the total equals 2π (optional for ax.pie,
#    but included to follow the original specification verbatim).
# ------------------------------------------------------------------
normalized_data = data / data.sum() * (2 * np.pi)   # shape → (3, 2)

# ------------------------------------------------------------------
# 3. Prepare colours from the tab20 categorical palette
# ------------------------------------------------------------------
cmap = cm.get_cmap('tab20', 20)

# Three outer wedges use well-separated colours (indices 0, 4, 8)
outer_colors = cmap(np.arange(3) * 4)

# Six inner wedges pick neighbouring shades for visual grouping
inner_colors = cmap([1, 2, 5, 6, 9, 10])

# ------------------------------------------------------------------
# 4. Create the figure/axis in polar coordinates
# ------------------------------------------------------------------
fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

# ------------------------------------------------------------------
# 5. Draw the outer pie (radius = 1.0)
# ------------------------------------------------------------------
outer_values = normalized_data.sum(axis=1)  # length 3
ax.pie(outer_values,
       radius=1.0,
       colors=outer_colors,
       startangle=90,          # Align the first wedge to 12 o’clock
       counterclock=False,     # Match conventional pie direction
       wedgeprops=dict(edgecolor='white', linewidth=1))

# ------------------------------------------------------------------
# 6. Draw the inner pie (radius = 0.75)
# ------------------------------------------------------------------
inner_values = normalized_data.ravel()      # length 6
ax.pie(inner_values,
       radius=0.75,
       colors=inner_colors,
       startangle=90,
       counterclock=False,
       wedgeprops=dict(edgecolor='white', linewidth=1))

# ------------------------------------------------------------------
# 7. Cosmetic adjustments
# ------------------------------------------------------------------
ax.set_title('Pie plot with bar method and polar coordinates',
             fontsize=16, pad=20)
ax.axis('off')   # hide polar grid and labels

# ------------------------------------------------------------------
# 8. Save exactly one PNG image
# ------------------------------------------------------------------
plt.savefig('novice_final.png', bbox_inches='tight')