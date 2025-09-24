import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

class GeographicProjection:
    def __init__(self, ax):
        self.ax = ax
        
    def setup_axes(self):
        pass  # Overridden in child class
        
    def set_limits(self, lon_min, lon_max, lat_min, lat_max):
        pass  # Not needed for global projection

class AitoffHammerProjection(GeographicProjection):
    def __init__(self, ax):
        super().__init__(ax)
        # Initialize Aitoff-Hammer projection
        self.map = Basemap(projection='aitoff', lon_0=0, ax=ax)
        
    def draw_map(self):
        # Render map features
        self.map.drawcoastlines(linewidth=0.5)
        self.map.drawcountries(linewidth=0.3)
        self.map.drawmapboundary(fill_color='aqua')
        self.map.fillcontinents(color='lightgreen', lake_color='aqua')
        
    def setup_axes(self):
        # Configure title and grid
        self.ax.set_title("Aitoff-Hammer Projection with Geographic Square", pad=20)
        # Draw grid lines and labels
        self.map.drawmeridians(range(-180, 181, 30), labels=[0,0,0,1], color='gray', linewidth=0.5)
        self.map.drawparallels(range(-90, 91, 30), labels=[1,0,0,0], color='gray', linewidth=0.5)

# Create figure and axis
fig, ax = plt.subplots(figsize=(12, 6))

# Initialize and draw the projection
projection = AitoffHammerProjection(ax)
projection.draw_map()

# Draw the geographic square
square_lon = [-60, 60, 60, -60, -60]
square_lat = [-60, -60, 60, 60, -60]
ax.plot(square_lon, square_lat, color='red', linewidth=2, label='Geographic Square')

# Configure axes and legend
projection.setup_axes()
ax.legend(loc='lower right')

# Save as PNG without displaying
plt.savefig("novice_final.png", bbox_inches='tight', dpi=150)