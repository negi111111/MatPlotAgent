import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

# Create data
z = np.linspace(-2, 2, 100)
w = np.linspace(-2, 2, 100)

# Create a 3x3 grid of subplots with shared x and y axes
fig, axs = plt.subplots(3, 3, sharex='col', sharey='row', figsize=(10, 10))

# Remove spacing between subplots
plt.subplots_adjust(wspace=0, hspace=0)

# Plot the data in each subplot with specified colors
axs[0, 0].plot(w, z, color='red')  # z against w
axs[0, 1].plot(w, z**3, color='blue')  # z**3 against w
axs[0, 2].plot(w + 1, -z, color='yellow')  # -z against w + 1
axs[1, 0].plot(w + 2, -z**3, color='purple')  # -z**3 against w + 2
axs[1, 1].plot(w**2, z**2, color='brown')  # z**2 against w**2
axs[1, 2].plot(w**2 + 1, -z**2, color='pink')  # -z**2 against w**2 + 1
axs[2, 0].plot(-w**2 + 2, z**2, color='grey')  # z**2 against -w**2 + 2
axs[2, 1].plot(-w**2 + 3, -z**2, color='black')  # -z**2 against -w**2 + 3
axs[2, 2].plot(-w, z, color='white')  # z against -w

# Set titles and labels
fig.suptitle('Sharing x per column, y per row', fontsize=16)
for ax in axs.flat:
    ax.label_outer()  # Only label outer axes
axs[2, 0].set_xlabel('X-axis')
axs[2, 1].set_xlabel('X-axis')
axs[2, 2].set_xlabel('X-axis')
axs[0, 0].set_ylabel('Y-axis')
axs[1, 0].set_ylabel('Y-axis')
axs[2, 0].set_ylabel('Y-axis')

# Save the plot to a PNG file
plt.savefig('novice_final.png', bbox_inches='tight')