import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt

# Set a fixed seed for reproducibility
np.random.seed(42)

# Generate data
num_bars = 30
theta = np.linspace(0, 2 * np.pi, num_bars, endpoint=False)  # Bar positions
diameters = np.random.rand(num_bars)  # Random diameters
thicknesses = np.linspace(0.1, 1.0, num_bars)  # Linearly spaced thicknesses

# Normalize diameters for color mapping
normalized_diameters = (diameters - np.min(diameters)) / (np.max(diameters) - np.min(diameters))
colors = plt.cm.Blues(normalized_diameters)  # Use a colormap for colors

# Create the polar bar plot
fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
bars = ax.bar(theta, diameters, width=thicknesses, color=colors, alpha=0.5)  # Set transparency to 0.5

# Enhance plot aesthetics
ax.set_title("Polar Bar Plot", va='bottom')
ax.set_xticks(theta)  # Set the ticks to the bar positions
ax.set_xticklabels([f'Bar {i+1}' for i in range(num_bars)])  # Label each bar

# Save the plot
plt.savefig("novice_final.png", bbox_inches='tight')  # Save the plot