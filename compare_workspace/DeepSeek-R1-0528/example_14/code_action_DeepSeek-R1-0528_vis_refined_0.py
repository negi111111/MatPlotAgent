import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import beta

# Set random seed for reproducibility
np.random.seed(42)

# Apply 'bmh' style equivalent using Matplotlib primitives
plt.style.use('bmh')

# Create figure and subplots
fig, axs = plt.subplots(2, 2, figsize=(12, 10))

# Function to plot beta distribution histograms
def plot_beta_histogram(ax, a, b):
    # Generate beta-distributed data
    data = np.random.beta(a, b, 1000)
    
    # Plot histogram
    ax.hist(data, bins=30, density=True, alpha=0.6, color='steelblue', edgecolor='white')
    
    # Overlay theoretical PDF
    x = np.linspace(0, 1, 200)
    ax.plot(x, beta.pdf(x, a, b), 'r', linewidth=2)
    
    # Set plot labels
    ax.set_title(f'Beta Distribution: α={a}, β={b}', fontsize=12)
    ax.set_xlabel('Value', fontsize=10)
    ax.set_ylabel('Density', fontsize=10)
    ax.grid(True, linestyle='--', alpha=0.7)

# Plot distributions with different parameters
plot_beta_histogram(axs[0, 0], 0.5, 0.5)
plot_beta_histogram(axs[0, 1], 2, 5)
plot_beta_histogram(axs[1, 0], 5, 1)
plot_beta_histogram(axs[1, 1], 1, 3)

# Add main title
plt.suptitle('Beta Distribution Histograms with Varying Parameters', fontsize=16, fontweight='bold')

# Adjust layout and save
plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.savefig('novice_final.png')