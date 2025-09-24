import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import Normalize

# 1. Fix seed for reproducibility
np.random.seed(42)

# 2. Number of bars
N = 30

# 3. Angles around the circle
theta = np.linspace(0.0, 2 * np.pi, N, endpoint=False)

# 4. Radii (diameters) linearly spaced
radii = np.linspace(0.1, 1.0, N)

# 5. Random bar thicknesses
max_width = 0.3
widths = max_width * np.random.rand(N)

# 6. Normalize radii for color mapping
norm = Normalize(vmin=radii.min(), vmax=radii.max())
cmap = plt.cm.viridis
colors = cmap(norm(radii))

# 7. Create polar plot
fig, ax = plt.subplots(subplot_kw={'polar': True})

# 8. Plot bars with alpha=0.5
bars = ax.bar(
    theta,        # angular positions
    radii,        # bar lengths
    width=widths, # bar thicknesses
    bottom=0.0,   # all bars start from r=0
    color=colors, # RGBA from the colormap
    alpha=0.5     # uniform transparency
)

# 9. Final touches
ax.set_title(
    "Reproducible Polar Bar Plot\n"
    "30 bars • random widths • linear radii",
    va='bottom'
)

plt.tight_layout()
plt.savefig("novice.png")