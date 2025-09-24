import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def rossler_attractor(a, b, c, initial_conditions, time):
    u, v, w = initial_conditions
    dt = time[1] - time[0]
    trajectory = []

    for t in time:
        trajectory.append((u, v, w))
        u_dot = -v - w
        v_dot = u + a * v
        w_dot = b + w * (u - c)
        u += u_dot * dt
        v += v_dot * dt
        w += w_dot * dt

    return np.array(trajectory)

# Parameters
a, b, c = 0.2, 0.2, 5.7
initial_conditions = (1.0, 1.0, 1.0)
time = np.linspace(0, 100, 10000)

# Generate trajectory
trajectory = rossler_attractor(a, b, c, initial_conditions, time)

# Create 3D plot
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')
ax.plot(trajectory[:, 0], trajectory[:, 1], trajectory[:, 2], linewidth=0.5, color='blue')
ax.set_xlabel('u', fontsize=12)
ax.set_ylabel('v', fontsize=12)
ax.set_zlabel('w', fontsize=12)
ax.set_title('Rossler Attractor', fontsize=14, pad=20)

# Adjust viewing angle for better visibility
ax.view_init(elev=30, azim=30)

# Add grid for better depth perception
ax.grid(True, linestyle='--', alpha=0.7)

# Set background color to white for better contrast
ax.set_facecolor('white')
fig.patch.set_facecolor('white')

# Save the plot
plt.savefig('novice_final.png', dpi=300, bbox_inches='tight')