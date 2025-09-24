import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

# Create data
z = np.linspace(-2, 2, 100)
w = np.linspace(-2, 2, 100)

# Create a 3x3 grid of subplots with shared axes
fig, axs = plt.subplots(3, 3, sharex='col', sharey='row')
plt.subplots_adjust(wspace=0, hspace=0)

# Top row
axs[0, 0].plot(w, z, color='black')        # z against w
axs[0, 1].plot(w, z**3, color='blue')      # z**3 against w
axs[0, 2].plot(w + 1, -z, color='yellow')  # -z against w + 1

# Middle row
axs[1, 0].plot(w + 2, -z**3, color='purple')  # -z**3 against w + 2
axs[1, 1].plot(w**2, z**2, color='brown')     # z**2 against w**2
axs[1, 2].plot(w**2 + 1, -z**2, color='pink') # -z**2 against w**2 + 1

# Bottom row
axs[2, 0].plot(-w**2 + 2, z**2, color='grey')   # z**2 against -w**2 + 2
axs[2, 1].plot(-w**2 + 3, -z**2, color='black') # -z**2 against -w**2 + 3
axs[2, 2].plot(-w, z, color='white')            # z against -w

# Overall title
fig.suptitle('Sharing x per column, y per row')

# Label only the outermost subplots
axs[0, 0].set_ylabel('z and -z')
axs[1, 0].set_ylabel('z**2 and -z**2')
axs[2, 0].set_ylabel('z**2 and -z**2')

axs[2, 0].set_xlabel('w and -w')
axs[2, 1].set_xlabel('w**2 and -w**2')
axs[2, 2].set_xlabel('w + 1 and -w + 1')

# Save the figure
plt.savefig('novice_final.png')