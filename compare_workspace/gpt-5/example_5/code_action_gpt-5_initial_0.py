import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import ConnectionPatch
from matplotlib.ticker import PercentFormatter

# Data preparation
fruit_labels = ['Apples', 'Oranges', 'Bananas']
fruit_sizes = np.array([0.35, 0.45, 0.20])  # fractions for the pie chart
fruit_colors = ['#d62728', '#ff7f0e', '#2ca02c']  # red/orange/green
explode = [0.10, 0.0, 0.0]  # separate the apples slice

age_labels = ['Under 18', '18-30', '30-50', 'Over 50']
age_shares = np.array([0.25, 0.40, 0.20, 0.15])  # fractions for stacked bar
age_colors = ['#9ecae1', '#6baed6', '#3182bd', '#08519c']  # blues

# Figure and axes
fig, (ax_pie, ax_bar) = plt.subplots(
    1, 2, figsize=(11, 5),
    gridspec_kw={'width_ratios': [1.0, 1.1]},
    constrained_layout=False
)
fig.subplots_adjust(wspace=0.30)

# Pie chart
wedges, texts, autotexts = ax_pie.pie(
    fruit_sizes,
    explode=explode,
    labels=fruit_labels,
    colors=fruit_colors,
    startangle=90,        # start at 12 o'clock
    counterclock=False,   # clockwise
    autopct='%1.0f%%',
    pctdistance=0.75,
    labeldistance=1.05,
    wedgeprops={'linewidth': 1, 'edgecolor': 'white'}
)
ax_pie.set_title('Fruit Distribution in Basket', pad=12)
ax_pie.axis('equal')  # keep the pie circular

# Compute anchor point on exploded apples slice (first wedge)
w_apples = wedges[0]
mid_angle_deg = 0.5 * (w_apples.theta1 + w_apples.theta2)
theta = np.deg2rad(mid_angle_deg)
r = w_apples.r
cx, cy = w_apples.center
xA = cx + r * np.cos(theta)
yA = cy + r * np.sin(theta)

# Stacked bar chart (single bar representing apples)
x_center = 0.0
bar_width = 0.6
bottom = 0.0
for share, label, color in zip(age_shares, age_labels, age_colors):
    ax_bar.bar(
        x_center,          # x position
        share,             # height of the segment
        width=bar_width,   # bar width
        bottom=bottom,     # start position of this segment
        color=color,       # segment color
        edgecolor='white', # separator lines between segments
        linewidth=1,
        label=label        # for legend
    )
    bottom += share

# Bar axis formatting
ax_bar.set_xlim(-0.8, 0.8)
ax_bar.set_xticks([x_center])
ax_bar.set_xticklabels(['Apples'])
ax_bar.set_ylim(0.0, 1.0)
ax_bar.yaxis.set_major_formatter(PercentFormatter(1.0))
ax_bar.set_ylabel('Percentage of Apple Lovers')
ax_bar.set_title('Apple Preference by Age Group', pad=12)
ax_bar.legend(title='Age Group', loc='upper right', frameon=False)

# Connection lines from apples slice to the bottom and top of the bar
cp_bottom = ConnectionPatch(
    xyA=(xA, yA), coordsA=ax_pie.transData,   # point on apples slice
    xyB=(x_center, 0.0), coordsB=ax_bar.transData,  # bottom of stacked bar
    color='black', linewidth=1
)
cp_top = ConnectionPatch(
    xyA=(xA, yA), coordsA=ax_pie.transData,   # same slice point
    xyB=(x_center, 1.0), coordsB=ax_bar.transData,  # top of stacked bar
    color='black', linewidth=1
)
fig.add_artist(cp_bottom)
fig.add_artist(cp_top)

# Save to file
plt.savefig("novice.png", dpi=300, bbox_inches='tight')