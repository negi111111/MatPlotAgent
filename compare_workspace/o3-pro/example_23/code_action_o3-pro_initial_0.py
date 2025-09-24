import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 (needed to register the 3-D projection)

# 1. Define numerical parameters
n_points = 1000
alpha_min, alpha_max = -6 * np.pi, 6 * np.pi
w_min, w_max = -3, 3

# 2. Generate raw data arrays
alpha = np.linspace(alpha_min, alpha_max, n_points)
w = np.linspace(w_min, w_max, n_points)

# 3. Compute helper array p = w³ + 2
p = w ** 3 + 2

# 4. Map (α, w, p) to (a, b, w) coordinates
a = p * np.sin(alpha)
b = p * np.cos(alpha)

# 5. Initialise a 3-D plotting canvas
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')

# 6. Draw the parametric curve
ax.plot(
    a,
    b,
    w,
    label='parametric curve',
    color='tab:blue',
    linewidth=1.5
)

# 7. Decorate the plot
ax.set_xlabel('a')
ax.set_ylabel('b')
ax.set_zlabel('w')
ax.set_title('Parametric Curve')
ax.legend(loc='best')
ax.grid(True)

plt.tight_layout()

# 8. Save the figure
plt.savefig("novice.png", dpi=300)