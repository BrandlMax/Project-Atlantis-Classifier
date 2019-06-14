# import the libraries
from Modules import DATA

import matplotlib.pyplot as plot
import numpy as np

# LOAD DATASETS
DataLoader = DATA.DATA()
data1 = DataLoader.load("data/noFinger.csv", 100)
data2 = DataLoader.load("data/OneFinger.csv", 100)
data3 = DataLoader.load("data/TwoFinger.csv", 100)

print(data1)
print(data2)
print(data3)


# def zero(n):
#     zeros = [0] * n
#     return zeros


# # Plot
# fig = plot.figure(1)
# plot.title('Spectrogram')

# plot.hist2d(zero(100), data1, bins=10, cmap=plot.cm.Reds)

# plot.show()
