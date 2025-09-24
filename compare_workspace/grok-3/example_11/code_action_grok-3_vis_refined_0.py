import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt

# Parameters
gamma = 1.0
omega = 2.0

# x values
x = np.linspace(-2, 2, 400)

# Curves
phase_field = 0.5 * (1 + np.tanh(gamma * x))
composition = 0.5 * (1 + np.tanh(omega * x))

# Plot
plt.figure(figsize=(10, 6))
plt.plot(x, phase_field, color='blue', label='Phase Field: 1/2 * (1 + tanh(gamma * x))')
plt.plot(x, composition, color='orange', label='Composition: 1/2 * (1 + tanh(omega * x))')

# Sharp interface
plt.axvline(x=0, color='green', linestyle='--', label='Sharp Interface')
plt.axhline(y=0, xmin=-2, xmax=0, color='green')
plt.axhline(y=1, xmin=0, xmax=2, color='green')

# Annotations
plt.text(-1.5, 0.8, 'Phase Field: 1/2 * (1 + tanh(gamma * x))', color='blue')
plt.text(-1.5, 0.6, 'Composition: 1/2 * (1 + tanh(omega * x))', color='orange')
plt.text(-1.5, 0.4, 'γ = 1.0\nΩ = 2.0', color='black')

# Arrow annotation
plt.annotate('', xy=(0, 0.5), xytext=(0, 0.6),
             arrowprops=dict(arrowstyle='->', color='black'))
plt.text(0.1, 0.55, 'Intersection', color='black')

# Labels and limits
plt.xlabel('x')
plt.ylabel('y')
plt.xlim(-2, 2)
plt.ylim(0, 1)

# Legend
plt.legend(loc='upper left')

# Save the plot
plt.savefig("novice_final.png")