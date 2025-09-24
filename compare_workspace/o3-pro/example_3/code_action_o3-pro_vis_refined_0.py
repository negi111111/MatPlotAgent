import matplotlib
matplotlib.use('Agg')
"""
Violin plot comparison
======================

Creates two side-by-side violin plots for five data sets:

1) Left subplot:
   • Plain violins.
   • Black vertical lines for the full data range (whiskers).
   • Thicker black vertical lines for the inter-quartile range.
   • A red point for the median of each distribution.

2) Right subplot:
   • Semi-transparent blue violins with black edges.
   • No additional statistical markers.

The graphic is saved as 'novice_final.png'.
"""

import numpy as np
import matplotlib.pyplot as plt

# -----------------------------
# Step 1: Reproducible data
# -----------------------------
np.random.seed(12345678)

# Generate five arrays of 150 normally-distributed values
# with a random standard deviation between 2 and 6.
data = [
    np.sort(
        np.random.normal(loc=0.0,
                         scale=np.random.uniform(2.0, 6.0),
                         size=150)
    )
    for _ in range(5)
]

# -----------------------------
# Step 2: Figure and axes
# -----------------------------
fig, axes = plt.subplots(nrows=1,
                         ncols=2,
                         sharey=True,
                         figsize=(12, 6))

# Common x-positions for both subplots
positions = np.arange(len(data))

# -----------------------------
# Step 3: Default-style violin plot (left)
# -----------------------------
vp_left = axes[0].violinplot(
    data,
    positions=positions,
    showmeans=False,
    showmedians=False,
    showextrema=False  # we'll draw these ourselves
)

# Overlay statistical markers
for i, sample in enumerate(data):
    median = np.median(sample)
    q1, q3 = np.percentile(sample, [25, 75])
    vmin, vmax = sample[0], sample[-1]

    # Whisker (min-max)
    axes[0].plot([i, i], [vmin, vmax], color='black', linewidth=1)

    # Inter-quartile range
    axes[0].plot([i, i], [q1, q3], color='black', linewidth=3)

    # Median
    axes[0].scatter(i, median, color='red', zorder=5)

# -----------------------------
# Step 4: Custom violin plot (right)
# -----------------------------
vp_right = axes[1].violinplot(
    data,
    positions=positions,
    showmeans=False,
    showmedians=False,
    showextrema=False
)

# Style the right-hand violins
for body in vp_right['bodies']:
    body.set_facecolor('blue')
    body.set_edgecolor('black')
    body.set_alpha(0.5)
    body.set_linewidth(1.25)

# -----------------------------
# Step 5: Axis cosmetics
# -----------------------------
labels = ['E', 'F', 'G', 'H', 'I']
for ax in axes:
    ax.set_xticks(positions)
    ax.set_xticklabels(labels)

# Extra spacing between the two subplots
plt.subplots_adjust(bottom=0.15, wspace=0.3)

# -----------------------------
# Step 6: Save to file
# -----------------------------
plt.savefig("novice_final.png", dpi=300, bbox_inches='tight')