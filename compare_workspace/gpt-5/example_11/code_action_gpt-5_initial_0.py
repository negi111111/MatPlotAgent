import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt

# Parameters
gamma = 1.0
omega = 2.0

# Domain
x = np.linspace(-2.0, 2.0, 1000)

# Curves
y_phase = 0.5 * (1 + np.tanh(gamma * x))
y_comp = 0.5 * (1 + np.tanh(omega * x))

# Figure and axes
fig, ax = plt.subplots(figsize=(8, 5))

# Plot curves
ax.plot(x, y_phase, color='blue', linewidth=2.0, label='Phase Field (γ=1.0)')
ax.plot(x, y_comp, color='orange', linewidth=2.0, label='Composition (Ω=2.0)')

# Sharp interface lines (green)
ax.axvline(x=0.0, color='green', linewidth=2.0, label='Sharp interface (x=0)')
ax.hlines(y=0.0, xmin=-2.0, xmax=0.0, color='green', linewidth=2.0)
ax.hlines(y=1.0, xmin=0.0, xmax=2.0, color='green', linewidth=2.0)

# Text annotations above curves on the left side
x_left = -1.5
y_left_phase = 0.5 * (1 + np.tanh(gamma * x_left))
y_left_comp = 0.5 * (1 + np.tanh(omega * x_left))

ax.text(x_left, y_left_phase + 0.08,
        'Phase Field: 1/2 * (1 + tanh(gamma * x))',
        color='blue', ha='left', va='bottom')

ax.text(x_left, y_left_comp + 0.08,
        'Composition: 1/2 * (1 + tanh(omega * x))',
        color='orange', ha='left', va='bottom')

# Parameter text in upper-left
ax.text(0.02, 0.95, 'γ = 1.0\nΩ = 2.0',
        transform=ax.transAxes, ha='left', va='top', color='black')

# Arrow annotation to intersection (0, 0.5)
ax.annotate('Intersection',
            xy=(0.0, 0.5),
            xytext=(-1.2, 0.7),
            textcoords='data',
            ha='center', va='center',
            arrowprops={'arrowstyle': '->', 'color': 'black'})

# Labels, limits, legend
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_xlim(-2.0, 2.0)
ax.set_ylim(0.0, 1.0)
ax.legend(loc='upper left')

# Render and save
plt.tight_layout()
plt.savefig("novice.png")