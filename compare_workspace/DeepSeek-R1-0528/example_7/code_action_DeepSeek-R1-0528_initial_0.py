import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt

# Set random seed for reproducibility
np.random.seed(42)

# Generate data
n_bars = 30
theta = np.linspace(0, 2 * np.pi, n_bars, endpoint=False)  # Angular positions
diameters = np.random.rand(n_bars)                         # Radial lengths
thicknesses = np.random.uniform(0.1, 0.3, n_bars)          # Angular widths

# Normalize diameters for color mapping
norm = plt.Normalize(diameters.min(), diameters.max())
colors = plt.cm.viridis(norm(diameters))  # Dark to light colormap

# Create polar plot
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection='polar')

# Plot bars with specified properties
bars = ax.bar(
    x=theta,
    height=diameters,
    width=thicknesses,
    color=colors,
    alpha=0.5,
    edgecolor='black',
    linewidth=0.7
)

# Configure plot appearance
ax.set_theta_zero_location('N')  # Set 0° at top
ax.set_theta_direction(-1)       # Clockwise direction
ax.set_rlabel_position(22.5)     # Radial labels at 22.5°
ax.grid(True, linestyle='--', alpha=0.7)
plt.title('Polar Bar Plot with Random Diameters and Thicknesses', pad=20)

# Save as PNG without displaying
plt.savefig("novice.png")