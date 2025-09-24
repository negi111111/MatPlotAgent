import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt

# 1. Prepare data
x = np.arange(0.0, 10.0 + 0.02, 0.02)
y = np.sin(3 * np.pi * x)

# 2. Create figure and axes
fig, ax = plt.subplots(figsize=(4, 4))

# 3. Plot the sine curve
ax.plot(x, y, color='blue', linewidth=2)

# 4. Midpoint annotation
mid_x = 5.0
mid_y = np.sin(3 * np.pi * mid_x)
ax.annotate(
    'Midpoint (5, 0)',
    xy=(mid_x, mid_y),
    xytext=(mid_x + 1, mid_y + 2),
    arrowprops={'arrowstyle': '->', 'color': 'black'}
)

# 5. Peak annotation
idx_peak = np.argmax(y)
peak_x = x[idx_peak]
peak_y = y[idx_peak]
ax.annotate(
    f'Peak ({peak_x:.2f}, {peak_y:.0f})',
    xy=(peak_x, peak_y),
    xytext=(peak_x - 2, peak_y + 1.5),
    arrowprops={'arrowstyle': '->', 'color': 'black'}
)

# 6. Specific data point annotation
data_x = 4.0
data_y = np.sin(12 * np.pi)
ax.annotate(
    'data point (4, sin(12π))',
    xy=(data_x, data_y),
    xytext=(data_x, data_y - 1),
    arrowprops={'arrowstyle': '->', 'color': 'black'}
)

# 7. Static text labels
ax.text(0.02, 0.98, 'Sine Curve', transform=ax.transAxes, ha='left', va='top')
fig.text(0.95, 0.05, 'Created by PlotAgent', ha='right', va='bottom')

# 8. Axis limits
ax.set_xlim(-2, 10)
ax.set_ylim(-6, 6)

# 9. Save the figure
plt.savefig("novice.png")