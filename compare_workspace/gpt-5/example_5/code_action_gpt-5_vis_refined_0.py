import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.lines import Line2D

# Data for pie chart
fruits = ['Apples', 'Oranges', 'Bananas']
sizes = [35, 45, 20]
explode = (0.1, 0, 0)  # only "explode" the 1st slice (Apples)

# Data for bar chart (apple preference by age group)
age_groups = ['Under 18', '18-30', '30-50', 'Over 50']
preferences = [25, 40, 20, 15]  # percentages

# Create figure and subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

# Plot pie chart
wedges, texts, autotexts = ax1.pie(
    sizes,
    explode=explode,
    labels=fruits,
    autopct='%1.1f%%',
    startangle=90,
    wedgeprops=dict(edgecolor='white')
)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
ax1.set_title('Fruit Distribution in Basket')

# Plot bar chart
bars = ax2.bar(
    age_groups,
    preferences,
    color=['lightblue', 'lightcyan', 'lightsteelblue', 'deepskyblue'],
    edgecolor='white'
)
ax2.set_title('Apple Preference by Age Group')
ax2.set_ylabel('Percentage of Apple Lovers')
ax2.set_ylim(0, 100)
ax2.set_yticks(np.arange(0, 101, 20))
ax2.grid(axis='y', linestyle='--', linewidth=0.5, alpha=0.6)

# Adjust layout first so transforms reflect final positions
plt.tight_layout()
fig.canvas.draw()  # Ensure layout is applied before coordinate transforms

# Draw connecting lines from the pie center to the top of each bar
# Convert coordinates to figure space and draw lines at the figure level
pie_center_fig = fig.transFigure.inverted().transform(
    ax1.transAxes.transform((0.5, 0.5))
)

for rect in bars:
    x_center = rect.get_x() + rect.get_width() / 2.0
    y_top = rect.get_height()
    bar_top_fig = fig.transFigure.inverted().transform(
        ax2.transData.transform((x_center, y_top))
    )
    line = Line2D(
        [pie_center_fig[0], bar_top_fig[0]],
        [pie_center_fig[1], bar_top_fig[1]],
        transform=fig.transFigure,
        color='black',
        linewidth=1
    )
    fig.add_artist(line)

# Save the plot
plt.savefig('novice_final.png')