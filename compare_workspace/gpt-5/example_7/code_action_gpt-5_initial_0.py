import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import Normalize
from matplotlib.cm import get_cmap

def main():
    # 1) Fixed random seed for reproducibility
    rng = np.random.default_rng(42)

    # 2) Number of bars
    n_bars = 30

    # 3) Angular positions (linearly spaced, in radians)
    positions = np.linspace(0, 2 * np.pi, n_bars, endpoint=False)

    # 4) Diameters (radial heights) determined by random values
    diameters = rng.uniform(low=0.2, high=1.0, size=n_bars)

    # 5) Thicknesses (angular widths) determined by random values
    spacing = 2 * np.pi / n_bars
    thicknesses = rng.uniform(low=0.1 * spacing, high=0.9 * spacing, size=n_bars)

    # 6) Color mapping from dark to light based on normalized diameters
    norm = Normalize(vmin=diameters.min(), vmax=diameters.max())
    cmap = get_cmap('Greys')  # dark (small) -> light (large)
    colors = cmap(norm(diameters))  # shape (n_bars, 4) RGBA

    # 7) Create polar plot
    fig, ax = plt.subplots(subplot_kw={'projection': 'polar'}, figsize=(8, 6))

    # 8) Draw polar bars with transparency 0.5
    bars = ax.bar(
        positions,              # x: angular positions (radians)
        diameters,              # height: radial lengths
        width=thicknesses,      # width: angular thickness (radians)
        bottom=0.0,             # start from radius 0
        color=colors,           # colors mapped from diameters
        alpha=0.5,              # transparency
        edgecolor='black',
        linewidth=0.5
    )

    # Optional aesthetics
    ax.set_title('Polar Bar Plot (Reproducible, 30 Bars)', va='bottom')
    ax.set_ylim(0, float(diameters.max()) * 1.1)
    ax.grid(True)

    plt.tight_layout()
    plt.savefig("novice.png")