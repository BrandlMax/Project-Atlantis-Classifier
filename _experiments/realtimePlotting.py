from Serial2Plot.MFramework import Serial
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation

# 'frequency', '/dev/cu.usbmodem143201', 115200, 160, '999'

# SERIAL DATA
Port = "COM3"
Baud = 115200
BufferLength = 160
Divider = "999"

SERIAL = Serial.CONNECTION(Port, Baud, BufferLength, Divider)

# PLOT
fig = plt.figure()
ax = plt.axes()
line, = ax.plot([], [], lw=2)

def init():
    line.set_data([], [])
    return line,

def animate(i):
   if (SERIAL.ready):
        SERIAL.READ()

        # GET DATA
        y = SERIAL.doneBUFFER.copy()
        
        x = range(len(y))
        
        # EXTEND
        extent = [x[0]-(x[1]-x[0])/2., x[-1]+(x[1]-x[0])/2.,0,1]
        ax.imshow(y[np.newaxis,:], cmap="plasma", aspect="auto", extent=extent)
        ax.set_yticks([])
        ax.set_xlim(extent[0], extent[1])

        # PLOT
        line.set_data(x, y)
        ax.plot(x, y, lw=2)
        return line,
       
anim = animation.FuncAnimation(fig, animate, init_func = init, frames = 200, interval = 20, blit = True)

plt.show()