import os, os.path
from os import walk, listdir
from os.path import isfile, join
from ImageGenerator.heatmap import Heatmap

class ImageGenerator:
    def __init__(self, parameter_list):
        self.labels = []  

    def prepareData(self, type):        
        # Get Labels from csv data
        labels = self.getLabels('./Data/csv/')
        print(labels)

        # Generate folders for images
        # Training Data        
        for label in labels:
            if not os.path.exists('./Data/images/training/' + label):
                os.mkdir('./Data/images/training/' + label)
            else:
                print(label + '-folder already exists')
        # Validation Data
        for label in labels:
            if not os.path.exists('./Data/images/validation/' + label):
                os.mkdir('./Data/images/validation/' + label)
            else:
                print(label + '-folder already exists')

        # Generate Images
        if type == 'heatmap':
            heatmap = Heatmap(0)
            heatmap.createImages(labels, 100)
            # Create Heatmap
        elif type == 'spectrogram':
            pass
            # Create Spectrogram
        else:
            print('No image mode found.')

    def getLabels(self, path):
        filenames = [f for f in listdir(path) if isfile(join(path, f))]
        # Get labels from files
        labels = []
        for file in filenames:
            labels.append(file.replace('.csv', ''))
        return labels