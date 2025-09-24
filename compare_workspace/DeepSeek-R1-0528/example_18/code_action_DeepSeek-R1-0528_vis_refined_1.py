import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

# Create figure and axis with Aitoff projection
fig = plt.figure(figsize=(12, 6))
ax = fig.add_subplot(111, projection='aitoff')

# Set title
ax.set_title("Aitoff Projection with Geographic Square", pad=20)

# Define square coordinates in degrees
lon_deg = [-60, 60, 60, -60, -60]
lat_deg = [-60, -60, 60, 60, -60]

# Convert to radians for Aitoff projection
lon_rad = np.radians(lon_deg)
lat_rad = np.radians(lat_deg)

# Plot the geographic square
ax.plot(lon_rad, lat_rad, color='red', linewidth=2, label='Geographic Square')

# Configure grid and ticks
ax.grid(True, linestyle='--', alpha=0.7)
ax.set_xticks(np.radians(np.arange(-180, 181, 30)))
ax.set_yticks(np.radians(np.arange(-90, 91, 30)))

# Format tick labels as degrees
ax.xaxis.set_major_formatter(plt.FuncFormatter(
    lambda val, _: f"{int(np.degrees(val))}°"))
ax.yaxis.set_major_formatter(plt.FuncFormatter(
    lambda val, _: f"{int(np.degrees(val))}°"))

# Add legend
ax.legend(loc='lower right')

# Save as PNG without displaying
plt.savefig("novice_final.png", bbox_inches='tight', dpi=150)