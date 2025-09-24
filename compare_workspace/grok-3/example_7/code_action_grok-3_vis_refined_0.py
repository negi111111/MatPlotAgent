import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt

# Set a fixed seed for reproducibility
np.random.seed(42)

# Generate 30 angles for the bars
num_bars = 30
angles = np.linspace(0, 2 * np.pi, num_bars, endpoint=False)

# Generate diameters and thicknesses
diameters = np.linspace(0.1, 1.0, num_bars)  # Linearly spaced diameters
thicknesses = np.random.rand(num_bars) * 0.5  # Random thicknesses

# Normalize diameters for color mapping
normalized_diameters = (diameters - np.min(diameters)) / (np.max(diameters) - np.min(diameters))
colors = plt.cm.Blues(normalized_diameters)  # Use a blue color map for gradient effect

# Create the polar bar plot
fig, ax = plt.subplots(figsize=(8, 8), subplot_kw={'projection': 'polar'})
bars = ax.bar(angles, diameters, width=thicknesses, color=colors, alpha=0.5)

# Add a title for clarity
ax.set_title('Polar Bar Plot with 30 Bars', va='bottom')

# Save the plot as a PNG file
plt.savefig('novice_final.png', bbox_inches='tight')