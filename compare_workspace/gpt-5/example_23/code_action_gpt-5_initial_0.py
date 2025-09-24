import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # registers 3D projection

# 1) Resolution
n_points = 1000

# 2) Parameters and dependent arrays
alpha = np.linspace(-6*np.pi, 6*np.pi, num=n_points, endpoint=True, dtype=float)
w = np.linspace(-3, 3, num=n_points, endpoint=True, dtype=float)
p = w**3 + 2

# 3) Curve coordinates
a = p * np.sin(alpha)
b = p * np.cos(alpha)

# 4) 3D plot setup
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')

# 5) Plot the parametric curve
ax.plot(a, b, w, label='parametric curve', color='C0', linewidth=2)

# 6) Labels, title, legend
ax.set_title('parametric curve')
ax.set_xlabel('a')
ax.set_ylabel('b')
ax.set_zlabel('w')
ax.legend(loc='best')

plt.tight_layout()
plt.savefig("novice.png")