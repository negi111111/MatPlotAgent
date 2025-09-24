import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Set random seed for reproducibility
np.random.seed(42)

# Number of data points
n_points = 700

# Split points between two clusters (350 each)
n1, n2 = 350, 350

# Means for two clusters
mean1 = [1, 1]
mean2 = [7, 6]

# Covariance matrices based on correlation parameters
cov1 = [[1, 0.6], [0.6, 1]]  # Simplified covariance with correlation 0.6
cov2 = [[1, -0.3], [-0.3, 1]]  # Simplified covariance with correlation -0.3

# Generate data for two clusters
data1 = np.random.multivariate_normal(mean1, cov1, n1)
data2 = np.random.multivariate_normal(mean2, cov2, n2)

# Combine the data
data = np.vstack([data1, data2])
x, y = data[:, 0], data[:, 1]

# Create a new figure with specified size
plt.figure(figsize=(6, 6))

# Create scatter plot of the data
plt.scatter(x, y, s=10, color='black', alpha=0.5, label='Data Points')

# Add vertical and horizontal lines through the mean of the data
plt.axvline(x=np.mean(x), color='grey', linestyle='-', alpha=0.5)
plt.axhline(y=np.mean(y), color='grey', linestyle='-', alpha=0.5)

# Compute mean and covariance of the entire dataset for ellipses
data_mean = np.mean(data, axis=0)
data_cov = np.cov(data.T)

# Compute eigenvalues and eigenvectors for ellipse orientation
eigvals, eigvecs = np.linalg.eigh(data_cov)
order = eigvals.argsort()[::-1]
eigvals, eigvecs = eigvals[order], eigvecs[:, order]

# Angle of rotation for the ellipse (in degrees)
angle = np.degrees(np.arctan2(*eigvecs[:, 0][::-1]))

# Width and height of ellipses based on standard deviations (1, 2, 3 sigma)
stds = [1, 2, 3]
colors = ['firebrick', 'fuchsia', 'blue']
linestyles = ['-', '--', ':']
labels = [r'$1\sigma$', r'$2\sigma$', r'$3\sigma$']

for i, std in enumerate(stds):
    width = 2 * std * np.sqrt(eigvals[0])
    height = 2 * std * np.sqrt(eigvals[1])
    ellipse = patches.Ellipse(xy=data_mean, width=width, height=height, angle=angle,
                              edgecolor=colors[i], linestyle=linestyles[i], facecolor='none',
                              label=labels[i])
    plt.gca().add_patch(ellipse)

# Highlight the specific point (1, 1) with a red marker
plt.plot(1, 1, 'o', color='red', markersize=10, label='Highlighted Point (1,1)')

# Set the plot title
plt.title('Different standard deviations', fontsize=12, pad=15)

# Add a legend
plt.legend(loc='best', fontsize=10)

# Save the plot as a PNG file
plt.savefig("novice.png")