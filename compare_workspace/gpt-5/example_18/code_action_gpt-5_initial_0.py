import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt
import math


def deg2rad(d):
    return np.radians(d)


def rad2deg(r):
    return np.degrees(r)


def wrap_lon_deg(lon):
    """
    Wrap longitude (degrees) into [-180, 180].
    Works with scalars or numpy arrays.
    """
    return ((lon + 180.0) % 360.0) - 180.0


class GeographicProjection:
    """
    Base class for geographic projections.

    Methods to:
      - setup and clear axes
      - set limits and transforms (coordinate formatter)
      - format coordinates (lon/lat)
      - set longitude and latitude grids
    """
    def __init__(self, central_longitude=0.0):
        self.central_longitude = float(central_longitude)

    def setup_axes(self, ax):
        """
        Configure axes for a globe-like map plot.
        """
        ax.set_aspect('equal', adjustable='box')
        ax.set_facecolor('white')
        # Hide spines and ticks; we'll draw our own boundary
        for spine in ax.spines.values():
            spine.set_visible(False)
        ax.set_xticks([])
        ax.set_yticks([])
        # Set default limits (subclass may override)
        self.set_limits(ax)

    def clear_axes(self, ax):
        """
        Clear the axes.
        """
        ax.cla()

    def set_limits(self, ax):
        """
        Set plotting limits; overridden by subclass if needed.
        """
        ax.set_xlim(-1.0, 1.0)
        ax.set_ylim(-1.0, 1.0)

    def set_transform(self, ax):
        """
        Attach a coordinate formatter that displays lon/lat for projected coordinates.
        """
        def _fmt(x, y):
            lonlat = self.inverse(x, y)
            if lonlat is None or np.isnan(lonlat[0]) or np.isnan(lonlat[1]):
                return f"x={x:.3f}, y={y:.3f} (outside)"
            lon, lat = lonlat
            return f"lon={lon:.2f}°, lat={lat:.2f}°"
        ax.format_coord = _fmt

    def format_coord(self, ax):
        """
        Alias for set_transform in this design (kept to match requirement naming).
        """
        self.set_transform(ax)

    def forward(self, lon_deg, lat_deg):
        """
        Forward transform lon/lat -> x/y.
        Must be implemented in subclass.
        """
        raise NotImplementedError

    def inverse(self, x, y):
        """
        Inverse transform x/y -> lon/lat.
        Must be implemented in subclass.
        """
        raise NotImplementedError

    def set_lonlat_grid(self, ax,
                        lon_ticks=None,
                        lat_ticks=None,
                        color='#808080',
                        linewidth=0.8,
                        alpha=0.6,
                        dashes=(2, 2)):
        """
        Draw longitude (meridians) and latitude (parallels) grid lines.

        Parameters:
          - lon_ticks: list/array of longitudes (degrees) to draw meridians.
          - lat_ticks: list/array of latitudes (degrees) to draw parallels.
          - color, linewidth, alpha, dashes: styling parameters for grid lines.
        """
        if lon_ticks is None:
            lon_ticks = np.arange(-150, 180, 30)  # -150,-120,...,150
        if lat_ticks is None:
            lat_ticks = np.arange(-60, 90, 30)    # -60,-30,0,30,60

        # Draw meridians (fixed lon, varying lat)
        lat_samples = np.linspace(-90.0, 90.0, 361)
        for lon0 in lon_ticks:
            lon_arr = np.full_like(lat_samples, float(lon0))
            x, y = self.forward(lon_arr, lat_samples)
            line = ax.plot(x, y, color=color, linewidth=linewidth, alpha=alpha)[0]
            line.set_dashes(dashes)

        # Draw parallels (fixed lat, varying lon)
        lon_samples = np.linspace(-180.0, 180.0, 721)
        for lat0 in lat_ticks:
            lat_arr = np.full_like(lon_samples, float(lat0))
            x, y = self.forward(lon_samples, lat_arr)
            line = ax.plot(x, y, color=color, linewidth=linewidth, alpha=alpha)[0]
            line.set_dashes(dashes)


