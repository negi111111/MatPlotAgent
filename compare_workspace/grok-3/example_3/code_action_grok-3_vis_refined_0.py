import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt

# Set the random seed for reproducibility
np.random.seed(12345678)

# Generate data: 5 arrays of 150 sorted random numbers from normal distribution
data = [np.sort(np.random.normal(0, std, 150)) for std in range(2, 7)]

# Create subplots with shared y-axis
fig, axes = plt.subplots(1, 2, sharey=True, figsize=(12, 6))

# Function to create a violin plot using Matplotlib
def create_violin_plot(ax, data, positions, color, alpha=1.0, linewidth=1.0, show_stats=False):
    for i, d in enumerate(data):
        # Calculate kernel density estimation for the violin shape
        from scipy.stats import gaussian_kde
        kde = gaussian_kde(d)
        x = np.linspace(min(d), max(d), 100)
        density = kde(x)
        density = density / density.max() * 0.4  # Scale the width of the violin
        
        # Plot the violin body (mirrored density)
        ax.fill_betweenx(x, positions[i] - density, positions[i] + density, 
                        color=color, alpha=alpha, edgecolor='black', linewidth=linewidth)
        
        if show_stats:
            # Calculate quartiles and whiskers for stats
            q1, median, q3 = np.percentile(d, [25, 50, 75])
            iqr = q3 - q1
            whisker_low = np.min(d[d >= q1 - 1.5 * iqr])
            whisker_high = np.max(d[d <= q3 + 1.5 * iqr])
            
            # Plot whiskers as vertical lines
            ax.plot([positions[i], positions[i]], [whisker_low, whisker_high], 
                    color='black', linewidth=1.0)
            # Plot median as a red dot
            ax.scatter([positions[i]], [median], color='red', zorder=5)
            # Plot a vertical dashed line at the center
            ax.axvline(x=positions[i], color='black', linestyle='--', linewidth=0.5)

# Positions for the violins (centered at 0,1,2,3,4)
positions = np.arange(len(data))

# Default Violin Plot (with stats) in the first subplot
create_violin_plot(axes[0], data, positions, color='gray', alpha=1.0, linewidth=1.0, show_stats=True)

# Customized Violin Plot (no stats) in the second subplot
create_violin_plot(axes[1], data, positions, color='blue', alpha=0.5, linewidth=1.5, show_stats=False)

# Set x-axis labels for both subplots
axes[0].set_xticks(positions)
axes[0].set_xticklabels(['E', 'F', 'G', 'H', 'I'])
axes[1].set_xticks(positions)
axes[1].set_xticklabels(['E', 'F', 'G', 'H', 'I'])

# Adjust layout for better spacing
plt.subplots_adjust(bottom=0.15, wspace=0.3)

# Add titles and labels
axes[0].set_title('Default Violin Plot with Medians and Whiskers')
axes[1].set_title('Customized Violin Plot (No Stats)')
axes[0].set_ylabel('Values')

# Save the plot to a PNG file
plt.savefig('novice_final.png', dpi=300)