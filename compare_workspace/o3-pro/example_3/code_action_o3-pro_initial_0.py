import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt

# 1. Make the result reproducible
np.random.seed(12345678)

# 2. Build the data
std_list = range(2, 7)  # 2, 3, 4, 5, 6
data = [np.sort(np.random.normal(loc=0, scale=std, size=150)) for std in std_list]

# 3. Prepare the figure canvas and two side-by-side Axes objects that share the y-axis
fig, (ax1, ax2) = plt.subplots(ncols=2, figsize=(9, 5), sharey=True)
plt.subplots_adjust(bottom=0.18, wspace=0.05)

# 4. Common definitions
x_positions = np.arange(1, len(data) + 1)   # 1 … 5
x_labels    = ['E', 'F', 'G', 'H', 'I']

# ------------------------------------------------------------------
# FIRST subplot – default violin plot plus extra summary elements
# ------------------------------------------------------------------
vp1 = ax1.violinplot(
    dataset=data,
    positions=x_positions,
    showmeans=False,
    showmedians=False,
    showextrema=True
)

# Summary statistics
quartiles = [np.percentile(d, [25, 50, 75]) for d in data]
mins      = [d.min() for d in data]
maxs      = [d.max() for d in data]
q1, med, q3 = zip(*quartiles)

# Plot medians
ax1.scatter(x_positions, med, color='red', zorder=3)

# IQR bars (thick) and whiskers (thin)
for x, lo, hi in zip(x_positions, q1, q3):
    ax1.vlines(x, lo, hi, color='k', linewidth=5)   # IQR bars
for x, lo, hi in zip(x_positions, mins, maxs):
    ax1.vlines(x, lo, hi, color='k', linewidth=1)   # whiskers

# Cosmetics
ax1.set_xticks(x_positions)
ax1.set_xticklabels(x_labels)
ax1.set_title('Default violin plot')

# ------------------------------------------------------------------
# SECOND subplot – customised violin plot
# ------------------------------------------------------------------
vp2 = ax2.violinplot(
    dataset=data,
    positions=x_positions,
    showmeans=False,
    showmedians=False,
    showextrema=False
)

# Re-style the violin bodies
for body in vp2['bodies']:
    body.set_facecolor('blue')
    body.set_edgecolor('black')
    body.set_alpha(0.5)
    body.set_linewidth(1.0)

# Cosmetics
ax2.set_xticks(x_positions)
ax2.set_xticklabels(x_labels)
ax2.set_title('Customised violin plot')

# ------------------------------------------------------------------
# Save the figure
# ------------------------------------------------------------------
plt.savefig("novice.png")