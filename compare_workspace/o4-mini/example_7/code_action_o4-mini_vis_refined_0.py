import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt

# Step 1: Set a fixed seed for reproducibility
np.random.seed(42)

# Step 2: Generate 30 angles for the bars
num_bars = 30
angles = np.linspace(0, 2 * np.pi, num_bars, endpoint=False)

# Step 3: Generate random diameters and fixed thickness
diameters = np.random.rand(num_bars)  # Random diameters
thickness = 0.1  # Fixed thickness for all bars

# Step 4: Normalize diameters for color mapping
normalized = (diameters - diameters.min()) / (diameters.max() - diameters.min())

# Step 5: Map normalized diameters to colors using the 'viridis' colormap
colors = plt.cm.viridis(normalized)

# Step 6: Create the polar bar plot
fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
ax.bar(angles, diameters, width=thickness, color=colors, alpha=0.5)

# Step 7: Add a descriptive title
ax.set_title(
    "Reproducible Polar Bar Plot\n30 bars · random diameters · fixed thickness",
    va='bottom',
    fontsize=14
)

# Step 8: Save the figure to a PNG file
plt.savefig("novice_final.png", bbox_inches='tight')