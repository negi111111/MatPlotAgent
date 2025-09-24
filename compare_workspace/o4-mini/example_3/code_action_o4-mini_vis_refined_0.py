import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt

# Set the random seed for reproducibility
np.random.seed(12345678)

# Generate five datasets of 150 sorted normal points with std from Uniform(2,6)
data = [
    np.sort(np.random.normal(loc=0, scale=np.random.uniform(2, 6), size=150))
    for _ in range(5)
]

# Compute the 1st quartile, median, and 3rd quartile for each dataset
quartiles = [np.percentile(d, [25, 50, 75]) for d in data]

# Prepare the positions for the violins (0 through 4)
positions = np.arange(len(data))

# Create the figure and two subplots, sharing the y-axis
fig, (ax1, ax2) = plt.subplots(1, 2, sharey=True, figsize=(12, 6))

# -------------------------------
# First subplot: Default violins + medians & whiskers
# -------------------------------
# Draw violins without the built-in extrema markers
vp1 = ax1.violinplot(
    dataset=data,
    positions=positions,
    showextrema=False
)

# Overlay whiskers (Q1 to Q3) and medians
for i, (q1, med, q3) in enumerate(quartiles):
    # Whisker line
    ax1.plot([i, i], [q1, q3], color='black', linewidth=1)
    # Median point
    ax1.plot(i, med, 'ro', markersize=5)

ax1.set_title('Default violins + medians & whiskers')

# -------------------------------
# Second subplot: Custom blue violins, no medians/extrema
# -------------------------------
vp2 = ax2.violinplot(
    dataset=data,
    positions=positions,
    showextrema=False
)

# Customize the violin bodies: blue fill, black edge, 50% opacity
for body in vp2['bodies']:
    body.set_facecolor('blue')
    body.set_edgecolor('black')
    body.set_alpha(0.5)

ax2.set_title('Custom violins (blue, no medians/extrema)')

# -------------------------------
# Common formatting for both subplots
# -------------------------------
for ax in (ax1, ax2):
    ax.set_xticks(positions)
    ax.set_xticklabels(['E', 'F', 'G', 'H', 'I'])
    ax.grid(axis='y', linestyle='--', alpha=0.5)

# Adjust layout for better spacing
fig.subplots_adjust(bottom=0.15, wspace=0.3)

# Save the figure as a PNG file
plt.savefig('novice_final.png')