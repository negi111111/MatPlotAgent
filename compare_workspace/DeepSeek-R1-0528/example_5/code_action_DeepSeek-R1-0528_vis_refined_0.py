import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

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
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', 
        startangle=90, colors=['#ff9999', '#66b3ff', '#99ff99'])
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

# Calculate arrow positions in figure coordinates
plt.tight_layout()
fig.canvas.draw()  # Update transformations

# Get apple slice position (exploded center)
total = sum(sizes)
start_angle = 90
apple_angle_deg = start_angle + 0.5 * (360 * sizes[0]/total)
apple_angle_rad = np.deg2rad(apple_angle_deg)
apple_center = (0.1 * np.cos(apple_angle_rad), 0.1 * np.sin(apple_angle_rad))

# Transform coordinates
inv_fig = fig.transFigure.inverted()
apple_point_fig = inv_fig.transform(ax1.transData.transform(apple_center))

# Get bar chart target positions (first bar)
bar_top = inv_fig.transform(ax2.transData.transform((0, apple_favor[0])))
bar_bottom = inv_fig.transform(ax2.transData.transform((0, 0)))

# Draw connecting arrows
fig.annotate('', 
             xy=bar_top, 
             xytext=apple_point_fig,
             arrowprops=dict(arrowstyle='->', color='black', linewidth=1),
             xycoords='figure fraction',
             textcoords='figure fraction')

fig.annotate('', 
             xy=bar_bottom, 
             xytext=apple_point_fig,
             arrowprops=dict(arrowstyle='->', color='black', linewidth=1),
             xycoords='figure fraction',
             textcoords='figure fraction')

# Save final output
plt.savefig('novice_final.png')