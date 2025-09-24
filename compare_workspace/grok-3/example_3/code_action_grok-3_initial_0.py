import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt

# Set random seed for reproducibility
np.random.seed(12345678)

# Generate 5 arrays with different standard deviations (2 to 6)
data = [np.sort(np.random.normal(loc=0, scale=std, size=150)) for std in range(2, 7)]

# Calculate quartiles, medians, and whiskers for each dataset
quartiles = []
whiskers = []
medians = []
for d in data:
    q1, q2, q3 = np.percentile(d, [25, 50, 75])
    iqr = q3 - q1
    whisker_low = max(d[0], q1 - 1.5 * iqr)  # Lower whisker limited to data range
    whisker_high = min(d[-1], q3 + 1.5 * iqr)  # Upper whisker limited to data range
    quartiles.append((q1, q2, q3))
    whiskers.append((whisker_low, whisker_high))
    medians.append(q2)

# Create a figure with two subplots sharing y-axis
fig, (ax1, ax2) = plt.subplots(1, 2, sharey=True, figsize=(10, 6))

# Adjust layout for better visualization
fig.subplots_adjust(bottom=0.15, wspace=0.1)

# Function to create a custom violin plot using kernel density estimation
def custom_violinplot(ax, data, positions, width=0.4, color='gray', edgecolor='black', alpha=1.0):
    from scipy.stats import gaussian_kde
    for i, d in enumerate(data):
        # Calculate kernel density estimation
        kde = gaussian_kde(d)
        # Define the range for density estimation
        x = np.linspace(min(d), max(d), 200)
        density = kde(x)
        # Scale density to fit the width of the violin
        density = density * (width / max(density))
        # Plot the violin (mirror the density for both sides)
        ax.fill_betweenx(x, positions[i] - density, positions[i] + density, 
                         color=color, edgecolor=edgecolor, alpha=alpha)

# Default violin plot on the first subplot
positions = np.arange(5)
custom_violinplot(ax1, data, positions, width=0.4, color='gray', edgecolor='black', alpha=1.0)

# Set x-axis labels for the first subplot
ax1.set_xticks(range(5))
ax1.set_xticklabels(['E', 'F', 'G', 'H', 'I'])

# Overlay medians as red dots
for i, median in enumerate(medians):
    ax1.plot(i, median, 'ro', markersize=8)

# Overlay vertical lines for quartiles and whiskers
for i, (q1, q2, q3) in enumerate(quartiles):
    ax1.vlines(i, q1, q3, colors='black', linestyles='-', lw=2)  # Q1 to Q3
for i, (w_low, w_high) in enumerate(whiskers):
    ax1.vlines(i, w_low, w_high, colors='black', linestyles='--', lw=1)  # Whiskers

ax1.set_title('Default Violin Plot with Medians and Whiskers')

# Customized violin plot on the second subplot
custom_violinplot(ax2, data, positions, width=0.4, color='blue', edgecolor='black', alpha=0.5)

# Set x-axis labels for the second subplot
ax2.set_xticks(range(5))
ax2.set_xticklabels(['E', 'F', 'G', 'H', 'I'])

ax2.set_title('Customized Violin Plot (No Stats)')

# Set common y-axis label
ax1.set_ylabel('Values')

# Save the plot as a PNG file
plt.savefig("novice.png")