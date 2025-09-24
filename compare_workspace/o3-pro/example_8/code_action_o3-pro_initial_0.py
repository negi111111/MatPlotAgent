import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors  # for hsv_to_rgb

# 1. Reproducible RNG
rng = np.random.default_rng(seed=42)

# 2. Constants
N_POINTS   = 200
AREA_SCALE = 2000   # area scaling factor for visibility

# 3. Generate random polar coordinates
r     = rng.random(N_POINTS)            # radii in [0, 1)
theta = rng.random(N_POINTS) * 2 * np.pi  # angles in [0, 2π)

# 4. Marker areas (area ∝ r²)
areas = AREA_SCALE * r**2

# 5. Colours determined by angle (HSV → RGB)
hsv        = np.column_stack((theta / (2 * np.pi),
                              np.ones(N_POINTS),
                              np.ones(N_POINTS)))
colors_rgb = colors.hsv_to_rgb(hsv)

# 6. Plot
fig, ax = plt.subplots(subplot_kw={'projection': 'polar'}, figsize=(8, 6))

ax.scatter(theta,
           r,
           s=areas,
           c=colors_rgb,
           linewidths=0.5,
           edgecolors='black',
           alpha=0.75)

ax.set_title("Random Polar Scatter (200 points)\n"
             "Area ∝ r², Hue ∝ θ",
             va='bottom')

# 7. Save the figure
plt.savefig("novice.png")