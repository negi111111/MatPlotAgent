import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt

# Parameters and data
gamma = 1.0
omega = 2.0
x = np.linspace(-2, 2, 400)
phase_field = 0.5 * (1 + np.tanh(gamma * x))
composition = 0.5 * (1 + np.tanh(omega * x))

# Create the plot
plt.figure(figsize=(10, 6))

# Plot the curves
plt.plot(x, phase_field, color='blue', label='Phase Field (γ=1.0)')
plt.plot(x, composition, color='orange', label='Composition (Ω=2.0)')

# Set axis limits before adding partial horizontal lines
plt.xlim(-2, 2)
plt.ylim(0, 1)

# Add sharp interface: vertical line at x=0, plus dashed horizontal segments
plt.axvline(x=0, color='green', linestyle='-', label='Sharp interface (x=0)')

# For axhline, xmin/xmax are in axes fraction [0,1]; compute fractions for x=-2,0,2
x_min, x_mid, x_max = -2.0, 0.0, 2.0
frac_left = (x_mid - x_min) / (x_max - x_min)  # 0.5
# Left segment at y=0 from x=-2 to x=0
plt.axhline(y=0, xmin=0.0, xmax=frac_left, color='green', linestyle='--')
# Right segment at y=1 from x=0 to x=2
plt.axhline(y=1, xmin=frac_left, xmax=1.0, color='green', linestyle='--')

# Text annotations
plt.text(-1.5, 0.8, 'Phase Field: 1/2 * (1 + tanh(gamma * x))', color='blue')
plt.text(-1.5, 0.6, 'Composition: 1/2 * (1 + tanh(omega * x))', color='orange')
plt.text(-1.85, 0.92, 'γ = 1.0\nΩ = 2.0', fontsize=10, va='top')

# Arrow annotation to intersection
intersection_x = 0.0
intersection_y = 0.5
plt.annotate(
    'Intersection',
    xy=(intersection_x, intersection_y),
    xytext=(-1.5, 0.4),  # adjusted to avoid overlap with the composition text
    arrowprops=dict(facecolor='black', arrowstyle='->', shrinkA=0, shrinkB=0),
    ha='left',
    va='center'
)

# Labels, title, legend, grid
plt.xlabel('x')
plt.ylabel('y')
plt.title('Phase Field and Composition Profiles')
plt.grid(True, alpha=0.3)
plt.legend(loc='upper left')

# Save the figure as a single PNG
plt.tight_layout()
plt.savefig('novice_final.png')