import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # Ensures 3D projection is registered

def rossler_attractor(a, b, c, initial_conditions, time):
    x, y, z = initial_conditions
    dt = 0.01
    trajectory = []

    steps = int(time / dt)
    for _ in range(steps):
        dx = -y - z
        dy = x + a * y
        dz = b + z * (x - c)
        x += dx * dt
        y += dy * dt
        z += dz * dt
        trajectory.append((x, y, z))

    return np.array(trajectory)

# Parameters
a, b, c = 0.2, 0.2, 5.7
initial_conditions = (1.0, 1.0, 1.0)
time = 100  # Total time for the simulation

# Generate trajectory
trajectory = rossler_attractor(a, b, c, initial_conditions, time)

# Create 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(trajectory[:, 0], trajectory[:, 1], trajectory[:, 2], linewidth=0.5)

# Customize plot
ax.set_title("Rossler Attractor")
ax.set_xlabel('u')
ax.set_ylabel('v')
ax.set_zlabel('w')

# Save the plot
plt.savefig("novice_final.png")