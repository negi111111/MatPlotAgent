import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import math

# 2a) Pie chart data
pie_sizes = [35, 45, 20]
pie_labels = ['Apples', 'Oranges', 'Bananas']
explode = [0.1, 0.0, 0.0]   # only “explode” the apples slice

# 2b) Stacked bar chart data
age_groups = ['Under 18', '18–30', '30–50', 'Over 50']
age_percents = [25, 40, 20, 15]     # these sum to 100
# Compute cumulative bottoms for stacking
bottoms = np.cumsum([0] + age_percents[:-1])

# 3) Create figure and axes
fig, (ax_pie, ax_bar) = plt.subplots(1, 2, figsize=(12, 6))
plt.subplots_adjust(wspace=0.4)

# 4) Draw the pie chart
wedges, texts, autotexts = ax_pie.pie(
    pie_sizes,
    labels=pie_labels,
    explode=explode,
    autopct='%1.1f%%',
    startangle=90,
    counterclock=False,
    textprops={'fontsize': 12}
)
ax_pie.set_title('Fruit Distribution in Basket', fontsize=14)
ax_pie.axis('equal')

# 5) Draw the stacked bar chart
bar_x = 0
bar_width = 0.5

for pct, bottom, label in zip(age_percents, bottoms, age_groups):
    ax_bar.bar(
        bar_x,
        pct,
        bar_width,
        bottom=bottom,
        label=label
    )

ax_bar.set_xticks([bar_x])
ax_bar.set_xticklabels(['People Favoring Apples'], fontsize=12)
ax_bar.set_ylabel('Percentage (%)', fontsize=12)
ax_bar.set_title('Age Distribution of Apple Preferences', fontsize=14)
ax_bar.legend(title='Age Groups', loc='upper right', fontsize=10)
ax_bar.set_ylim(0, 100)

# 6) Connect the exploded “Apples” pie slice to the stacked bar
apple_wedge = wedges[0]
theta1, theta2 = apple_wedge.theta1, apple_wedge.theta2
center = apple_wedge.center
radius = apple_wedge.r
explode_dist = explode[0]

# Target y-positions on bar: bottom=0, top=100
bar_targets = [0, 100]

for angle, bar_y in zip((theta1, theta2), bar_targets):
    # Convert angle to radians
    rad = math.radians(angle)
    # Compute the point on the rim of the exploded slice
    pie_x = center[0] + (radius + explode_dist) * math.cos(rad)
    pie_y = center[1] + (radius + explode_dist) * math.sin(rad)

    # Draw a straight black line from pie to bar
    fig.annotate(
        '',
        xy=(pie_x, pie_y),
        xycoords=ax_pie.transData,
        xytext=(bar_x + bar_width / 2, bar_y),
        textcoords=ax_bar.transData,
        arrowprops=dict(arrowstyle='-', color='black', lw=1)
    )

# 7) Aesthetic tweaks
ax_bar.spines['top'].set_visible(False)
ax_bar.spines['right'].set_visible(False)

# 2) Save the figure
plt.savefig("novice.png")