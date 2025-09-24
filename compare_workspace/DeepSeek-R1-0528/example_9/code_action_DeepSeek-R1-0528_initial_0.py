import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt

# Generate data
x = np.arange(0.0, 10.01, 0.02)  # Include 10.0 via 10.01
y = np.sin(3 * np.pi * x)

# Initialize figure
fig, ax = plt.subplots(figsize=(4, 4))

# Plot the sine curve
ax.plot(x, y, color='blue', linewidth=1.5)

# Set axis limits
ax.set_xlim(-2, 10)
ax.set_ylim(-6, 6)

# Annotate midpoint (x=5)
ax.annotate('Midpoint', 
            xy=(5, 0), 
            xytext=(5, 2), 
            arrowprops=dict(arrowstyle='->', color='black', linewidth=0.8),
            ha='center', 
            va='bottom')

# Annotate peak (first maximum at x=1/6)
peak_x = 1/6
peak_y = 1.0
ax.annotate('Peak', 
            xy=(peak_x, peak_y), 
            xytext=(peak_x, 2), 
            arrowprops=dict(arrowstyle='->', color='black', linewidth=0.8),
            ha='center', 
            va='bottom')

# Annotate data point (4, sin(12π))
ax.annotate('data point (4, sin(12π))', 
            xy=(4, 0), 
            xytext=(4, -2), 
            arrowprops=dict(arrowstyle='->', color='black', linewidth=0.8),
            ha='center', 
            va='top')

# Add "Sine Curve" label in top-left (axis coordinates)
ax.text(0.02, 0.98, 'Sine Curve', 
        transform=ax.transAxes, 
        ha='left', 
        va='top', 
        fontsize=10,
        bbox=dict(facecolor='white', alpha=0.8, edgecolor='none', pad=2))

# Add "Created by PlotAgent" in bottom-right (figure coordinates)
fig.text(0.98, 0.02, 'Created by PlotAgent', 
         ha='right', 
         va='bottom', 
         fontsize=8,
         bbox=dict(facecolor='white', alpha=0.8, edgecolor='none', pad=2))

# Adjust layout and save
plt.tight_layout()
plt.savefig("novice.png", dpi=150)