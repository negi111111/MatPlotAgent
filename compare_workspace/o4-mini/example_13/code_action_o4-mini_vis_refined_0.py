import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Ellipse, Polygon

# Data for the bar plots
x = np.arange(5)
data = [5, 7, 3, 6, 4]

# Create figure and axes with a 3x2 grid; third row is twice as tall
fig, axs = plt.subplots(
    3, 2,
    figsize=(10, 8),
    gridspec_kw={'height_ratios': [1, 1, 2]}
)

# Row 1, Column 1: hatch '/'
axs[0, 0].bar(x, data, hatch='/', color='lightblue', edgecolor='black')
axs[0, 0].set_title('Row 1: hatch "/"')

# Row 1, Column 2: hatch '\'
axs[0, 1].bar(x, data, hatch='\\', color='lightgreen', edgecolor='black')
axs[0, 1].set_title('Row 1: hatch "\\"')

# Row 2, Column 1: hatch 'x'
axs[1, 0].bar(x, data, hatch='x', color='salmon', edgecolor='black')
axs[1, 0].set_title('Row 2: hatch "x"')

# Row 2, Column 2: hatch 'o'
axs[1, 1].bar(x, data, hatch='o', color='yellow', edgecolor='black')
axs[1, 1].set_title('Row 2: hatch "o"')

# Third row: filled cosine curve with patches
x_cos = np.linspace(0, 4 * np.pi, 200)
y_cos = np.cos(x_cos)

ax3 = axs[2, 0]
# Fill between x-axis and cosine curve
poly = ax3.fill_between(
    x_cos, y_cos, 0,
    facecolor='magenta',
    alpha=0.5
)
# Add hatch and edge color to the filled area
poly.set_hatch('/')
poly.set_edgecolor('black')

# Set limits and title
ax3.set_xlim(0, 4 * np.pi)
ax3.set_ylim(-1.5, 1.5)
ax3.set_title('Row 3: filled cosine + patches')
ax3.set_aspect('auto')

# Add an ellipse centered at (2π, 0)
ellipse = Ellipse(
    xy=(2 * np.pi, 0),
    width=1.0,
    height=0.5,
    edgecolor='blue',
    facecolor='none',
    hatch='\\'
)
ax3.add_patch(ellipse)

# Add a small polygon
polygon = Polygon(
    [[2.5, 0.5], [2.7, 0.8], [2.9, 0.5]],
    closed=True,
    facecolor='cyan',
    edgecolor='black',
    hatch='x'
)
ax3.add_patch(polygon)

# Remove the unused subplot in the third row, second column
fig.delaxes(axs[2, 1])

# Adjust layout and save to PNG
plt.tight_layout()
plt.savefig("novice_final.png")