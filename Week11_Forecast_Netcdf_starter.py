# This script assumes you have already downloaded several netcdf files
# see the assignment instructions for how to do this
# %%
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import xarray as xr
import rioxarray
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import seaborn as sns
import geopandas as gpd
import fiona
import shapely
from netCDF4 import Dataset
import os
import numpy as np

#NOTE To install the packages you need you should use the followin line:
# conda install xarray dask netCDF4 bottleneck

# %%
# reading in the basin file for mapping
basin_file = os.path.join('../../../data/Shape', 'WBDHU8.shp')
HUC8 = gpd.read_file(basin_file)

#Check the type and see the list of layers
type(HUC8)
HUC8.head()

# %%
# Net CDF file of precip forecast
# https://towardsdatascience.com/handling-netcdf-files-using-xarray-for-absolute-beginners-111a8ab4463f
data_path = os.path.join('C:\\Users\\certain\\Desktop',
                         'gfs.0p25.2021110300.f003.grib2.nc')

# Read in the dataset as an x-array
dataset = xr.open_dataset(data_path)
# look at it
dataset


# We can inspect the metadata of the file like this:
metadata = dataset.attrs
metadata
# And we can grab out any part of it like this:
metadata['title']

# we can also look at other  attributes like this
dataset.values
dataset.dims
dataset.coords

# Focusing on just the precip values
precip = dataset['A_PCP_L1_Accum_1']
precip

# Now to grab out data first lets look at spatail coordinates:
dataset['A_PCP_L1_Accum_1']['lat'].values.shape
# The first 4 lat values
dataset['A_PCP_L1_Accum_1']['lat'].values[:3]
# All of the lat values
dataset['A_PCP_L1_Accum_1']['lat'].values

print("The min and max latitude values in the data is:",
      dataset["A_PCP_L1_Accum_1"]["lat"].values.min(),
      dataset["A_PCP_L1_Accum_1"]["lat"].values.max())
print("The min and max longitude values in the data is:",
      dataset["A_PCP_L1_Accum_1"]["lon"].values.min(),
      dataset["A_PCP_L1_Accum_1"]["lon"].values.max())


# Now looking at the time;
dataset["A_PCP_L1_Accum_1"]["time"].values
dataset["A_PCP_L1_Accum_1"]["time"].values.shape


# Now lets take a slice: Grabbing data for just one point
lat  = dataset["A_PCP_L1_Accum_1"]["lat"].values[1]
lon = dataset["A_PCP_L1_Accum_1"]["lon"].values[1]
print("Long, Lat values:", lon, lat)
one_point = dataset["A_PCP_L1_Accum_1"].sel(lat=lat,
                                               lon=lon)
one_point.shape
precip_val = one_point.values

# Or grabbing out one time
time = dataset["A_PCP_L1_Accum_1"]["time"].values[0]
one_time = dataset["A_PCP_L1_Accum_1"].sel(time=time)
one_time_vals = one_time.values
one_time_vals.shape


# %%
# %%
# Making a map
# values for ploting
lat = one_time['lat'].values
lon = one_time['lon'].values
precip = one_time.values

# set up colormap, levels and colorbar intervals
cmap = plt.get_cmap('Blues')  # pick the desired colormap,
levs = np.arange(0, 5, 0.25)   # sensible levels,
norm = mpl.colors.BoundaryNorm(levs, ncolors=cmap.N, clip=True)

# PlateCarree is just a cylindrical projection
projection = ccrs.PlateCarree()

# start a figure named fig, set axis name, dimesions of fig, and projection
fig, ax = plt.subplots(1, 1, figsize=(6, 6), subplot_kw={
                       'projection': projection})

cs = ax.pcolormesh(lon, lat, precip, transform=projection, cmap=cmap, norm=norm)

# crop extent of map to lat/lon of data
central_lon, central_lat = np.median(lon), np.median(lat)
extent = [np.min(lon)-.125, np.max(lon)+.125,
          np.min(lat)-.125, np.max(lat)+.125]
ax.set_extent(extent)

# add lat lon gridline
ax.gridlines(draw_labels=True,
             xlocs=np.arange(-180, 180, 1.),
             ylocs=np.arange(-90, 90, 1.),
             linewidth=1, color='k', alpha=0.5, linestyle=':')

# add some reference locations to map
ax.plot(-111.8543, 34.5636, 'ko', markersize=6, transform=projection)
ax.text(-111.9, 34.47, 'Camp Verde', fontweight='bold', transform=projection)
ax.plot(-112.4685, 34.5400, 'ko', markersize=6, transform=projection)
ax.text(-112.5, 34.42, 'Prescott', fontweight='bold', transform=projection)
ax.plot(-111.6513, 35.1983, 'ko', markersize=6, transform=projection)
ax.text(-111.62, 35.13, 'Flagstaff', fontweight='bold', transform=projection)

# plotfile = 'forecast_precip_accu.png'
# sf = fig.savefig(plotfile, dpi=300, bbox_inches='tight')
plt.show()

