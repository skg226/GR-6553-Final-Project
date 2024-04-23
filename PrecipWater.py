#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 12:42:23 2024

@author: sydneygoldberg
"""

import numpy as np
import matplotlib.pyplot as plt
import cartopy.feature as cf
import cartopy.crs as ccrs
import pygrib

# Open the GRIB file
grbGFS = pygrib.open('/Users/sydneygoldberg/Desktop/CM_Project/gfs.0p25.2016081100.f000.grib2')

# Select the variable for Precipitable Water
grbGFS.select(name='Precipitable water')
precipwater = grbGFS[274]
pw = precipwater['values'] * 0.0393701  # Convert kg/m² to inches

lats, lons = precipwater.latlons()

# Set up the plot
fig = plt.figure(figsize=(8, 8))
proj = ccrs.LambertConformal(central_longitude=-96., central_latitude=40., standard_parallels=(40., 40.))
ax = plt.axes(projection=proj)
ax.set_extent([-125., -70., 20., 60.])

# Add map features
ax.add_feature(cf.LAND, color='white')
ax.add_feature(cf.OCEAN, color='white')
ax.add_feature(cf.COASTLINE, edgecolor='black')
ax.add_feature(cf.BORDERS, edgecolor='black')
ax.add_feature(cf.STATES, edgecolor='black')
ax.add_feature(cf.LAKES, alpha=0.5, color='white')

# Plot precipitable water
levels = np.arange(0, 3.3, 0.1)  
contour = ax.contourf(lons, lats, pw, levels, cmap=plt.cm.gist_earth_r, transform=ccrs.PlateCarree())
cbar = plt.colorbar(contour, ax=ax, orientation='horizontal', pad=0.05)
cbar.set_label('Precipitable Water (inches)')

# Add title
plt.title('GFS Forecast Precipitable Water 08-11-2016')

# Show the plot
plt.show()

# Close the GRIB file
grbGFS.close()


