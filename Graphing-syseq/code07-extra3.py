# Import Meteostat library and dependencies
from datetime import datetime
import matplotlib.pyplot as plt
from meteostat import Point, Daily

# Documentation
# https://dev.meteostat.net/python/daily.html#data-structure

# Set time period
start = datetime(2022, 1, 1)
end = datetime(2022, 7, 31)

# Create Point for Vancouver,BC or Philadelphia, PA
#vancouver = Point(49.2497, -123.1193, 70)
philly = Point(39.97,-75.13,25)

# Get daily data for 2018
data = Daily(philly, start, end)
data = data.fetch()

# Plot line chart including average, minimum and maximum temperature
data.plot(y=['tavg', 'prcp','snow'])
plt.show()

