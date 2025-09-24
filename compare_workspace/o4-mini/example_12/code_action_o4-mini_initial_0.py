import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors as mcolors

# 1. Fix the random seed for reproducibility
np.random.seed(42)

# 2. Prepare the data
x = np.arange(1, 21)                         # array([ 1,  2, …, 20])
y = np.random.uniform(-10, 10, size=20)      # 20 random floats in [-10,10)

# 3. Build list of bar colors: blue for positive y, orange for non-positive y
bar_colors = ['blue' if yi > 0 else 'orange' for yi in y]

# 4. Compute RGBA color lists for the first subplot (uniform transparency)
uniform_alpha = 0.7
facecolors_uniform = [mcolors.to_rgba(c, uniform_alpha) for c in bar_colors]
edgecolors_uniform = facecolors_uniform.copy()

# 5. Compute RGBA color lists for the second subplot (per-bar, per-edge alpha)
abs_y = np.abs(y)
max_abs = abs_y.max()
normalized = abs_y / max_abs

facealphas = normalized
edgealphas = 1.0 - normalized

facecolors_dynamic = [
    mcolors.to_rgba(bar_colors[i], facealphas[i])
    for i in range(len(y))
]
edgecolors_dynamic = [
    mcolors.to_rgba(bar_colors[i], edgealphas[i])
    for i in range(len(y))
]

# 6. Create figure with two side-by-side subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

# 7. Plot the first bar chart (uniform transparency)
ax1.bar(
    x,
    y,
    color=facecolors_uniform,
    edgecolor=edgecolors_uniform,
    linewidth=1
)
ax1.set_title("Uniform transparency value for all bars and edges")
ax1.set_xlabel("x")
ax1.set_ylabel("y")

# 8. Plot the second bar chart (adjusted transparencies)
ax2.bar(
    x,
    y,
    color=facecolors_dynamic,
    edgecolor=edgecolors_dynamic,
    linewidth=1
)
ax2.set_title("Adjusted transparencies for each bar and each edge")
ax2.set_xlabel("x")
ax2.set_ylabel("y")

# 9. Improve layout and save to file
plt.tight_layout()
plt.savefig("novice.png")