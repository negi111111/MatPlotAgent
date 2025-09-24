import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import Normalize

# Set a fixed seed for reproducibility
np.random.seed(42)

# Define the number of bars
num_bars = 30

# Generate linearly spaced angles (theta) for bar positions between 0 and 2*pi
theta = np.linspace(0, 2 * np.pi, num_bars, endpoint=False)

# Generate random diameters (radii) for the bars
diameters = np.random.uniform(low=0.5, high=2.0, size=num_bars)

# Generate random thicknesses (widths) for the bars
widths = np.random.uniform(low=0.05, high=0.2, size=num_bars)

# Normalize the diameters for color mapping (dark to light)
norm = Normalize(vmin=min(diameters), vmax=max(diameters))
# Choose a colormap for the gradient (dark to light)
cmap = plt.get_cmap('Blues')

# Create a polar plot
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection='polar')

# Plot the bars
bars = ax.bar(theta, diameters, width=widths, color=cmap(norm(diameters)), alpha=0.5)

# Set a title for the plot
ax.set_title('Polar Bar Plot with 30 Bars', pad=20)

# Remove radial labels for cleaner visualization
ax.set_yticklabels([])

# Adjust layout to prevent clipping of the title
plt.tight_layout()

# Save the plot as a PNG file
plt.savefig("novice.png")