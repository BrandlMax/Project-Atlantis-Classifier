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
fig, ax = plt.subplots()

def init():
    line.set_data([], [])
    return line,

def animate(i):
   if (SERIAL.ready):
        SERIAL.READ()

        y = np.array(SERIAL.doneBUFFER.copy())
        x = np.linspace(0, 160, 160)     

        extent = [x[0]-(x[1]-x[0])/2., x[-1]+(x[1]-x[0])/2.,0,1]
        
        ax.cla()
        ax.imshow(y[np.newaxis,:], cmap="plasma", aspect="auto", extent=extent)
        ax.set_title("frame {}".format(i))
        plt.pause(0.001)
       
anim = animation.FuncAnimation(fig, animate, interval = 1)

plt.show()