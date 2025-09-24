import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# 1. Define the parameter array
t = np.linspace(0, 4 * np.pi + 0.1, 1000)

# 2. Define the parametric equations
x = np.cos(t)
y = np.sin(2 * t)
z = np.cos(4 * t)

# 3. Calculate which indices get error bars
#    Every 20th point, but only if the block index % 3 is 0 or 2
i = np.arange(len(t))
mask = (i % 20 == 0) & ( ((i // 20) % 3 == 0) | ((i // 20) % 3 == 2) )

# 4. Extract the points for error bars
x_err = x[mask]
y_err = y[mask]
z_err = z[mask]
error = 0.3

# 5. Create the 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# 6. Plot the parametric curve
ax.plot(x, y, z, label='Parametric Curve')

# 7. Add error bars in the Z direction at the selected points
ax.errorbar(x_err, y_err, z_err, zerr=error, fmt='o', color='r', label='Error Bars')

# 8. Label the axes
ax.set_xlabel('X label')
ax.set_ylabel('Y label')
ax.set_zlabel('Z label')

# 9. Add a legend
ax.legend()

# 10. Save the figure (no interactive window)
plt.savefig('novice_final.png')