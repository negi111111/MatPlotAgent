import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt

# Parameters
gamma = 1.0
omega = 2.0

# Generate data
x = np.linspace(-2, 2, 1000)
phase_field = 0.5 * (1 + np.tanh(gamma * x))
composition = 0.5 * (1 + np.tanh(omega * x))

# Create figure
fig, ax = plt.subplots(figsize=(10, 6))

# Plot curves
ax.plot(x, phase_field, 'b-', label='Phase Field', linewidth=2)
ax.plot(x, composition, color='orange', label='Composition', linewidth=2)
ax.plot([-2, 0, 2], [0, 0, 1], 'g-', drawstyle='steps-post', 
        label='Sharp Interface', linewidth=2)

# Annotations
ax.text(-1.5, 0.25, 'Phase Field: $\\frac{1}{2} (1 + \\tanh(\\gamma x))$', 
        color='blue', fontsize=10)
ax.text(-1.5, 0.05, 'Composition: $\\frac{1}{2} (1 + \\tanh(\\Omega x))$', 
        color='orange', fontsize=10)
ax.text(-1.95, 0.9, '$\\gamma = 1.0$\n$\\Omega = 2.0$', 
        fontsize=12, verticalalignment='top')
ax.annotate('', xy=(0, 0.5), xytext=(0.8, 0.7),
            arrowprops=dict(arrowstyle='->', lw=1.5, color='black'))

# Axis settings
ax.set_xlabel('x', fontsize=12)
ax.set_ylabel('y', fontsize=12)
ax.set_xlim(-2, 2)
ax.set_ylim(0, 1)
ax.legend(loc='upper left', frameon=False)

# Final adjustments and save
plt.tight_layout()
plt.savefig("novice.png")