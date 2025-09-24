import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm

# Define the data
data = np.array([[80., 20.], [50., 50.], [40., 60.]])

# Normalize each row to 2π radians
row_sums = data.sum(axis=1, keepdims=True)
normalized_data = (data / row_sums) * (2 * np.pi)

# Create colormap and color arrays
cmap = cm.get_cmap('tab20', 20)
outer_colors = cmap(np.arange(3) * 4)  # Colors for outer ring
inner_colors = cmap([1, 2, 5, 6, 9, 10])  # Colors for inner ring

# Set up polar plot
fig, ax = plt.subplots(figsize=(8, 8), subplot_kw={'polar': True})

# Create outer ring (first column values)
wedges_outer, _ = ax.pie(
    normalized_data[:, 0],
    colors=outer_colors,
    radius=1,
    startangle=90,
    counterclock=False,
    wedgeprops={'edgecolor': 'white', 'linewidth': 1}
)

# Create inner ring (second column values)
wedges_inner, _ = ax.pie(
    normalized_data[:, 1],
    colors=inner_colors,
    radius=0.7,  # Smaller radius for nesting
    startangle=90,
    counterclock=False,
    wedgeprops={'edgecolor': 'white', 'linewidth': 1}
)

# Set consistent ring thickness
plt.setp(wedges_outer, width=0.3)
plt.setp(wedges_inner, width=0.3)

# Add title and hide axis
ax.set_title('Pie plot with bar method and polar coordinates', va='bottom')
ax.axis('off')

# Save as PNG without displaying
plt.savefig("novice_final.png", bbox_inches='tight')