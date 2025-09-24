import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt

# Step 1 & 2: Define the function
def f(z):
    return (z - 4) * (z - 6) * (z - 8) + 90

# Step 3 & 4: Generate data
z = np.linspace(0, 11, 400)
y = f(z)

# Step 5: Create the plot
fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(z, y, color='blue', linewidth=2)

# Step 6: Shaded region for the integral
mask = (z >= 3) & (z <= 10)
ax.fill_between(z[mask], y[mask], color='lightblue', alpha=0.5)

# Step 7: Text annotation in the middle of the shaded region
ax.text(
    6.5,
    f(6.5),
    r'$\displaystyle\int\bigl[(z-4)(z-6)(z-8)+90\bigr]\,dz$',
    horizontalalignment='center',
    fontsize=12
)

# Step 8: Axis limits and labels
ax.set_xlim(0, 11)
ax.set_ylim(bottom=0)
ax.set_xlabel('z-axis')
ax.set_ylabel('f(z)')

# Step 9: Customize ticks
ax.set_xticks([3, 10])
ax.set_xticklabels(['3', '10'])
ax.set_yticks([])  # Remove y-ticks

# Step 10: Hide top and right borders
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# Step 11: Save the plot
plt.savefig('novice_final.png', bbox_inches='tight')