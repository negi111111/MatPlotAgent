import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

# ------------------------------------------------------------------
# 1. Generate deterministic data
# ------------------------------------------------------------------
z = np.linspace(-10, 10, 100)
w = np.linspace(-10, 10, 100)

# ------------------------------------------------------------------
# 2. Create a 3 × 3 grid of sub-plots with shared axes
# ------------------------------------------------------------------
fig, axs = plt.subplots(3, 3, sharex='col', sharey='row', figsize=(8, 8))
plt.subplots_adjust(wspace=0, hspace=0)     # remove gaps between panels

# ------------------------------------------------------------------
# 3. Populate every panel with the requested curves
# ------------------------------------------------------------------
axs[0, 0].plot(w, z,             color='black')   # z       vs  w
axs[0, 1].plot(w, z**3,          color='blue')    # z**3    vs  w
axs[0, 2].plot(w + 1, -z,        color='yellow')  # -z      vs  w+1

axs[1, 0].plot(w + 2, -z**3,     color='purple')  # -z**3   vs  w+2
axs[1, 1].plot(w**2, z**2,       color='brown')   # z**2    vs  w**2
axs[1, 2].plot(w**2 + 1, -z**2,  color='pink')    # -z**2   vs  w**2+1

axs[2, 0].plot(-w**2 + 2, z**2,  color='grey')    # z**2    vs -w**2+2
axs[2, 1].plot(-w**2 + 3, -z**2, color='black')   # -z**2   vs -w**2+3
axs[2, 2].set_facecolor('k')                      # black bg so a white line is visible
axs[2, 2].plot(-w, z,            color='white')   # z       vs -w

# ------------------------------------------------------------------
# 4. Only outer panels keep tick labels, all others are hidden
# ------------------------------------------------------------------
for row in range(3):
    for col in range(3):
        if row < 2:                        # not bottom row → hide x-tick labels
            axs[row, col].tick_params(labelbottom=False)
        if col > 0:                        # not leftmost col → hide y-tick labels
            axs[row, col].tick_params(labelleft=False)

# ------------------------------------------------------------------
# 5. Minimal outer labels and a global title
# ------------------------------------------------------------------
axs[0, 0].set_ylabel('Y-axis label')       # leftmost column
axs[2, 0].set_xlabel('X-axis label')       # bottom row
fig.suptitle('Sharing x per column, y per row')

# ------------------------------------------------------------------
# 6. Save exactly one PNG file
# ------------------------------------------------------------------
plt.savefig('novice_final.png', dpi=300, bbox_inches='tight')