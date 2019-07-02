# Load / Generate Trainingsdata
import numpy as np
from keras.preprocessing.image import ImageDataGenerator
from keras.preprocessing import image
import tensorflow as tf
from tensorflow import keras
import math as Math

# Build Model
hiddenUnits = 100
numClasses = 3
learningRate = 0.0001
batchSize = 0.4
epochs = 100


def BuildModel(IMAGESasFEATURES, LABELS):

    numClasses = len(LABELS[0])

    customModel = keras.Sequential([
        keras.layers.Flatten(input_shape=(7, 7, 1024)),
        keras.layers.Dense(units=hiddenUnits, activation='relu',
                           kernel_initializer='VarianceScaling', use_bias=True),
        keras.layers.Dense(units=numClasses, activation='softmax',
                           kernel_initializer='VarianceScaling', use_bias=False)
    ])

    optimizer = tf.train.AdamOptimizer(learningRate)
    customModel.compile(optimizer, loss='mean_squared_error')
    calcBatchSize = Math.floor(IMAGESasFEATURES.shape[0] * batchSize)
    if not calcBatchSize > 0:
        print('Batch size is 0 or NaN. Please choose a non-zero fraction.')

    # customModel.summary()
    customModel.fit(IMAGESasFEATURES, LABELS,
                    batch_size=calcBatchSize, epochs=epochs)
    return customModel
