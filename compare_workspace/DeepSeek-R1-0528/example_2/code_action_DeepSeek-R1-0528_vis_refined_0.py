import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

# Generate deterministic data
w = np.linspace(-100, 100, 400)
z = np.sin(w) * 100

# Create 3x3 subplot grid with shared axes
fig, axs = plt.subplots(3, 3, sharex='col', sharey='row', figsize=(10, 8))
plt.subplots_adjust(wspace=0, hspace=0)  # Remove spacing

# Plot functions in each subplot with specified colors
axs[0, 0].plot(w, z, color='blue')
axs[0, 1].plot(w, z**3, color='blue')
axs[0, 2].plot(w + 1, -z, color='yellow')
axs[1, 0].plot(w + 2, -z**3, color='purple')
axs[1, 1].plot(w**2, z**2, color='brown')
axs[1, 2].plot(w**2 + 1, -z**2, color='pink')
axs[2, 0].plot(-w**2 + 2, z**2, color='grey')
axs[2, 1].plot(-w**2 + 3, -z**2, color='black')
axs[2, 2].plot(-w, z, color='white')

# Configure labels and titles
fig.suptitle('Sharing x per column, y per row')
for ax in axs.flat:
    ax.label_outer()  # Hide inner labels

# Set axis labels for outer subplots
axs[2, 0].set_xlabel('w (transformed)')
axs[2, 1].set_xlabel('w (transformed)')
axs[2, 2].set_xlabel('w (transformed)')
axs[0, 0].set_ylabel('z (transformed)')
axs[1, 0].set_ylabel('z (transformed)')
axs[2, 0].set_ylabel('z (transformed)')

# Save as PNG without displaying
plt.savefig('novice_final.png', bbox_inches='tight')