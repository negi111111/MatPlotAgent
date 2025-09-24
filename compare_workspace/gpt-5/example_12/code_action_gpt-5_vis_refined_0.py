import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import to_rgba

# Set seed for reproducibility
np.random.seed(42)

# Generate data
x = np.arange(1, 21)
y = np.random.uniform(-2, 2, size=20)

# Create figure and subplots
fig, axs = plt.subplots(1, 2, figsize=(14, 6))

# First bar chart with uniform transparency
transparency = 0.5
colors = ['tab:blue' if val > 0 else 'tab:orange' for val in y]
axs[0].bar(x, y, color=colors, edgecolor='black', linewidth=1, alpha=transparency)
axs[0].set_title("Uniform transparency value for all bars and edges")
axs[0].set_xlabel("x")
axs[0].set_ylabel("y")
axs[0].axhline(0, color='gray', linewidth=0.8)
axs[0].grid(True, axis='y', linestyle='--', linewidth=0.5, alpha=0.6)

# Second bar chart with adjusted transparencies
abs_y = np.abs(y)
max_abs_y = np.max(abs_y) if np.max(abs_y) != 0 else 1.0
face_alphas = abs_y / max_abs_y  # Normalize to get face alpha values
edge_alphas = 1 - face_alphas    # Ensure sum of face and edge alpha is 1

for i in range(len(x)):
    face_rgba = to_rgba(colors[i], face_alphas[i])
    edge_rgba = to_rgba('black', edge_alphas[i])
    axs[1].bar(x[i], y[i], color=face_rgba, edgecolor=edge_rgba, linewidth=1)

axs[1].set_title("Adjusted transparencies for each bar and each edge")
axs[1].set_xlabel("x")
axs[1].set_ylabel("y")
axs[1].axhline(0, color='gray', linewidth=0.8)
axs[1].grid(True, axis='y', linestyle='--', linewidth=0.5, alpha=0.6)

# Adjust layout
plt.tight_layout()

# Save the plot
plt.savefig("novice_final.png")