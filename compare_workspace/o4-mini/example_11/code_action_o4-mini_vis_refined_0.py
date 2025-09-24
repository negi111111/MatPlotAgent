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

# Create plot
plt.figure(figsize=(10, 6))

# Plot curves
plt.plot(x, phase_field, color='blue', label='Phase Field: 1/2 * (1 + tanh(γ x))')
plt.plot(x, composition, color='orange', label='Composition: 1/2 * (1 + tanh(Ω x))')

# Sharp interface lines
plt.axvline(x=0, color='green', linestyle='--', label='Sharp Interface (x=0)')
plt.axhline(y=0, color='green', linestyle='--')
plt.axhline(y=1, color='green', linestyle='--')

# Text annotations
plt.text(-1.5, 0.8, 'Phase Field: 1/2 * (1 + tanh(γ x))', fontsize=10, color='blue')
plt.text(-1.5, 0.6, 'Composition: 1/2 * (1 + tanh(Ω x))', fontsize=10, color='orange')
plt.text(-1.8, 0.9, 'γ = 1.0\nΩ = 2.0', fontsize=10, color='black')

# Arrow annotation pointing at intersection
plt.annotate(
    '', 
    xy=(0, 0.5), 
    xytext=(-0.5, 0.5),
    arrowprops=dict(arrowstyle='->', color='black')
)

# Labels and limits
plt.xlabel('x')
plt.ylabel('y')
plt.xlim(-2, 2)
plt.ylim(0, 1)

# Legend
plt.legend(loc='upper left')

# Save the figure
plt.savefig('novice_final.png')