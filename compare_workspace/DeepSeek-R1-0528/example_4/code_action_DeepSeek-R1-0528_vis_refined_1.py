import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse

# Set figure size
plt.figure(figsize=(6, 6))

# Generate correlated dataset
np.random.seed(0)
n = 700
mean = [0, 0]
cov = [[1, 0.6], [0.6, 1]]
x, y = np.random.multivariate_normal(mean, cov, n).T

# Plot the data points
plt.scatter(x, y, s=10, color='black', alpha=0.5)

# Add reference lines
plt.axhline(0, color='grey', lw=0.5)
plt.axvline(0, color='grey', lw=0.5)

# Function to draw confidence ellipses
def draw_ellipse(ax, mean, cov, n_std, color, linestyle, label):
    # Compute eigenvalues and eigenvectors
    eigenvalues, eigenvectors = np.linalg.eigh(cov)
    
    # Get largest eigenvalue and corresponding eigenvector
    max_index = np.argmax(eigenvalues)
    max_eigenvector = eigenvectors[:, max_index]
    
    # Calculate angle in degrees
    angle = np.degrees(np.arctan2(max_eigenvector[1], max_eigenvector[0]))
    
    # Calculate width and height based on eigenvalues
    width = 2 * n_std * np.sqrt(eigenvalues[1])
    height = 2 * n_std * np.sqrt(eigenvalues[0])
    
    # Create ellipse with angle as keyword argument
    ell = Ellipse(mean, width, height, angle=angle, 
                  color=color, linestyle=linestyle, 
                  label=label, fill=False)
    ax.add_patch(ell)

# Draw confidence ellipses
draw_ellipse(plt.gca(), mean, cov, 1, 'firebrick', '-', r'$1\sigma$')
draw_ellipse(plt.gca(), mean, cov, 2, 'fuchsia', '--', r'$2\sigma$')
draw_ellipse(plt.gca(), mean, cov, 3, 'blue', ':', r'$3\sigma$')

# Highlight specific point
plt.scatter(1, 1, color='red', s=100, label='Point (1,1)', edgecolor='black')

# Configure plot
plt.title('Different standard deviations')
plt.legend()
plt.gca().set_aspect('equal')
plt.xlim(-4, 4)
plt.ylim(-4, 4)

# Save output
plt.savefig("novice_final.png")