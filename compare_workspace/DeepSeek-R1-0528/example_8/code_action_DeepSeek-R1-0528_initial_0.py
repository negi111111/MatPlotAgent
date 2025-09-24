import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import hsv_to_rgb

# Set random seed for reproducibility
np.random.seed(42)

# Generate 200 random points
n_points = 200
r = np.random.rand(n_points)          # Radial distances [0, 1)
theta = 2 * np.pi * np.random.rand(n_points)  # Angles [0, 2π)

# Calculate point areas (proportional to r²)
areas = (r ** 2) * 200  # Scaled for visibility

# Create HSV colors: Hue = normalized angle, Saturation=1, Value=1
hue = theta / (2 * np.pi)  # Normalize to [0, 1)
saturation = np.ones_like(hue)
value = np.ones_like(hue)
hsv_colors = np.column_stack((hue, saturation, value))
rgb_colors = hsv_to_rgb(hsv_colors)  # Convert to RGB

# Create polar plot
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection='polar')

# Scatter plot with computed properties
ax.scatter(
    theta, 
    r, 
    c=rgb_colors,
    s=areas,
    alpha=0.7,
    edgecolors='none'
)

# Adjust plot settings
ax.set_ylim(0, 1)  # Radial axis limit
ax.set_title("Polar Scatter: Color=Angle, Area∝Radius²", fontsize=14, pad=20)

# Save plot as PNG
plt.savefig("novice.png")