#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 27 13:15:16 2024

@author: sydneygoldberg
"""

#8/11/2016 0z-------------------------------------------------------------------------------------------
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import matplotlib.pyplot as plt

from metpy.cbook import get_test_data
from metpy.io import parse_wpc_surface_bulletin
from metpy.plots import (add_metpy_logo, ColdFront, OccludedFront, StationaryFront,
                         StationPlot, WarmFront)
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
#from mpl_toolkits.basemap import Basemap
import cartopy.feature as cf
import cartopy.crs as ccrs
import pygrib

###########################################
# Define a function that can be used to readily plot a bulletin that has been parsed into a
# pandas `DataFrame`. This essentially encapsulates some appropriate plotting methods as well
# as the necessary keyword arguments for giving the expected visual appearance for the
# features.
# Open the GRIB file
grbGFS = pygrib.open('/Users/sydneygoldberg/Desktop/CM_Project/gfs.0p25.2016081100.f000.grib2')

# Select the variables for geopotential height, temperature, and RH
grbGFS.select(name='Geopotential height')
grbGFS.select(name='Relative humidity')

geopot850 = grbGFS[197]; geopot = geopot850['values']
rh850 = grbGFS[199]; rh = rh850['values']

# Read the data
lats, lons = geopot850.latlons()

# Convert to data to correct units
geopotential_data = geopot850.values / 10
humidity_data = rh850.values

def plot_bulletin(ax, data):
    """Plot a dataframe of surface features on a map."""
    # Set some default visual styling
    size = 45
    fontsize = 8
    complete_style = {'HIGH': {'color': 'blue', 'fontsize': size},
                      'LOW': {'color': 'red', 'fontsize': size},
                      'WARM': {'linewidth': 1, 'path_effects': [WarmFront(size=size)]},
                      'COLD': {'linewidth': 1, 'path_effects': [ColdFront(size=size)]},
                      'OCFNT': {'linewidth': 1, 'path_effects': [OccludedFront(size=size)]},
                      'STNRY': {'linewidth': 1, 'path_effects': [StationaryFront(size=size)]},
                      'TROF': {'linewidth': 4, 'linestyle': 'dashed',
                               'edgecolor': 'darkorange'}}

    # Handle H/L points using MetPy's StationPlot class
    for field in ('HIGH', 'LOW'):
        rows = data[data.feature == field]
        x, y = zip(*((pt.x, pt.y) for pt in rows.geometry))
        sp = StationPlot(ax, x, y, transform=ccrs.PlateCarree(), clip_on=True)
        sp.plot_text('C', [field[0]] * len(x), **complete_style[field])
        #sp.plot_parameter('S', rows.strength, **complete_style[field])
        
    
    # Handle all the boundary types
    for field in ('WARM', 'COLD', 'STNRY', 'OCFNT', 'TROF'):
        rows = data[data.feature == field]
        ax.add_geometries(rows.geometry, crs=ccrs.PlateCarree(), **complete_style[field],
                          facecolor='none')


###########################################
# Set up the map for plotting, parse the bulletin, and plot it

# Set up a default figure and map
fig = plt.figure(figsize=(8, 8))
proj=ccrs.LambertConformal(central_longitude=-96.,central_latitude=40.,standard_parallels=(40.,40.))
ax=plt.axes(projection=proj)
ax.set_extent([-95.75, -84.75, 27.75, 34.75])
ax.add_feature(cfeature.COASTLINE)
ax.add_feature(cfeature.OCEAN)
ax.add_feature(cfeature.LAND)
ax.add_feature(cfeature.BORDERS)
ax.add_feature(cfeature.STATES)
ax.add_feature(cfeature.LAKES)

gl = ax.gridlines(crs=ccrs.PlateCarree(), draw_labels=True,
                  linewidth=2, color='white', alpha=0.5, linestyle='--')

gl.top_labels = False
gl.left_labels = False
gl.bottom_labels = False

map=plt.contourf(lons,lats,rh,np.arange(70,101,10), cmap=plt.cm.YlGn,transform=ccrs.PlateCarree())
cbar = plt.colorbar (location='bottom')
cbar.set_label ('Relative Humidity (%)')

# Plot geopotential height contours
cpot=plt.contour (lons, lats, geopotential_data, np.arange(np.min(geopotential_data),np.max(geopotential_data),2), linewidths=1.5, colors='black', linestyles='solid', transform=ccrs.PlateCarree())

# Parse the bulletin and plot it
df = parse_wpc_surface_bulletin('/Users/sydneygoldberg/Desktop/CompMethodsslay/afos.txt')
plot_bulletin(ax, df)

plot_bulletin(ax, df)

ax.set_title(f'WPC Surface Analysis Valid {df.valid.dt.strftime("%HZ %d %b %Y")[0]} with Relative Humidity and 850 mb Heights')
plt.show()

#8/12/2016 0z-------------------------------------------------------------------------------------------
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import matplotlib.pyplot as plt

from metpy.cbook import get_test_data
from metpy.io import parse_wpc_surface_bulletin
from metpy.plots import (add_metpy_logo, ColdFront, OccludedFront, StationaryFront,
                         StationPlot, WarmFront)
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
#from mpl_toolkits.basemap import Basemap
import cartopy.feature as cf
import cartopy.crs as ccrs
import pygrib

###########################################
# Define a function that can be used to readily plot a bulletin that has been parsed into a
# pandas `DataFrame`. This essentially encapsulates some appropriate plotting methods as well
# as the necessary keyword arguments for giving the expected visual appearance for the
# features.
# Open the GRIB file
grbGFS = pygrib.open('/Users/sydneygoldberg/Desktop/CM_Project/gfs.0p25.2016081200.f000.grib2')

# Select the variables for geopotential height, temperature, and RH
grbGFS.select(name='Geopotential height')
grbGFS.select(name='Relative humidity')

geopot850 = grbGFS[197]; geopot = geopot850['values']
rh850 = grbGFS[199]; rh = rh850['values']

# Read the data
lats, lons = geopot850.latlons()

# Convert to data to correct units
geopotential_data = geopot850.values / 10
humidity_data = rh850.values

def plot_bulletin(ax, data):
    """Plot a dataframe of surface features on a map."""
    # Set some default visual styling
    size = 45
    fontsize = 8
    complete_style = {'HIGH': {'color': 'blue', 'fontsize': size},
                      'LOW': {'color': 'red', 'fontsize': size},
                      'WARM': {'linewidth': 1, 'path_effects': [WarmFront(size=size)]},
                      'COLD': {'linewidth': 1, 'path_effects': [ColdFront(size=size)]},
                      'OCFNT': {'linewidth': 1, 'path_effects': [OccludedFront(size=size)]},
                      'STNRY': {'linewidth': 1, 'path_effects': [StationaryFront(size=size)]},
                      'TROF': {'linewidth': 4, 'linestyle': 'dashed',
                               'edgecolor': 'darkorange'}}

    # Handle H/L points using MetPy's StationPlot class
    for field in ('HIGH', 'LOW'):
        rows = data[data.feature == field]
        x, y = zip(*((pt.x, pt.y) for pt in rows.geometry))
        sp = StationPlot(ax, x, y, transform=ccrs.PlateCarree(), clip_on=True)
        sp.plot_text('C', [field[0]] * len(x), **complete_style[field])
        #sp.plot_parameter('S', rows.strength, **complete_style[field])
        
    
    # Handle all the boundary types
    for field in ('WARM', 'COLD', 'STNRY', 'OCFNT', 'TROF'):
        rows = data[data.feature == field]
        ax.add_geometries(rows.geometry, crs=ccrs.PlateCarree(), **complete_style[field],
                          facecolor='none')


###########################################
# Set up the map for plotting, parse the bulletin, and plot it

# Set up a default figure and map
fig = plt.figure(figsize=(8, 8))
proj=ccrs.LambertConformal(central_longitude=-96.,central_latitude=40.,standard_parallels=(40.,40.))
ax=plt.axes(projection=proj)
ax.set_extent([-95.75, -84.75, 27.75, 34.75])
ax.add_feature(cfeature.COASTLINE)
ax.add_feature(cfeature.OCEAN)
ax.add_feature(cfeature.LAND)
ax.add_feature(cfeature.BORDERS)
ax.add_feature(cfeature.STATES)
ax.add_feature(cfeature.LAKES)

gl = ax.gridlines(crs=ccrs.PlateCarree(), draw_labels=True,
                  linewidth=2, color='white', alpha=0.5, linestyle='--')

gl.top_labels = False
gl.left_labels = False
gl.bottom_labels = False

map=plt.contourf(lons,lats,rh,np.arange(70,101,10), cmap=plt.cm.YlGn,transform=ccrs.PlateCarree())
cbar = plt.colorbar (location='bottom')
cbar.set_label ('Relative Humidity (%)')

# Plot geopotential height contours
cpot=plt.contour (lons, lats, geopotential_data, np.arange(np.min(geopotential_data),np.max(geopotential_data),2), linewidths=1.5, colors='black', linestyles='solid', transform=ccrs.PlateCarree())

# Parse the bulletin and plot it
df = parse_wpc_surface_bulletin('/Users/sydneygoldberg/Desktop/CM_Project/afos8_12_16.txt')
plot_bulletin(ax, df)

plot_bulletin(ax, df)

ax.set_title(f'WPC Surface Analysis Valid {df.valid.dt.strftime("%HZ %d %b %Y")[0]} with Relative Humidity and 850 mb Heights')
plt.show()