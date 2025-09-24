import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse, Polygon

# Create mosaic layout (3 rows, 2 columns with bottom row spanning both)
fig, axs = plt.subplot_mosaic(
    [['bar1', 'bar2'],
     ['bar3', 'bar4'],
     ['cosine', 'cosine']],
    figsize=(10, 12),
    constrained_layout=True
)

# Sample data for bar plots
categories = ['A', 'B', 'C']
values = [4, 6, 2]

# Top-left bar plot (diagonal hatch)
axs['bar1'].bar(categories, values, hatch='//', 
                color='skyblue', edgecolor='black')
axs['bar1'].set_title('Hatch: //', fontweight='bold')

# Top-right bar plot (back-diagonal hatch)
axs['bar2'].bar(categories, values, hatch='\\\\', 
                color='lightgreen', edgecolor='black')
axs['bar2'].set_title('Hatch: \\\\', fontweight='bold')

# Bottom-left bar plot (vertical hatch)
axs['bar3'].bar(categories, values, hatch='||', 
                color='salmon', edgecolor='black')
axs['bar3'].set_title('Hatch: ||', fontweight='bold')

# Bottom-right bar plot (horizontal hatch)
axs['bar4'].bar(categories, values, hatch='--', 
                color='gold', edgecolor='black')
axs['bar4'].set_title('Hatch: --', fontweight='bold')

# Cosine plot with shapes
x = np.linspace(0, 2 * np.pi, 500)
y = np.cos(x)
axs['cosine'].fill_between(x, y, 0, 
                           color='magenta', alpha=0.3, 
                           hatch='xx', edgecolor='purple')

# Add ellipse at (π, 0)
ellipse = Ellipse((np.pi, 0), width=2, height=0.5,
                  facecolor='yellow', hatch='++', 
                  edgecolor='brown', alpha=0.7)
axs['cosine'].add_patch(ellipse)

# Add triangle at (π, 0.5)
triangle_verts = [(np.pi, 0.7), (np.pi - 0.5, 0.3), (np.pi + 0.5, 0.3)]
polygon = Polygon(triangle_verts, closed=True,
                  facecolor='cyan', hatch='*', 
                  edgecolor='darkblue', alpha=0.7)
axs['cosine'].add_patch(polygon)

# Configure cosine plot
axs['cosine'].set_aspect('equal')
axs['cosine'].set_xlim(0, 2 * np.pi)
axs['cosine'].set_ylim(-1.2, 1.2)
axs['cosine'].set_title('Cosine with Shapes', fontweight='bold')
axs['cosine'].grid(True, linestyle='--', alpha=0.6)

# Save as PNG without displaying
plt.savefig("novice.png", dpi=120)