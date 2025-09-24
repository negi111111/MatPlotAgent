import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt

# ------------------------------------------------------------------
# Generate the data
# ------------------------------------------------------------------
x = np.arange(0.0, 10.0, 0.02)
y = np.sin(3 * np.pi * x)

# ------------------------------------------------------------------
# Create the figure and main axis
# ------------------------------------------------------------------
fig, ax = plt.subplots(figsize=(4, 4))

# Plot the sine curve
ax.plot(x, y, label='3π sine')

# ------------------------------------------------------------------
# Annotations
# ------------------------------------------------------------------
# 1. Mid-point annotation
ax.annotate(
    'midpoint (5, 0)',
    xy=(5, 0),
    xytext=(6, 1),
    arrowprops=dict(facecolor='black', shrink=0.05),
    fontsize=10,
    color='black'
)

# 2. Peak annotation (first positive peak)
peak_x = 1 / 6            # exact 0.1666…
peak_y = np.sin(3 * np.pi * peak_x)
ax.annotate(
    f'peak ({peak_x:.3f}, {peak_y:.1f})',
    xy=(peak_x, peak_y),
    xytext=(peak_x + 1, peak_y + 1),
    arrowprops=dict(facecolor='red', shrink=0.05),
    fontsize=10,
    color='red'
)

# 3. Specific data point annotation at x = 4
data_point_x = 4
data_point_y = np.sin(12 * np.pi)  # exactly 0
ax.annotate(
    f'data point (4, {data_point_y:.1f})',
    xy=(data_point_x, data_point_y),
    xytext=(data_point_x + 1, data_point_y - 1),
    arrowprops=dict(facecolor='green', shrink=0.05),
    fontsize=10,
    color='green'
)

# ------------------------------------------------------------------
# Axis limits
# ------------------------------------------------------------------
ax.set_xlim(-2, 10)
ax.set_ylim(-6, 6)

# ------------------------------------------------------------------
# Additional text
# ------------------------------------------------------------------
# Top-left on the axis
ax.text(
    0.05, 0.95, 'Sine Curve',
    transform=ax.transAxes,
    fontsize=12,
    verticalalignment='top'
)

# Bottom-right on the full figure
fig.text(
    0.95, 0.05, 'Created by PlotAgent',
    fontsize=10,
    horizontalalignment='right'
)

# ------------------------------------------------------------------
# Legend
# ------------------------------------------------------------------
ax.legend()

# ------------------------------------------------------------------
# Save exactly one PNG file
# ------------------------------------------------------------------
plt.savefig('novice_final.png')