import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt

def f(z):
    return (z - 4) * (z - 6) * (z - 8) + 90

# Generate data
z = np.linspace(0, 11, 400)
y = f(z)

# Create figure and axis
fig, ax = plt.subplots(figsize=(8, 5))

# Plot the function
ax.plot(z, y, color='blue', linewidth=2)

# Shade region between z=3 and z=10
ax.axvspan(3, 10, color='#add8e6', alpha=0.3)

# Axis limits
ax.set_xlim(0, 11)
ax.set_ylim(bottom=0)

# Labels
ax.set_xlabel('z')
ax.set_ylabel('f(z)')

# Customize ticks
ax.set_xticks([3, 10])
ax.set_xticklabels(['3', '10'])
ax.set_yticks([])

# Hide top and right spines
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# Add integral annotation
x_text = (3 + 10) / 2
y_text = 0.5 * max(y)
integral_str = r'$\displaystyle \int_{3}^{10}\bigl((z-4)(z-6)(z-8)+90\bigr)\,dz$'
ax.text(x_text, y_text, integral_str, fontsize=14, ha='center', va='center')

# Finalize and save
plt.tight_layout()
plt.savefig("novice.png")