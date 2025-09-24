import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Ellipse, Polygon

# Data for bar plots
categories = ['Cat 1', 'Cat 2', 'Cat 3', 'Cat 4']
values = [5, 3, 7, 2]

# Set up subplots
fig, axs = plt.subplots(3, 2, figsize=(10, 10), gridspec_kw={'height_ratios': [1, 1, 2]})

# First row of bar plots with different hatch patterns
axs[0, 0].bar(categories, values, hatch='//', color='lightblue', edgecolor='black')
axs[0, 0].set_title('Row 1 - Bars (hatch="//")')

axs[0, 1].bar(categories, values, hatch='\\', color='lightblue', edgecolor='black')
axs[0, 1].set_title('Row 1 - Bars (hatch="\\")')

# Second row of bar plots with different hatch patterns
axs[1, 0].bar(categories, values, hatch='xx', color='lightblue', edgecolor='black')
axs[1, 0].set_title('Row 2 - Bars (hatch="xx")')

axs[1, 1].bar(categories, values, hatch='++', color='lightblue', edgecolor='black')
axs[1, 1].set_title('Row 2 - Bars (hatch="++")')

# Third row: filled area under cosine curve with hatch pattern
x = np.linspace(0, 2 * np.pi, 400)
y = np.cos(x)

# Create a hatched polygon to emulate hatch within filled area under the curve
vertices = list(zip(x, y)) + list(zip(x[::-1], np.zeros_like(x)))
filled_area = Polygon(vertices, closed=True, facecolor='magenta', edgecolor='black', hatch='/', alpha=0.5)
axs[2, 0].add_patch(filled_area)

axs[2, 0].set_title('Filled area under cos(x) with Ellipse and Polygon')
axs[2, 0].set_xlim(0, 2 * np.pi)
axs[2, 0].set_ylim(-1.5, 1.5)

# Add Ellipse and Polygon in the third subplot
ellipse = Ellipse(xy=(np.pi, 0), width=1, height=0.5, edgecolor='black', facecolor='yellow', hatch='x')
axs[2, 0].add_patch(ellipse)

polygon = Polygon([[np.pi - 0.5, 0.5], [np.pi + 0.5, 0.5], [np.pi, 1]],
                  closed=True, edgecolor='black', facecolor='cyan', hatch='.')
axs[2, 0].add_patch(polygon)

# Adjust aspect ratio
axs[2, 0].set_aspect('equal', adjustable='box')

# Remove the unused subplot in the third row
fig.delaxes(axs[2, 1])

# Layout and save
plt.tight_layout()
plt.savefig("novice_final.png")