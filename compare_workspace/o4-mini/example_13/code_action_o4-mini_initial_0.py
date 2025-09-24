import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse, Polygon

# 1. Data for bar plots
x = np.arange(5)
heights = [5, 7, 3, 4, 6]

# 2. Mosaic layout
mosaic = [
    ["A", "B"],
    ["C", "D"],
    ["E", "E"]
]

# 3. Create figure and axes
fig, axes = plt.subplot_mosaic(mosaic, figsize=(10, 8))

# 4. First row
axes["A"].bar(x, heights, color="skyblue", edgecolor="black", hatch="/")
axes["A"].set_title('Row 1: hatch "/"')

axes["B"].bar(x, heights, color="lightgreen", edgecolor="black", hatch="\\")
axes["B"].set_title('Row 1: hatch "\\"')

# 5. Second row
axes["C"].bar(x, heights, color="salmon", edgecolor="black", hatch="x")
axes["C"].set_title('Row 2: hatch "x"')

axes["D"].bar(x, heights, color="gold", edgecolor="black", hatch="o")
axes["D"].set_title('Row 2: hatch "o"')

# 6. Third row: filled cosine curve
ax = axes["E"]
x_fine = np.linspace(0, 4, 400)
y_cos = np.cos(x_fine)

ax.fill_between(
    x_fine, y_cos, 0,
    facecolor="magenta",
    edgecolor="black",
    hatch=".",
    alpha=0.5
)

# Ellipse at center
x_center = (x_fine.min() + x_fine.max()) / 2
y_center = 0.0
ellipse = Ellipse(
    (x_center, y_center),
    width=1.0,
    height=0.5,
    angle=0,
    facecolor="yellow",
    edgecolor="black",
    hatch="*",
    alpha=0.7
)
ax.add_patch(ellipse)

# Polygon triangle at center
verts = [
    (x_center,     y_center + 0.3),
    (x_center - 0.2, y_center - 0.2),
    (x_center + 0.2, y_center - 0.2)
]
polygon = Polygon(
    verts,
    closed=True,
    facecolor="cyan",
    edgecolor="black",
    hatch="/",
    alpha=0.7
)
ax.add_patch(polygon)

# Aspect ratio and limits
ax.set_aspect("equal", adjustable="box")
ax.set_xlim(x_fine.min(), x_fine.max())
ax.set_ylim(y_cos.min(), y_cos.max())
ax.set_title("Row 3: filled cosine + patches")

# 7. Finalize and save
plt.tight_layout()
plt.savefig("novice.png")