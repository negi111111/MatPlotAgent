import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt

# Define the mathematical function
def f(z):
    return (z - 4) * (z - 6) * (z - 8) + 90

# Generate data points
x = np.linspace(0, 11, 400)
y = f(x)

# Initialize plot
fig, ax = plt.subplots(figsize=(8, 5))

# Plot the curve
ax.plot(x, y, color='blue', linewidth=2, linestyle='-')

# Shade the specified region
ax.fill_between(x, y, where=((x >= 3) & (x <= 10)), color='lightblue')

# Calculate text position and add integral notation
x_text = (3 + 10) / 2
y_text = (f(3) + f(10)) / 2
ax.text(x_text, y_text, r"$\int_{3}^{10} f(z)\,dz$", 
        horizontalalignment='center', verticalalignment='center',
        fontsize=14)

# Label axes
ax.set_xlabel('x', fontsize=12)
ax.set_ylabel('y', fontsize=12)

# Customize ticks and borders
ax.set_xticks([3, 10])
ax.set_yticks([])
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# Set axis limits
ax.set_xlim(0, 11)
ax.set_ylim(0, 200)

# Save the plot
plt.tight_layout()
plt.savefig("novice.png", dpi=100)