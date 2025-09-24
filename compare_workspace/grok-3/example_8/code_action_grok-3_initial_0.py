import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt
import colorsys

# Set random seed for reproducibility
np.random.seed(42)

# Generate random data for 200 points
n_points = 200
r = np.random.uniform(low=0, high=1, size=n_points)  # Radial distance between 0 and 1
theta = np.random.uniform(low=0, high=2 * np.pi, size=n_points)  # Angle between 0 and 2pi

# Calculate point sizes proportional to the square of radial distance
sizes = 1000 * r**2  # Scale factor 1000 for visibility

# Generate colors based on angle (theta) using HSV color space
colors = []
for angle in theta:
    hue = angle / (2 * np.pi)  # Normalize angle to 0-1 range for hue
    saturation = 1.0  # Full saturation
    value = 1.0  # Full brightness
    rgb = colorsys.hsv_to_rgb(hue, saturation, value)  # Convert HSV to RGB
    colors.append(rgb)

# Create a polar scatter plot
fig, ax = plt.subplots(subplot_kw={'projection': 'polar'}, figsize=(8, 8))
scatter = ax.scatter(theta, r, s=sizes, c=colors, alpha=0.6)

# Customize the plot
ax.set_title('Polar Scatter Plot with Random Points', pad=20, fontsize=12, fontweight='bold')
ax.set_rlim(0, 1)  # Set radial limits from 0 to 1

# Save the plot as a PNG file
plt.savefig("novice.png", dpi=300, bbox_inches='tight')
plt.close()