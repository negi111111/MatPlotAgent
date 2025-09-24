import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt

# Define the polynomial function
def f(z):
    return (z - 4) * (z - 6) * (z - 8) + 90

# Generate data points
z = np.linspace(0, 11, 400)
y = f(z)

# Create figure and axis
fig, ax = plt.subplots(figsize=(8, 5))

# Plot the function
ax.plot(z, y, color='blue', linewidth=2)

# Shade the region under the curve between z=3 and z=10
ax.fill_between(z, y, where=(z >= 3) & (z <= 10), 
                color='lightblue', alpha=0.5)

# Add integral notation at the center of the shaded region
ax.text(6.5, f(6.5) + 5, r'$\int_{3}^{10} f(z) \, dz$', 
        fontsize=14, ha='center', color='darkblue')

# Set axis limits and labels
ax.set_xlim(0, 11)
ax.set_ylim(bottom=0)
ax.set_xlabel('z', fontsize=12)
ax.set_ylabel('f(z)', fontsize=12)

# Configure ticks and spines
ax.set_xticks([3, 10])
ax.set_xticklabels(['3', '10'], fontsize=10)
ax.set_yticks([])
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# Save as PNG without displaying
plt.savefig('novice_final.png', bbox_inches='tight', dpi=100)