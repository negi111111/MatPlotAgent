import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt

# 1. Ensure reproducibility
np.random.seed(42)

# 2. Set the plotting style
plt.style.use('bmh')

# 3. Helper function to plot a beta-distribution histogram
def plot_beta_hist(ax, alpha, beta, n_samples=1000, n_bins=30):
    data = np.random.beta(alpha, beta, size=n_samples)
    ax.hist(
        data,
        bins=n_bins,
        density=True,       # normalize to form a probability density
        alpha=0.75,         # transparency for better overlap visibility
        edgecolor='black'   # black edges help define each bar
    )
    ax.set_title(f'α={alpha}, β={beta}')

# 4. Create a 2×2 grid of subplots
fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(10, 8))
axes = axes.flatten()

# 5. Four different (alpha, beta) settings
shape_params = [
    (2, 5),
    (5, 2),
    (2, 2),
    (5, 5),
]

# 6. Populate each subplot
for ax, (a, b) in zip(axes, shape_params):
    plot_beta_hist(ax, alpha=a, beta=b)

# 7. Add a main title and adjust layout
fig.suptitle('Beta Distribution Histograms', fontsize=16)
plt.tight_layout(rect=[0, 0.03, 1, 0.95])

# 8. Save the figure as a PNG file
plt.savefig("novice.png")