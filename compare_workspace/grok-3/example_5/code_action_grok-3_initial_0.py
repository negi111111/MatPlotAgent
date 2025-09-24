import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# Data for pie chart (distribution of fruits)
fruits = ['Apples', 'Oranges', 'Bananas']
fruit_sizes = [35, 45, 20]
explode = [0.1, 0, 0]  # Explode the Apples slice by 0.1 for separation

# Data for stacked bar chart (distribution of people favoring apples by age group)
age_groups = ['<18', '18-30', '30-50', '>50']
apple_favor_percentages = [25, 40, 20, 15]

# Create a figure with two subplots side by side
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))

# Adjust spacing between subplots for clarity
fig.subplots_adjust(wspace=0.5)

# Create pie chart for fruit distribution
wedges, texts, autotexts = ax1.pie(fruit_sizes, explode=explode, labels=fruits, autopct='%1.1f%%', startangle=90,
                                   colors=['#ff9999', '#ffcc00', '#99cc00'])  # High-contrast colors

# Set pie chart to be a perfect circle
ax1.axis('equal')

# Add title to pie chart
ax1.set_title('Fruit Distribution in Basket')

# Create stacked bar chart for distribution of people favoring apples by age group
bottom = 0
colors = ['#ff6666', '#ff9966', '#ffcc66', '#ffeb66']  # High-contrast colors for stacked bars
for i, percentage in enumerate(apple_favor_percentages):
    ax2.bar('Apples', percentage, bottom=bottom, label=age_groups[i], color=colors[i])
    bottom += percentage

# Add labels and title for stacked bar chart
ax2.set_ylabel('Percentage of People Favoring Apples')
ax2.set_title('Apple Preference by Age Group')

# Add legend to stacked bar chart
ax2.legend(title='Age Group')

# Get the position of the exploded Apples slice (approximate center of the slice)
apple_slice_center_x = 0.5 + 0.1 * 0.707  # Rough x-coordinate with explosion
apple_slice_center_y = 0.5 + 0.1 * 0.707  # Rough y-coordinate with explosion
apple_slice_point = ax1.transAxes.transform((apple_slice_center_x, apple_slice_center_y))

# Get the top and bottom points of the stacked bar for Apples
bar_bottom_point = ax2.transData.transform((0, 0))  # Bottom of bar
bar_top_point = ax2.transData.transform((0, 100))  # Top of bar

# Convert to figure coordinates
apple_slice_point_fig = fig.transFigure.inverted().transform(apple_slice_point)
bar_bottom_point_fig = fig.transFigure.inverted().transform(bar_bottom_point)
bar_top_point_fig = fig.transFigure.inverted().transform(bar_top_point)

# Draw lines from Apples slice to top and bottom of bar chart
line1 = plt.Line2D(
    [apple_slice_point_fig[0], bar_top_point_fig[0]],
    [apple_slice_point_fig[1], bar_top_point_fig[1]],
    color='black', linewidth=1, transform=fig.transFigure
)
line2 = plt.Line2D(
    [apple_slice_point_fig[0], bar_bottom_point_fig[0]],
    [apple_slice_point_fig[1], bar_bottom_point_fig[1]],
    color='black', linewidth=1, transform=fig.transFigure
)

# Add lines to the figure
fig.add_artist(line1)
fig.add_artist(line2)

# Adjust layout to prevent overlap
plt.tight_layout()

# Re-apply subplot spacing if needed
fig.subplots_adjust(wspace=0.5)

# Save the plot as a PNG file
plt.savefig("novice.png")