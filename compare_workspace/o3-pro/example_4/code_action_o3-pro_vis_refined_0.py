import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse

# 1. Create a square figure 6x6 inches
fig, ax = plt.subplots(figsize=(6, 6))

# 2. Generate a correlated data set (700 points, fixed seed for determinism)
np.random.seed(0)
mean = np.array([4, 2])
cov = np.array([[1, 0.6],
                [0.6, 1]])
data = np.random.multivariate_normal(mean, cov, 700)
x, y = data.T

# 3. Scatter plot of the data points
ax.scatter(x, y, color='gray', alpha=0.5, label='data')

# 4. Grey reference axes
ax.axhline(0, color='grey', linewidth=0.8)
ax.axvline(0, color='grey', linewidth=0.8)

# 5. Function to draw n-sigma confidence ellipses
def draw_ellipse(ax, mean, cov, n_std, **kwargs):
    """
    Draw an ellipse representing the covariance matrix scaled to n_std.
    """
    # Eigenvalues/vectors give ellipse axes
    eigvals, eigvecs = np.linalg.eigh(cov)
    # Sort descending for consistent orientation
    order = eigvals.argsort()[::-1]
    eigvals, eigvecs = eigvals[order], eigvecs[:, order]

    # Width and height (full lengths) of the ellipse
    width, height = 2 * n_std * np.sqrt(eigvals)

    # Angle of the first eigenvector w.r.t. x-axis
    angle = np.degrees(np.arctan2(*eigvecs[:, 0][::-1]))

    ellipse = Ellipse(xy=mean,
                      width=width,
                      height=height,
                      angle=angle,
                      fill=False,
                      **kwargs)
    ax.add_patch(ellipse)

# Draw 1σ, 2σ, 3σ ellipses
draw_ellipse(ax, mean, cov, 1, edgecolor='firebrick', linestyle='-',  label=r'$1\sigma$')
draw_ellipse(ax, mean, cov, 2, edgecolor='fuchsia',  linestyle='--', label=r'$2\sigma$')
draw_ellipse(ax, mean, cov, 3, edgecolor='blue',     linestyle=':',  label=r'$3\sigma$')

# 6. Highlight the specific point (1,1)
ax.scatter(1, 1, color='red', s=100, edgecolors='black', label='highlighted (1,1)')

# 7. Titles and labels
ax.set_title('Different standard deviations')
ax.set_xlabel('X')
ax.set_ylabel('Y')

# 8. Legend
ax.legend()

# 9. Grid, layout, and save
ax.grid()
plt.tight_layout()
plt.savefig('novice_final.png')