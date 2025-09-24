import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse

# 1) RNG for reproducibility
rng = np.random.default_rng(seed=42)

# 2) Parameters
n_total = 700
n1 = n2 = n_total // 2

mu1 = np.array([1.0, 1.0])
mu2 = np.array([7.0, 6.0])

# Correlation ranges
rho1 = rng.uniform(0.6, 0.85)   # for cluster centered at (1, 1)
rho2 = rng.uniform(-0.3, 0.25)  # for cluster centered at (7, 6)

# Standard deviations for each dimension (unit stds)
sx1 = sy1 = 1.0
sx2 = sy2 = 1.0

# 3) Covariance matrices
cov1 = np.array([[sx1**2, rho1*sx1*sy1],
                 [rho1*sx1*sy1, sy1**2]])
cov2 = np.array([[sx2**2, rho2*sx2*sy2],
                 [rho2*sx2*sy2, sy2**2]])

# 4) Sample data
X1 = rng.multivariate_normal(mean=mu1, cov=cov1, size=n1)
X2 = rng.multivariate_normal(mean=mu2, cov=cov2, size=n2)
X = np.vstack([X1, X2])  # shape (700, 2)

# 5) Mean and covariance of full dataset
mean = X.mean(axis=0)
cov = np.cov(X, rowvar=False)

# 6) Helper to draw confidence ellipse
def add_confidence_ellipse(ax, mean, cov, n_std, edgecolor, linestyle='-', linewidth=2.0, label=None):
    vals, vecs = np.linalg.eigh(cov)
    order = np.argsort(vals)[::-1]
    vals = vals[order]
    vecs = vecs[:, order]
    width = 2.0 * n_std * np.sqrt(vals[0])
    height = 2.0 * n_std * np.sqrt(vals[1])
    angle = np.degrees(np.arctan2(vecs[1, 0], vecs[0, 0]))
    ell = Ellipse(xy=mean, width=width, height=height, angle=angle,
                  facecolor='none', edgecolor=edgecolor, linestyle=linestyle,
                  linewidth=linewidth, label=label)
    ax.add_patch(ell)
    return ell

# 7) Plot
fig, ax = plt.subplots(figsize=(6, 6))

# Scatter
ax.scatter(X[:, 0], X[:, 1], s=10, c='tab:blue', alpha=0.6, label='Data')

# Guide lines through dataset mean
ax.axvline(x=mean[0], color='grey', linewidth=1.0, alpha=0.8)
ax.axhline(y=mean[1], color='grey', linewidth=1.0, alpha=0.8)

# Confidence ellipses: 1σ, 2σ, 3σ
add_confidence_ellipse(ax, mean, cov, n_std=1, edgecolor='firebrick', linestyle='-', label=r'$1\sigma$')
add_confidence_ellipse(ax, mean, cov, n_std=2, edgecolor='fuchsia', linestyle='--', label=r'$2\sigma$')
add_confidence_ellipse(ax, mean, cov, n_std=3, edgecolor='blue', linestyle=':', label=r'$3\sigma$')

# Highlight point (1, 1)
ax.scatter(1, 1, color='red', s=60, marker='o', zorder=3, label='(1, 1)')

# Titles and legend
ax.set_title('Different standard deviations')
ax.set_aspect('equal', adjustable='datalim')
ax.legend()
plt.tight_layout()

# Save to file
plt.savefig("novice.png")