import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt

# Set plot style
plt.style.use('bmh')

# Ensure reproducible random number generation
rng = np.random.default_rng(42)

# Function to create a beta-distribution histogram on a given Axes
def plot_beta_hist(ax, alpha, beta, n_samples=10000, bins=50):
    # Generate samples from Beta(alpha, beta)
    samples = rng.beta(alpha, beta, size=n_samples)
    # Plot histogram of the samples
    ax.hist(
        samples,
        bins=bins,
        range=(0, 1),
        density=True,
        alpha=0.8,
        edgecolor='black',
        color='#1f77b4'
    )
    # Annotate the subplot
    ax.set_title(f"Beta(α={alpha}, β={beta})")
    ax.set_xlabel("x")
    ax.set_ylabel("Density")
    ax.set_xlim(0, 1)

# Create a 2x2 subplot grid
fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(10, 8), constrained_layout=True)

# Plot four different beta distributions
plot_beta_hist(axes[0, 0], 0.5, 0.5)
plot_beta_hist(axes[0, 1], 5, 1)
plot_beta_hist(axes[1, 0], 1, 3)
plot_beta_hist(axes[1, 1], 2, 2)

# Add an overall title
fig.suptitle("Beta Distribution Histograms for Different Shape Parameters", fontsize=16)

# Save the plot to a PNG file
plt.savefig("novice.png")