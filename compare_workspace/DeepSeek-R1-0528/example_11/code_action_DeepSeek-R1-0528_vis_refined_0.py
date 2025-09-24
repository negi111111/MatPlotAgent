import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt

# Set parameters
gamma = 1.0
omega = 2.0

# Generate data points
x = np.linspace(-2, 2, 400)
phase_field = 0.5 * (1 + np.tanh(gamma * x))
composition = 0.5 * (1 + np.tanh(omega * x))

# Create figure with custom styling
plt.figure(figsize=(10, 6), facecolor='white')
ax = plt.gca()
ax.set_facecolor('#f8f8f8')

# Plot curves with enhanced styling
plt.plot(x, phase_field, color='#1f77b4', linewidth=3, label='Phase Field')
plt.plot(x, composition, color='#ff7f0e', linewidth=3, linestyle='-', label='Composition')

# Add sharp interface lines
plt.axvline(x=0, color='#2ca02c', linestyle='--', linewidth=2, label='Sharp Interface')
plt.axhline(y=0, xmin=0.0, xmax=0.5, color='#2ca02c', linestyle='--', linewidth=2)
plt.axhline(y=1, xmin=0.5, xmax=1.0, color='#2ca02c', linestyle='--', linewidth=2)

# Add annotations with background
text_props = {'bbox': dict(boxstyle='round', facecolor='white', alpha=0.8, edgecolor='none')}
plt.text(-1.8, 0.8, 'Phase Field: 1/2 * (1 + tanh(γx))', 
         color='#1f77b4', fontsize=12, **text_props)
plt.text(-1.8, 0.6, 'Composition: 1/2 * (1 + tanh(Ωx))', 
         color='#ff7f0e', fontsize=12, **text_props)
plt.text(-1.8, 0.4, 'γ = 1.0\nΩ = 2.0', 
         color='black', fontsize=12, **text_props)

# Add arrow annotation
plt.annotate('', xy=(0, 0.5), xytext=(-0.5, 0.5),
             arrowprops=dict(arrowstyle='->', color='black', linewidth=1.5))

# Configure axes
plt.xlabel('x', fontsize=14, labelpad=10)
plt.ylabel('y', fontsize=14, labelpad=10)
plt.xlim(-2, 2)
plt.ylim(0, 1)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)

# Add grid and legend
plt.grid(True, linestyle='--', alpha=0.3)
plt.legend(loc='upper left', fontsize=12, framealpha=0.9)

# Add title
plt.title('Phase Field and Composition Profiles', fontsize=16, pad=15)

# Save as PNG without displaying
plt.tight_layout()
plt.savefig("novice_final.png", dpi=100)