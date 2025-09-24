import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.lines import Line2D

# -----------------------------
# 1. Prepare the data
# -----------------------------
# Pie-chart data
fruit_labels = ['Apples', 'Oranges', 'Bananas']
fruit_sizes  = [35, 45, 20]          # percentages
explode      = [0.08, 0, 0]          # explode ONLY the apple slice

# Stacked-bar data (all percentages add to 100)
age_labels   = ['<18', '18-30', '30-50', '>50']
age_apples   = [25, 40, 20, 15]      # percentages
bar_colors   = ['#8dd3c7', '#ffffb3', '#bebada', '#fb8072']   # 4 distinct colours

# -----------------------------
# 2. Create the figure & axes
# -----------------------------
fig, (ax_pie, ax_bar) = plt.subplots(
    nrows=1, ncols=2,
    figsize=(10, 5),
    gridspec_kw={'wspace': 0.25}
)

# -----------------------------
# 3. Pie chart
# -----------------------------
wedges, texts, autotexts = ax_pie.pie(
    fruit_sizes,
    explode=explode,
    labels=fruit_labels,
    autopct='%1.0f%%',
    startangle=90,
    counterclock=False
)
ax_pie.set_title('Fruit in Basket')
ax_pie.axis('equal')  # keep the pie circular

# -----------------------------
# 4. Stacked bar chart
# -----------------------------
x_pos = 0          # single bar at x = 0
bottom = 0
for pct, lbl, color in zip(age_apples, age_labels, bar_colors):
    ax_bar.bar(
        x_pos,
        pct,
        bottom=bottom,
        color=color,
        edgecolor='black',
        label=lbl
    )
    bottom += pct   # update stacking baseline

# Cosmetic settings
ax_bar.set_ylim(0, 100)
ax_bar.set_xticks([x_pos])
ax_bar.set_xticklabels(['Apples'])
ax_bar.set_ylabel('Percentage of people')
ax_bar.set_title('Apple popularity by age group')
ax_bar.legend(title='Age groups', loc='upper right')

# -----------------------------
# 5. Connector lines
# -----------------------------
# 5.1 Anchor point on the exploded apple slice
apple_wedge = wedges[0]                         # first slice = Apples
theta1, theta2 = apple_wedge.theta1, apple_wedge.theta2
mean_theta = np.deg2rad((theta1 + theta2) / 2)  # mid-angle in radians

r = 1                # default pie radius used by matplotlib
offset = explode[0]  # explode distance for Apples slice

x_anchor = (r + offset) * np.cos(mean_theta)
y_anchor = (r + offset) * np.sin(mean_theta)

# 5.2 Two target points on the bar (bottom & top)
bar_x = x_pos
y_bottom = 0
y_top = 100

# 5.3 Helper to convert from Axes data coordinates -> Figure fraction
def axes_to_fig(ax, x, y):
    return fig.transFigure.inverted().transform(ax.transData.transform((x, y)))

pie_point_fig   = axes_to_fig(ax_pie, x_anchor, y_anchor)
bar_bottom_fig  = axes_to_fig(ax_bar, bar_x, y_bottom)
bar_top_fig     = axes_to_fig(ax_bar, bar_x, y_top)

# Draw the two lines directly on the figure
line_kwargs = dict(color='black', linewidth=1)
fig.lines.append(Line2D(
    [pie_point_fig[0], bar_bottom_fig[0]],
    [pie_point_fig[1], bar_bottom_fig[1]],
    **line_kwargs
))
fig.lines.append(Line2D(
    [pie_point_fig[0], bar_top_fig[0]],
    [pie_point_fig[1], bar_top_fig[1]],
    **line_kwargs
))

# -----------------------------
# 6. Layout & export
# -----------------------------
plt.tight_layout()
plt.savefig("novice.png")