class AitoffHammerProjection(GeographicProjection):
    """
    Hammer–Aitoff equal-area projection.

    Forward:
      x = (2*sqrt(2)*cos(phi)*sin(lambda/2)) / sqrt(1 + cos(phi)*cos(lambda/2))
      y = (sqrt(2)*sin(phi)) / sqrt(1 + cos(phi)*cos(lambda/2))

    Inverse (stable closed form):
      xh = x / 4
      yh = y / 2
      q = xh^2 + yh^2
      if q > 1: outside domain
      z = sqrt(1 - q)
      phi = asin(z * yh)
      lambda_rel = 2 * atan2(z * xh, z^2 - 0.5)
      lon = wrap_deg(deg(lambda_rel) + central_longitude)
      lat = deg(phi)
    """
    def set_limits(self, ax):
        a = 2.0 * math.sqrt(2.0)  # semi-major (x)
        b = math.sqrt(2.0)        # semi-minor (y)
        ax.set_xlim(-a, a)
        ax.set_ylim(-b, b)

    def forward(self, lon_deg, lat_deg):
        lon_deg = np.asarray(lon_deg, dtype=float)
        lat_deg = np.asarray(lat_deg, dtype=float)

        # Shift by central longitude and wrap
        lam_deg = wrap_lon_deg(lon_deg - self.central_longitude)
        lam = deg2rad(lam_deg)
        phi = deg2rad(lat_deg)

        cos_phi = np.cos(phi)
        sin_phi = np.sin(phi)
        lam_half = lam / 2.0
        cos_lam_half = np.cos(lam_half)
        sin_lam_half = np.sin(lam_half)

        D = np.sqrt(1.0 + (cos_phi * cos_lam_half))
        D = np.where(D == 0.0, np.finfo(float).eps, D)

        x = (2.0 * math.sqrt(2.0) * cos_phi * sin_lam_half) / D
        y = (math.sqrt(2.0) * sin_phi) / D
        return x, y

    def inverse(self, x, y):
        x = float(x)
        y = float(y)

        xh = x / 4.0
        yh = y / 2.0
        q = xh * xh + yh * yh
        if q > 1.0:
            return (np.nan, np.nan)

        z = math.sqrt(max(0.0, 1.0 - q))
        phi = math.asin(z * yh)
        denom = (z * z - 0.5)
        lam_rel = 2.0 * math.atan2(z * xh, denom)

        lon = wrap_lon_deg(rad2deg(lam_rel) + self.central_longitude)
        lat = rad2deg(phi)
        return (lon, lat)


def draw_hammer_boundary(ax):
    """
    Draw the boundary ellipse of the Hammer projection: x^2/8 + y^2/2 = 1
    Semi-axes: a = 2*sqrt(2), b = sqrt(2)
    """
    a = 2.0 * math.sqrt(2.0)
    b = math.sqrt(2.0)
    t = np.linspace(0.0, 2.0 * math.pi, 721)
    x = a * np.cos(t)
    y = b * np.sin(t)
    ax.plot(x, y, color='black', linewidth=1.0)


def main():
    # 1) Create figure and axes
    fig, ax = plt.subplots(figsize=(10, 5))

    # 2) Instantiate projection (central_longitude = 0 degrees)
    proj = AitoffHammerProjection(central_longitude=0.0)

    # 3) Setup axes and limits, attach coordinate formatter
    proj.setup_axes(ax)
    proj.set_transform(ax)  # adds lon/lat to mouse-over via format_coord

    # 4) Draw "globe" boundary ellipse
    draw_hammer_boundary(ax)

    # 5) Draw longitude/latitude grid
    proj.set_lonlat_grid(ax,
                         lon_ticks=np.arange(-150, 180, 30),
                         lat_ticks=np.arange(-60, 90, 30),
                         color='#606060',
                         linewidth=0.8,
                         alpha=0.7,
                         dashes=(4, 3))

    # 6) Prepare and plot the square edges:
    #    Top: lat = +60°, lon from -60° to +60°
    #    Bottom: lat = -60°, lon from -60° to +60°
    #    Left: lon = -60°,  lat from -60° to +60°
    #    Right: lon = +60°,  lat from -60° to +60°
    N = 400
    lon_range = np.linspace(-60.0, 60.0, N)
    lat_range = np.linspace(-60.0, 60.0, N)

    # Top edge (lat = +60°)
    x_top, y_top = proj.forward(lon_range, np.full_like(lon_range, 60.0))
    ax.plot(x_top, y_top, color='crimson', linewidth=2.0)

    # Bottom edge (lat = -60°)
    x_bot, y_bot = proj.forward(lon_range, np.full_like(lon_range, -60.0))
    ax.plot(x_bot, y_bot, color='crimson', linewidth=2.0)

    # Left edge (lon = -60°)
    x_left, y_left = proj.forward(np.full_like(lat_range, -60.0), lat_range)
    ax.plot(x_left, y_left, color='crimson', linewidth=2.0)

    # Right edge (lon = +60°)
    x_right, y_right = proj.forward(np.full_like(lat_range, 60.0), lat_range)
    ax.plot(x_right, y_right, color='crimson', linewidth=2.0)

    # 7) Title and save
    ax.set_title("Hammer–Aitoff Equal-Area Projection\nSquare edges at ±60° latitude and ±60° longitude", fontsize=12)
    plt.tight_layout()
    plt.savefig("novice.png", dpi=150)