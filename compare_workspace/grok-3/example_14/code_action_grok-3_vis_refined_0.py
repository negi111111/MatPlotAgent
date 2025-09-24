import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import beta

# Set random seed for reproducibility
np.random.seed(42)

# Use 'bmh' style for the plot
plt.style.use('bmh')

# Function to create histograms based on beta distributions
def plot_beta_histogram(ax, a, b):
    data = beta.rvs(a, b, size=1000)  # Generate random data from a beta distribution
    ax.hist(data, bins=30, density=True, alpha=0.6, color='blue')  # Create histogram
    ax.set_title(f'Beta({a}, {b})')  # Set title for the subplot
    ax.set_xlabel('Value')  # Set x-axis label
    ax.set_ylabel('Density')  # Set y-axis label

# Create subplots
fig, axs = plt.subplots(2, 2, figsize=(10, 8))

# Call the histogram function for each subplot
plot_beta_histogram(axs[0, 0], 1, 1)  # Beta(1, 1)
plot_beta_histogram(axs[0, 1], 2, 2)  # Beta(2, 2)
plot_beta_histogram(axs[1, 0], 2, 5)  # Beta(2, 5)
plot_beta_histogram(axs[1, 1], 5, 2)  # Beta(5, 2)

# Set the overall title
plt.suptitle('Histograms of Beta Distributions with Different Shape Parameters')

# Adjust layout
plt.tight_layout(rect=[0, 0, 1, 0.96])  # Adjust layout

# Save the plot
plt.savefig('novice_final.png')  # Save the plot as a PNG file