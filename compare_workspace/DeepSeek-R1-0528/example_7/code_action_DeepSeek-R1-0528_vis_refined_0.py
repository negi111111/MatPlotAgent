import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt

# Set random seed for reproducibility
np.random.seed(42)

# Generate data for 30 bars
num_bars = 30
theta = np.linspace(0, 2 * np.pi, num_bars, endpoint=False)  # Angular positions
diameters = np.random.rand(num_bars)  # Random bar heights
thicknesses = np.random.rand(num_bars) * 0.1  # Random bar widths

# Normalize diameters for color mapping
normalized_diameters = (diameters - diameters.min()) / (diameters.max() - diameters.min())
colors = plt.cm.viridis(normalized_diameters)  # Create color gradient

# Create plot with polar projection
fig, ax = plt.subplots(figsize=(8, 8), subplot_kw={'projection': 'polar'})

# Plot bars with specified properties
ax.bar(theta, diameters, width=thicknesses, 
       color=colors, alpha=0.5, edgecolor='black', linewidth=0.5)

# Configure plot aesthetics
ax.set_title('Polar Bar Plot with Random Diameters and Thicknesses', 
             fontsize=14, pad=20)
ax.set_theta_zero_location('N')  # Set 0° at top
ax.set_theta_direction(-1)  # Clockwise orientation
ax.set_rlabel_position(0)  # Move radial labels to horizontal position
ax.grid(True, linestyle='--', alpha=0.7)  # Add grid lines

# Save as PNG without displaying
plt.savefig('novice_final.png', bbox_inches='tight', dpi=100)