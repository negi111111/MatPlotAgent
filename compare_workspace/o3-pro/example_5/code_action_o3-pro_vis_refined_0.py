import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import ConnectionPatch, Patch

# -------------------------
# Data Preparation
# -------------------------
# Pie chart data
fruits = ['Apples', 'Oranges', 'Bananas']
sizes = [35, 45, 20]
explode = (0.1, 0.0, 0.0)  # “explode” the Apples slice

# Stacked-bar (here: single-series clustered bar) data
age_groups = ['<18', '18-30', '30-50', '>50']
people_distribution = [25, 40, 20, 15]
bar_colors = ['lightgreen', 'lightblue', 'lightyellow', 'lightcoral']

# -------------------------
# Figure & Axes
# -------------------------
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

# -------------------------
# Pie Chart
# -------------------------
wedges, texts, autotexts = ax1.pie(
    sizes,
    explode=explode,
    labels=fruits,
    autopct='%1.1f%%',
    startangle=90
)
ax1.axis('equal')  # Draw the pie as a circle.
ax1.set_title('Fruit in Basket')

# -------------------------
# Bar Chart
# -------------------------
# Explicit x-positions ensure consistency for the connection lines
x_pos = np.arange(len(age_groups))
bars = ax2.bar(x_pos, people_distribution, color=bar_colors, width=0.6)

ax2.set_xticks(x_pos)
ax2.set_xticklabels(age_groups)
ax2.set_ylabel('Percentage of people')
ax2.set_title('Apple popularity by age group')

# Custom legend so each colour corresponds to its age group entry
legend_handles = [Patch(facecolor=c, label=l) for c, l in zip(bar_colors, age_groups)]
ax2.legend(handles=legend_handles, title='Age groups', loc='upper right')

# -------------------------
# Connecting Lines
# -------------------------
# Compute the centre of the exploded “Apples” slice.
# Matplotlib returns theta1/theta2 in the wedge object itself.
apple_wedge = wedges[0]  # first slice is Apples
theta_deg = (apple_wedge.theta1 + apple_wedge.theta2) / 2.0
theta_rad = np.deg2rad(theta_deg)

# The radius of the pie is 1 by default; incorporate explode offset.
r = apple_wedge.r + explode[0]
xA = r * np.cos(theta_rad)
yA = r * np.sin(theta_rad)

# Coordinates on the bar chart: connect to the top of the first bar (<18 group)
xB = x_pos[0]
yB_top = people_distribution[0]

# Add two connection patches for a visual “fork”
con1 = ConnectionPatch(
    xyA=(xA, yA), coordsA="data",
    xyB=(xB, yB_top), coordsB="data",
    axesA=ax1, axesB=ax2,
    color='black', linewidth=1
)
con2 = ConnectionPatch(
    xyA=(xA, yA), coordsA="data",
    xyB=(xB, 0), coordsB="data",
    axesA=ax1, axesB=ax2,
    color='black', linewidth=1
)
fig.add_artist(con1)
fig.add_artist(con2)

# -------------------------
# Layout & Save
# -------------------------
plt.tight_layout()
plt.savefig('novice_final.png')  # exactly one PNG as required