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

NFFT = 160  # the length of the windowing segments
Fs = 160  # the sampling frequency

# Plot
fig = plot.figure(1)
plot.title('Spectrogram')
plot.xlabel('Sample')
plot.ylabel('Amplitude')

fig.add_subplot(311)
im = plot.specgram(
    data1, NFFT=NFFT, Fs=Fs, scale_by_freq=True)

fig.add_subplot(312)
im = plot.specgram(
    data2, NFFT=NFFT, Fs=Fs, scale_by_freq=True)

fig.add_subplot(313)
im = plot.specgram(
    data3, NFFT=NFFT, Fs=Fs, scale_by_freq=True)


plot.show()
