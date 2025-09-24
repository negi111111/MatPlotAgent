import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt

# 1. Data generation
x = np.linspace(0, 11, 500)
y = (x - 4) * (x - 6) * (x - 8) + 90

# 2. Figure / axes setup
fig, ax = plt.subplots(figsize=(8, 4.5))

# 3. Plot the curve
ax.plot(x, y, color='blue', linewidth=2)

# 4. Shade the region from x = 3 to x = 10
ax.axvspan(3, 10, facecolor='lightblue', alpha=0.4)

# 5. Axis limits and labels
ax.set_xlim(0, 11)
ax.set_ylim(0, y.max() * 1.05)
ax.set_xlabel('x')
ax.set_ylabel('y')

# 6. Custom ticks
ax.set_xticks([3, 10])
ax.set_xticklabels(['3', '10'])
ax.set_yticks([])

# 7. Hide top and right spines
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# 8. Integral annotation
ax.text(
    6.5,
    0.5 * y.max(),
    r'$\displaystyle \int_{3}^{10} [(z-4)(z-6)(z-8)+90]\;dz$',
    ha='center',
    va='center',
    fontsize=12,
    color='navy'
)

# 9. Layout adjustment and save
fig.tight_layout()
plt.savefig("novice.png")