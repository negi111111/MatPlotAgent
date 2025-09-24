import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt

def f(z):
    return (z - 4) * (z - 6) * (z - 8) + 90

# Generate x values and compute y values
z = np.linspace(0, 11, 400)
y = f(z)

# Create the plot
plt.figure(figsize=(10, 6))
plt.plot(z, y, color='blue', linewidth=2)

# Shade the region between x=3 and x=10
plt.fill_between(z, y, where=(z >= 3) & (z <= 10), color='lightblue', alpha=0.5)

# Add integral formula text in the shaded region
plt.text(
    6.5, 
    f(6.5), 
    r'$\displaystyle \int \bigl((z - 4)(z - 6)(z - 8) + 90\bigr)\,dz$', 
    horizontalalignment='center', 
    fontsize=12
)

# Axis limits and labels
plt.xlim(0, 11)
plt.ylim(bottom=0)
plt.xlabel('z-axis')
plt.ylabel('f(z)')

# Customize ticks
plt.xticks([3, 10], ['3', '10'])
plt.yticks([])

# Hide top and right spines
ax = plt.gca()
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# Save the figure
plt.savefig('novice_final.png', bbox_inches='tight')