import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import ConnectionPatch

# Data for pie chart
labels = ['Apples', 'Oranges', 'Bananas']
sizes = [35, 45, 20]
explode = (0.1, 0, 0)  # Only explode the apples slice

# Data for stacked bar chart
age_groups = ['Under 18', '18-30', '30-50', 'Over 50']
apple_favor = [25, 40, 20, 15]
non_apple_favor = [75, 60, 80, 85]  # Complement to 100%

# Create figure and axes
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

# Plot pie chart
wedges, texts, autotexts = ax1.pie(
    sizes, 
    explode=explode, 
    labels=labels, 
    autopct='%1.1f%%',
    startangle=90, 
    colors=['#ff9999', '#66b3ff', '#99ff99']
)
ax1.axis('equal')  # Ensure circular shape
ax1.set_title('Fruit Distribution in Basket', fontweight='bold')

# Plot stacked bar chart
bar_width = 0.4
x = np.arange(len(age_groups))
ax2.bar(x, apple_favor, width=bar_width, label='Apple', color='#ff9999')
ax2.bar(x, non_apple_favor, width=bar_width, bottom=apple_favor, 
        label='Non-Apple', color='#dddddd')
ax2.set_xticks(x)
ax2.set_xticklabels(age_groups)
ax2.set_ylabel('Percentage')
ax2.set_title('Apple Favor by Age Group', fontweight='bold')
ax2.legend(loc='upper right')

# Calculate apple slice position (exploded center)
total = sum(sizes)
start_angle = 90
end_angle = start_angle + 360 * sizes[0] / total
centroid_angle_deg = (start_angle + end_angle) / 2
centroid_angle_rad = np.deg2rad(centroid_angle_deg)
apple_center = (0.1 * np.cos(centroid_angle_rad), 0.1 * np.sin(centroid_angle_rad))

# Create connecting arrows using ConnectionPatch
arrow1 = ConnectionPatch(
    xyA=apple_center, 
    xyB=(0, apple_favor[0]), 
    coordsA=ax1.transData, 
    coordsB=ax2.transData,
    arrowstyle="->", 
    color="black', 
    linewidth=1
)
fig.add_artist(arrow1)

arrow2 = ConnectionPatch(
    xyA=apple_center, 
    xyB=(0, 0), 
    coordsA=ax1.transData, 
    coordsB=ax2.transData,
    arrowstyle="->", 
    color="black", 
    linewidth=1
)
fig.add_artist(arrow2)

# Adjust layout and save
plt.tight_layout()
plt.savefig('novice_final.png')