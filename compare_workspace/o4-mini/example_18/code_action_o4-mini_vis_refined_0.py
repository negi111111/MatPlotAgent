import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import FuncFormatter

class GeographicProjection:
    def __init__(self):
        # Create a figure with an Aitoff projection axis
        self.fig, self.ax = plt.subplots(subplot_kw={'projection': 'aitoff'})

    def setup_axes(self):
        # Set a title and enable the grid
        self.ax.set_title("Aitoff-Hammer Projection")
        self.ax.grid(True)

    def clear_axes(self):
        # Clear the axis contents
        self.ax.cla()

    def set_limits(self, lon_min, lon_max, lat_min, lat_max):
        # Aitoff uses radians internally, so convert degrees to radians
        lon_min_rad = np.radians(lon_min)
        lon_max_rad = np.radians(lon_max)
        lat_min_rad = np.radians(lat_min)
        lat_max_rad = np.radians(lat_max)
        self.ax.set_xlim(lon_min_rad, lon_max_rad)
        self.ax.set_ylim(lat_min_rad, lat_max_rad)

    def format_coordinates(self):
        # Define tick positions in radians but label in degrees
        lon_ticks = np.radians(np.arange(-180, 181, 30))
        lat_ticks = np.radians(np.arange(-90, 91, 30))
        self.ax.set_xticks(lon_ticks)
        self.ax.set_yticks(lat_ticks)
        # Formatter to append degree symbol
        self.ax.xaxis.set_major_formatter(FuncFormatter(lambda x, pos: f"{int(np.degrees(x))}°"))
        self.ax.yaxis.set_major_formatter(FuncFormatter(lambda y, pos: f"{int(np.degrees(y))}°"))

    def set_grids(self):
        # Draw gridlines
        self.ax.grid(True)

class AitoffHammerProjection(GeographicProjection):
    def __init__(self):
        super().__init__()
        self.setup_axes()

    def plot_square(self):
        # Define the square corners in degrees
        lon_deg = [-60,  60,  60, -60, -60]
        lat_deg = [ 60,  60, -60, -60,  60]
        # Convert to radians for plotting
        lon_rad = np.radians(lon_deg)
        lat_rad = np.radians(lat_deg)
        # Plot the square
        self.ax.plot(lon_rad, lat_rad, color='blue', linewidth=2)

# Instantiate and build the plot
projection = AitoffHammerProjection()
projection.set_limits(-60, 60, -60, 60)
projection.format_coordinates()
projection.set_grids()
projection.plot_square()

# Save the figure to a PNG file
plt.savefig("novice_final.png", bbox_inches='tight')