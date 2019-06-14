import numpy as np
import asyncio

import tensorflow as tf

from keras.backend import clear_session
from neuralnetwork.ML import MobileNet, ImageConverter, ImageClassifierModel


# GLOBALS
IMAGESasFEATURES = np.array([])
LABELS = np.array([])

CLASSESAMOUNT = 0

IMAGE_SIZE = 224

graph = []

# SETUP

def Setup(ClassesAmount: int):

    # LOAD FEATURES
    global FEATUREMODEL
    FEATUREMODEL = MobileNet.LoadFeatureModel()
    global graph
    graph = tf.get_default_graph()
    print(graph)

    # SETTINGS
    global CLASSESAMOUNT
    CLASSESAMOUNT = ClassesAmount



# ADD

def Add(label_id: int, img_path):    
    global IMAGESasFEATURES
    global LABELS

    img = ImageConverter.convert(img_path, IMAGE_SIZE)
    featurePredictionResult = FEATUREMODEL.predict(img)

    # CREATE EMPTY ARRAY WITH ZEROS
    labelArray = np.zeros((CLASSESAMOUNT,), dtype=int)
    # SET THE LABEL OF CURRENT IMAGE
    labelArray[label_id] = 1

    if len(labelArray) <= label_id:
        CLASSAMOUNT = CLASSAMOUNT + 1
        for label in LABELS:
            if len(label) <= CLASSAMOUNT:
                label.append(0)

    if len(IMAGESasFEATURES) == 0:
        IMAGESasFEATURES = np.array(featurePredictionResult)
        LABELS = np.array([labelArray])
    else:
        IMAGESasFEATURES = np.append(IMAGESasFEATURES, featurePredictionResult, axis=0)
        LABELS = np.append(LABELS, [labelArray], axis=0)

    print('Image Added ({})'.format(label_id))



# TRAIN

def Train():
    global MODEL
    MODEL = ImageClassifierModel.BuildModel(IMAGESasFEATURES, LABELS)
    print('MODEL Trained')


# PREDICT

def Predict(img_path):
    img = ImageConverter.convert(img_path, IMAGE_SIZE)
    Features = FEATUREMODEL.predict(img)
    RESULT = MODEL.predict(Features)
    return np.around(RESULT)

# same as Predict but with image instead of path

async def PredictFrame(frame):
    global graph
    with graph.as_default():
        img = ImageConverter.convertFrame(frame)
        Features = FEATUREMODEL.predict(img)
        RESULT = MODEL.predict(Features)
        return np.around(RESULT)