import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt

# 1) Reproducibility
np.random.seed(12345678)

# 2) Generate five datasets: 150 samples each, std devs 2..6, sorted
std_devs = [2, 3, 4, 5, 6]
data = [np.sort(np.random.normal(loc=0.0, scale=sd, size=150)) for sd in std_devs]

# 3) Compute quartiles and medians per dataset
quartiles = []  # list of tuples (Q1, Q2/median, Q3)
for arr in data:
    q1, q2, q3 = np.percentile(arr, [25, 50, 75])
    quartiles.append((q1, q2, q3))

# 4) Positions and labels
positions = np.arange(1, len(data) + 1)
labels = ['E', 'F', 'G', 'H', 'I']

# 5) Create figure and subplots (share y-axis)
fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, sharey=True, figsize=(10, 6))

# Adjust layout for better visualization
fig.subplots_adjust(bottom=0.15, wspace=0.35)

# 6) First subplot: default violin plot
parts1 = ax1.violinplot(data, positions=positions)  # defaults: means=False, medians=False, extrema=True

# Plot medians as red dots, and whiskers as vertical lines spanning Q1 to Q3
# Also add short vertical ticks at Q1 and Q3 to mark quartile locations.
all_min = min(arr.min() for arr in data)
all_max = max(arr.max() for arr in data)
data_range = all_max - all_min
tick_len = 0.03 * data_range  # short tick length around quartile levels

for x, (q1, med, q3) in zip(positions, quartiles):
    # Median red dot
    ax1.scatter(x, med, color='red', s=30, zorder=3)
    # Whisker (vertical line from Q1 to Q3)
    ax1.vlines(x, q1, q3, color='black', linewidth=2)
    # Short vertical ticks at Q1 and Q3 (emphasize quartile positions)
    ax1.vlines(x, q1 - tick_len / 2, q1 + tick_len / 2, color='black', linewidth=1)
    ax1.vlines(x, q3 - tick_len / 2, q3 + tick_len / 2, color='black', linewidth=1)

# Set x-axis labels
ax1.set_xticks(positions)
ax1.set_xticklabels(labels)
ax1.set_title('Default violin plot with median dots and quartile whiskers')

# 7) Second subplot: customized violin plot (no means, no medians, no extrema)
parts2 = ax2.violinplot(
    data,
    positions=positions,
    showmeans=False,
    showmedians=False,
    showextrema=False
)

# Customize violin bodies: blue face, black edges, alpha=0.5
for body in parts2['bodies']:
    body.set_facecolor('blue')
    body.set_edgecolor('black')
    body.set_alpha(0.5)
    body.set_linewidth(1)

# Set x-axis labels
ax2.set_xticks(positions)
ax2.set_xticklabels(labels)
ax2.set_title('Customized violin plot (blue bodies, black edges, alpha=0.5)')

# 8) Save plot to PNG
plt.savefig("novice.png")