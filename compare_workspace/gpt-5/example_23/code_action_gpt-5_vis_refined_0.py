import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define the parameter arrays
alpha = np.linspace(-6 * np.pi, 6 * np.pi, 1000)  # Range for alpha
w = np.linspace(-3, 3, 1000)  # Range for w
p = w**3 + 2  # p is the cube of w plus 2

# Calculate 'a' and 'b'
a = p * np.sin(alpha)  # a is the product of p and the sine of alpha
b = p * np.cos(alpha)  # b is the product of p and the cosine of alpha

# Create the 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(a, b, w, label='parametric curve', color='blue')  # Plot the curve

# Label the axes
ax.set_xlabel('a')
ax.set_ylabel('b')
ax.set_zlabel('w')

# Add a title and legend
ax.set_title('Parametric Curve')
ax.legend()

# Save the plot
plt.savefig('novice_final.png')