import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Generate parameter array
t = np.linspace(0, 4 * np.pi + 0.1, 1000)

# Parametric equations
x = np.cos(t)
y = np.sin(2 * t)
z = np.cos(4 * t)

# Identify error bar locations
indices = np.arange(len(t))
cond1 = (indices % 20 == 0)          # Every 20th point
cond2 = ((indices // 20) % 3 != 1)   # Exclude indices where (index//20) mod 3 is 1
selected_indices = indices[cond1 & cond2]

# Initialize plot
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Plot main curve
ax.plot(x, y, z, 'b-', alpha=0.6, linewidth=1.5)

# Add error bars
error = 0.3
for i in selected_indices:
    # X-error bar
    ax.plot([x[i] - error, x[i] + error], [y[i], y[i]], [z[i], z[i]], 
            'r-', linewidth=1.2, alpha=0.8)
    # Y-error bar
    ax.plot([x[i], x[i]], [y[i] - error, y[i] + error], [z[i], z[i]], 
            'r-', linewidth=1.2, alpha=0.8)
    # Z-error bar
    ax.plot([x[i], x[i]], [y[i], y[i]], [z[i] - error, z[i] + error], 
            'r-', linewidth=1.2, alpha=0.8)

# Label axes and set title
ax.set_xlabel('X Axis', fontsize=12, labelpad=10)
ax.set_ylabel('Y Axis', fontsize=12, labelpad=10)
ax.set_zlabel('Z Axis', fontsize=12, labelpad=10)
ax.set_title('3D Parametric Curve with Error Bars', fontsize=14, pad=20)

# Adjust layout and save
plt.tight_layout()
plt.savefig("novice.png", dpi=150, bbox_inches='tight')