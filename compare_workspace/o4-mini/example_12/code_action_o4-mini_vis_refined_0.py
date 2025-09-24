import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

# Ensure reproducibility
np.random.seed(42)

# Generate data
x = np.arange(1, 21)
y = np.random.randint(-10, 10, size=20)

# Define bar colors based on sign of y
colors = ['blue' if val > 0 else 'orange' for val in y]

# Create figure and subplots
fig, axs = plt.subplots(1, 2, figsize=(12, 6))

# First bar chart: uniform transparency
alpha_value = 0.5
axs[0].bar(x, y, color=colors, alpha=alpha_value, edgecolor='black', linewidth=1)
axs[0].set_title("Uniform transparency for all bars and edges")
axs[0].set_xlabel("x")
axs[0].set_ylabel("y")

# Second bar chart: adjusted transparencies per bar and edge
abs_y = np.abs(y)
max_abs_y = np.max(abs_y)
face_alpha = abs_y / max_abs_y           # normalized face alpha
edge_alpha = 1.0 - face_alpha             # ensure face_alpha + edge_alpha = 1

for xi, yi, col, fa, ea in zip(x, y, colors, face_alpha, edge_alpha):
    axs[1].bar(
        xi,
        yi,
        color=col,
        alpha=fa,
        edgecolor=(0, 0, 0, ea),
        linewidth=1
    )

axs[1].set_title("Adjusted transparencies for each bar and each edge")
axs[1].set_xlabel("x")
axs[1].set_ylabel("y")

# Layout adjustment and save
plt.tight_layout()
plt.savefig("novice_final.png")