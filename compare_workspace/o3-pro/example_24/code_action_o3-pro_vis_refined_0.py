import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401  (keeps the 3D projection registered)

def rossler_attractor(a: float, b: float, c: float, initial_conditions, time_steps: int):
    """
    Generate the Rossler attractor trajectory.

    Parameters
    ----------
    a, b, c : float
        Rossler system parameters.
    initial_conditions : tuple(float, float, float)
        Initial state (u0, v0, w0).
    time_steps : int
        Number of integration steps.

    Returns
    -------
    u, v, w : np.ndarray
        Arrays containing the trajectory coordinates.
    """
    # Allocate arrays
    u = np.zeros(time_steps, dtype=float)
    v = np.zeros(time_steps, dtype=float)
    w = np.zeros(time_steps, dtype=float)

    # Set initial conditions
    u[0], v[0], w[0] = initial_conditions

    dt = 0.01  # Fixed, deterministic time‐step

    # Integrate using simple Euler scheme
    for i in range(1, time_steps):
        u[i] = u[i - 1] + (-v[i - 1] - w[i - 1]) * dt
        v[i] = v[i - 1] + (u[i - 1] + a * v[i - 1]) * dt
        w[i] = w[i - 1] + (b + w[i - 1] * (u[i - 1] - c)) * dt

    return u, v, w


if __name__ == "__main__":
    # Rossler parameters and simulation settings
    a, b, c = 0.2, 0.2, 5.7
    initial_conditions = (1.0, 1.0, 1.0)
    time_steps = 10_000

    # Generate trajectory
    u, v, w = rossler_attractor(a, b, c, initial_conditions, time_steps)

    # Create 3-D plot
    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111, projection="3d")

    ax.plot(u, v, w, linewidth=0.5, color="blue")
    ax.set_title("Rossler Attractor", fontsize=14, pad=15)

    ax.set_xlabel("u", labelpad=10)
    ax.set_ylabel("v", labelpad=10)
    ax.set_zlabel("w", labelpad=10)

    # Optional aesthetic tweaks for clarity
    ax.grid(False)
    ax.set_facecolor("white")
    fig.patch.set_facecolor("white")

    # Save exactly one PNG file
    plt.savefig("novice_final.png", dpi=300, bbox_inches="tight")