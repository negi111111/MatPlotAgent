import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # ensures 3D plotting support

# 1. Number of sample points
N = 1000

# 2. Parametric arrays
alpha = np.linspace(-6 * np.pi, 6 * np.pi, N)
w     = np.linspace(-3.0,       3.0,       N)

# 3. Compute p = w^3 + 2
p = w**3 + 2

# 4. Compute a and b
a = p * np.sin(alpha)
b = p * np.cos(alpha)

# 5. Create figure and 3D axes
fig = plt.figure()
ax  = fig.add_subplot(111, projection='3d')

# 6. Plot the parametric curve
ax.plot(a, b, w,
        label='parametric curve',
        color='blue',
        linewidth=1.5)

# 7. Label axes
ax.set_xlabel('a = p·sin(alpha)')
ax.set_ylabel('b = p·cos(alpha)')
ax.set_zlabel('w')

# 8. Add legend
ax.legend(loc='best')

# 9. Save the plot to a PNG file
plt.savefig("novice.png")