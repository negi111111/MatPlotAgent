import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

# Set random seed for reproducibility
np.random.seed(42)

# Apply 'bmh' plot style
plt.style.use('bmh')

# Create 2x2 subplots
fig, axes = plt.subplots(2, 2, figsize=(10, 8))

# Function to plot beta distribution histogram
def plot_beta_hist(ax, a, b):
    # Generate 1000 samples from beta distribution
    samples = np.random.beta(a, b, 1000)
    # Plot histogram with density and transparency
    ax.hist(samples, bins=30, density=True, alpha=0.7, edgecolor='k')
    # Set subplot title and labels
    ax.set_title(f'Beta Distribution: α={a}, β={b}')
    ax.set_xlabel('Value')
    ax.set_ylabel('Density')

# Different beta distribution parameters
params = [(0.5, 0.5), (2, 5), (5, 1), (1, 3)]

# Plot histograms for each parameter set
for ax, (a, b) in zip(axes.flat, params):
    plot_beta_hist(ax, a, b)

# Configure main title and layout
fig.suptitle('Beta Distribution Histograms with Varying Parameters', fontsize=16)
plt.tight_layout(rect=[0, 0, 1, 0.96])  # Adjust for main title

# Save the figure as PNG
plt.savefig("novice.png")