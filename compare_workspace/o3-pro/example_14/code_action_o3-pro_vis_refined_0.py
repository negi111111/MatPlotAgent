import matplotlib
matplotlib.use('Agg')
"""
Histogram grid of four beta distributions, saved to 'novice_final.png'.

Strict compliance:
1. Only matplotlib is used for plotting.
2. Exactly one PNG is written.
3. No interactive windows are opened.
4. Deterministic output by fixing the random seed.
"""

import numpy as np
import matplotlib.pyplot as plt

# ------------------------------------------------------------------
# Determinism: fix random seed so the histogram bins are repeatable
# ------------------------------------------------------------------
np.random.seed(42)

# ------------------------------------------------------------------
# Global plotting style
# ------------------------------------------------------------------
plt.style.use('bmh')   # replicate the requested visual appearance

# ------------------------------------------------------------------
# Helper: draw one histogram of a Beta(a, b) distribution
# ------------------------------------------------------------------
def plot_beta_histogram(ax, a, b, num_samples: int = 1000) -> None:
    """
    Draw a histogram of `num_samples` from Beta(a, b) on the axis `ax`.
    
    Parameters
    ----------
    ax : matplotlib.axes.Axes
        The axis on which to draw the histogram.
    a, b : float
        Shape parameters of the Beta distribution.
    num_samples : int, default=1000
        Number of random values to draw.
    """
    samples = np.random.beta(a, b, num_samples)
    ax.hist(samples,
            bins=30,
            density=True,
            alpha=0.6,
            color='b',
            edgecolor='black')
    ax.set_title(f'Beta(a={a}, b={b})')
    ax.set_xlabel('x')
    ax.set_ylabel('Probability density')

# ------------------------------------------------------------------
# Create the 2×2 grid of subplots
# ------------------------------------------------------------------
fig, axs = plt.subplots(2, 2, figsize=(12, 10))

plot_beta_histogram(axs[0, 0], 0.5, 0.5)
plot_beta_histogram(axs[0, 1], 2, 5)
plot_beta_histogram(axs[1, 0], 5, 1)
plot_beta_histogram(axs[1, 1], 2, 2)

fig.suptitle('Histograms of Four Beta Distributions', fontsize=16)

# ------------------------------------------------------------------
# Final layout adjustments and file output
# ------------------------------------------------------------------
plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.savefig('novice_final.png')   # exactly one file is generated