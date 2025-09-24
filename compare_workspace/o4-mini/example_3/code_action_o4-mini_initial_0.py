import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt

# 1. Fix the random seed for reproducibility
np.random.seed(12345678)

# 2. Generate five datasets of 150 points each from Normal(0, σ)
stds = [2, 3, 4, 5, 6]
data = [np.sort(np.random.normal(loc=0.0, scale=s, size=150)) for s in stds]

# 3. Pre-compute quartiles, IQR, and whiskers
quartiles = [np.percentile(d, [25, 50, 75]) for d in data]  # Q1, Q2 (median), Q3
iqr = [q[2] - q[0] for q in quartiles]
whiskers = [
    (q[0] - 1.5 * i, q[2] + 1.5 * i)
    for q, i in zip(quartiles, iqr)
]

# 4. Create a figure with two side-by-side subplots sharing the y-axis
fig, (ax1, ax2) = plt.subplots(ncols=2, sharey=True, figsize=(8, 5))

# Positions and labels
x_positions = np.arange(1, len(data) + 1)
labels = ['E', 'F', 'G', 'H', 'I']

# ---- First subplot: default violins + medians & whiskers ----

# a. Draw the default violins without any statistics
parts1 = ax1.violinplot(data, showmeans=False, showmedians=False, showextrema=False)

# b. Overlay red dots at each median
medians = [q[1] for q in quartiles]
ax1.scatter(x_positions, medians, color='red', marker='o', zorder=3)

# c. Draw vertical lines for Q1–Q3 and whiskers
for i, (q, w) in enumerate(zip(quartiles, whiskers), start=1):
    # Q1 to Q3
    ax1.vlines(i, q[0], q[2], color='black', linestyle='-', linewidth=2)
    # Whiskers
    ax1.vlines(i, w[0], w[1], color='black', linestyle='--', linewidth=1)

# d. Label the x-axis
ax1.set_xticks(x_positions)
ax1.set_xticklabels(labels)
ax1.set_title("Default violins + medians & whiskers")

# ---- Second subplot: custom violins (blue, no medians/extrema) ----

# a. Draw the violins without statistics
parts2 = ax2.violinplot(data, showmeans=False, showmedians=False, showextrema=False)

# b. Style the violin bodies
for body in parts2['bodies']:
    body.set_facecolor('blue')
    body.set_edgecolor('black')
    body.set_alpha(0.5)

# c. Label the x-axis
ax2.set_xticks(x_positions)
ax2.set_xticklabels(labels)
ax2.set_title("Custom violins (blue, no medians/extrema)")

# 5. Tidy up spacing
fig.subplots_adjust(bottom=0.15, wspace=0.05)

# 6. Save the figure to a PNG file
plt.savefig("novice.png")