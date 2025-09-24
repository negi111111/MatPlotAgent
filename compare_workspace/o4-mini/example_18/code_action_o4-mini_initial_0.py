import matplotlib
matplotlib.use('Agg')
# custom_aitoff.py

# fundamental array and plotting libraries
import numpy as np
import matplotlib.pyplot as plt

# Cartopy for coordinate reference systems
import cartopy.crs as ccrs

# optional: for nicer coastlines/background
import cartopy.feature as cfeature

class GeographicProjection:
    """
    A base class that wraps a Cartopy projection and
    provides common setup routines.
    """

    def __init__(self, projection, fig=None):
        # store the Cartopy projection object
        self.projection = projection
        # if the user did not pass in a figure, create one now
        self.fig = fig if fig is not None else plt.figure(figsize=(8, 5))
        # placeholder for the GeoAxes
        self.ax = None
        # the data‐coordinate→display‐coordinate transform
        # (we will always use PlateCarree for lon/lat data input)
        self.transform = ccrs.PlateCarree()

    def setup_axes(self):
        """
        Add a single GeoAxes to the figure, using our projection.
        """
        # 111 = full region, projection=self.projection
        self.ax = self.fig.add_subplot(1, 1, 1, projection=self.projection)
        # draw a light gray land feature for context
        self.ax.add_feature(
            cfeature.LAND.with_scale('50m'),
            facecolor='#dddddd',
            edgecolor='black',
            linewidth=0.5
        )

    def clear_axes(self):
        """
        Clear everything on the axes so we can start fresh.
        """
        self.ax.cla()
        # re‐add the land feature
        self.ax.add_feature(
            cfeature.LAND.with_scale('50m'),
            facecolor='#dddddd',
            edgecolor='black',
            linewidth=0.5
        )

    def set_limits(self, lon_min, lon_max, lat_min, lat_max):
        """
        Set the map extent in degrees.
        """
        # set_extent takes [west, east, south, north], and
        # must be told in what coordinate system those bounds are given
        self.ax.set_extent(
            [lon_min, lon_max, lat_min, lat_max],
            crs=self.transform
        )

    def format_coordinates(self, grid_color='gray', grid_linestyle='--'):
        """
        Draw graticule lines with labels on the left and bottom axes.
        """
        gl = self.ax.gridlines(
            crs=self.transform,
            draw_labels=True,
            linewidth=1,
            color=grid_color,
            linestyle=grid_linestyle,
            alpha=0.7
        )
        # turn off the top and right labels
        gl.top_labels = False
        gl.right_labels = False
        gl.xlabel_style = {'size': 10}
        gl.ylabel_style = {'size': 10}

    def set_lonlat_grid(self, lon_ticks, lat_ticks):
        """
        Explicitly set tick positions for longitude and latitude.
        """
        # xticks in PlateCarree (lon/lat) coordinates
        self.ax.set_xticks(lon_ticks, crs=self.transform)
        self.ax.set_yticks(lat_ticks, crs=self.transform)
        # format ticklabels as degrees
        lon_formatter = ccrs.LongitudeFormatter(zero_direction_label=True)
        lat_formatter = ccrs.LatitudeFormatter()
        self.ax.xaxis.set_major_formatter(lon_formatter)
        self.ax.yaxis.set_major_formatter(lat_formatter)

class AitoffHammerProjection(GeographicProjection):
    """
    A subclass of GeographicProjection that
    specifically uses the equal‐area Hammer projection.
    """

    def __init__(self, fig=None):
        # instantiate the Cartopy Hammer projection
        hammer = ccrs.Hammer()
        # call the base‐class initializer
        super().__init__(projection=hammer, fig=fig)

if __name__ == '__main__':
    # 1. Create our custom projection instance
    proj = AitoffHammerProjection()

    # 2. Set up the axes on the figure
    proj.setup_axes()

    # 3. Optionally clear any default content
    proj.clear_axes()

    # 4. Set the map extent to global
    proj.set_limits(-180, 180, -90, 90)

    # 5. Draw graticules with labels and choose ticks every 30 degrees
    proj.format_coordinates(grid_color='black', grid_linestyle=':')
    proj.set_lonlat_grid(
        lon_ticks=np.arange(-180, 181, 30),
        lat_ticks=np.arange(-90, 91, 30)
    )

    # 6. Prepare the square at ±60° lat, ±60° lon
    lons = np.array([-60,  60,  60, -60, -60])
    lats = np.array([-60, -60,  60,  60, -60])

    # 7. Plot the square in red, telling Cartopy that the data are in
    #    PlateCarree (simple lon/lat) coords
    proj.ax.plot(
        lons,
        lats,
        transform=proj.transform,
        color='red',
        linewidth=2,
        label='60° square'
    )

    # 8. Add a legend and a title
    proj.ax.legend(loc='lower left')
    proj.ax.set_title('Square at ±60° on Aitoff–Hammer Projection')

    # 9. Save the figure to a PNG file
    plt.savefig("novice.png")