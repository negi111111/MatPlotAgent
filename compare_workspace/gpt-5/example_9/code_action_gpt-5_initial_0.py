import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# 1) Figure and axes
fig, ax = plt.subplots(figsize=(4, 4), dpi=100)

# 2) Data
x = arange(0.0, 10.0 + 1e-9, 0.02)
y = sin(3 * pi * x)

# 3) Plot line
ax.plot(x, y, color='C0', linewidth=1.8)

# 4) Axis limits
ax.set_xlim(-2, 10)
ax.set_ylim(-6, 6)

# 5) Midpoint
x_mid = 5.0
y_mid = sin(3 * pi * x_mid)  # equals 0.0

# 6) Peak (nearest to x=5)
k_peak = int(round((5.0 - (1.0 / 6.0)) * (3.0 / 2.0)))  # -> 7
x_peak = (1.0 / 6.0) + (2.0 * k_peak / 3.0)             # 29/6 ≈ 4.8333
y_peak = 1.0

# 7) Specific data point (4, sin(12pi))
x_pt = 4.0
y_pt = sin(12 * pi)  # equals 0.0

# 8) Annotations with arrows
ax.annotate(
    "Midpoint (x=5)",
    xy=(x_mid, y_mid),
    xytext=(x_mid + 0.7, y_mid + 3.0),
    textcoords='data',
    arrowprops={'arrowstyle': '->', 'color': 'black', 'linewidth': 1.2},
    ha='left', va='bottom'
)

ax.annotate(
    f"Peak (x={x_peak:.3f})",
    xy=(x_peak, y_peak),
    xytext=(x_peak + 0.7, y_peak - 3.0),
    textcoords='data',
    arrowprops={'arrowstyle': '->', 'color': 'black', 'linewidth': 1.2},
    ha='left', va='top'
)

ax.annotate(
    "data point (4, sin(12pi))",
    xy=(x_pt, y_pt),
    xytext=(x_pt + 0.6, y_pt - 3.5),
    textcoords='data',
    arrowprops={'arrowstyle': '->', 'color': 'black', 'linewidth': 1.2},
    ha='left', va='top'
)

# 9) Axis and figure text
ax.text(0.01, 0.99, "Sine Curve", transform=ax.transAxes, ha='left', va='top')
fig.text(0.99, 0.01, "Created by PlotAgent", transform=fig.transFigure, ha='right', va='bottom')

# 10) Layout and save
fig.tight_layout()
plt.savefig("novice.png")