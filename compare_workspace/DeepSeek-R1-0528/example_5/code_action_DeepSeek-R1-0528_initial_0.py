import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

# Create figure with subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 7))
fig.subplots_adjust(wspace=0.4)  # Space between subplots

# Pie chart data
sizes = [35, 45, 20]
labels_pie = ['Apples', 'Oranges', 'Bananas']
explode = (0.1, 0, 0)  # Explode apples
colors_pie = ['#ff4d4d', '#ffa64d', '#ffff4d']  # High-contrast colors
ax1.pie(sizes, explode=explode, labels=labels_pie, colors=colors_pie,
        autopct='%1.1f%%', startangle=90)
ax1.set_title('Fruit Distribution in Basket', fontweight='bold')

# Stacked bar chart data
age_groups = ['Under 18', '18-30', '30-50', 'Over 50']
apple_percent = [25, 40, 20, 15]
non_apple_percent = [100 - x for x in apple_percent]
ax2.bar(age_groups, apple_percent, color='#ff4d4d', label='Apple')
ax2.bar(age_groups, non_apple_percent, bottom=apple_percent,
        color='#cccccc', label='Non-Apple')
ax2.set_title('Apple Favor by Age Group', fontweight='bold')
ax2.set_ylabel('Percentage')
ax2.set_ylim(0, 100)
ax2.legend(loc='upper right')

# Get bar chart's left edge (xmin) for line connections
xmin_bar = ax2.get_xlim()[0]

# Calculate pie chart edge points (in data coordinates)
# 1.1 multiplier accounts for explosion offset
p1_pie = (0, 1.1)  # Top edge of apples slice (90°)
angle_rad = np.radians(216)  # Bottom edge of apples slice
p2_pie = (1.1 * np.cos(angle_rad), 1.1 * np.sin(angle_rad))

# Bar chart connection points (xmin, y)
p1_bar = (xmin_bar, 100)  # Top-left of bar chart
p2_bar = (xmin_bar, 0)    # Bottom-left of bar chart

# Transform coordinates to figure space
p1_pie_fig = ax1.transData.transform(p1_pie)
p2_pie_fig = ax1.transData.transform(p2_pie)
p1_bar_fig = ax2.transData.transform(p1_bar)
p2_bar_fig = ax2.transData.transform(p2_bar)

# Draw connecting lines
line1 = plt.Line2D(
    [p1_pie_fig[0], p1_bar_fig[0]], [p1_pie_fig[1], p1_bar_fig[1]],
    color='black', linewidth=1, transform=fig.transFigure
)
line2 = plt.Line2D(
    [p2_pie_fig[0], p2_bar_fig[0]], [p2_pie_fig[1], p2_bar_fig[1]],
    color='black', linewidth=1, transform=fig.transFigure
)
fig.add_artist(line1)
fig.add_artist(line2)

# Save as PNG without displaying
plt.savefig("novice.png")