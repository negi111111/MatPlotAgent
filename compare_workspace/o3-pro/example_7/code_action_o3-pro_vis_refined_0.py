import matplotlib
matplotlib.use('Agg')
"""
Deterministic polar bar plot that meets the specified requirements:

1. Uses only Matplotlib (no seaborn, plotly, etc.).
2. Generates 30 bars positioned evenly around the circle.
3. Diameters are linearly spaced; bar widths (“thicknesses”) are random.
4. Bar colours follow a viridis gradient based on the diameter magnitude.
5. Global transparency (alpha) is 0.5.
6. The random seed is fixed for reproducibility.
7. Exactly one PNG called ``novice_final.png`` is written; no interactive
   windows are opened.
"""

import numpy as np
import matplotlib.pyplot as plt

# ------------------------------------------------------------------
# 1. Reproducibility
# ------------------------------------------------------------------
np.random.seed(42)           # Fixed seed ensures identical output each run

# ------------------------------------------------------------------
# 2. Data generation
# ------------------------------------------------------------------
num_bars = 30
# Evenly-spaced angles (bar positions)
angles = np.linspace(0, 2 * np.pi, num_bars, endpoint=False)

# Diameters: linearly spaced from 0.1 to 1.0
diameters = np.linspace(0.1, 1.0, num_bars)

# Thickness (bar widths in radians): random, max 0.1 rad
thicknesses = np.random.rand(num_bars) * 0.1

# ------------------------------------------------------------------
# 3. Colour mapping
# ------------------------------------------------------------------
# Normalize diameters to 0–1 range
norm_diameters = (diameters - diameters.min()) / (diameters.max() - diameters.min())
# Map to viridis colours
colors = plt.cm.viridis(norm_diameters)

# ------------------------------------------------------------------
# 4. Plotting
# ------------------------------------------------------------------
fig, ax = plt.subplots(subplot_kw={'projection': 'polar'}, figsize=(8, 8))

# Draw bars
ax.bar(
    angles,                     # bar locations
    diameters,                  # bar heights (radial length)
    width=thicknesses,          # bar angular width
    color=colors,               # colour gradient
    alpha=0.5,                  # transparency
    edgecolor='black',          # thin outline for clarity
    linewidth=0.5
)

# Minimal aesthetic tweaks
ax.set_title('Random Polar Bar Plot', va='bottom')
ax.set_yticklabels([])         # Hide radial tick labels for cleaner look
ax.grid(True, linestyle=':', linewidth=0.5, alpha=0.7)

# ------------------------------------------------------------------
# 5. Save figure (exactly one PNG file)
# ------------------------------------------------------------------
plt.savefig('novice_final.png', dpi=300, bbox_inches='tight')
# Do NOT call  complies with non-interactive requirement.