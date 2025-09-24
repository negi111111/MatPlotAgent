import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt

# Create figure with specified size
plt.figure(figsize=(4, 4))

# Generate data
x = np.arange(0.0, 10.0, 0.02)
y = np.sin(3 * np.pi * x)

# Plot sine wave
plt.plot(x, y, color='blue')

# Add annotations with arrows
plt.annotate('Midpoint', 
             xy=(5, np.sin(15 * np.pi)), 
             xytext=(5, 1),
             arrowprops=dict(facecolor='black', shrink=0.05))

plt.annotate('Peak', 
             xy=(1, np.sin(3 * np.pi)), 
             xytext=(1, 1.5),
             arrowprops=dict(facecolor='black', shrink=0.05))

plt.annotate('data point (4, sin(12π))', 
             xy=(4, np.sin(12 * np.pi)), 
             xytext=(4.5, np.sin(12 * np.pi) + 0.5),
             arrowprops=dict(facecolor='black', shrink=0.05))

# Set axis limits
plt.xlim(-2, 10)
plt.ylim(-6, 6)

# Add text annotations
plt.text(0.05, 0.95, 'Sine Curve', 
         transform=plt.gca().transAxes,
         fontsize=12, 
         verticalalignment='top')

plt.text(0.95, 0.05, 'Created by PlotAgent', 
         transform=plt.gcf().transFigure,
         fontsize=10, 
         horizontalalignment='right')

# Save to file without displaying
plt.savefig('novice_final.png')