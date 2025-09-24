import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse, Polygon

# 1) Import libraries done above

# 2) Create the subplot mosaic with constrained layout
fig = plt.figure(figsize=(10, 10), constrained_layout=True)
axd = fig.subplot_mosaic([
    ['A', 'B'],
    ['C', 'D'],
    ['E', 'E'],
])

# 3) Prepare bar chart data
categories = ['Cat 1', 'Cat 2', 'Cat 3', 'Cat 4']
x = np.arange(len(categories))
heights = np.array([5, 3, 7, 2])
bar_width = 0.7
bar_color = 'skyblue'
edge_color = 'black'

# 4) Plot bar charts in the first two rows with different hatch patterns
axA = axd['A']
axA.bar(x, heights, width=bar_width, color=bar_color, edgecolor=edge_color, hatch='///', linewidth=1.0)
axA.set_title('Row 1 - Bars (hatch="///")')
axA.set_xticks(x)
axA.set_xticklabels(categories)

axB = axd['B']
axB.bar(x, heights, width=bar_width, color=bar_color, edgecolor=edge_color, hatch='\\\\', linewidth=1.0)
axB.set_title('Row 1 - Bars (hatch="\\\\")')
axB.set_xticks(x)
axB.set_xticklabels(categories)

axC = axd['C']
axC.bar(x, heights, width=bar_width, color=bar_color, edgecolor=edge_color, hatch='xx', linewidth=1.0)
axC.set_title('Row 2 - Bars (hatch="xx")')
axC.set_xticks(x)
axC.set_xticklabels(categories)

axD = axd['D']
axD.bar(x, heights, width=bar_width, color=bar_color, edgecolor=edge_color, hatch='++', linewidth=1.0)
axD.set_title('Row 2 - Bars (hatch="++")')
axD.set_xticks(x)
axD.set_xticklabels(categories)

# 5) Prepare cosine data for the filled area
x_line = np.linspace(0, 2 * np.pi, 500)
y_cos = np.cos(x_line)

# 6) Plot the filled area in axis 'E'
axE = axd['E']
axE.fill_between(
    x_line,
    y_cos,   # y1
    0,       # y2 baseline
    facecolor='magenta',
    edgecolor='black',
    hatch='..',
    alpha=0.5,
    linewidth=1.0,
    zorder=1
)

# 7) Add an Ellipse and a Polygon centered in axis 'E'
axE.set_xlim(0, 2 * np.pi)
axE.set_ylim(-1.5, 1.5)

xmin, xmax = axE.get_xlim()
ymin, ymax = axE.get_ylim()
cx = 0.5 * (xmin + xmax)
cy = 0.5 * (ymin + ymax)

ellipse = Ellipse(
    xy=(cx, cy),
    width=1.5,
    height=0.6,
    angle=0.0,
    facecolor='yellow',
    edgecolor='black',
    hatch='oo',
    alpha=0.4,
    linewidth=1.0,
    zorder=3
)
axE.add_patch(ellipse)

poly_points = np.array([
    (cx,       cy + 0.5),
    (cx + 0.5, cy),
    (cx,       cy - 0.5),
    (cx - 0.5, cy),
])
polygon = Polygon(
    poly_points,
    closed=True,
    facecolor='cyan',
    edgecolor='black',
    hatch='xx',
    alpha=0.4,
    linewidth=1.0,
    zorder=4
)
axE.add_patch(polygon)

# 8) Adjust aspect ratio and limits for axis 'E'
axE.set_aspect('equal', adjustable='box')
axE.set_title('Filled area under cos(x) with Ellipse and Polygon')

# 9) Save the plot to a PNG file
plt.savefig("novice.png")