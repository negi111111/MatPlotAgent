import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt

# Set random seed for reproducibility
np.random.seed(12345678)

# Generate sorted normal distributions with increasing std
data = [np.sort(np.random.normal(0, std, 150)) for std in range(2, 7)]

# Create figure with two subplots sharing y-axis
fig, axs = plt.subplots(1, 2, figsize=(12, 6), sharey=True)

# First plot: Default style with statistical markers
violins1 = axs[0].violinplot(data, showmeans=False, showmedians=False, showextrema=False)
for i, d in enumerate(data):
    # Calculate statistics
    q1, median, q3 = np.percentile(d, [25, 50, 75])
    
    # Add quartile line and median marker
    axs[0].vlines(i+1, q1, q3, color='black', linewidth=1.5)
    axs[0].plot(i+1, median, 'ro', markersize=4)

# Customize first plot
axs[0].set_title('Violin Plot with Statistical Markers')
axs[0].set_xticks(range(1, 6))
axs[0].set_xticklabels(['E', 'F', 'G', 'H', 'I'])

# Second plot: Custom styled violins
violins2 = axs[1].violinplot(data, showmeans=False, showmedians=False, showextrema=False)
for pc in violins2['bodies']:
    pc.set_facecolor('blue')
    pc.set_edgecolor('black')
    pc.set_alpha(0.5)
    pc.set_linewidth(1.5)

# Customize second plot
axs[1].set_title('Custom Styled Violin Plot')
axs[1].set_xticks(range(1, 6))
axs[1].set_xticklabels(['E', 'F', 'G', 'H', 'I'])

# Adjust layout and save
plt.subplots_adjust(bottom=0.15, wspace=0.3)
plt.savefig('novice_final.png', bbox_inches='tight')