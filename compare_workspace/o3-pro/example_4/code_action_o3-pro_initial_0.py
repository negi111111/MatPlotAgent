import matplotlib
matplotlib.use('Agg')
"""
Scatter plot with confidence ellipses
-------------------------------------
A self-contained script that

1. generates two correlated 2-D Gaussian clouds,
2. combines them into a single 700-point sample,
3. draws the sample, the overall mean cross-hairs,
   three confidence ellipses (1 σ, 2 σ, 3 σ),
   and a highlighted point (1,1).

The output is stored as  'novice.png'.
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse
from numpy.random import multivariate_normal


def main() -> None:
    # ------------------------------------------------------------------
    # 1. Reproducibility
    # ------------------------------------------------------------------
    np.random.seed(42)

    # ------------------------------------------------------------------
    # 2. Two bivariate normal clouds
    # ------------------------------------------------------------------
    mu_1 = (1.0, 1.0)
    mu_2 = (7.0, 6.0)

    cov_1 = np.array([[1.0, 0.60],
                      [0.60, 1.0]])

    cov_2 = np.array([[1.0, 0.85],
                      [0.85, 1.0]])

    n_total = 700
    n_first = n_total // 2
    n_second = n_total - n_first

    data_1 = multivariate_normal(mu_1, cov_1, size=n_first)
    data_2 = multivariate_normal(mu_2, cov_2, size=n_second)

    data = np.vstack((data_1, data_2))
    x, y = data.T  # column vectors

    # ------------------------------------------------------------------
    # 3. Statistics for the ellipses and guide lines
    # ------------------------------------------------------------------
    x_mean, y_mean = data.mean(axis=0)
    cov = np.cov(x, y)

    # Eigen-decomposition (principal axes)
    eigenvals, eigenvecs = np.linalg.eigh(cov)
    order = eigenvals.argsort()[::-1]        # largest first
    eigenvals = eigenvals[order]
    eigenvecs = eigenvecs[:, order]

    # Angle of first principal axis
    vx, vy = eigenvecs[:, 0]
    ellipse_angle_deg = np.degrees(np.arctan2(vy, vx))

    # ------------------------------------------------------------------
    # 4. Plotting
    # ------------------------------------------------------------------
    fig, ax = plt.subplots(figsize=(6, 6))

    # Scatter points
    ax.scatter(x, y, s=15, alpha=0.5, color="slategray", label="data")

    # Cross-hairs at the overall mean
    ax.axhline(y=y_mean, color="grey", linewidth=1)
    ax.axvline(x=x_mean, color="grey", linewidth=1)

    # Confidence ellipses: 1 σ, 2 σ, 3 σ
    for k, colour, lstyle, lbl in (
        (1, "firebrick", "-",  r"1$\sigma$"),
        (2, "fuchsia",   "--", r"2$\sigma$"),
        (3, "blue",      ":",  r"3$\sigma$")
    ):
        width  = 2 * k * np.sqrt(eigenvals[0])   # full width along 1st axis
        height = 2 * k * np.sqrt(eigenvals[1])   # full height along 2nd axis
        ellipse = Ellipse(xy=(x_mean, y_mean),
                          width=width,
                          height=height,
                          angle=ellipse_angle_deg,
                          edgecolor=colour,
                          facecolor="none",
                          linestyle=lstyle,
                          linewidth=2,
                          label=lbl)
        ax.add_patch(ellipse)

    # Highlight the specific point (1,1)
    ax.plot(1, 1, marker="o", color="red", markersize=8, label="highlighted (1,1)")

    # ------------------------------------------------------------------
    # 5. Final touches
    # ------------------------------------------------------------------
    ax.set_title("Different standard deviations", fontsize=14)
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_aspect("equal", adjustable="box")
    ax.margins(0.08)
    ax.legend(loc="best", fontsize=9)

    # ------------------------------------------------------------------
    # 6. Save to file (no interactive window)
    # ------------------------------------------------------------------
    plt.savefig("novice.png", dpi=300)


if __name__ == "__main__":
    main()