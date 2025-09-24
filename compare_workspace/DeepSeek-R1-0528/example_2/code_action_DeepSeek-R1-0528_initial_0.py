import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt

# Generate sample data
w = np.linspace(0, 10, 100)
z = np.linspace(-5, 5, 100)

# Precompute plot data: (x, y, color) for each subplot
plots = [
    (w, z, None),               # Plot 1: Default color
    (w, z**3, 'blue'),          # Plot 2
    (w + 1, -z, 'yellow'),      # Plot 3
    (w + 2, -z**3, 'purple'),   # Plot 4
    (w**2, z**2, 'brown'),      # Plot 5
    (w**2 + 1, -z**2, 'pink'),  # Plot 6
    (-w**2 + 2, z**2, 'grey'),  # Plot 7
    (-w**2 + 3, -z**2, 'black'),# Plot 8
    (-w, z, 'white')            # Plot 9
]

# Create 3x3 subplot grid with shared axes
fig, axs = plt.subplots(3, 3, sharex='col', sharey='row', figsize=(10, 8))
fig.suptitle('Sharing x per column, y per row')
plt.subplots_adjust(wspace=0, hspace=0)  # Remove spacing

# Plot data on each subplot
for i in range(3):
    for j in range(3):
        idx = i * 3 + j
        x, y_data, color = plots[idx]
        ax = axs[i, j]
        if color:
            ax.plot(x, y_data, color=color)
        else:
            ax.plot(x, y_data)

# Set black background for last subplot (white line visibility)
axs[2, 2].set_facecolor('black')

# Label outermost subplots
for j in range(3):
    axs[2, j].set_xlabel('w (transformed)')  # Bottom row
for i in range(3):
    axs[i, 0].set_ylabel('z (transformed)')  # Leftmost column

# Save the figure
plt.savefig("novice.png")