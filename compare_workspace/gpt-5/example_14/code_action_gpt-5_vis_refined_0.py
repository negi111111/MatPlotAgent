import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt

# Set random seed for consistency
np.random.seed(42)

# Use 'bmh' style for the plot
plt.style.use('bmh')

# Function to create histograms based on beta distributions
def plot_beta_histogram(ax, alpha, beta_param):
    x = np.random.beta(alpha, beta_param, 1000)  # Generate random beta data
    ax.hist(x, bins=30, density=True, alpha=0.6, color='b', edgecolor='black')  # Create histogram
    ax.set_title(f'Beta(α={alpha}, β={beta_param})')
    ax.set_xlabel('x')
    ax.set_ylabel('Density')

# Create subplots
fig, axs = plt.subplots(2, 2, figsize=(12, 10))  # Create a 2x2 subplot grid

# Define shape parameters for the beta distributions
params = [(0.5, 0.5), (5, 1), (1, 3), (2, 2)]

for ax, (alpha, beta_param) in zip(axs.flatten(), params):
    plot_beta_histogram(ax, alpha, beta_param)  # Call the histogram function

# Add a title to the entire plot
plt.suptitle('Beta Distribution Histograms for Different Shape Parameters', fontsize=16)

# Adjust layout and save the plot
plt.tight_layout(rect=[0, 0, 1, 0.96])  # Adjust layout to make room for the title
plt.savefig('novice_final.png')  # Save the plot as a PNG file