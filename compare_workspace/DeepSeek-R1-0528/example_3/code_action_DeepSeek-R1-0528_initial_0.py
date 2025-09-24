import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt

# Set random seed for reproducibility
np.random.seed(12345678)

# Generate data: 5 arrays of 150 sorted random numbers
std_devs = [2, 3, 4, 5, 6]
data = []
for std in std_devs:
    arr = np.random.normal(0, std, 150)
    arr.sort()
    data.append(arr)

# Calculate quartiles and whiskers
q1 = [np.percentile(arr, 25) for arr in data]
medians = [np.median(arr) for arr in data]
q3 = [np.percentile(arr, 75) for arr in data]
iqr = [q3_i - q1_i for q1_i, q3_i in zip(q1, q3)]
lower_whisker = [q1_i - 1.5 * iqr_i for q1_i, iqr_i in zip(q1, iqr)]
upper_whisker = [q3_i + 1.5 * iqr_i for q3_i, iqr_i in zip(q3, iqr)]

# Create figure with two subplots sharing y-axis
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6), sharey=True)
plt.subplots_adjust(bottom=0.15, wspace=0.05)  # Adjust layout

# First subplot: Default violin plot with custom annotations
violin1 = ax1.violinplot(data, showmedians=False, showextrema=False)

# Overlay medians as red dots
positions = np.arange(1, len(data) + 1)
ax1.scatter(positions, medians, color='red', zorder=3, s=30)

# Add vertical lines for Q1, Q3, and whiskers
for pos, lw, q1_val, q3_val, uw in zip(positions, lower_whisker, q1, q3, upper_whisker):
    ax1.vlines(pos, lw, uw, color='black', linestyles='dashed', alpha=0.7, linewidth=1)
    ax1.vlines(pos, q1_val, q3_val, color='black', linewidths=2)

# Set x-axis labels
ax1.set_xticks(positions)
ax1.set_xticklabels(['E', 'F', 'G', 'H', 'I'])
ax1.set_title('Violin Plot with Statistical Markers')

# Second subplot: Customized violin plot
violin2 = ax2.violinplot(data, showmedians=False, showextrema=False)

# Customize violin bodies
for body in violin2['bodies']:
    body.set_facecolor('blue')
    body.set_edgecolor('black')
    body.set_alpha(0.5)

# Set x-axis labels
ax2.set_xticks(positions)
ax2.set_xticklabels(['E', 'F', 'G', 'H', 'I'])
ax2.set_title('Custom Styled Violin Plot')

# Save the figure
plt.savefig("novice.png")