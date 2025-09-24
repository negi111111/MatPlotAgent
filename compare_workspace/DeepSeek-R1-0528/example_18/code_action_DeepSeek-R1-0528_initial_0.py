import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.path import Path
import matplotlib.patches as patches
from matplotlib.transforms import Transform
import matplotlib.projections as projections

class AitoffHammerTransform(Transform):
    input_dims = 2
    output_dims = 2
    is_separable = False

    def transform_non_affine(self, ll):
        lon, lat = ll.T
        cos_lat = np.cos(lat)
        sin_lat = np.sin(lat)
        lon_half = lon / 2.0
        cos_lon_half = np.cos(lon_half)
        denom = np.sqrt(1.0 + cos_lat * cos_lon_half)
        x = (2.0 * np.sqrt(2) * cos_lat * np.sin(lon_half)) / denom
        y = (np.sqrt(2) * sin_lat) / denom
        return np.column_stack([x, y])

    def inverted(self):
        return AitoffHammerTransform.InvertedAitoffHammerTransform()

    class InvertedAitoffHammerTransform(Transform):
        input_dims = 2
        output_dims = 2
        is_separable = False
        def transform_non_affine(self, xy):
            return xy  # Placeholder inverse

class GeoProjection(projections.Projection):
    name = 'geo'
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._longitude_min = -180
        self._longitude_max = 180
        self._latitude_min = -90
        self._latitude_max = 90
    
    def set_limits(self, lon_min, lon_max, lat_min, lat_max):
        self._longitude_min = lon_min
        self._longitude_max = lon_max
        self._latitude_min = lat_min
        self._latitude_max = lat_max
    
    def clear(self):
        if hasattr(self, 'ax'):
            self.ax.cla()
    
    def format_coord(self, x, y):
        return f'x: {x:.4f}, y: {y:.4f}'

class AitoffHammerProjection(GeoProjection):
    name = 'aitoff_hammer'
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.transform = AitoffHammerTransform()
    
    def set_transform(self):
        return self.transform
    
    def _as_mpl_axes(self):
        return AitoffHammerAxes, {'projection': self}

class AitoffHammerAxes(plt.Axes):
    name = 'aitoff_hammer_axes'
    
    def __init__(self, *args, **kwargs):
        self.projection = kwargs.pop('projection')
        super().__init__(*args, **kwargs)
        self.set_aspect('equal')
        self.set_xlim(-2.5, 2.5)
        self.set_ylim(-1.25, 1.25)

# Register custom projection
projections.register_projection(AitoffHammerProjection)

# Create geographic square vertices (degrees)
square_vertices_deg = np.array([
    [-60, -60],
    [60, -60],
    [60, 60],
    [-60, 60],
    [-60, -60]  # Close polygon
])
square_vertices_rad = np.radians(square_vertices_deg)

# Generate plot
fig = plt.figure(figsize=(10, 6), facecolor='white')
ax = fig.add_subplot(111, projection='aitoff_hammer')
ax.grid(True, linestyle='--', alpha=0.7, color='gray')

# Create and add square patch
transform = ax.projection.transform
square_vertices_proj = transform.transform(square_vertices_rad)
square_patch = patches.Polygon(
    square_vertices_proj,
    closed=True,
    edgecolor='red',
    facecolor='none',
    linewidth=2.5,
    zorder=10
)
ax.add_patch(square_patch)

# Add title and save
plt.title('Aitoff-Hammer Projection with Geographic Square', fontsize=14, pad=20)
plt.savefig("novice.png", bbox_inches='tight', dpi=100)