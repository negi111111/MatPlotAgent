import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

# Define a function to approximate Aitoff-Hammer projection transformation
def aitoff_hammer_transform(lon, lat):
    """
    Approximate Aitoff-Hammer projection transformation.
    Converts longitude and latitude to x, y coordinates.
    Parameters:
    - lon: longitude in degrees
    - lat: latitude in degrees
    Returns:
    - x, y: transformed coordinates for plotting
    """
    # Convert degrees to radians
    lon_rad = np.radians(lon)
    lat_rad = np.radians(lat)
    
    # Aitoff-Hammer formulas (simplified)
    alpha = np.arccos(np.cos(lat_rad) * np.cos(lon_rad / 2))
    x = 2 * np.cos(lat_rad) * np.sin(lon_rad / 2) / np.sinc(alpha / np.pi)
    y = np.sin(lat_rad) / np.sinc(alpha / np.pi)
    
    # Scale for visualization
    x = x * 180 / np.pi
    y = y * 180 / np.pi
    
    return x, y

# Define the corners of the square in longitude and latitude (±60°)
lon_corners = [-60, 60, 60, -60, -60]  # Close the loop
lat_corners = [-60, -60, 60, 60, -60]  # Close the loop for a square

# Transform coordinates to Aitoff-Hammer projection space
x, y = aitoff_hammer_transform(np.array(lon_corners), np.array(lat_corners))

# Create the plot
fig, ax = plt.subplots(figsize=(10, 6))

# Plot the square boundary
ax.plot(x, y, color='red', linewidth=2, label='Square Boundary (±60° Lat/Lon)')

# Add grid lines for longitude and latitude (approximated)
lon_grid = np.arange(-180, 181, 30)
lat_grid = np.arange(-90, 91, 30)

# Plot longitude grid lines (meridians)
for lon in lon_grid:
    lon_arr = np.full(50, lon)
    lat_arr = np.linspace(-90, 90, 50)
    x_grid, y_grid = aitoff_hammer_transform(lon_arr, lat_arr)
    ax.plot(x_grid, y_grid, color='gray', linestyle='--', alpha=0.5)

# Plot latitude grid lines (parallels)
for lat in lat_grid:
    lat_arr = np.full(50, lat)
    lon_arr = np.linspace(-180, 180, 50)
    x_grid, y_grid = aitoff_hammer_transform(lon_arr, lat_arr)
    ax.plot(x_grid, y_grid, color='gray', linestyle='--', alpha=0.5)

# Set plot attributes
ax.set_title('Approximated Aitoff-Hammer Projection with Square Boundary', pad=20, size=12)
ax.set_xlabel('X (Projected)')
ax.set_ylabel('Y (Projected)')
ax.legend()
ax.grid(False)  # Disable default grid to use custom grid lines
ax.set_aspect('equal')  # Maintain aspect ratio for projection-like appearance

# Save the plot as a PNG file
plt.savefig("novice.png", dpi=300, bbox_inches='tight')
plt.close()