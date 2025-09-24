import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

class GeographicProjection:
    def __init__(self):
        # Use Matplotlib's built-in Aitoff projection (expects radians)
        self.fig, self.ax = plt.subplots(figsize=(10, 5), subplot_kw={'projection': 'aitoff'})
        self.ax.set_facecolor('#f7f7f7')

    def setup_axes(self):
        # Draw gridlines resembling geographic graticules
        self.ax.grid(True, linestyle=':', linewidth=0.8, color='gray', alpha=0.6)
        # Default ticks across the globe; will be refined by set_limits if called
        lon_ticks_deg = np.arange(-180, 181, 30)
        lat_ticks_deg = np.arange(-90, 91, 30)
        self.ax.set_xticks(np.radians(lon_ticks_deg))
        self.ax.set_yticks(np.radians(lat_ticks_deg))
        self.format_coordinates()

    def set_limits(self, lon_min, lon_max, lat_min, lat_max):
        # For Matplotlib's 'aitoff' projection, we cannot clip the map extent,
        # but we can adjust the graticule ticks to focus on the region of interest.
        def deg_range(a, b, step):
            # Inclusive range with integer steps; handles direction too
            if a <= b:
                return np.arange(a, b + 1e-9, step)
            else:
                return np.arange(a, b - 1e-9, -step)

        # Constrain ticks within provided limits at 30-degree intervals
        xticks_deg = deg_range(lon_min, lon_max, 30)
        yticks_deg = deg_range(lat_min, lat_max, 30)
        self.ax.set_xticks(np.radians(xticks_deg))
        self.ax.set_yticks(np.radians(yticks_deg))
        self.format_coordinates()

    def format_coordinates(self):
        # Format longitude as E/W and latitude as N/S
        def fmt_lon(x, pos=None):
            deg = np.degrees(x)
            deg_rounded = int(np.round(deg))
            if deg_rounded == 0:
                return "0°"
            return f"{abs(deg_rounded)}°E" if deg_rounded > 0 else f"{abs(deg_rounded)}°W"

        def fmt_lat(y, pos=None):
            deg = np.degrees(y)
            deg_rounded = int(np.round(deg))
            if deg_rounded == 0:
                return "0°"
            return f"{abs(deg_rounded)}°N" if deg_rounded > 0 else f"{abs(deg_rounded)}°S"

        self.ax.xaxis.set_major_formatter(FuncFormatter(fmt_lon))
        self.ax.yaxis.set_major_formatter(FuncFormatter(fmt_lat))


class AitoffHammerProjection(GeographicProjection):
    def __init__(self):
        super().__init__()
        self.setup_axes()

    def draw_square(self):
        # Define the corners of the square in degrees
        square_lon_deg = [-60, 60, 60, -60, -60]
        square_lat_deg = [60, 60, -60, -60, 60]
        # Convert to radians for the Aitoff projection
        square_lon = np.radians(square_lon_deg)
        square_lat = np.radians(square_lat_deg)
        # Draw the square with markers
        self.ax.plot(
            square_lon,
            square_lat,
            color='red',
            linewidth=2,
            marker='o',
            markersize=5,
            zorder=3
        )


if __name__ == "__main__":
    projection = AitoffHammerProjection()
    projection.set_limits(-60, 60, -60, 60)
    projection.draw_square()
    projection.ax.set_title('Aitoff-Hammer Projection with Square', pad=20)
    plt.tight_layout()
    plt.savefig('novice_final.png', dpi=300)