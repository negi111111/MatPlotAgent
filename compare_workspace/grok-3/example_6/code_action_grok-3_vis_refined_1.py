import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm

# Define the data
data = np.array([[80., 20.], [50., 50.], [40., 60.]])

# Normalize the data to 2 * np.pi for the pie chart
normalized_data = data / data.sum(axis=1, keepdims=True) * (2 * np.pi)

# Create color maps
cmap = cm.get_cmap('tab20')(np.linspace(0, 1, 20))
outer_colors = cmap[[0, 4, 8]]  # Select colors for outer ring
inner_colors = cmap[[1, 2, 5, 6, 9, 10]]  # Select colors for inner ring

# Create the nested pie plot using bar method in polar coordinates
fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

# Outer ring
outer_width = normalized_data.sum(axis=1)
theta_outer = np.linspace(0, 2 * np.pi, len(outer_width) + 1)[:-1]
ax.bar(theta_outer, [1] * len(outer_width), width=(2 * np.pi) / len(outer_width), 
       color=outer_colors, edgecolor='white', linewidth=1)

# Inner ring
inner_width = normalized_data.flatten()
# Compute starting angles for inner segments based on cumulative sums within each outer segment
start_angles = []
current_angle = 0
for row in normalized_data:
    start_angles.append(current_angle)
    start_angles.append(current_angle)
    current_angle += row.sum()
ax.bar(start_angles, [0.5] * len(inner_width), width=inner_width, 
       color=inner_colors, edgecolor='white', linewidth=1)

# Add title and turn off axis
ax.set_title('Pie plot with bar method and polar coordinates', va='bottom')
ax.axis('off')  # Turn off the axis

# Save the plot to a PNG file
plt.savefig('novice_final.png', bbox_inches='tight')