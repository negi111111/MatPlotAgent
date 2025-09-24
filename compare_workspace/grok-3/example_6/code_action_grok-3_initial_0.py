import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm

# Define the input data as provided
data = np.array([[80., 20.], [50., 50.], [40., 60.]])

# Normalize the data to 2 * pi
total = np.sum(data)
normalized_data = (data / total) * 2 * np.pi

# Calculate widths for the outer pie (sum of each row)
outer_widths = np.sum(normalized_data, axis=1)

# Calculate widths for the inner pie (flattened data)
inner_widths = normalized_data.flatten()

# Set up a colormap with 20 colors
cmap = cm.get_cmap('tab20')(np.linspace(0, 1, 20))

# Define colors for outer and inner rings as per user instruction
outer_colors = cmap[np.arange(3) * 4]
inner_colors = cmap[[1, 2, 5, 6, 9, 10]]

# Create a figure and axis with polar coordinates
fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})

# Define the radius for outer and inner rings (to control thickness and blank center)
outer_radius = 2.0
inner_radius = 1.0
ring_thickness = 1.0  # Same thickness for both rings

# Plot the outer ring using bar method
theta = np.cumsum(outer_widths) - outer_widths
ax.bar(theta, ring_thickness, width=outer_widths, bottom=outer_radius, color=outer_colors, 
       edgecolor='white', linewidth=1)

# Plot the inner ring using bar method
# Compute starting angles for inner ring (aligned with outer ring segments)
inner_theta = []
for i in range(len(outer_widths)):
    start = theta[i]
    widths = normalized_data[i]
    inner_theta.extend(start + np.cumsum(widths) - widths)
inner_theta = np.array(inner_theta)

ax.bar(inner_theta, ring_thickness, width=inner_widths, bottom=inner_radius, color=inner_colors, 
       edgecolor='white', linewidth=1)

# Set the title of the plot
ax.set_title('Pie plot with bar method and polar coordinates', pad=20)

# Turn off the axis
ax.set_axis_off()

# Ensure blank center by setting radius limits
ax.set_rlim(0, outer_radius + ring_thickness)

# Save the plot as a PNG file
plt.savefig("novice.png")