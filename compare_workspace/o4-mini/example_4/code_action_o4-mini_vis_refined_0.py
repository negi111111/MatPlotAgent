import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse

# 1. Set up the figure
fig, ax = plt.subplots(figsize=(6, 6))

# 2. Generate the correlated dataset
np.random.seed(0)  # for reproducibility
mean = [4, 3]
cov = [[1, 0.6], [0.6, 1]]
data = np.random.multivariate_normal(mean, cov, 700)
x, y = data.T

# Plot the data points
ax.scatter(x, y, s=10, color='black', alpha=0.5, label='Data points')

# 3. Add grey horizontal and vertical lines
ax.axhline(0, color='grey', lw=1)
ax.axvline(0, color='grey', lw=1)

# 4. Function to overlay a confidence ellipse
def plot_ellipse(ax, mean, cov, n_std, color, linestyle, label):
    # Eigen decomposition of the covariance matrix
    v, w = np.linalg.eigh(cov)
    # Width and height of the ellipse are 2*sqrt(eigenvalues)*n_std*sqrt(2)
    widths = 2.0 * np.sqrt(2.0) * n_std * np.sqrt(v)
    # Angle of rotation from the largest eigenvector
    unit_vec = w[0] / np.linalg.norm(w[0])
    angle = np.degrees(np.arctan2(unit_vec[1], unit_vec[0]))
    # Create and add the ellipse patch
    ell = Ellipse(xy=mean,
                  width=widths[0],
                  height=widths[1],
                  angle=angle,
                  edgecolor=color,
                  facecolor='none',
                  linestyle=linestyle,
                  label=label)
    ax.add_patch(ell)

# 4a. Overlay 1σ, 2σ, and 3σ ellipses
plot_ellipse(ax, mean, cov, 1, 'firebrick', '-',  r'$1\sigma$')
plot_ellipse(ax, mean, cov, 2, 'fuchsia', '--',  r'$2\sigma$')
plot_ellipse(ax, mean, cov, 3, 'blue',    ':',  r'$3\sigma$')

# 5. Highlight the point (1,1)
ax.scatter(1, 1,
           color='red',
           edgecolor='black',
           s=100,
           label='(1,1) highlight',
           zorder=5)

# 6. Set title and legend
ax.set_title('Different standard deviations')
ax.legend()

# 7. Save the figure
plt.savefig('novice_final.png')