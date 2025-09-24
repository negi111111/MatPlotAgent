import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # Ensures 3D projection is registered

# Define the parameter array
t = np.linspace(0, 4 * np.pi + 0.1, 1000)  # 1000 points for smoothness

# Define the parametric equations
x = np.cos(t)
y = np.sin(2 * t)
z = np.cos(4 * t)

# Calculate error bars
error = 0.3
i = np.arange(len(t))
groups = np.floor(i / 20).astype(int)
condition = ((i % 20 == 0) & (groups % 3 == 0)) | (groups % 3 == 2)
indices = np.where(condition)[0]

# Extract error bar data
x_error = x[indices]
y_error = y[indices]
z_error = z[indices]

# Create the 3D plot
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')
ax.plot(x, y, z, label='Parametric Curve', color='blue', linewidth=1.5)

# Add error bars using Matplotlib primitives (scatter + line segments in x, y, z)
ax.scatter(x_error, y_error, z_error, marker='o', s=20, color='red', label='Error Bars')
for xe, ye, ze in zip(x_error, y_error, z_error):
    # x-direction error bar
    ax.plot([xe - error, xe + error], [ye, ye], [ze, ze], color='red', linewidth=0.8, alpha=0.8)
    # y-direction error bar
    ax.plot([xe, xe], [ye - error, ye + error], [ze, ze], color='red', linewidth=0.8, alpha=0.8)
    # z-direction error bar
    ax.plot([xe, xe], [ye, ye], [ze - error, ze + error], color='red', linewidth=0.8, alpha=0.8)

# Label the axes
ax.set_xlabel('X label')
ax.set_ylabel('Y label')
ax.set_zlabel('Z label')

# Display the legend
ax.legend()

# Save the plot
plt.tight_layout()
plt.savefig('novice_final.png')