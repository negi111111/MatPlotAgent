import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Ellipse, Polygon
from matplotlib.gridspec import GridSpec

# Data for bar plots
categories = ['A', 'B', 'C']
values = [4, 6, 2]

# Create figure with GridSpec layout
fig = plt.figure(figsize=(10, 10))
gs = GridSpec(3, 2, figure=fig)

# First row: bar plots
ax1 = fig.add_subplot(gs[0, 0])
ax1.bar(categories, values, hatch='//', color='lightblue')
ax1.set_title('Hatch: //')

ax2 = fig.add_subplot(gs[0, 1])
ax2.bar(categories, values, hatch='\\', color='lightgreen')
ax2.set_title('Hatch: \\')

# Second row: bar plots
ax3 = fig.add_subplot(gs[1, 0])
ax3.bar(categories, values, hatch='||', color='lightcoral')
ax3.set_title('Hatch: ||')

ax4 = fig.add_subplot(gs[1, 1])
ax4.bar(categories, values, hatch='--', color='lightgoldenrodyellow')
ax4.set_title('Hatch: --')

# Third row: cosine wave with shapes (spans both columns)
ax5 = fig.add_subplot(gs[2, :])
x = np.linspace(0, 2 * np.pi, 100)
y = np.cos(x)
ax5.fill_between(x, y, color='magenta', alpha=0.5, hatch='x')
ax5.plot(x, y, color='black')
ax5.set_title('Cosine with Shapes')
ax5.set_xlim(0, 2 * np.pi)
ax5.set_ylim(-1.5, 1.5)

# Add geometric shapes
ellipse = Ellipse((np.pi, 0), width=2, height=1, 
                  edgecolor='black', facecolor='yellow', hatch='//')
ax5.add_patch(ellipse)

polygon = Polygon([[3, 0.5], [3.5, 1], [4, 0.5], [3.5, 0]], 
                 closed=True, color='blue', hatch='*')
ax5.add_patch(polygon)

# Set aspect ratio for cosine plot
ax5.set_aspect('equal', adjustable='box')

# Save and close
plt.tight_layout()
plt.savefig("novice_final.png")
plt.close()