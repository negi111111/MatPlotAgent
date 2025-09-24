import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import matplotlib.colors as mcolors

# Set seed for reproducibility
np.random.seed(42)

# Generate data
x_values = np.arange(1, 21)
y_values = np.random.randint(-10, 10, 20)

# Create figure with subplots
fig, axs = plt.subplots(1, 2, figsize=(15, 5))

# First subplot: Uniform transparency
colors = ['blue' if y > 0 else 'orange' for y in y_values]
axs[0].bar(x_values, y_values, color=colors, alpha=0.5, 
           edgecolor='black', linewidth=1)
axs[0].set_title("Uniform transparency value for all bars and edges")
axs[0].set_xlabel("X Values")
axs[0].set_ylabel("Y Values")

# Second subplot: Dynamic transparencies
abs_y = np.abs(y_values)
max_abs = np.max(abs_y)
face_alphas = abs_y / max_abs
edge_alphas = 1 - face_alphas  # Complementary alpha values

for i in range(len(x_values)):
    x = x_values[i]
    y = y_values[i]
    base_color = 'blue' if y > 0 else 'orange'
    face_rgba = mcolors.to_rgba(base_color, alpha=face_alphas[i])
    edge_rgba = (0, 0, 0, edge_alphas[i])  # Black with dynamic alpha
    
    # Calculate bar position and dimensions
    bottom = min(0, y)
    height = abs(y)
    rect = Rectangle((x - 0.4, bottom), 0.8, height,
                     facecolor=face_rgba, edgecolor=edge_rgba, linewidth=1)
    axs[1].add_patch(rect)

axs[1].set_title("Adjusted transparencies for each bar and each edge")
axs[1].set_xlabel("X Values")
axs[1].set_ylabel("Y Values")

# Set consistent axes limits and ticks
x_min, x_max = 0.5, 20.5
y_min, y_max = min(y_values) - 1, max(y_values) + 1
for ax in axs:
    ax.set_xlim(x_min, x_max)
    ax.set_ylim(y_min, y_max)
    ax.set_xticks(x_values)

# Finalize and save
plt.tight_layout()
plt.savefig("novice_final.png")