import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse

# Set the figure size
plt.figure(figsize=(6, 6))

# Generate the correlated dataset
np.random.seed(0)
mean = [4, 4]
cov = [[1, 0.6], [0.6, 1]]
data = np.random.multivariate_normal(mean, cov, 700)
x, y = data.T

# Create the scatter plot
plt.scatter(x, y, color='black', label='Data Points')

# Add vertical and horizontal lines
plt.axhline(0, color='grey', lw=0.5)
plt.axvline(0, color='grey', lw=0.5)

# Function to draw ellipses
def draw_ellipse(ax, mean, cov, n_std, color, linestyle, label):
    v, w = np.linalg.eigh(cov)
    v = 2.0 * np.sqrt(2.0) * n_std * np.sqrt(v)
    u = w[0] / np.linalg.norm(w[0])
    angle = np.arctan(u[1] / u[0]) * 180.0 / np.pi
    ell = Ellipse(mean, v[0], v[1], 180 + angle, color=color, linestyle=linestyle, label=label, fill=False)
    ax.add_patch(ell)

# Overlay confidence ellipses
draw_ellipse(plt.gca(), mean, cov, 1, 'firebrick', '-', '$1\sigma$')
draw_ellipse(plt.gca(), mean, cov, 2, 'fuchsia', '--', '$2\sigma$')
draw_ellipse(plt.gca(), mean, cov, 3, 'blue', ':', '$3\sigma$')

# Highlight the specific point
plt.scatter(1, 1, color='red', s=100, label='Highlighted Point (1,1)')

# Set the title
plt.title('Different standard deviations')

# Add a legend
plt.legend()

# Save the plot to a PNG file
plt.savefig('novice_final.png')

# Close the figure to prevent any display
plt.close()