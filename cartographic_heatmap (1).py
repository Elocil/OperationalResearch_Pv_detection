import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

import geopandas as gpd
from shapely.geometry import Point
import contextily as ctx

# ===============================
# LOAD CSV
# ===============================
df = pd.read_csv("lyon7_2018.csv")

# mean over time at each grid point
m = df.groupby(["latitude", "longitude"])["GHI"].mean().reset_index()

# Convert to GeoDataFrame (WGS84)
gdf = gpd.GeoDataFrame(
    m,
    geometry=[Point(xy) for xy in zip(m["longitude"], m["latitude"])],
    crs="EPSG:4326"
)

# Project to Web Mercator (needed for OSM tiles)
gdf_3857 = gdf.to_crs(epsg=3857)

# ===============================
# MAKE A GRID IMAGE IN 3857
# ===============================
# We'll build a regular grid in 3857 and interpolate using nearest neighbor on the CAMS grid points.

# Extract x/y and values
x = gdf_3857.geometry.x.values
y = gdf_3857.geometry.y.values
v = gdf_3857["GHI"].values

# Build pivot-like grid using unique x/y from CAMS points (regular enough)
xu = np.unique(x)
yu = np.unique(y)

# Create 2D grid of values
# (Nearest neighbor fill using exact grid points)
grid = np.full((len(yu), len(xu)), np.nan)

# Map each point into the grid
x_index = {val: i for i, val in enumerate(xu)}
y_index = {val: i for i, val in enumerate(yu)}
for xi, yi, vi in zip(x, y, v):
    grid[y_index[yi], x_index[xi]] = vi

# Extent for imshow
extent = [xu.min(), xu.max(), yu.min(), yu.max()]

# ===============================
# PLOT
# ===============================
fig, ax = plt.subplots(figsize=(8, 7))

# Base map first (tiles)
ax.set_xlim(extent[0], extent[1])
ax.set_ylim(extent[2], extent[3])
ctx.add_basemap(ax, source=ctx.providers.OpenStreetMap.Mapnik, zoom=9)

# Heatmap overlay
im = ax.imshow(
    grid,
    origin="lower",
    extent=extent,
    alpha=0.55,          # transparency so you see the map
    aspect="auto"
)
cbar = plt.colorbar(im, ax=ax, label="Mean GHI")

ax.set_title("Mean GHI – Lyon region – July 2018 (clear-sky) with OSM basemap")
ax.set_xlabel("Web Mercator X")
ax.set_ylabel("Web Mercator Y")

plt.tight_layout()
plt.savefig("map_meanGHI_lyon7_2018_osm.png", dpi=200)
plt.show()

print("✅ Saved: map_meanGHI_lyon7_2018_osm.png")
