import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # Ensures 3D projection is registered

def rossler(t, y, a, b, c):
    """
    Rössler system derivatives.
    y = [u, v, w]
    du/dt = -v - w
    dv/dt = u + a*v
    dw/dt = b + w*(u - c)
    """
    u, v, w = y
    du = -v - w
    dv = u + a * v
    dw = b + w * (u - c)
    return np.array([du, dv, dw], dtype=float)

def rk4(f, t_eval, y0, args):
    """
    Classic fixed-step 4th-order Runge-Kutta integrator over specified t_eval grid.
    Returns an array with shape (len(y0), len(t_eval)).
    """
    n = len(t_eval)
    y = np.empty((len(y0), n), dtype=float)
    y[:, 0] = y0
    for i in range(1, n):
        t = t_eval[i - 1]
        h = t_eval[i] - t
        yi = y[:, i - 1]

        k1 = f(t, yi, *args)
        k2 = f(t + 0.5 * h, yi + 0.5 * h * k1, *args)
        k3 = f(t + 0.5 * h, yi + 0.5 * h * k2, *args)
        k4 = f(t + h, yi + h * k3, *args)

        y[:, i] = yi + (h / 6.0) * (k1 + 2 * k2 + 2 * k3 + k4)
    return y

def main():
    # Parameters for the Rössler attractor (chaotic regime)
    a = 0.2
    b = 0.2
    c = 5.7

    # Initial conditions (as requested)
    y0 = np.array([1.0, 1.0, 1.0], dtype=float)

    # Time span and evaluation grid
    t0 = 0.0
    t1 = 200.0
    t_eval = np.linspace(t0, t1, 20000)

    # Integrate the system using RK4
    sol_y = rk4(rossler, t_eval, y0, (a, b, c))

    # Extract solution components
    u, v, w = sol_y

    # Plot the 3D trajectory
    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111, projection='3d')
    ax.plot(u, v, w, linewidth=0.5, color='tab:blue')
    ax.set_xlabel('u')
    ax.set_ylabel('v')
    ax.set_zlabel('w')
    ax.set_title('Rossler Attractor')

    plt.tight_layout()
    plt.savefig("novice.png")