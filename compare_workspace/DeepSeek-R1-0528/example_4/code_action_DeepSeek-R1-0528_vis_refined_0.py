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

# Add reference lines
plt.axhline(0, color='grey', lw=0.5)
plt.axvline(0, color='grey', lw=0.5)

# Function to draw confidence ellipses
def draw_ellipse(ax, mean, cov, n_std, color, linestyle, label):
    v, w = np.linalg.eigh(cov)
    idx = np.argmax(v)
    u = w[:, idx]
    angle = np.arctan2(u[1], u[0])
    angle = np.degrees(angle)
    
    # Scale axes by standard deviation
    width = 2 * n_std * np.sqrt(v[1])
    height = 2 * n_std * np.sqrt(v[0])
    
    ell = Ellipse(mean, width, height, angle, 
                  color=color, linestyle=linestyle, 
                  label=label, fill=False)
    ax.add_patch(ell)

# Draw confidence ellipses
draw_ellipse(plt.gca(), mean, cov, 1, 'firebrick', '-', '$1\sigma$')
draw_ellipse(plt.gca(), mean, cov, 2, 'fuchsia', '--', '$2\sigma$')
draw_ellipse(plt.gca(), mean, cov, 3, 'blue', ':', '$3\sigma$')

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