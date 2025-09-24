import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Generate parameter values
t = np.linspace(0, 4 * np.pi + 0.1, 1000)

# Parametric equations
x = np.cos(t)
y = np.sin(2 * t)
z = np.cos(4 * t)

# Calculate indices for error bars (every 20th point in every 3-group cycle)
indices = np.arange(len(t))
condition = (indices % 20 == 0) & (
    ((indices // 20) % 3 == 0) | ((indices // 20) % 3 == 2)
)
error_indices = indices[condition]

# Create error values (0.3 for all directions)
error = 0.3
x_err = np.full(len(error_indices), error)
y_err = np.full(len(error_indices), error)
z_err = np.full(len(error_indices), error)

# Create figure and 3D axis
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Plot parametric curve
ax.plot(x, y, z, color='royalblue', linewidth=2, label='Parametric Curve')

# Add error bars
ax.errorbar(
    x[error_indices], y[error_indices], z[error_indices],
    xerr=x_err, yerr=y_err, zerr=z_err,
    fmt='o', color='crimson', ecolor='crimson',
    elinewidth=1.5, capsize=3, label='Error Bars'
)

# Configure plot appearance
ax.set_xlabel('X Axis', fontsize=12, labelpad=10)
ax.set_ylabel('Y Axis', fontsize=12, labelpad=10)
ax.set_zlabel('Z Axis', fontsize=12, labelpad=10)
ax.set_title('3D Parametric Curve with Error Bars', fontsize=14, pad=20)
ax.legend(loc='upper right', fontsize=10)

# Set viewing angle for better visualization
ax.view_init(elev=25, azim=-45)

# Save to file without displaying
plt.savefig('novice_final.png', dpi=100, bbox_inches='tight')