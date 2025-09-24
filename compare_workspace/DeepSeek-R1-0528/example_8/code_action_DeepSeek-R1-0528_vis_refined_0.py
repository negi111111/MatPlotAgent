import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors as mcolors

# Set fixed seed for reproducibility
np.random.seed(42)

# Generate 200 random points
num_points = 200
r = np.random.rand(num_points)  # Radial distances [0, 1)
theta = np.random.rand(num_points) * 2 * np.pi  # Angles [0, 2π)

# Calculate point areas (proportional to r²)
area = r**2 * 1000  # Scaled for visibility

# Convert angles to HSV colors (hue = normalized angle)
hue = theta / (2 * np.pi)
saturation = np.ones(num_points)
value = np.ones(num_points)
hsv_colors = np.column_stack((hue, saturation, value))
rgb_colors = mcolors.hsv_to_rgb(hsv_colors)

# Create polar plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='polar')
scatter = ax.scatter(
    theta, 
    r, 
    # Visual properties
    s=area, 
    c=rgb_colors, 
    # Styling
    alpha=0.75, 
    edgecolor='white',
    linewidth=0.5
)

# Configure plot appearance
ax.set_title("Polar Scatter: Color=Angle, Area∝Radius²", pad=20)
ax.grid(True, linestyle='--', alpha=0.7)
ax.set_theta_zero_location('N')
ax.set_theta_direction(-1)

# Save as PNG without displaying
plt.savefig("novice_final.png", bbox_inches='tight', dpi=100)