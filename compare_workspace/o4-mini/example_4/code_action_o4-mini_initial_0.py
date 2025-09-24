import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse
from matplotlib.transforms import Affine2D

# 1. Fix random seed for reproducibility
np.random.seed(0)

# 2. Parameters for the four Gaussian clusters
total_points = 700
corr_params  = [[0.6,  0.85],
                [-0.3, 0.25]]
means        = [(1, 1),
                (7, 6)]
n_clusters   = len(corr_params) * len(means)      # 2 × 2 = 4
points_per_cluster = total_points // n_clusters   # 700//4 = 175

# 3. Generate the data
all_x = []
all_y = []
for i_row, row in enumerate(corr_params):
    for j_col, corr in enumerate(row):
        mu  = np.array(means[j_col])
        cov = np.array([[1.0, corr],
                        [corr, 1.0]])
        data = np.random.multivariate_normal(mu, cov, size=points_per_cluster)
        all_x.append(data[:, 0])
        all_y.append(data[:, 1])

x = np.hstack(all_x)
y = np.hstack(all_y)

# 4. Create figure and scatter
fig, ax = plt.subplots(figsize=(6, 6))
ax.scatter(x, y,
           s=10,
           alpha=0.7,
           color='C0',
           label='Data points')

# 5. Add grey cross‐hairs at the overall mean
mean_x, mean_y = x.mean(), y.mean()
ax.axvline(mean_x, color='grey', linewidth=1)
ax.axhline(mean_y, color='grey', linewidth=1)

# 6. Compute overall covariance (for reference)
cov = np.cov(x, y)

# 7. Helper to draw confidence ellipses
def confidence_ellipse(x, y, ax,
                       n_std=1.0,
                       edgecolor='black',
                       linestyle='-',
                       label=None):
    """
    Add an ellipse corresponding to the covariance of x vs y,
    scaled to n_std standard deviations.
    """
    cov = np.cov(x, y)
    pearson = cov[0, 1] / np.sqrt(cov[0, 0] * cov[1, 1])
    ell_radius_x = np.sqrt(1 + pearson)
    ell_radius_y = np.sqrt(1 - pearson)

    # create the ellipse in unit space
    ellipse = Ellipse((0, 0),
                      width=ell_radius_x * 2,
                      height=ell_radius_y * 2,
                      facecolor='none',
                      edgecolor=edgecolor,
                      linestyle=linestyle,
                      linewidth=2,
                      label=label)

    # scale & rotate & translate to the data
    scale_x = np.sqrt(cov[0, 0]) * n_std
    scale_y = np.sqrt(cov[1, 1]) * n_std
    transf = (Affine2D()
              .rotate_deg(45)
              .scale(scale_x, scale_y)
              .translate(mean_x, mean_y))

    ellipse.set_transform(transf + ax.transData)
    ax.add_patch(ellipse)
    return ellipse

# 8. Draw 1σ, 2σ, 3σ ellipses
confidence_ellipse(x, y, ax,
                   n_std=1,
                   edgecolor='firebrick',
                   linestyle='-',
                   label=r'$1\sigma$')
confidence_ellipse(x, y, ax,
                   n_std=2,
                   edgecolor='fuchsia',
                   linestyle='--',
                   label=r'$2\sigma$')
confidence_ellipse(x, y, ax,
                   n_std=3,
                   edgecolor='blue',
                   linestyle=':',
                   label=r'$3\sigma$')

# 9. Highlight the point (1, 1)
ax.scatter(1, 1,
           color='red',
           s=50,
           marker='X',
           label='(1,1) highlight')

# 10. Finishing touches
ax.set_title('Different standard deviations')
ax.legend(loc='best')

# 11. Save the figure
plt.savefig("novice.png")