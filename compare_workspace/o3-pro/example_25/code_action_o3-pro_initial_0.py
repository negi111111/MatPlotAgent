import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # Registers the 3-D projection

def main() -> None:
    # -------------------------------------------------
    # 1. Prepare 1-D domain and damped sine functions
    # -------------------------------------------------
    s_min, s_max, num = 0.0, 2.0, 400
    s = np.linspace(s_min, s_max, num)

    g  = np.sin(3 * np.pi * s) * np.exp(-s)
    g1 = np.sin(3 * np.pi * (s + 0.1)) * np.exp(-(s + 0.1))
    g2 = np.sin(3 * np.pi * (s + 0.2)) * np.exp(-(s + 0.2))

    # -------------------------------------------------
    # 2. Prepare 2-D domain and surface data
    # -------------------------------------------------
    p_min = q_min = -5.0
    p_max = q_max =  5.0
    pts = 200

    p = np.linspace(p_min, p_max, pts)
    q = np.linspace(q_min, q_max, pts)
    P, Q = np.meshgrid(p, q)

    R = np.sqrt(P**2 + Q**2)
    E = np.cos(R)

    # -------------------------------------------------
    # 3. Build the figure with two subplots
    # -------------------------------------------------
    fig = plt.figure(figsize=(10, 5))
    fig.suptitle('A Story of 2 Subplots', fontsize=16)

    # ---- First subplot: 2-D lines ----
    ax1 = fig.add_subplot(1, 2, 1)
    ax1.plot(s, g,  label='g(s)',        color='navy',       linewidth=1.8)
    ax1.plot(s, g1, label='g(s + 0.1)',  color='firebrick',  linestyle='--', linewidth=1.5)
    ax1.plot(s, g2, label='g(s + 0.2)',  color='forestgreen',linestyle=':',  linewidth=1.5)

    ax1.set_xlabel('s')
    ax1.set_ylabel('g(s)')
    ax1.set_title('Damped sine waves')
    ax1.legend(loc='best')
    ax1.grid(True, linestyle=':')

    # ---- Second subplot: 3-D surface ----
    ax2 = fig.add_subplot(1, 2, 2, projection='3d')
    surface = ax2.plot_surface(P, Q, E,
                               cmap='viridis',
                               edgecolor='none',
                               rstride=1, cstride=1)

    ax2.set_xlabel('P')
    ax2.set_ylabel('Q')
    ax2.set_zlabel('E(P, Q)')
    ax2.set_title('E(P, Q) = cos(√(P² + Q²))')

    fig.colorbar(surface, ax=ax2, shrink=0.6, aspect=10, label='E value')

    # -------------------------------------------------
    # 4. Final layout adjustments and save
    # -------------------------------------------------
    fig.tight_layout(rect=[0, 0.03, 1, 0.95])
    plt.savefig("novice.png")   # <-- Required by the instructions

if __name__ == '__main__':
    main()