import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt

# Define the range of x-values (from 0 to 11) with a small step size for smooth plotting
z = np.linspace(0, 11, 500)

# Compute y-values based on the given equation: (z - 4) * (z - 6) * (z - 8) + 90
y = (z - 4) * (z - 6) * (z - 8) + 90

# Create the plot with a blue line of thickness 2
plt.plot(z, y, color='blue', linewidth=2)

# Add a shaded region between x=3 and x=10 with light blue color
plt.fill_between(z, y, where=(z >= 3) & (z <= 10), color='lightblue', alpha=0.5)

# Add text at the center of the shaded region (approximate x=6.5, y=100 for visibility)
plt.text(6.5, 100, r'$\int (z-4)(z-6)(z-8) + 90 \, dz$', fontsize=12, ha='center')

# Set the x-axis range from 0 to 11
plt.xlim(0, 11)

# Set the y-axis to start from 0
plt.ylim(bottom=0)

# Add labels for x and y axes
plt.xlabel('z')
plt.ylabel('y')

# Set x-ticks at 3 and 10 with corresponding labels
plt.xticks([3, 10], ['3', '10'])

# Remove y-ticks
plt.yticks([])

# Hide the top and right borders of the subplot
ax = plt.gca()  # Get the current axis
ax.spines['top'].set_visible(False)  # Hide top border
ax.spines['right'].set_visible(False)  # Hide right border

# Save the plot as a PNG file
plt.savefig("novice.png")