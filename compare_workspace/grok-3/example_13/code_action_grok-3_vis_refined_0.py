import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

# Create data for bar plots
x = np.arange(1, 6)
data = [5, 6, 2, 4, 7]

# Set up the figure
fig = plt.figure(figsize=(10, 8))

# First row of bar plots
ax1 = plt.subplot(231)
ax1.bar(x, data, color='blue', hatch='/')
ax1.set_title('Bar Plot 1 (Hatch: /)')

ax2 = plt.subplot(232)
ax2.bar(x, data, color='blue', hatch='\\')
ax2.set_title('Bar Plot 2 (Hatch: \\)')

ax3 = plt.subplot(233)
ax3.bar(x, data, color='green', hatch='*')
ax3.set_title('Bar Plot 3 (Hatch: *)')

# Second row of bar plots
ax4 = plt.subplot(234)
ax4.bar(x, data, color='green', hatch='o')
ax4.set_title('Bar Plot 4 (Hatch: o)')

# Final section for cosine curve spanning two columns
ax5 = plt.subplot(235, colspan=2)
x_cos = np.linspace(-2 * np.pi, 2 * np.pi, 100)
y_cos = np.cos(x_cos)
ax5.fill_between(x_cos, y_cos, color='magenta', alpha=0.5, hatch='//')
ax5.plot(x_cos, y_cos, color='black')
ax5.set_title('Cosine Curve with Filled Area')
ax5.set_xlim(-2 * np.pi, 2 * np.pi)
ax5.set_ylim(-1.5, 1.5)

# Add ellipse and polygon to cosine plot
from matplotlib.patches import Ellipse, Polygon

ellipse = Ellipse(xy=(0, 0), width=2, height=1, edgecolor='yellow', facecolor='none', hatch='\\')
ax5.add_patch(ellipse)

polygon = Polygon([[1, 0], [0, 1], [-1, 0], [0, -1]], closed=True, edgecolor='red', facecolor='none', hatch='*')
ax5.add_patch(polygon)

# Adjust aspect ratio for cosine plot
ax5.set_aspect('equal', adjustable='box')

# Adjust layout and save the plot
plt.tight_layout()
plt.savefig("novice_final.png")