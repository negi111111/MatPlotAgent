import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import to_rgba

# 1. Make random numbers reproducible
np.random.seed(42)

# 2. Prepare data
x_vals = list(range(1, 21))               # 1 … 20
y_vals = np.random.uniform(-1, 1, 20)     # 20 random floats in [-1, 1]

# 3. Decide face colour of every bar (sign test)
face_colours = ['blue' if y > 0 else 'orange' for y in y_vals]

# 4. Create the figure with two side-by-side subplots
fig, axes = plt.subplots(1, 2, figsize=(14, 5), sharey=True)

# -------- FIRST subplot — uniform transparency everywhere --------
uniform_alpha = 0.6
face_rgba_uniform = [to_rgba(c, uniform_alpha) for c in face_colours]
edge_rgba_uniform = [to_rgba(c, uniform_alpha) for c in face_colours]

axes[0].bar(
    x_vals,
    y_vals,
    color=face_rgba_uniform,
    edgecolor=edge_rgba_uniform
)
axes[0].set_title("Uniform transparency value for all bars and edges")

# -------- SECOND subplot — individual α so face α + edge α = 1 --------
abs_y = np.abs(y_vals)
face_alpha = abs_y / abs_y.max()          # α_face in [0, 1]
edge_alpha = 1.0 - face_alpha             # complementary α_edge

face_rgba_var = [to_rgba(c, fa) for c, fa in zip(face_colours, face_alpha)]
edge_rgba_var = [to_rgba(c, ea) for c, ea in zip(face_colours, edge_alpha)]

axes[1].bar(
    x_vals,
    y_vals,
    color=face_rgba_var,
    edgecolor=edge_rgba_var
)
axes[1].set_title("Adjusted transparencies for each bar and each edge")

# -------- Cosmetics --------
for ax in axes:
    ax.axhline(0, color='black', linewidth=0.7)
    ax.set_xlabel("Index")
axes[0].set_ylabel("Value")

plt.tight_layout()

# -------- Save the figure --------
plt.savefig("novice.png")