import matplotlib
matplotlib.use('Agg')
import numpy as np
   import matplotlib.pyplot as plt
   from matplotlib.axes import Axes
   from matplotlib.projections import register_projection
square_lon = np.array([-60,  60,  60, -60, -60])
   square_lat = np.array([-60, -60,  60,  60, -60])
fig = plt.figure(figsize=(8, 4.2))
     ax  = fig.add_subplot(1, 1, 1, projection='hammer_equal_area')
ax.draw_grid(lon_step=30, lat_step=30, color='lightgray', lw=0.5)
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.axes import Axes
from matplotlib.projections import register_projection

# ─────────────────────────────────────
# 1. Generic geographic Axes base class
# ─────────────────────────────────────
class GeographicAxes(Axes):
    """
    A tiny mix-in that supplies the non-projection-specific
    conveniences every geographic plot normally needs.
    """
    name = 'geo_base'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._setup_axes()

    # -------- internal helpers --------
    def _setup_axes(self):
        self.set_aspect('equal', adjustable='box')
        # generous limits – will be tightened later
        self.set_xlim(-np.pi * 2.0, np.pi * 2.0)
        self.set_ylim(-np.pi,       np.pi)
        # no ticks / spines
        self.set_xticks([]); self.set_yticks([])
        for spine in self.spines.values():
            spine.set_visible(False)

    # -------- public helpers ----------
    def clear_axis(self):
        self.cla()
        self._setup_axes()

    def set_global(self):
        lim_x = 2.0 * np.sqrt(2.0)
        lim_y =      np.sqrt(2.0)
        self.set_xlim(-lim_x, lim_x)
        self.set_ylim(-lim_y, lim_y)

    def set_extent(self, lon_min, lon_max, lat_min, lat_max):
        x0, y0 = self.project(lon_min, lat_min)
        x1, y1 = self.project(lon_max, lat_max)
        self.set_xlim(min(x0, x1), max(x0, x1))
        self.set_ylim(min(y0, y1), max(y0, y1))

    def draw_grid(self, lon_step=30, lat_step=30, **kwargs):
        # latitude lines
        lats = np.arange(-90, 91, lat_step)
        for lat in lats:
            lon_line = np.linspace(-180, 180, 361)
            lat_line = np.full_like(lon_line, lat)
            x, y = self.project(lon_line, lat_line)
            self.plot(x, y, **kwargs)

        # longitude lines
        lons = np.arange(-180, 181, lon_step)
        for lon in lons:
            lat_line = np.linspace(-90, 90, 181)
            lon_line = np.full_like(lat_line, lon)
            x, y = self.project(lon_line, lat_line)
            self.plot(x, y, **kwargs)

    # subclasses must provide `.project`
    def project(self, lon, lat):
        raise NotImplementedError("Subclasses must implement 'project'.")


# ─────────────────────────────────────
# 2. Hammer / Aitoff equal-area Axes
# ─────────────────────────────────────
class HammerEqualAreaAxes(GeographicAxes):
    """
    Matplotlib Axes that renders data in an equal-area Hammer projection.
    """
    name = 'hammer_equal_area'

    # ---------- forward transform ----------
    @staticmethod
    def _forward(lon_deg, lat_deg):
        lon = np.radians(lon_deg)
        lat = np.radians(lat_deg)
        z   = np.sqrt(1.0 + np.cos(lat) * np.cos(lon / 2.0))
        x   =  2.0 * np.sqrt(2.0) * np.cos(lat) * np.sin(lon / 2.0) / z
        y   =      np.sqrt(2.0)   * np.sin(lat)                     / z
        return x, y

    # ---------- inverse transform ----------
    @staticmethod
    def _inverse(x, y):
        # ensure ndarray semantics
        x = np.asarray(x, dtype=float)
        y = np.asarray(y, dtype=float)
        s = (x / 4.0) ** 2 + (y / 2.0) ** 2
        with np.errstate(invalid='ignore'):
            z   = np.sqrt(1.0 - s)
            lon = 2.0 * np.arctan2(z * x, 2.0 * (2.0 * z * z - 1.0))
            lat = np.arcsin(z * y)
        lon_deg = np.degrees(lon)
        lat_deg = np.degrees(lat)
        # mask points that lie outside the valid ellipse
        mask = s > 1.0
        lon_deg[mask] = np.nan
        lat_deg[mask] = np.nan
        return lon_deg, lat_deg

    # ---------- public wrappers ----------
    def project(self, lon, lat):
        return self._forward(lon, lat)

    # show lon/lat while hovering
    def format_coord(self, x, y):
        lon, lat = self._inverse(np.array([x]), np.array([y]))
        lon, lat = lon[0], lat[0]
        if np.isnan(lon) or np.isnan(lat):
            return ''
        return f'lon={lon:.1f}°,  lat={lat:.1f}°'

    # ensure world view by default
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.set_global()


# let Matplotlib know about the new projection
register_projection(HammerEqualAreaAxes)

# ─────────────────────────────────────
# 3. Data for the square
# ─────────────────────────────────────
square_lon = np.array([-60,  60,  60, -60, -60])
square_lat = np.array([-60, -60,  60,  60, -60])

# ─────────────────────────────────────
# 4. Plot
# ─────────────────────────────────────
fig = plt.figure(figsize=(8, 4.2))
ax  = fig.add_subplot(1, 1, 1, projection='hammer_equal_area')

# graticules
ax.draw_grid(lon_step=30, lat_step=30, color='lightgray', lw=0.5)

# the square
x_sq, y_sq = ax.project(square_lon, square_lat)
ax.plot(x_sq, y_sq, lw=2.5, color='firebrick')

ax.set_title('Square bounded by ±60° Latitude / ±60° Longitude')
plt.tight_layout()

# IMPORTANT: no  instead save directly
plt.savefig("novice.png")