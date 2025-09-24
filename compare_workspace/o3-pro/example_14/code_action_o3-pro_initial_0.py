import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style

# 1) Make results reproducible
np.random.seed(42)

# 2) Apply the requested style
style.use('bmh')

def draw_beta_hist(ax, a, b, n=10_000, bins=50, alpha=0.75):
    """
    Draw a normalized histogram of Beta(a, b) samples on the provided Axes.
    """
    samples = np.random.beta(a, b, size=n)
    ax.hist(
        samples,
        bins=bins,
        density=True,
        color='C0',
        alpha=alpha,
        edgecolor='black'
    )
    ax.set_title(f"Beta(a={a}, b={b})")
    ax.set_xlabel("x")
    ax.set_ylabel("Probability density")

# 3) Create a 2×2 grid of subplots
fig, axes = plt.subplots(2, 2, figsize=(10, 8), constrained_layout=True)
axes = axes.ravel()

# 4) Shape-parameter pairs for the four subplots
shape_params = [(0.5, 0.5), (2, 5), (5, 1), (2, 2)]

for ax, (a, b) in zip(axes, shape_params):
    draw_beta_hist(ax, a, b)

# 5) Figure-level title
fig.suptitle("Histograms of Four Beta Distributions", fontsize=16, weight='bold')

# 6) Save the plot
plt.savefig("novice.png")