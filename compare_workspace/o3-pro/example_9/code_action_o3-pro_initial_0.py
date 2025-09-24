import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt

# 1. Prepare the data
x = np.arange(0.0, 10.0, 0.02)        # x from 0 (inclusive) to 10 (exclusive)
y = np.sin(3 * np.pi * x)             # 3π–frequency sine curve

# 2. Create the figure and axes
fig, ax = plt.subplots(figsize=(4, 4))

# 3. Plot the sine curve
ax.plot(x, y, color='steelblue', linewidth=1.5, label='3π sine')

# 4. Annotate the midpoint (x = 5)
y_mid = np.sin(3 * np.pi * 5)         # equals 0
ax.annotate(
    'midpoint (5, 0)',
    xy=(5, y_mid),                    # point to annotate
    xytext=(5, 3),                    # label position
    textcoords='data',
    arrowprops=dict(arrowstyle='->', color='black'),
    ha='center', va='bottom'
)

# 5. Annotate the first peak (x = 1/6, y = 1)
x_peak = 1/6
y_peak = 1.0
ax.annotate(
    f'peak ({x_peak:.3g}, 1)',
    xy=(x_peak, y_peak),
    xytext=(1.5, 4),                  # label position
    textcoords='data',
    arrowprops=dict(arrowstyle='->', color='red'),
    color='red',
    ha='left', va='bottom'
)

# 6. Annotate the point (4, sin(12π)) which is (4, 0)
y_dp = 0
ax.annotate(
    'data point (4, sin(12π))',
    xy=(4, y_dp),
    xytext=(6, -3),                   # label position
    textcoords='data',
    arrowprops=dict(arrowstyle='->', color='green'),
    color='green',
    ha='left', va='center'
)

# 7. Add static text labels
ax.text(
    0.02, 0.95, 'Sine Curve',
    transform=ax.transAxes,
    fontsize=10, fontweight='bold',
    ha='left', va='top'
)
fig.text(
    0.98, 0.02, 'Created by PlotAgent',
    transform=fig.transFigure,
    ha='right', va='bottom',
    fontsize=8, color='gray'
)

# 8. Configure axes limits, grid, legend
ax.set_xlim(-2, 10)
ax.set_ylim(-6, 6)
ax.grid(True, linestyle=':')
ax.legend(loc='upper right')

# 9. Save the figure
plt.savefig("novice.png", dpi=300, bbox_inches='tight')