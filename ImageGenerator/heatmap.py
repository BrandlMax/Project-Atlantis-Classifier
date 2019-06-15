# import the libraries
from ImageGenerator.Modules import DATA

import matplotlib.pyplot as plot
import numpy as np

class Heatmap:
    def __init__(self, parameter_list):
        self.dataLoader = DATA.DATA()        

    def createImages(self, labels, packageSize):
        t_data = []
        v_data = []

        # LOAD DATASETS
        # Get Data Packages
        for label in labels:
            t_data.append(self.dataLoader.load('./Data/csv/' + label + '.csv', packageSize))

        # Move some data to validation
        for idx, label in enumerate(t_data):
            e = []
            v_data.append(e)
            for i in range(0, int(len(label)*0.2) - 2):
                v_data[idx].append(t_data[idx][i])
                t_data[idx].remove(t_data[idx][i])

        # ?
        plot.rcParams["figure.figsize"] = 5,2

        # Save Images
        print('Saving images for training')
        self.drawPlot(labels, t_data, 'training')
        print('Saving images for validation')
        print(len(v_data))
        self.drawPlot(labels, v_data, 'validation')

    def drawPlot(self, labels, data, set): 
        i = 0
        # label = [] mit allen packages die im datensatz waren
        for label in data:
            print('Label: ', labels[data.index(label)])
            for package in label:
                print(i)
                d1 = []
                for d in package:
                    d1.append(int(d[0]))

                x = np.linspace(0,160, 160)

                fig, (ax) = plot.subplots(nrows=1, sharex=True)

                # First
                y = np.array(d1)

                extent = [x[0]-(x[1]-x[0])/2., x[-1]+(x[1]-x[0])/2.,0,1]
                ax.imshow(y[np.newaxis,:], cmap="plasma", aspect="auto", extent=extent)
                ax.set_yticks([])
                ax.set_xlim(extent[0], extent[1])

                plot.tight_layout()

                path = './Data/images/' + set + '/' + labels[data.index(label)] + '/'

                plot.savefig(path + str(i) + '.jpg')
                plot.close()
                i += 1
            i = 0
        return True