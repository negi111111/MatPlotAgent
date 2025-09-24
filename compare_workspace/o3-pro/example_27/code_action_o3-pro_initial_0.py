import matplotlib
matplotlib.use('Agg')
# 3-D stem plot of sin(x) – π/4 and cos(x) – π/4
# ------------------------------------------------
# Requirements:
#   • NumPy for calculations
#   • Matplotlib for plotting (no external high-level wrappers)
#   • Final figure saved as "novice.png"

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D   # registers the 3-D projection

# --------------------------------------------------------------------
# 1. Generate the x-axis samples (0 … 4π, inclusive)
num_pts = 50
x = np.linspace(0, 4 * np.pi, num_pts)

# 2. Create the two data sets (shifted downward by π/4)
shift = np.pi / 4
y_sin = np.sin(x) - shift
y_cos = np.cos(x) - shift

# 3. Place each data set on its own “rail” in the y-dimension
y_pos_sin = np.zeros_like(x)   # rail at y = 0
y_pos_cos = np.ones_like(x)    # rail at y = 1

# --------------------------------------------------------------------
# 4. Build the figure and 3-D axes
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111, projection='3d')

# 5. Draw the stem plots
#    (Different colours for clarity; thin black baseline)
ax.stem(x, y_pos_sin, y_sin,
        linefmt='b-', markerfmt='bo', basefmt='k-', label='sin(x) – π/4')
ax.stem(x, y_pos_cos, y_cos,
        linefmt='r-', markerfmt='ro', basefmt='k-', label='cos(x) – π/4')

# --------------------------------------------------------------------
# 6. Decorate the plot
ax.set_xlabel('x')
ax.set_ylabel('Dataset rail (0 = sin, 1 = cos)')
ax.set_zlabel('Amplitude')
ax.set_title('3-D stem plot of sin(x) – π/4 and cos(x) – π/4 from 0 to 4π')
ax.legend()

# Frame the data neatly
ax.set_xlim(0, 4 * np.pi)
ax.set_ylim(-0.5, 1.5)
ax.set_zlim(min(y_sin.min(), y_cos.min()) - 0.5,
            max(y_sin.max(), y_cos.max()) + 0.5)

plt.tight_layout()

# --------------------------------------------------------------------
# 7. Save the figure as the required PNG file
plt.savefig("novice.png")