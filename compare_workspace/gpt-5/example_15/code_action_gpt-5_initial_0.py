import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt

# 1-3) Data preparation
z = np.linspace(0, 11, 1000)  # x-domain from 0 to 11
y = (z - 4) * (z - 6) * (z - 8) + 90  # function definition

# 4) Figure and axes
fig, ax = plt.subplots(figsize=(8, 5))

# 5) Shaded region between 3 and 10
ax.axvspan(3, 10, color='lightblue', alpha=0.3, zorder=1)

# 6) Plot the function line
ax.plot(z, y, color='blue', linewidth=2, zorder=2)

# 7) Axis limits (y starts at 0)
ax.set_xlim(0, 11)
y_max = y.max()
ax.set_ylim(0, y_max * 1.15)

# 8) Integral text centered in the shaded region
x_center = (3 + 10) / 2
y_center = (ax.get_ylim()[0] + ax.get_ylim()[1]) / 2
ax.text(x_center, y_center, r"$\int_{3}^{10} [(z-4)(z-6)(z-8) + 90]\,dz$",
        ha='center', va='center', color='black', fontsize=12)

# 9) Axis labels
ax.set_xlabel('z')
ax.set_ylabel('f(z)')

# 10) X-ticks at 3 and 10 with labels
ax.set_xticks([3, 10])
ax.set_xticklabels(['3', '10'])

# 11) Remove y-ticks
ax.set_yticks([])

# 12) Hide top and right spines
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# 13) Render and save
plt.tight_layout()
plt.savefig("novice.png")