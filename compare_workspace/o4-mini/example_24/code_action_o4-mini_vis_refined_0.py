import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def rossler_attractor(a, b, c, initial_conditions, total_time, dt=0.01):
    """
    Compute the Rossler attractor trajectory.
    a, b, c: parameters of the Rossler system
    initial_conditions: tuple (u0, v0, w0)
    total_time: total integration time
    dt: integration time step
    Returns: numpy array of shape (N, 3) with (u, v, w) trajectory
    """
    num_steps = int(total_time / dt)
    u, v, w = initial_conditions
    trajectory = np.empty((num_steps, 3))
    for i in range(num_steps):
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
total_time = 100.0

# Compute trajectory
trajectory = rossler_attractor(a, b, c, initial_conditions, total_time)

# Create 3D plot
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')
ax.plot(
    trajectory[:, 0],
    trajectory[:, 1],
    trajectory[:, 2],
    linewidth=0.5,
    color='blue'
)

# Labels and title
ax.set_xlabel('u')
ax.set_ylabel('v')
ax.set_zlabel('w')
ax.set_title('Rossler Attractor')

# Grid for better readability
ax.grid(True)

# Equal aspect ratio
# Available in Matplotlib >= 3.3
try:
    ax.set_box_aspect([1, 1, 1])
except AttributeError:
    pass  # Older Matplotlib: skip equal aspect setting

# Save the figure to a PNG file
plt.savefig("novice_final.png", dpi=300)