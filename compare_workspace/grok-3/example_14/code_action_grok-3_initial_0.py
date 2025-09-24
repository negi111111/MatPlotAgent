import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt

# Set random seed for consistent random number generation
np.random.seed(42)

# Set the plot style to 'bmh'
plt.style.use('bmh')

# Create a figure and a 2x2 grid of subplots
fig, axes = plt.subplots(2, 2, figsize=(10, 8))

# Define different shape parameters for the beta distributions
params = [(1, 1), (2, 2), (2, 5), (5, 2)]

# Function to plot histogram of beta distribution using numpy.random.beta
def plot_beta_histogram(ax, a, b, bins=50):
    """
    Generate and plot a histogram of a beta distribution on the given axes.
    
    Parameters:
    - ax: matplotlib.axes.Axes, the subplot axes to plot the histogram on.
    - a: float, first shape parameter of the beta distribution.
    - b: float, second shape parameter of the beta distribution.
    - bins: int, number of bins for the histogram (default=50).
    """
    # Generate random samples from the beta distribution using numpy
    data = np.random.beta(a, b, size=10000)
    # Plot the histogram of the samples
    ax.hist(data, bins=bins, density=True, alpha=0.7, color='#1f77b4')  # High-contrast blue
    # Set title for the subplot with the shape parameters
    ax.set_title(f'Beta({a}, {b})')
    # Set x and y labels
    ax.set_xlabel('Value')
    ax.set_ylabel('Density')

# Plot histograms for each set of parameters on the respective subplot
plot_beta_histogram(axes[0, 0], params[0][0], params[0][1])
plot_beta_histogram(axes[0, 1], params[1][0], params[1][1])
plot_beta_histogram(axes[1, 0], params[2][0], params[2][1])
plot_beta_histogram(axes[1, 1], params[3][0], params[3][1])

# Add a main title to the figure
fig.suptitle('Histograms of Beta Distributions with Different Shape Parameters', fontsize=14)

# Adjust the layout to prevent overlap
plt.tight_layout()

# Add padding between the main title and subplots
fig.subplots_adjust(top=0.85)

# Save the plot as a PNG file
plt.savefig("novice.png")