import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # Registers 3D projection

def main():
    # 1) Initialize RNG with fixed seed
    rng = np.random.default_rng(1234567)

    # 2) Generate two sets of 200 random values in [-5, 5]
    x_values = rng.uniform(low=-5.0, high=5.0, size=200)
    y_values = rng.uniform(low=-5.0, high=5.0, size=200)

    # 3) Compute a 2D histogram with 10 bins across [-5, 5] for both axes
    H, xedges, yedges = np.histogram2d(
        x_values,
        y_values,
        bins=[10, 10],
        range=[[-5.0, 5.0], [-5.0, 5.0]]
    )

    # 4) Prepare bar positions (lower-left), widths, and heights for 3D bar plot
    xpos_grid, ypos_grid = np.meshgrid(xedges[:-1], yedges[:-1], indexing='ij')
    xpos = xpos_grid.ravel()
    ypos = ypos_grid.ravel()

    dx_vals = np.diff(xedges)
    dy_vals = np.diff(yedges)
    dx_grid, dy_grid = np.meshgrid(dx_vals, dy_vals, indexing='ij')
    dx = dx_grid.ravel()
    dy = dy_grid.ravel()

    zpos = np.zeros_like(xpos)
    dz = H.ravel()

    # 5) Create the 3D bar plot
    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111, projection='3d')

    ax.bar3d(
        xpos,
        ypos,
        zpos,
        dx,
        dy,
        dz,
        color='steelblue',
        shade=True,
        alpha=0.9
    )

    ax.set_title('3D Bar Plot of 2D Histogram (10 bins, range [-5, 5])')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Count')
    ax.set_xlim(-5, 5)
    ax.set_ylim(-5, 5)
    ax.set_zlim(0, dz.max() if dz.size > 0 else 1)

    plt.tight_layout()
    plt.savefig("novice.png", dpi=150)