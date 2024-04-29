# GR-6553-Final-Project
# This code is for a Computer Methods Final Project on the 2016 Louisiana Flood by Sydney Goldberg.
This repository contains code that evaluates the meteorological setup and rainfall results of the historic Louisiana flooding that took place August 11th through August 13th 2016 in south Louisiana, specificaly looking at rainfall in East Baton Rouge Parish. Code and data are included for investigation of the precipitable water and surface anlaysis of August 11th, 2016. All code was written in phython.
# Data and Code explanations
  **Aug_2016_24h_rainfall_Meteogram.py**
 - This python code plots a 24 hour meteogram of rainfall from the ASOS station in East Baton Rouge Parish at the Baton Rouge Metroplotitan Airport, Ryan Field (KBTR).
 - Here is where I pulled the data: https://mesonet.agron.iastate.edu/request/download.phtml?network=LA_ASOS
  Select Network: Louisiana ASOS and select BATON ROUGE/RYAN (1942-Now)
  - Select "1 hour Precipitation [inch] and two days worth of data.
  - Make sure to remove missing data and Trace reports by selecting float or enter     0.00 manually.
  - Convert the data into a text file for the code to read.
 ** Aug_2016_surfaceannalysis_RH_850mb.py**
- This phython code plots WPC surface analysis, GFS relative humidty, and GFS 850 mb pressure lines.
- Here is where I pulled the data:
- WPC suface analysis: https://www.mesonet.agron.iastate.edu/wx/afos/p.php?pil=CODSUS&e=202010201500
- Make sure to create separate text files if you need a time that is not 0 UTC.
- For my code, it plots the 00 UTC surface analysis on August 11th 2016 and 00 UTC on August 12th 2016.
- GFS data: https://rda.ucar.edu/datasets/ds084.1/dataaccess/
- Use this link to plot both the 850mb data and relative humidity data.
**NEXRAD_Level_2_File_08_12_2016.py**
  -This code plots radar data from August 12th 2016. This code has 5 sections to plot 5 different run times of the radar. The ouputs were then downloaded and placed together to form a GIF.
  - Here is where I pulled the data:
  - https://www.roc.noaa.gov/wsr88d/Level_III/Level3Info.aspx
  - This code uses Level II archived radar data from 2016 using the KLIX Slidell, LA radar site.
**Plotting_Surface_Analysis_Aug_2016.py**
    -
