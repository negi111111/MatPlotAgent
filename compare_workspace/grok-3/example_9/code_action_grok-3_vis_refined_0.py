import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt

# Generate data
x = np.arange(0.0, 10.0, 0.02)
y = np.sin(3 * np.pi * x)

# Create figure
plt.figure(figsize=(4, 4))

# Plot the data
plt.plot(x, y, color='blue')

# Annotate midpoint
plt.annotate('Midpoint', xy=(5, 0), xytext=(6, 1),
             arrowprops=dict(facecolor='black', shrink=0.05))

# Annotate peak
plt.annotate('Peak', xy=(1/6, 1), xytext=(1, 1.5),
             arrowprops=dict(facecolor='black', shrink=0.05))

# Annotate specific data point
plt.annotate('data point (4, sin(12π))', xy=(4, np.sin(12 * np.pi)), xytext=(5, -1),
             arrowprops=dict(facecolor='black', shrink=0.05))

# Add text annotations
plt.text(0.05, 0.95, 'Sine Curve', transform=plt.gca().transAxes, fontsize=12, color='red')
plt.text(0.95, 0.05, 'Created by PlotAgent', transform=plt.gcf().transFigure, fontsize=10, ha='right')

# Set axis limits
plt.xlim(-2, 10)
plt.ylim(-6, 6)

# Save the plot
plt.savefig('novice_final.png')