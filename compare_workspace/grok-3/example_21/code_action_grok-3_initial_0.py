import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define the range for the parameter t (from 0 to 4*pi + 0.1)
t = np.linspace(0, 4 * np.pi + 0.1, 1000)

# Calculate x, y, z coordinates of the parametric curve
x = np.cos(t)
y = np.sin(2 * t)
z = np.cos(4 * t)

# Create a boolean mask for indices where error bars should be added
indices = np.arange(len(t))
condition1 = (indices % 20 == 0)  # Every 20th index
condition2 = ((indices // 20) % 3 == 0) | ((indices // 20) % 3 == 2)  # Secondary condition
error_bar_mask = condition1 & condition2  # Combine both conditions

# Extract the points for error bars
x_err = x[error_bar_mask]
y_err = y[error_bar_mask]
z_err = z[error_bar_mask]

# Define the error value (0.3) for x, y, z dimensions
error_val = 0.3
xerr = np.full_like(x_err, error_val)
yerr = np.full_like(y_err, error_val)
zerr = np.full_like(z_err, error_val)

# Create a 3D plot
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Plot the parametric curve
ax.plot(x, y, z, label='Parametric Curve', color='blue')

# Plot error bars at selected points
ax.errorbar(x_err, y_err, z_err, xerr=xerr, yerr=yerr, zerr=zerr, fmt='o', color='red', label='Error Bars')

# Set axis labels
ax.set_xlabel('X label')
ax.set_ylabel('Y label')
ax.set_zlabel('Z label')

# Add a legend
ax.legend()

# Save the plot as a PNG file
plt.savefig("novice.png")
plt.close()