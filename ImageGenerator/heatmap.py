# import the libraries
from ImageGenerator.Modules import DATA

import matplotlib.pyplot as plot
import numpy as np

class Heatmap:
    def __init__(self, parameter_list):
        self.dataLoader = DATA.DATA()

    def createImages(self, labels):
        data = []

        # LOAD DATASETS
        # Save the data from each .csv file in data[]
        for label in labels:
            data.append(self.dataLoader.load('./Data/csv/' + label + '.csv', 1))

        # ?
        plot.rcParams["figure.figsize"] = 5,2

        # Save Images
        i = 0
        for entry in data:
            d1 = []
            for d in data[0][0]:
                d1.append(int(d))

            x = np.linspace(0,160, 160)

            fig, (ax) = plot.subplots(nrows=1, sharex=True)

            # First
            y = np.array(d1)

            extent = [x[0]-(x[1]-x[0])/2., x[-1]+(x[1]-x[0])/2.,0,1]
            ax.imshow(y[np.newaxis,:], cmap="plasma", aspect="auto", extent=extent)
            ax.set_yticks([])
            ax.set_xlim(extent[0], extent[1])

            plot.tight_layout()

            path = './Data/images/training/' + labels[data.index(entry)] + '/'

            plot.savefig(path + str(i) + '.png')
            i += 1