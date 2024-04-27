# Copyright (c) 2023 MetPy Developers.
# Distributed under the terms of the BSD 3-Clause License.
# SPDX-License-Identifier: BSD-3-Clause
"""
===============
Plotting Fronts
===============

This uses MetPy to decode text surface analysis bulletins from the Weather Prediction Center.
The features in this bulletin are then plotted on a map, making use of MetPy's various
path effects for matplotlib than can be used to represent a line as a traditional front.
"""
#8/11/2016 0z-------------------------------------------------------------------------------------------
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import matplotlib.pyplot as plt

from metpy.cbook import get_test_data
from metpy.io import parse_wpc_surface_bulletin
from metpy.plots import (add_metpy_logo, ColdFront, OccludedFront, StationaryFront,
                         StationPlot, WarmFront)

###########################################
# Define a function that can be used to readily plot a bulletin that has been parsed into a
# pandas `DataFrame`. This essentially encapsulates some appropriate plotting methods as well
# as the necessary keyword arguments for giving the expected visual appearance for the
# features.


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


# Parse the bulletin and plot it
df = parse_wpc_surface_bulletin('/Users/sydneygoldberg/Desktop/CompMethodsslay/afos.txt')
plot_bulletin(ax, df)

plot_bulletin(ax, df)

ax.set_title(f'WPC Surface Analysis Valid {df.valid.dt.strftime("%HZ %d %b %Y")[0]}')
plt.show()
#8/11/2016 6z-------------------------------------------------------------------------------------------
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import matplotlib.pyplot as plt

from metpy.cbook import get_test_data
from metpy.io import parse_wpc_surface_bulletin
from metpy.plots import (add_metpy_logo, ColdFront, OccludedFront, StationaryFront,
                         StationPlot, WarmFront)

###########################################
# Define a function that can be used to readily plot a bulletin that has been parsed into a
# pandas `DataFrame`. This essentially encapsulates some appropriate plotting methods as well
# as the necessary keyword arguments for giving the expected visual appearance for the
# features.


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


# Parse the bulletin and plot it
df = parse_wpc_surface_bulletin('/Users/sydneygoldberg/Desktop/CM_Project/afos_11_6z.txt')
plot_bulletin(ax, df)

plot_bulletin(ax, df)

ax.set_title(f'WPC Surface Analysis Valid {df.valid.dt.strftime("%HZ %d %b %Y")[0]}')
plt.show()
#8/11/2016 12z-------------------------------------------------------------------------------------------
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import matplotlib.pyplot as plt

from metpy.cbook import get_test_data
from metpy.io import parse_wpc_surface_bulletin
from metpy.plots import (add_metpy_logo, ColdFront, OccludedFront, StationaryFront,
                         StationPlot, WarmFront)

###########################################
# Define a function that can be used to readily plot a bulletin that has been parsed into a
# pandas `DataFrame`. This essentially encapsulates some appropriate plotting methods as well
# as the necessary keyword arguments for giving the expected visual appearance for the
# features.


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


# Parse the bulletin and plot it
df = parse_wpc_surface_bulletin('/Users/sydneygoldberg/Desktop/CM_Project/afos_11_12z.txt')
plot_bulletin(ax, df)

plot_bulletin(ax, df)

ax.set_title(f'WPC Surface Analysis Valid {df.valid.dt.strftime("%HZ %d %b %Y")[0]}')
plt.show()
#8/12/2016 0z-------------------------------------------------------------------------------------------
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import matplotlib.pyplot as plt

from metpy.cbook import get_test_data
from metpy.io import parse_wpc_surface_bulletin
from metpy.plots import (add_metpy_logo, ColdFront, OccludedFront, StationaryFront,
                         StationPlot, WarmFront)

###########################################
# Define a function that can be used to readily plot a bulletin that has been parsed into a
# pandas `DataFrame`. This essentially encapsulates some appropriate plotting methods as well
# as the necessary keyword arguments for giving the expected visual appearance for the
# features.


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


# Parse the bulletin and plot it
df = parse_wpc_surface_bulletin('//Users/sydneygoldberg/Desktop/CM_Project/afos8_12_16.txt')
plot_bulletin(ax, df)

plot_bulletin(ax, df)

ax.set_title(f'WPC Surface Analysis Valid {df.valid.dt.strftime("%HZ %d %b %Y")[0]}')
plt.show()
#8/12/2016 6z-------------------------------------------------------------------------------------------
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import matplotlib.pyplot as plt

from metpy.cbook import get_test_data
from metpy.io import parse_wpc_surface_bulletin
from metpy.plots import (add_metpy_logo, ColdFront, OccludedFront, StationaryFront,
                         StationPlot, WarmFront)

###########################################
# Define a function that can be used to readily plot a bulletin that has been parsed into a
# pandas `DataFrame`. This essentially encapsulates some appropriate plotting methods as well
# as the necessary keyword arguments for giving the expected visual appearance for the
# features.


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


# Parse the bulletin and plot it
df = parse_wpc_surface_bulletin('/Users/sydneygoldberg/Desktop/CM_Project/afos8_12_16_6z.txt')
plot_bulletin(ax, df)

plot_bulletin(ax, df)

ax.set_title(f'WPC Surface Analysis Valid {df.valid.dt.strftime("%HZ %d %b %Y")[0]}')
plt.show()
#8/12/2016 12z-------------------------------------------------------------------------------------------
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import matplotlib.pyplot as plt

from metpy.cbook import get_test_data
from metpy.io import parse_wpc_surface_bulletin
from metpy.plots import (add_metpy_logo, ColdFront, OccludedFront, StationaryFront,
                         StationPlot, WarmFront)

###########################################
# Define a function that can be used to readily plot a bulletin that has been parsed into a
# pandas `DataFrame`. This essentially encapsulates some appropriate plotting methods as well
# as the necessary keyword arguments for giving the expected visual appearance for the
# features.


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


# Parse the bulletin and plot it
df = parse_wpc_surface_bulletin('/Users/sydneygoldberg/Desktop/CM_Project/afos8_12_16_12z.txt')
plot_bulletin(ax, df)

plot_bulletin(ax, df)

ax.set_title(f'WPC Surface Analysis Valid {df.valid.dt.strftime("%HZ %d %b %Y")[0]}')
plt.show()
