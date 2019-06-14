# import the libraries

import matplotlib.pyplot as plot
import numpy as np
import csv

data = []

with open("CSVData/noFinger.csv") as csvfile:
    # change contents to floats
    reader = csv.reader(csvfile, quoting=csv.QUOTE_NONNUMERIC)
    for row in reader:  # each row is a list
        data.append(row)

# remove header
data.pop(0)

print(data[0])

dt = 0.0005

NFFT = 1024  # the length of the windowing segments
Fs = int(1.0 / dt)  # the sampling frequency

# Plot
plot.subplot(211)

plot.xlabel('Sample')

plot.ylabel('Amplitude')

Pxx, freqs, bins, im = plot.specgram(data, NFFT=NFFT, Fs=Fs, noverlap=900)

plot.show()
