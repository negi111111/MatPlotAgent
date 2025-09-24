import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt

# Create data
x = np.arange(0.0, 10.0, 0.02)
y = np.sin(3 * np.pi * x)

# Set up the figure
plt.figure(figsize=(4, 4))

# Plot the data
plt.plot(x, y, label='Sine Curve')

# Annotate the midpoint
midpoint_x = 5
midpoint_y = np.sin(3 * np.pi * midpoint_x)
plt.annotate('Midpoint', xy=(midpoint_x, midpoint_y), xytext=(midpoint_x + 1, midpoint_y + 0.5),
             arrowprops=dict(facecolor='black', shrink=0.05))

# Annotate the peak
peak_x = 1/6
peak_y = np.sin(3 * np.pi * peak_x)
plt.annotate('Peak', xy=(peak_x, peak_y), xytext=(peak_x + 1, peak_y + 0.5),
             arrowprops=dict(facecolor='black', shrink=0.05))

# Annotate specific data point
data_point_x = 4
data_point_y = np.sin(12 * np.pi)
plt.plot(data_point_x, data_point_y, 'ro')  # Mark the data point
plt.annotate('data point (4, sin(12pi))', xy=(data_point_x, data_point_y), 
             xytext=(data_point_x + 1, data_point_y + 0.5),
             arrowprops=dict(facecolor='black', shrink=0.05))

# Add text annotations
plt.text(0.05, 0.95, 'Sine Curve', transform=plt.gca().transAxes, fontsize=12, verticalalignment='top')
plt.text(0.95, 0.05, 'Created by PlotAgent', transform=plt.gcf().transFigure, fontsize=10, horizontalalignment='right')

# Set axis limits
plt.xlim(-2, 10)
plt.ylim(-6, 6)

# Add a legend
plt.legend()

# Save the plot
plt.savefig('novice_final.png')