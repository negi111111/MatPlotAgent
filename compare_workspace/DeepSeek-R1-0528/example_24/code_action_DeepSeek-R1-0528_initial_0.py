import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Parameters for the Rössler system
a = 0.2
b = 0.2
c = 5.7

# Initial conditions
u0, v0, w0 = 1.0, 1.0, 1.0

# Time step and number of steps
h = 0.01
num_steps = 10000

# Arrays to store the solution
u = np.zeros(num_steps)
v = np.zeros(num_steps)
w = np.zeros(num_steps)

# Set initial values
u[0], v[0], w[0] = u0, v0, w0

# Function defining the Rössler derivatives
def rossler_deriv(u_val, v_val, w_val, a, b, c):
    du = -v_val - w_val
    dv = u_val + a * v_val
    dw = b + w_val * (u_val - c)
    return du, dv, dw

# Runge-Kutta 4th order integration
for i in range(num_steps - 1):
    # Calculate k1 values
    k1u, k1v, k1w = rossler_deriv(u[i], v[i], w[i], a, b, c)
    k1u *= h
    k1v *= h
    k1w *= h
    
    # Calculate k2 values
    u2 = u[i] + k1u / 2
    v2 = v[i] + k1v / 2
    w2 = w[i] + k1w / 2
    k2u, k2v, k2w = rossler_deriv(u2, v2, w2, a, b, c)
    k2u *= h
    k2v *= h
    k2w *= h
    
    # Calculate k3 values
    u3 = u[i] + k2u / 2
    v3 = v[i] + k2v / 2
    w3 = w[i] + k2w / 2
    k3u, k3v, k3w = rossler_deriv(u3, v3, w3, a, b, c)
    k3u *= h
    k3v *= h
    k3w *= h
    
    # Calculate k4 values
    u4 = u[i] + k3u
    v4 = v[i] + k3v
    w4 = w[i] + k3w
    k4u, k4v, k4w = rossler_deriv(u4, v4, w4, a, b, c)
    k4u *= h
    k4v *= h
    k4w *= h
    
    # Update next step values
    u[i+1] = u[i] + (k1u + 2*k2u + 2*k3u + k4u) / 6
    v[i+1] = v[i] + (k1v + 2*k2v + 2*k3v + k4v) / 6
    w[i+1] = w[i] + (k1w + 2*k2w + 2*k3w + k4w) / 6

# Create 3D plot
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Plot trajectory using high-contrast colors
ax.plot(u, v, w, c='#1f77b4', lw=0.5)  # Using matplotlib default blue

# Set labels and title with increased font size
ax.set_title("Rössler Attractor", fontsize=16)
ax.set_xlabel('u', fontsize=12)
ax.set_ylabel('v', fontsize=12)
ax.set_zlabel('w', fontsize=12)

# Adjust viewing angle for better perspective
ax.view_init(elev=20, azim=-70)

# Save as PNG without displaying
plt.savefig("novice.png", dpi=150, bbox_inches='tight')