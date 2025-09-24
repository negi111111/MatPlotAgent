import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

# Generate data
z = np.linspace(-10, 10, 100)
w = np.linspace(-10, 10, 100)

# Create a 3x3 grid of subplots with shared axes
fig, axs = plt.subplots(3, 3, sharex='col', sharey='row', figsize=(9, 9))
plt.subplots_adjust(wspace=0, hspace=0)

# Plot the required data
axs[0, 0].plot(w, z, color='black')           # z against w
axs[0, 1].plot(w, z**3, color='blue')         # z**3 against w
axs[0, 2].plot(w + 1, -z, color='yellow')     # -z against w + 1
axs[1, 0].plot(w + 2, -z**3, color='purple')  # -z**3 against w + 2
axs[1, 1].plot(w**2, z**2, color='brown')     # z**2 against w**2
axs[1, 2].plot(w**2 + 1, -z**2, color='pink') # -z**2 against w**2 + 1
axs[2, 0].plot(-w**2 + 2, z**2, color='grey') # z**2 against -w**2 + 2
axs[2, 1].plot(-w**2 + 3, -z**2, color='black') # -z**2 against -w**2 + 3
axs[2, 2].plot(-w, z, color='white')          # z against -w

# Titles for each subplot
axs[0, 0].set_title('Plot 1: z vs w')
axs[0, 1].set_title('Plot 2: z^3 vs w')
axs[0, 2].set_title('Plot 3: -z vs w+1')
axs[1, 0].set_title('Plot 4: -z^3 vs w+2')
axs[1, 1].set_title('Plot 5: z^2 vs w^2')
axs[1, 2].set_title('Plot 6: -z^2 vs w^2+1')
axs[2, 0].set_title('Plot 7: z^2 vs -w^2+2')
axs[2, 1].set_title('Plot 8: -z^2 vs -w^2+3')
axs[2, 2].set_title('Plot 9: z vs -w')

# Set the overall title
fig.suptitle('Sharing x per column, y per row', fontsize=16)

# Show only outer labels/ticks for shared axes
for ax in axs.flat:
    ax.label_outer()

# Label only the outermost subplots (left column y, bottom row x)
for i in range(3):
    axs[i, 0].set_ylabel('Y-axis label')
for j in range(3):
    axs[2, j].set_xlabel('X-axis label')

# Save the plot as a single PNG
plt.savefig('novice_final.png', bbox_inches='tight')