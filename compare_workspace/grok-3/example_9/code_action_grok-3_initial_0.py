import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt

# Create x array from 0.0 to 10.0 with step 0.02
x = np.arange(0.0, 10.0, 0.02)

# Compute y as sin(3 * pi * x)
y = np.sin(3 * np.pi * x)

# Create a figure of size 4x4 inches
plt.figure(figsize=(4, 4))

# Plot the sine curve
plt.plot(x, y, color='blue', linewidth=1.5)

# Set axis limits
plt.xlim(-2, 10)
plt.ylim(-6, 6)

# Annotate the midpoint at x=5
mid_x = 5.0
mid_y = np.sin(3 * np.pi * mid_x)
plt.annotate(f'Midpoint (5, {mid_y:.2f})', 
             xy=(mid_x, mid_y), 
             xytext=(mid_x + 1, mid_y + 1), 
             arrowprops=dict(facecolor='black', shrink=0.05))

# Annotate the first peak of the sine curve
peak_x = 1/6  # First peak at x=1/6 for sin(3πx)
peak_y = np.sin(3 * np.pi * peak_x)  # Should be 1.0 (peak value)
plt.annotate(f'Peak ({peak_x:.2f}, {peak_y:.2f})', 
             xy=(peak_x, peak_y), 
             xytext=(peak_x + 1, peak_y + 1), 
             arrowprops=dict(facecolor='black', shrink=0.05))

# Annotate the data point at x=4
data_x = 4.0
data_y = np.sin(3 * np.pi * data_x)  # sin(12π)
plt.annotate('data point (4, sin(12π))', 
             xy=(data_x, data_y), 
             xytext=(data_x + 1, data_y - 1), 
             arrowprops=dict(facecolor='black', shrink=0.05))

# Add text 'Sine Curve' in top-left using axis coordinates
plt.text(-1.5, 5, 'Sine Curve', fontsize=12, color='red')

# Add text 'Created by PlotAgent' in bottom-right using figure coordinates
plt.figtext(0.95, 0.05, 'Created by PlotAgent', fontsize=10, color='gray', ha='right')

# Add grid for better readability
plt.grid(True, linestyle='--', alpha=0.7)

# Save the plot as a PNG file
plt.savefig("novice.png")