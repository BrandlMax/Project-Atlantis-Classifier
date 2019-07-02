import os.path
import os
import numpy as np
from ImageClassifier.neuralnetwork import nn
from PIL import Image
from random import randint


# Classifier
# trainModel()
# Nimmt die Daten und trainiert das netzwerk
# ImageClassifier(labels[]) -> returns Loss

# validateModel()
# nimmt die Testdaten und predicted
# returns accuracy


class IMAGECLASSIFIER:
    def __init__(self, trainingPath='./Data/images/training', validationPath='./Data/images/validation'):
        self.labels = []
        self.images = []

        self.trainingPath = trainingPath
        self.validationPath = validationPath

        self.val_labels = []
        self.val_images = []

        self.possibleLabels = []

    def trainModel(self):
        print("Train Model")
        self.Train()

    def validateModel(self):
        print("Validate Model")
        resultList = []
        for idx, valImage in enumerate(self.val_images):
            result = self.Predict(valImage)
            # print("Image: ", valImage)
            # print("ShouldBe: ", self.val_labels[idx])
            # print("Is: ", result)
            if(result == self.val_labels[idx]):
                resultList.append(1)
            else:
                resultList.append(0)
        acc = str(sum(resultList) / len(resultList))
        print("Accuracy: ", acc)

    def predictFrame(self, frame):
        print("Predicting")
        pre = nn.PredictFrame(frame)
        print("Prediction: " + str(pre))

    def Train(self):        
        # LOAD ALL TRAININGSDATA
        self.Get_Datasets(self.trainingPath, self.validationPath)

        nn.Setup(len(self.possibleLabels))
        for image in self.images:
            l = image.split('/')
            print("l1", l)
            l = self.possibleLabels.index(l[-2])
            print("addLabel", l)
            print("addImage", image)
            nn.Add(l, image)
        nn.Train()

    def Predict(self, path):
        pre = nn.Predict(path)
        labelIndex = np.where(pre[0] == 1.0)
        predictionResult = self.possibleLabels[labelIndex[0][0]]
        return predictionResult
        # print("Prediction:", predictionResult)

    def Get_Datasets(self, trainingPath, validationPath):
        trainingFolder = os.walk(trainingPath)
        validationFolder = os.walk(validationPath)
        self.possibleLabels = next(trainingFolder)[1]

        # TRAINING DATA
        for idx, labels in enumerate(trainingFolder):
            for image in labels[2]:
                if(image != ".DS_Store"):
                    pathLabelPart = "/" + self.possibleLabels[idx] + "/"
                    self.images.append(os.path.join(
                        trainingPath + pathLabelPart, image))
                    self.labels.append(self.possibleLabels[idx])

        # VALIDATION DATA
        for idx, labels in enumerate(validationFolder):
            # Some how he counts the validation folder. so we have to ignore the first entry
            if(idx != 0):
                idx = idx - 1
                for image in labels[2]:
                    if(image != ".DS_Store"):
                        pathLabelPart = "/" + self.possibleLabels[idx] + "/"
                        self.val_images.append(os.path.join(
                            validationPath + pathLabelPart, image))
                        self.val_labels.append(self.possibleLabels[idx])

        print("IMAGES LOADED", self.images)
        print("LABELS LOADED", self.labels)
        print("VAL IMAGES LOADED", self.val_images)
        print("VAL LABELS LOADED", self.val_labels)
