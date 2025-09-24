import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt

# Set the random seed
np.random.seed(12345678)

# Generate data: five arrays of 150 sorted normal values with std 2..6
data = [np.sort(np.random.normal(0, std, 150)) for std in range(2, 7)]

# Calculate quartiles and whiskers (Q1, median, Q3) and (Q1, Q3) respectively
quartiles = [np.percentile(d, [25, 50, 75]) for d in data]
whiskers = [(q[0], q[2]) for q in quartiles]  # (Q1, Q3)

# Create subplots
fig, (ax1, ax2) = plt.subplots(1, 2, sharey=True, figsize=(12, 6))
positions = np.arange(1, len(data) + 1)

# Default violin plot (no inner marks)
vp1 = ax1.violinplot(data, positions=positions, showmeans=False, showextrema=False, showmedians=False)
for i, q in enumerate(quartiles):
    x = positions[i]
    # Whiskers (Q1 to Q3)
    ax1.plot([x, x], [q[0], q[2]], color='black')
    # Median dot
    ax1.plot(x, q[1], marker='o', color='red', linestyle='None')
ax1.set_title('Default violin plot with median dots and quartile whiskers')

# Customized violin plot (blue bodies, black edges, alpha=0.5)
vp2 = ax2.violinplot(data, positions=positions, showmeans=False, showextrema=False, showmedians=False)
for body in vp2['bodies']:
    body.set_facecolor('blue')
    body.set_edgecolor('black')
    body.set_linewidth(1)
    body.set_alpha(0.5)
ax2.set_title('Customized violin plot (blue bodies, black edges, alpha=0.5)')

# Set x-axis labels
labels = ['E', 'F', 'G', 'H', 'I']
ax1.set_xticks(positions)
ax1.set_xticklabels(labels)
ax2.set_xticks(positions)
ax2.set_xticklabels(labels)

# Adjust layout
plt.subplots_adjust(bottom=0.15, wspace=0.3)

# Save the plot
plt.savefig('novice_final.png', dpi=300)