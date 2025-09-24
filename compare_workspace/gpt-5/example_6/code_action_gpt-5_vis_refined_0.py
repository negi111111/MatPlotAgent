import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm

# Define the data
data = np.array([[80., 20.], [50., 50.], [40., 60.]])

# Normalize the data to 2*pi
normalized_data = data / data.sum(axis=1, keepdims=True) * (2 * np.pi)

# Create a colormap
cmap = cm.get_cmap('tab20', 20)
outer_colors = cmap(np.arange(3) * 4)           # indices 0, 4, 8
inner_colors = cmap([1, 2, 5, 6, 9, 10])        # six colors for inner wedges

# Set up the polar plot
fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))

# Create the outer pie plot (three wedges)
wedges_outer, _ = ax.pie(
    normalized_data[:, 0],
    colors=outer_colors,
    radius=1.0,
    startangle=90,
    counterclock=False,
    wedgeprops=dict(edgecolor='white', linewidth=1, width=0.25)
)

# Create the inner pie plot (six wedges - flattened)
wedges_inner, _ = ax.pie(
    normalized_data.flatten(),
    colors=inner_colors,
    radius=0.75,
    startangle=90,
    counterclock=False,
    wedgeprops=dict(edgecolor='white', linewidth=1, width=0.25)
)

# Set the title
ax.set_title('Pie plot with bar method and polar coordinates', fontsize=16)

# Turn off the axis for a cleaner look
ax.axis('off')

# Save exactly one PNG
plt.savefig("novice_final.png", bbox_inches='tight')