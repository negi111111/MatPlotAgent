import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt

def f(z):
    return (z - 4) * (z - 6) * (z - 8) + 90

# Generate data
z = np.linspace(0, 11, 400)
y = f(z)

# Create plot
plt.plot(z, y, color='blue', linewidth=2)

# Shaded region between z=3 and z=10 down to y=0
plt.fill_between(z, y, where=(z >= 3) & (z <= 10), color='lightblue', alpha=0.5)

# Add integral text centered in the shaded area
plt.text(6.5, 100, r'$\int_{3}^{10} [(z - 4)(z - 6)(z - 8) + 90]dz$', fontsize=12, ha='center')

# Axis limits and labels
plt.xlim(0, 11)
plt.ylim(bottom=0)
plt.xlabel('z')
plt.ylabel('f(z)')

# Customize ticks
plt.xticks([3, 10], ['3', '10'])
plt.yticks([])

# Hide top and right spines
ax = plt.gca()
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# Save the plot
plt.savefig('novice_final.png', bbox_inches='tight')