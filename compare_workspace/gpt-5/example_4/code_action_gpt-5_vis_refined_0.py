import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse

# Set the figure size
plt.figure(figsize=(6, 6))

# Generate correlated dataset
np.random.seed(0)
mean = [4, 3]
cov = [[1, 0.6], [0.6, 1]]
data = np.random.multivariate_normal(mean, cov, 700)
x, y = data[:, 0], data[:, 1]

# Create scatter plot
plt.scatter(x, y, color='lightblue', label='Data')

# Add vertical and horizontal lines
plt.axvline(x=0, color='grey', linestyle='--')
plt.axhline(y=0, color='grey', linestyle='--')

# Function to draw ellipses
def draw_ellipse(ax, mean, cov, n_std, color, linestyle, label):
    vals, vecs = np.linalg.eigh(cov)
    # Order eigenvalues/vectors from largest to smallest
    order = vals.argsort()[::-1]
    vals = vals[order]
    vecs = vecs[:, order]

    # Width/height scaled by n_std (matching provided formulation)
    width = 2.0 * np.sqrt(2.0) * n_std * np.sqrt(vals[0])
    height = 2.0 * np.sqrt(2.0) * n_std * np.sqrt(vals[1])

    # Angle of rotation from the largest eigenvector
    angle = np.degrees(np.arctan2(vecs[1, 0], vecs[0, 0]))
    ell = Ellipse(mean, width, height, 180 + angle, color=color, linestyle=linestyle, label=label)
    ax.add_patch(ell)
    return width, height

ax = plt.gca()

# Draw confidence ellipses
w1, h1 = draw_ellipse(ax, mean, cov, 1, 'firebrick', '-', '$1\\sigma$')
w2, h2 = draw_ellipse(ax, mean, cov, 2, 'fuchsia', '--', '$2\\sigma$')
w3, h3 = draw_ellipse(ax, mean, cov, 3, 'blue', ':', '$3\\sigma$')

# Ensure the full 3σ ellipse is visible
max_half = max(w3, h3) / 2.0
plt.xlim(mean[0] - max_half - 1, mean[0] + max_half + 1)
plt.ylim(mean[1] - max_half - 1, mean[1] + max_half + 1)
plt.gca().set_aspect('equal', adjustable='box')

# Highlight specific point
plt.scatter(1, 1, color='red', s=100, label='(1, 1)', edgecolor='black')

# Set title and legend
plt.title('Different standard deviations')
plt.legend()

# Save the plot to a single PNG file
plt.savefig('novice_final.png')