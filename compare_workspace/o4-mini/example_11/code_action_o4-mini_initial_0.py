import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt

# Parameters
gamma = 1.0    # controls the width of the phase‐field interface
omega = 2.0    # controls the width of the composition interface

# Create x grid
x = np.linspace(-2.0, 2.0, 400)

# Compute profiles
phi = 0.5 * (1.0 + np.tanh(gamma * x))
comp = 0.5 * (1.0 + np.tanh(omega * x))

# Set up figure and axes
fig, ax = plt.subplots(figsize=(6, 4))

# Plot the two tanh curves
ax.plot(
    x, phi,
    color='blue',
    linewidth=2,
    label=r'Phase Field: $\tfrac12(1 + \tanh(\gamma x))$, $\gamma=1.0$'
)

ax.plot(
    x, comp,
    color='orange',
    linewidth=2,
    label=r'Composition: $\tfrac12(1 + \tanh(\Omega x))$, $\Omega=2.0$'
)

# Draw the sharp interface
ax.axvline(
    0.0,
    color='green',
    linestyle='-',
    linewidth=1.5,
    label='Sharp interface (x=0)'
)
ax.hlines(
    0.0, xmin=-2.0, xmax=0.0,
    color='green',
    linewidth=1.5
)
ax.hlines(
    1.0, xmin=0.0, xmax=2.0,
    color='green',
    linewidth=1.5
)

# Text annotations above each curve on the left
x_text = -1.5
y_text_phi = 0.5 * (1.0 + np.tanh(gamma * x_text)) + 0.05
ax.text(
    x_text, y_text_phi,
    r'Phase Field: $\tfrac12(1 + \tanh(\gamma x))$, $\gamma=1.0$',
    color='blue',
    fontsize=10
)

y_text_comp = 0.5 * (1.0 + np.tanh(omega * x_text)) + 0.05
ax.text(
    x_text, y_text_comp,
    r'Composition: $\tfrac12(1 + \tanh(\Omega x))$, $\Omega=2.0$',
    color='orange',
    fontsize=10
)

# Parameter values in the upper left
ax.text(
    -1.9, 0.95,
    r'$\gamma = 1.0$' + '\n' + r'$\Omega = 2.0$',
    color='black',
    fontsize=10,
    verticalalignment='top'
)

# Arrow annotation at intersection
ax.annotate(
    'Intersection',
    xy=(0.0, 0.5),
    xytext=(0.7, 0.2),
    arrowprops=dict(arrowstyle='->', color='black'),
    fontsize=10
)

# Axis labels, limits, legend
ax.set_xlabel('x', fontsize=12)
ax.set_ylabel('y', fontsize=12)
ax.set_xlim(-2.0, 2.0)
ax.set_ylim(0.0, 1.0)
ax.legend(loc='upper left', fontsize=9)

# Final layout adjustments and save
plt.tight_layout()
plt.savefig("novice.png")