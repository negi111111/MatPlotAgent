import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.colors import Normalize

# ------------------------------------------------------------------
# 1. Reproducibility
# ------------------------------------------------------------------
np.random.seed(42)                 # fixed seed for repeatable results

# ------------------------------------------------------------------
# 2. Data generation
# ------------------------------------------------------------------
N = 30                             # number of bars

# Angular positions (bar centers)
theta = np.linspace(0.0, 2 * np.pi, N, endpoint=False)

# Bar heights
heights = np.random.rand(N)        # values already in the 0–1 range

# Bar angular widths (jittered around the mean spacing)
base_width = 2 * np.pi / N
widths = base_width * (0.5 + np.random.rand(N))   # between 0.5× and 1.5× base

# ------------------------------------------------------------------
# 3. Map heights to colors
# ------------------------------------------------------------------
norm = Normalize(vmin=heights.min(), vmax=heights.max())
colors = cm.viridis(norm(heights))                 # sequential colormap

# ------------------------------------------------------------------
# 4. Create the polar bar plot
# ------------------------------------------------------------------
fig, ax = plt.subplots(subplot_kw=dict(polar=True))

bars = ax.bar(theta,
              heights,
              width=widths,
              bottom=0.0,
              color=colors,
              alpha=0.5)

# Optional cosmetic adjustments
ax.set_yticklabels([])                            # hide radial tick labels
ax.set_title('Random Polar Bar Plot', va='bottom')

plt.tight_layout()

# ------------------------------------------------------------------
# 5. Save the figure
# ------------------------------------------------------------------
plt.savefig("novice.png", dpi=150)