from PIL import Image
from random import randint
from neuralnetwork import nn

import numpy as np
import os
import os.path

labels = []
images = []

sizeDataset = 100

possibleLabels = ['Cat', 'Dog']
randTest = randint(0, sizeDataset)


def LoadImages():
    for label in possibleLabels:
        path = 'data/' + label + '/'
        filename = randint(0, 1000)
        for filename in range(sizeDataset):
            images.append(os.path.join(path, str(filename) + '.jpg'))
            labels.append(label)
    print("Images Count: " + str(len(images)))
    print("Labels Count: " + str(len(labels)))
    print("Image file: " + images[randTest])
    print("Image Label: " + labels[randTest])


def Train():
    nn.Setup(len(possibleLabels))
    for image in images:
        l = image.split('/')
        l = possibleLabels.index(l[1])
        nn.Add(l, image)
    nn.Train()


def Predict():
    sizeTestdata = 100
    result = []
    print('Cat Test (' + str(sizeTestdata) + ')')
    for i in range(sizeTestdata):
        r = randint(2000, 3000)
        pre = nn.Predict('data/Cat/' + str(r) + '.jpg')
        correct = pre[0][0]
        result.append(correct)
    print('Acc: ' + str(sum(result) / len(result)))
    result = []
    print('Dog Test (' + str(sizeTestdata) + ')')
    for i in range(sizeTestdata):
        r = randint(2000, 3000)
        pre = nn.Predict('data/Dog/' + str(r) + '.jpg')
        correct = pre[0][1]
        result.append(correct)
    print('Acc: ' + str(sum(result) / len(result)))


LoadImages()
Train()
Predict()
