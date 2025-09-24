import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def rossler_attractor(a, b, c, initial_conditions, time):
    u, v, w = initial_conditions
    dt = 0.01
    steps = int(time / dt)
    trajectory = np.zeros((steps, 3))
    
    for i in range(steps):
        u_dot = -v - w
        v_dot = u + a * v
        w_dot = b + w * (u - c)
        u += u_dot * dt
        v += v_dot * dt
        w += w_dot * dt
        trajectory[i] = (u, v, w)
        
    return trajectory

# Parameters and initial conditions
a, b, c = 0.2, 0.2, 5.7
initial_conditions = (1.0, 1.0, 1.0)
time = 100
trajectory = rossler_attractor(a, b, c, initial_conditions, time)

# Create 3D plot with custom styling
fig = plt.figure(figsize=(10, 8), dpi=100)
ax = fig.add_subplot(111, projection='3d')

# Plot trajectory with thin line and custom color
ax.plot(trajectory[:, 0], trajectory[:, 1], trajectory[:, 2], 
        color='#1f77b4',  # Matplotlib default blue
        linewidth=0.5,
        alpha=0.8)

# Set labels and title with font adjustments
ax.set_title("Rossler Attractor", fontsize=16, pad=20)
ax.set_xlabel('u', fontsize=12, labelpad=10)
ax.set_ylabel('v', fontsize=12, labelpad=10)
ax.set_zlabel('w', fontsize=12, labelpad=10)

# Customize grid and background
ax.xaxis.pane.fill = False
ax.yaxis.pane.fill = False
ax.zaxis.pane.fill = False
ax.grid(True, linestyle='--', alpha=0.6)
ax.set_facecolor('white')

# Adjust viewing angle for better visualization
ax.view_init(elev=30, azim=-60)

# Save figure without displaying
plt.tight_layout()
plt.savefig("novice_final.png", bbox_inches='tight')