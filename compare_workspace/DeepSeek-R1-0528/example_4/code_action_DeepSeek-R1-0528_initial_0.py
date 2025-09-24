import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse

# Set random seed for reproducibility
np.random.seed(42)

# Define distribution parameters
mean = [1, 1]
std_dev = [7, 6]
corr = 0.6

# Build covariance matrix
cov_matrix = np.array([
    [std_dev[0]**2, corr * std_dev[0] * std_dev[1]],
    [corr * std_dev[0] * std_dev[1], std_dev[1]**2]
])

# Generate 700 correlated data points
data = np.random.multivariate_normal(mean, cov_matrix, 700)

# Create figure and axis
fig, ax = plt.subplots(figsize=(6, 6))

# Scatter plot with high-contrast styling
ax.scatter(data[:, 0], data[:, 1], alpha=0.6, color='steelblue', edgecolor='k', linewidth=0.5)

# Add reference lines at mean values
ax.axvline(x=mean[0], color='grey', linestyle='-', alpha=0.7, linewidth=1)
ax.axhline(y=mean[1], color='grey', linestyle='-', alpha=0.7, linewidth=1)

# Confidence ellipse function
def confidence_ellipse(mean, cov, ax, n_std=1, **kwargs):
    eigenvalues, eigenvectors = np.linalg.eigh(cov)
    order = eigenvalues.argsort()[::-1]
    eigenvalues = eigenvalues[order]
    eigenvectors = eigenvectors[:, order]
    angle = np.degrees(np.arctan2(eigenvectors[1, 0], eigenvectors[0, 0]))
    width = 2 * n_std * np.sqrt(eigenvalues[0])
    height = 2 * n_std * np.sqrt(eigenvalues[1])
    ellipse = Ellipse(mean, width, height, angle=angle, **kwargs)
    ax.add_patch(ellipse)

# Plot confidence ellipses with specified styles
confidence_ellipse(mean, cov_matrix, ax, n_std=1, 
                   edgecolor='firebrick', facecolor='none', linewidth=1.5, label='$1\sigma$')
confidence_ellipse(mean, cov_matrix, ax, n_std=2, 
                   edgecolor='fuchsia', facecolor='none', linewidth=1.5, 
                   linestyle='--', label='$2\sigma$')
confidence_ellipse(mean, cov_matrix, ax, n_std=3, 
                   edgecolor='blue', facecolor='none', linewidth=1.5, 
                   linestyle=':', label='$3\sigma$')

# Highlight mean point
ax.scatter(mean[0], mean[1], color='red', s=80, zorder=5, label='Point (1,1)')

# Add titles and legend
ax.set_title('Different standard deviations', fontsize=14)
ax.legend(loc='upper left', frameon=True, edgecolor='black')

# Save as PNG
plt.tight_layout()
plt.savefig("novice.png")