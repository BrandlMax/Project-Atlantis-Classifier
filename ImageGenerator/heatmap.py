# import the libraries
from Modules import DATA

import matplotlib.pyplot as plot
import numpy as np

# LOAD DATASETS
DataLoader = DATA.DATA()
data1 = DataLoader.load("data/noFinger.csv", 1)
data2 = DataLoader.load("data/OneFinger.csv", 1)
data3 = DataLoader.load("data/TwoFinger.csv", 1)
data4 = DataLoader.load("data/noFinger.csv", 100)

plot.rcParams["figure.figsize"] = 5,2

d1 = []
for d in data1[0]:
    d1.append(int(d))

d2 = []
for d in data2[0]:
    d2.append(int(d))

d3 = []
for d in data3[0]:
    d3.append(int(d))

d4 = []
for d in data4[0]:
    d4.append(int(d))

x = np.linspace(0,160, 160)

fig, (ax,ax2, ax3) = plot.subplots(nrows=3, sharex=True)

# First
y = np.array(d1)

extent = [x[0]-(x[1]-x[0])/2., x[-1]+(x[1]-x[0])/2.,0,1]
ax.imshow(y[np.newaxis,:], cmap="plasma", aspect="auto", extent=extent)
ax.set_yticks([])
ax.set_xlim(extent[0], extent[1])

# Second
y = np.array(d2)

ax2.imshow(y[np.newaxis,:], cmap="plasma", aspect="auto", extent=extent)
ax2.set_yticks([])
ax2.set_xlim(extent[0], extent[1])

# Third
y = np.array(d3)

ax3.imshow(y[np.newaxis,:], cmap="plasma", aspect="auto", extent=extent)
ax3.set_yticks([])
ax3.set_xlim(extent[0], extent[1])

plot.tight_layout()
plot.show()