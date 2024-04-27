#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 12:23:40 2024

@author: sydneygoldberg
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 12:22:53 2024

@author: sydneygoldberg
"""
#24 hour meteogram for aug 11 & 12 2016--------------------------------------------
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import datetime as dt

def plot_precipitation(fig, dates, precipitation, title):
    ax = fig.add_subplot(1, 1, 1)
    ax.plot(dates, precipitation, marker='o', linestyle='-', color='b')
    ax.xaxis_date()
    plt.ylim(0,2)
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M'))
    ax.set_xlabel('24 Hours (UTC)')
    ax.set_ylabel('Rainfall (inches)')
    ax.set_title(title)
    plt.xticks(rotation=45)
    fig.autofmt_xdate()
    plt.tight_layout()

# Read the text file
file_path = '2016_KBTR_Rain_New.txt'
with open(file_path, 'r') as file:
    lines = file.readlines()

dates = []
precipitation = []
for line in lines:
    parts = line.strip().split(',')
    if len(parts) >= 3:
        dates.append(dt.datetime.strptime(parts[1], '%Y-%m-%d %H:%M'))
        precipitation.append(float(parts[2]))

# Specify the x-axis labels
x_labels = ['2016-08-11', '2016-08-12']

# Create the figure
fig = plt.figure(figsize=(12, 6))

# Plot the precipitation
plot_precipitation(fig, dates, precipitation, '24-Hour Rainfall at KBTR (08-11-2016 to 08-12-2016)')

# Show the plot
plt.show()

#24 hour meteogram for aug 12 & 13 2016---------------------------------------------
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import datetime as dt

def plot_precipitation(fig, dates, precipitation, title):
    ax = fig.add_subplot(1, 1, 1)
    ax.plot(dates, precipitation, marker='o', linestyle='-', color='b')
    ax.xaxis_date()
    plt.ylim(0,2)
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M'))
    ax.set_xlabel('24 Hours (UTC)')
    ax.set_ylabel('Rainfall (inches)')
    ax.set_title(title)
    plt.xticks(rotation=45)
    fig.autofmt_xdate()
    plt.tight_layout()

# Read the text file
file_path = '/Users/sydneygoldberg/Desktop/CM_Project/New_Rainfall_1213.txt'
with open(file_path, 'r') as file:
    lines = file.readlines()

dates = []
precipitation = []
for line in lines:
    parts = line.strip().split(',')
    if len(parts) >= 3:
        dates.append(dt.datetime.strptime(parts[1], '%Y-%m-%d %H:%M'))
        precipitation.append(float(parts[2]))

# Specify the x-axis labels
x_labels = ['2016-08-12', '2016-08-13']

# Create the figure
fig = plt.figure(figsize=(12, 6))

# Plot the precipitation
plot_precipitation(fig, dates, precipitation, '24-Hour Rainfall at KBTR (08-12-2016 to 08-13-2016)')

# Show the plot
plt.show()