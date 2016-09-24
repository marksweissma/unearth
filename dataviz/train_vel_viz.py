# Simple DataViz for the train routes
import sys
import matplotlib.pyplot as plt
import string

# read the latitude and longitudes

lon=[] #longitudes
lat=[] #latitudes
redlon = []
redlat = []
lon_bad=[]
lat_bad=[]
filename_ext = sys.argv[1]
filename = filename_ext.split('.')[0]
fi=open(filename_ext,'r')

# plot them
# TODO: make a basemap
fig = plt.figure(facecolor = '0.05')
ax = plt.Axes(fig, [0., 0., 1., 1.], )
ax.set_aspect('equal')
ax.set_axis_off()
fig.add_axes(ax)

linenum=0
for line in fi:
    if linenum>0:
        line=string.replace(line, "\n","")
        try:
            fields=string.split(line,",")
            x,y=fields[2:4]
            vel=fields[6]
            if vel > 0:
                lon.append(float(y))
                lat.append(float(x))
            else:
                redlon.append(float(y))
                redlat.append(float(x))
        except:
            pass
    linenum+=1
fi.close()

plt.plot(lon, lat, color = "green", lw = 0.8, alpha = 0.8)
plt.plot(redlon, redlat, color = "red", lw = 0.8, alpha = 0.8)
filename = "%s.%s" % (filename,'png')
plt.savefig(filename, facecolor = fig.get_facecolor(), bbox_inches='tight', pad_inches=0, dpi=300)
