import matplotlib
matplotlib.use('Agg')
"""
Deterministic, Matplotlib–only script that

1. Defines a small helper class hierarchy for geographic projections.
2. Uses Matplotlib’s built-in Aitoff projection to emulate a Hammer–Aitoff view.
3. Draws a square bounded by ±60° latitude / longitude.
4. Saves exactly one PNG called  “novice_final.png”.

No interactive windows are opened; `` is intentionally omitted.
"""

import numpy as np
import matplotlib.pyplot as plt


class GeographicProjection:
    """Base utilities shared by all projection helpers."""

    def __init__(self, projection_name: str = "aitoff") -> None:
        # Note: Matplotlib’s 'aitoff' projection already provides the Hammer–Aitoff transform.
        self.fig, self.ax = plt.subplots(subplot_kw={"projection": projection_name})

    # -------------------------- cosmetic helpers -------------------------- #
    def setup_axes(self, title: str = "Aitoff–Hammer Projection") -> None:
        self.ax.set_title(title, pad=20)
        self.ax.grid(True)

    def clear_axes(self) -> None:
        self.ax.cla()

    def set_limits(self, lon_min: float, lon_max: float,
                   lat_min: float, lat_max: float) -> None:
        """
        lon/lat arguments expected in degrees.
        Matplotlib’s geographic projections work in radians internally,
        so convert before handing the values to set_xlim/ylim.
        """
        self.ax.set_xlim(np.radians([lon_min, lon_max]))
        self.ax.set_ylim(np.radians([lat_min, lat_max]))

    def format_coordinates(self, lon_step: int = 30, lat_step: int = 30) -> None:
        deg2rad = np.radians
        # Longitude ticks: -180 … +180°
        lon_ticks_deg = np.arange(-180, 181, lon_step)
        lat_ticks_deg = np.arange(-90,  91, lat_step)

        self.ax.set_xticks(deg2rad(lon_ticks_deg))
        self.ax.set_yticks(deg2rad(lat_ticks_deg))

        # Label ticks in degrees, keep the ° symbol for clarity
        self.ax.xaxis.set_major_formatter(
            plt.FuncFormatter(lambda val, _: f"{np.degrees(val):.0f}°")
        )
        self.ax.yaxis.set_major_formatter(
            plt.FuncFormatter(lambda val, _: f"{np.degrees(val):.0f}°")
        )

    def set_grids(self) -> None:
        self.ax.grid(True)


class AitoffHammerProjection(GeographicProjection):
    """Concrete helper that works with the Hammer–Aitoff projection."""

    def __init__(self) -> None:
        super().__init__(projection_name="aitoff")

    # --------------------------- plotting utils --------------------------- #
    def plot_square(self,
                    lon_extent: float = 60,
                    lat_extent: float = 60,
                    color: str = "royalblue") -> None:
        """
        Draw a closed square centred on (0°,0°) with the specified longitude/latitude extents.
        Default: a square from −60° .. +60° in both lon and lat directions.
        """
        lon_corners = np.radians(
            [-lon_extent, lon_extent, lon_extent, -lon_extent, -lon_extent]
        )
        lat_corners = np.radians(
            [lat_extent,  lat_extent, -lat_extent, -lat_extent,  lat_extent]
        )

        self.ax.plot(lon_corners, lat_corners,
                     marker="o", markersize=4,
                     color=color, lw=1.5)


def main() -> None:
    projection = AitoffHammerProjection()
    projection.setup_axes()
    projection.set_limits(-60, 60, -60, 60)
    projection.format_coordinates()
    projection.set_grids()
    projection.plot_square()

    # Save exactly one PNG file as required by the specification.
    plt.savefig("novice_final.png", bbox_inches="tight", dpi=300)


if __name__ == "__main__":
    main()