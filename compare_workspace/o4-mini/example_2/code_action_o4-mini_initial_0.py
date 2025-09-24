import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt

# Prepare data
w = np.linspace(-2, 2, 100)
z = w

# Create 3x3 subplots with shared axes
fig, axes = plt.subplots(
    nrows=3,
    ncols=3,
    sharex='col',
    sharey='row',
    figsize=(8, 8)
)

# Remove spacing between subplots
plt.subplots_adjust(wspace=0, hspace=0)

# Top row
axes[0, 0].plot(w,       z,       color='C0')     # 1. z vs. w
axes[0, 1].plot(w,       z**3,    color='blue')   # 2. z**3 vs. w
axes[0, 2].plot(w + 1,  -z,       color='yellow') # 3. -z vs. (w + 1)

# Middle row
axes[1, 0].plot(w + 2,  -z**3,    color='purple') # 4. -z**3 vs. (w + 2)
axes[1, 1].plot(w**2,    z**2,    color='brown')  # 5. z**2 vs. w**2
axes[1, 2].plot(w**2 + 1,-z**2,    color='pink')   # 6. -z**2 vs. (w**2 + 1)

# Bottom row
axes[2, 0].plot(-w**2 + 2,  z**2, color='grey')   # 7. z**2 vs. (-w**2 + 2)
axes[2, 1].plot(-w**2 + 3, -z**2, color='black')  # 8. -z**2 vs. (-w**2 + 3)
axes[2, 2].plot(-w,         z,   color='white')   # 9. z vs. -w

# Only show outer tick labels
for ax in axes.flat:
    ax.label_outer()

# Overall title
fig.suptitle('Sharing x per column, y per row')

# Save to file
plt.savefig("novice.png")