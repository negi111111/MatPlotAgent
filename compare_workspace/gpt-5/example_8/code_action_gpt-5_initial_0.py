import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import Normalize

# 1) Fixed random state for reproducibility
rng = np.random.default_rng(42)

# 2) Generate random polar coordinates
N = 200
theta = rng.uniform(0.0, 2 * np.pi, size=N)  # angles in radians
r = rng.uniform(0.0, 1.0, size=N)            # radial distances

# 3) Marker area proportional to r^2
size_scale = 800.0
sizes = size_scale * (r ** 2)

# 4) Color by angle using HSV colormap
angle_norm = Normalize(vmin=0.0, vmax=2 * np.pi)

# 5) Create polar scatter plot
fig, ax = plt.subplots(figsize=(6, 6), subplot_kw={'projection': 'polar'})
scatter = ax.scatter(
    theta,
    r,
    s=sizes,
    c=theta,
    cmap='hsv',
    norm=angle_norm,
    alpha=0.85,
    edgecolors='none'
)

# 6) Aesthetics
ax.set_ylim(0, 1)
ax.grid(True)
ax.set_title('Polar Scatter: Positions Random, Size ∝ r², Color by Angle (HSV)')

# 7) Optional colorbar
cbar = plt.colorbar(scatter, ax=ax, pad=0.1)
cbar.set_label('Angle (radians)')

# 8) Save to file (no interactive window)
plt.tight_layout()
plt.savefig("novice.png")