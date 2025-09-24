import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt

# Set random seed for reproducibility
np.random.seed(42)

# Generate data
x = np.arange(1, 21)  # X-values: 1 to 20
y = np.random.uniform(-10, 10, 20)  # Random Y-values

# Determine bar colors based on sign of Y-values
bar_colors = ['blue' if val > 0 else 'orange' for val in y]

# Calculate normalized alpha values
abs_y = np.abs(y)
max_abs = np.max(abs_y) if np.max(abs_y) != 0 else 1
face_alpha = abs_y / max_abs
edge_alpha = 1 - face_alpha

# Create RGBA colors for variable transparency
face_rgba = []
edge_rgba = []
for i in range(len(y)):
    if bar_colors[i] == 'blue':
        face_rgba.append((0, 0, 1, face_alpha[i]))
    else:
        face_rgba.append((1, 0.5, 0, face_alpha[i]))
    edge_rgba.append((0, 0, 0, edge_alpha[i]))

# Create figure with two subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6), sharey=True)

# First plot: Uniform transparency
ax1.bar(x, y, color=bar_colors, alpha=0.5, edgecolor='black', linewidth=1.5)
ax1.set_title("Uniform transparency value for all bars and edges", fontsize=12)
ax1.grid(axis='y', linestyle='--', alpha=0.7)

# Second plot: Variable transparency
ax2.bar(x, y, color=face_rgba, edgecolor=edge_rgba, linewidth=1.5)
ax2.set_title("Adjusted transparencies for each bar and each edge", fontsize=12)
ax2.grid(axis='y', linestyle='--', alpha=0.7)

# Common settings
for ax in (ax1, ax2):
    ax.set_xlabel('X Values', fontsize=10)
    ax.set_xticks(x)
    ax.set_xlim(0, 21)
ax1.set_ylabel('Y Values', fontsize=10)

plt.tight_layout()
plt.savefig("novice.png")  # Save to file