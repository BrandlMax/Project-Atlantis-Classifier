# MFramework for my future projects, for faster Serial Plotting
from Serial2Plot.MFramework import Plotter


class SERIAL2PLOT:
    def __int__(self):
        print("SERIAL2PLOT")

    def start(self):
        PLOTTER = Plotter.HARRY_PLOTTER(
            'frequency', '/dev/cu.usbmodem142201', 115200, 160, '999')
        # Start Plotting Loop
        PLOTTER.render()
        # On End
        PLOTTER.close()
