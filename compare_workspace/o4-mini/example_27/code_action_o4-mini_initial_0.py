import matplotlib
matplotlib.use('Agg')
import numpy as np
    import matplotlib.pyplot as plt
    from mpl_toolkits.mplot3d import Axes3D
num_points = 100
    x = np.linspace(0.0, 4.0 * np.pi, num=num_points)
offset = np.pi / 4.0
y1 = np.sin(x) - offset
    y2 = np.cos(x) - offset
fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111, projection='3d')
# color and marker settings for the first series
    stem_color1 = 'tab:blue'
    marker_style1 = 'o'
    for xi, yi in zip(x, y1):
        ax.plot([xi, xi],     # x coordinates of the two ends of the stem
                [0.0, 0.0],   # y coordinates (constant at 0)
                [0.0, yi],    # z coordinates from 0 up to yi
                color=stem_color1,
                linewidth=1.5)
    # scatter markers at the top of each stem
    ax.scatter(x, 
               np.zeros_like(x), 
               y1,
               color=stem_color1,
               marker=marker_style1,
               s=30,
               label='sin(x) – π/4')
stem_color2 = 'tab:red'
    marker_style2 = '^'
    for xi, yi in zip(x, y2):
        ax.plot([xi, xi],        # x coordinates
                [1.0, 1.0],      # y coordinates (constant at 1)
                [0.0, yi],       # z coordinates up to yi
                color=stem_color2,
                linewidth=1.5)
    ax.scatter(x, 
               np.ones_like(x), 
               y2,
               color=stem_color2,
               marker=marker_style2,
               s=30,
               label='cos(x) – π/4')
ax.set_xlabel('x')
    ax.set_ylabel('Series index (0=sin, 1=cos)')
    ax.set_zlabel('Value')
    ax.set_title('3D Stem Plot of sin(x) – π/4 and cos(x) – π/4')
    ax.legend(loc='upper right')
plt.tight_layout()
    import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# 1. Prepare the data
num_points = 100
x = np.linspace(0.0, 4.0 * np.pi, num=num_points)
offset = np.pi / 4.0
y1 = np.sin(x) - offset
y2 = np.cos(x) - offset

# 2. Create a 3D plot
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')

# 3. Plot first stem series (sin)
stem_color1 = 'tab:blue'
marker_style1 = 'o'
for xi, yi in zip(x, y1):
    ax.plot([xi, xi], [0.0, 0.0], [0.0, yi],
            color=stem_color1, linewidth=1.5)
ax.scatter(x, np.zeros_like(x), y1,
           color=stem_color1, marker=marker_style1,
           s=30, label='sin(x) – π/4')

# 4. Plot second stem series (cos)
stem_color2 = 'tab:red'
marker_style2 = '^'
for xi, yi in zip(x, y2):
    ax.plot([xi, xi], [1.0, 1.0], [0.0, yi],
            color=stem_color2, linewidth=1.5)
ax.scatter(x, np.ones_like(x), y2,
           color=stem_color2, marker=marker_style2,
           s=30, label='cos(x) – π/4')

# 5. Annotate and show
ax.set_xlabel('x')
ax.set_ylabel('Series index (0=sin, 1=cos)')
ax.set_zlabel('Value')
ax.set_title('3D Stem Plot of sin(x) – π/4 and cos(x) – π/4')
ax.legend(loc='upper right')

plt.tight_layout()

plt.savefig('novice.png')
