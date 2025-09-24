import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt

# Set random seed for reproducibility
np.random.seed(42)

# Use 'bmh' style for the plot
plt.style.use('bmh')

# Function to create histograms based on beta distributions
def plot_beta_histogram(ax, alpha, beta_param):
    data = np.random.beta(alpha, beta_param, 1000)
    ax.hist(data, bins=30, density=True, alpha=0.6, color='blue', edgecolor='black')
    ax.set_title(f'α={alpha}, β={beta_param}')
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 3)

# Create a 2x2 grid of subplots
fig, axs = plt.subplots(2, 2, figsize=(12, 10))

# Parameters for the beta distributions
params = [(2, 5), (5, 2), (2, 2), (5, 5)]

# Plot each histogram
for ax, (alpha, beta_param) in zip(axs.flatten(), params):
    plot_beta_histogram(ax, alpha, beta_param)

# Add a title for the entire figure
plt.suptitle('Beta Distribution Histograms', fontsize=16)

# Adjust layout to make room for the suptitle
plt.tight_layout(rect=[0, 0, 1, 0.96])

# Save the figure to a PNG file
plt.savefig('novice_final.png')