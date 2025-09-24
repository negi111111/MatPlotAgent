import matplotlib
matplotlib.use('Agg')
"""
Rössler attractor simulation and visualisation

Strictly follows the constraints:
1. Only NumPy (for numerics) and Matplotlib (for plotting) are used.
2. No external ODE solvers (e.g. SciPy) are imported – a classic
   fourth-order Runge–Kutta (RK-4) integrator is coded from scratch.
3. The final figure is written to 'novice.png' and no interactive
   windows are opened.
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D     # registers the 3-D projection

# ---------------------------------------------------------------------
# 1.  Rössler right-hand side
# ---------------------------------------------------------------------
def rossler_rhs(t, y, a=0.2, b=0.2, c=5.7):
    """
    Parameters
    ----------
    t : float
        Current time (unused but kept for API compatibility).
    y : array_like, shape (3,)
        Current state vector [u, v, w].
    a, b, c : float, optional
        Standard Rössler parameters.

    Returns
    -------
    dydt : ndarray, shape (3,)
        Time derivatives [du/dt, dv/dt, dw/dt].
    """
    u, v, w = y
    du_dt = -v - w
    dv_dt =  u + a * v
    dw_dt =  b + w * (u - c)
    return np.array([du_dt, dv_dt, dw_dt], dtype=float)

# ---------------------------------------------------------------------
# 2.  One RK-4 step
# ---------------------------------------------------------------------
def rk4_step(fun, t, y, dt):
    """
    Perform a single Runge–Kutta 4th-order step.

    Parameters
    ----------
    fun : callable
        Derivative function f(t, y) -> dy/dt.
    t : float
        Current time.
    y : ndarray
        Current state.
    dt : float
        Time step.

    Returns
    -------
    y_next : ndarray
        State advanced by dt.
    """
    k1 = fun(t,             y)
    k2 = fun(t + dt/2.0,    y + dt*k1/2.0)
    k3 = fun(t + dt/2.0,    y + dt*k2/2.0)
    k4 = fun(t + dt,        y + dt*k3)
    return y + (dt/6.0)*(k1 + 2*k2 + 2*k3 + k4)

# ---------------------------------------------------------------------
# 3.  Time grid and initial condition
# ---------------------------------------------------------------------
t_start, t_stop, num_points = 0.0, 200.0, 20_000
t_eval = np.linspace(t_start, t_stop, num_points)
y0 = np.array([1.0, 1.0, 1.0], dtype=float)

# ---------------------------------------------------------------------
# 4.  Integrate using the RK-4 scheme
# ---------------------------------------------------------------------
trajectory = np.zeros((num_points, 3), dtype=float)
trajectory[0] = y0

for i in range(1, num_points):
    dt = t_eval[i] - t_eval[i - 1]
    trajectory[i] = rk4_step(rossler_rhs, t_eval[i - 1], trajectory[i - 1], dt)

u, v, w = trajectory.T   # unpack for clarity

# ---------------------------------------------------------------------
# 5.  3-D visualisation
# ---------------------------------------------------------------------
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')

ax.plot(u, v, w, lw=0.5, color='royalblue')
ax.set_xlabel('u')
ax.set_ylabel('v')
ax.set_zlabel('w')
ax.set_title('Rossler Attractor')

plt.tight_layout()
plt.savefig('novice.png')    # mandatory output