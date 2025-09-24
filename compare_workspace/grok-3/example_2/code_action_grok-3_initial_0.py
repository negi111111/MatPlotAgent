import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt

# Create data for z and w
z = np.linspace(-2, 2, 100)
w = np.linspace(-2, 2, 100)

# Create a 3x3 grid of subplots with shared x per column and y per row
fig, axs = plt.subplots(3, 3, sharex='col', sharey='row', figsize=(10, 8), constrained_layout=False)

# Remove spacing between subplots
fig.subplots_adjust(wspace=0, hspace=0)

# Plot the data in each subplot as per the requirements
axs[0, 0].plot(w, z, color='red')  # z against w, using red for visibility
axs[0, 1].plot(w, z**3, color='blue')  # z**3 against w
axs[0, 2].plot(w + 1, -z, color='yellow')  # -z against w + 1
axs[1, 0].plot(w + 2, -z**3, color='purple')  # -z**3 against w + 2
axs[1, 1].plot(w**2, z**2, color='brown')  # z**2 against w**2
axs[1, 2].plot(w**2 + 1, -z**2, color='pink')  # -z**2 against w**2 + 1
axs[2, 0].plot(-w**2 + 2, z**2, color='grey')  # z**2 against -w**2 + 2
axs[2, 1].plot(-w**2 + 3, -z**2, color='black')  # -z**2 against -w**2 + 3
axs[2, 2].plot(-w, z, color='cyan')  # z against -w, changed from white to cyan for visibility

# Add y-labels to the leftmost subplots (first column)
for i in range(3):
    axs[i, 0].set_ylabel('Y-axis')

# Add x-labels to the bottom subplots (last row)
for j in range(3):
    axs[2, j].set_xlabel('X-axis')

# Set the overall title for the figure
fig.suptitle('Sharing x per column, y per row', y=1.05)

# Save the plot as a PNG file
plt.savefig("novice.png")