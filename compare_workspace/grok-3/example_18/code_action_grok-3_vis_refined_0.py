import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

class GeographicProjection:
    def __init__(self):
        self.fig, self.ax = plt.subplots(figsize=(10, 5))
    
    def setup_axes(self):
        self.ax.set_title("Approximated Aitoff-Hammer Projection with Square Boundary")
        self.ax.set_xlabel("X (Projected)")
        self.ax.set_ylabel("Y (Projected)")
    
    def clear_axes(self):
        self.ax.cla()
    
    def set_limits(self, xlim, ylim):
        self.ax.set_xlim(xlim)
        self.ax.set_ylim(ylim)
    
    def format_coordinates(self):
        # Placeholder for coordinate formatting
        pass
    
    def set_grids(self):
        self.ax.grid(True, linestyle='--', alpha=0.5, color='gray')

class AitoffHammerProjection(GeographicProjection):
    def __init__(self):
        super().__init__()
        self.setup_axes()
    
    def transform(self, lon, lat):
        # Aitoff-Hammer projection transformation
        # Convert longitude and latitude to radians if not already
        lon = np.array(lon)
        lat = np.array(lat)
        
        # Compute the parameter alpha
        alpha = np.arccos(np.cos(lat) * np.cos(lon / 2))
        # Avoid division by zero or invalid values
        mask = alpha != 0
        x = np.zeros_like(lon)
        y = np.zeros_like(lat)
        x[mask] = (2 * np.cos(lat[mask]) * np.sin(lon[mask] / 2)) / np.sin(alpha[mask])
        y[mask] = np.sin(lat[mask]) / np.sin(alpha[mask])
        # Scale the coordinates for better visualization
        x *= 180 / np.pi
        y *= 90 / np.pi
        return x, y

# Create the plot
projection = AitoffHammerProjection()
lon = [-60, 60, 60, -60, -60]  # Longitude points for the square
lat = [60, 60, -60, -60, 60]    # Latitude points for the square

# Transform the coordinates
x, y = projection.transform(np.radians(lon), np.radians(lat))

# Plot the square boundary
projection.ax.plot(x, y, color='red', label='Square Boundary (±60° Lat/Lon)', linewidth=2)

# Add annotations for the corners
for i, (xi, yi, loni, lati) in enumerate(zip(x[:-1], y[:-1], lon[:-1], lat[:-1])):
    projection.ax.annotate(f'({loni}°, {lati}°)', (xi, yi), textcoords="offset points", xytext=(0, 5), ha='center', fontsize=8)

# Set background color for better aesthetics
projection.ax.set_facecolor('lightblue')

# Add legend and set limits
projection.ax.legend()
projection.set_limits([-150, 150], [-75, 75])
projection.set_grids()

# Save the plot to a PNG file
plt.savefig("novice_final.png", bbox_inches='tight')