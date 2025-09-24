import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt

# Define the range of x values from -2 to 2 with 100 points for smooth curves
x = np.linspace(-2, 2, 100)

# Define parameters
gamma = 1.0
omega = 2.0

# Compute y values for the phase field profile: 1/2 * (1 + tanh(gamma * x))
phase_field = 0.5 * (1 + np.tanh(gamma * x))

# Compute y values for the composition profile: 1/2 * (1 + tanh(omega * x))
composition = 0.5 * (1 + np.tanh(omega * x))

# Create a figure and axis
fig, ax = plt.subplots(figsize=(8, 6))

# Plot the phase field curve in blue
ax.plot(x, phase_field, color='blue', label='Phase Field')

# Plot the composition curve in orange
ax.plot(x, composition, color='darkorange', label='Composition')

# Plot the sharp interface lines in green
ax.axvline(x=0, color='green', linestyle='--', label='Sharp Interface')  # Vertical line at x=0
ax.axhline(y=0, xmin=-2, xmax=0, color='green', linestyle='--')  # Horizontal line y=0 for x<0
ax.axhline(y=1, xmin=0, xmax=2, color='green', linestyle='--')   # Horizontal line y=1 for x>0

# Set axis limits
ax.set_xlim(-2, 2)
ax.set_ylim(0, 1)

# Set axis labels
ax.set_xlabel('x')
ax.set_ylabel('y')

# Add text annotations for the equations above the curves on the left side
ax.text(-1.8, 0.6, 'Phase Field: 1/2 * (1 + tanh(γ * x))', color='blue', fontsize=10)
ax.text(-1.8, 0.8, 'Composition: 1/2 * (1 + tanh(Ω * x))', color='darkorange', fontsize=10)

# Add parameter values in the upper left part
ax.text(-1.8, 0.95, 'γ = 1.0', fontsize=10)
ax.text(-1.8, 0.9, 'Ω = 2.0', fontsize=10)

# Add an arrow pointing to the intersection of the curves (approximately at x=0, y=0.5)
ax.annotate('Intersection', xy=(0, 0.5), xytext=(-0.5, 0.7),
            arrowprops=dict(facecolor='black', shrink=0.05))

# Add a legend in the top left corner
ax.legend(loc='upper left')

# Save the plot as a PNG file
plt.savefig("novice.png")