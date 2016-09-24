import pandas as pd
from bs4 import BeautifulSoup
import numpy as np
import matplotlib.pyplot as plt
import sys

inp = sys.argv[1]

def hav(lon1, lat1, lon2, lat2):
    """
    Calculate the great circle distance between two points
    on the earth (specified in decimal degrees)
    """
    # convert decimal degrees to radians
    lon1, lat1, lon2, lat2 = map(np.radians, [lon1, lat1, lon2, lat2])
    # haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = np.sin(dlat/2)**2 + np.cos(lat1) * np.cos(lat2) * np.sin(dlon/2)**2
    c = -2 * np.arcsin(np.sqrt(a))
    if lon1 > lon2 or lat1 > lat2:
        km = 6367 * c
    else:
        km = -6367 * c
    return km

coords = []

with open (inp,'r') as f:
    bs = BeautifulSoup(f,'xml')
    r = bs.find_all('coordinates')
    for elements in r:
        e = elements.text
        for location in e.split():
            coords.append(location.split(','))

coords = np.array(coords)

lat_long = coords[:,[0,1]].astype(float)
lat_center = lat_long[:,1].mean()
lon_center = lat_long[:,0].mean()
scaled = np.array(map(lambda x: [hav(lon_center,lat_center,x[0],lat_center), \
								hav(lon_center,lat_center,lon_center,x[1])],lat_long))
plt.figure(figsize = (12,10))
plt.scatter(scaled[:,0],scaled[:,1])
plt.show()
