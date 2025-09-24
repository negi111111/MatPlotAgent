import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # Ensures 3D toolkit is registered

# Create the parameter array t
t = np.arange(0.0, 4 * np.pi + 0.1, 0.05)

# Define the parametric curve coordinates
x = np.cos(t)
y = np.sin(2 * t)
z = np.cos(4 * t)

# Set up the 3D figure and axes
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')

# Plot the 3D parametric curve
ax.plot(x, y, z, color='C0', linewidth=2)

# Determine the indices where error bars will be drawn
idx = np.arange(t.size)
mask = (idx % 20 == 0) & (((idx // 20) % 3 == 0) | ((idx // 20) % 3 == 2))
selected_idx = idx[mask]

# Draw 3D error bars at the selected points
err = 0.3
for i in selected_idx:
    xi, yi, zi = x[i], y[i], z[i]
    # X-axis error bar segment
    ax.plot([xi - err, xi + err], [yi, yi], [zi, zi], color='red', linewidth=1)
    # Y-axis error bar segment
    ax.plot([xi, xi], [yi - err, yi + err], [zi, zi], color='red', linewidth=1)
    # Z-axis error bar segment
    ax.plot([xi, xi], [yi, yi], [zi - err, zi + err], color='red', linewidth=1)

# Optional: mark the points where error bars are drawn
ax.scatter(x[selected_idx], y[selected_idx], z[selected_idx], color='red', s=15)

# Label the axes
ax.set_xlabel("X label")
ax.set_ylabel("Y label")
ax.set_zlabel("Z label")

# Save the plot to a PNG file
plt.tight_layout()
plt.savefig("novice.png")