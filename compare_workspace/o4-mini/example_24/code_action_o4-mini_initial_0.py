import matplotlib
matplotlib.use('Agg')
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def rossler(state, t, a, b, c):
    u, v, w = state
    du = -v - w
    dv = u + a * v
    dw = b + w * (u - c)
    return [du, dv, dw]

# Parameters for the Rossler attractor
a = 0.2
b = 0.2
c = 5.7

# Initial condition
initial_state = [1.0, 1.0, 1.0]

# Time vector
t_max = 100.0
n_steps = 10000
t = np.linspace(0.0, t_max, n_steps)

# Integrate the system of ODEs
solution = odeint(rossler, initial_state, t, args=(a, b, c))

# Unpack the result
u = solution[:, 0]
v = solution[:, 1]
w = solution[:, 2]

# Create 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(u, v, w, linewidth=0.5, color='blue')

# Label axes and title
ax.set_xlabel('u')
ax.set_ylabel('v')
ax.set_zlabel('w')
ax.set_title('Rossler Attractor')

# Adjust layout and save to file
plt.tight_layout()
plt.savefig("novice.png")