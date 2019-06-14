# Signal Classifier
###########################################
# Imports
###########################################

# Import TensorFlow and TensorFlow Datasets
import tensorflow as tf
from tensorflow import keras

# Helper libraries
import math
import numpy as np
import matplotlib.pyplot as plt

# Components
from Components import DataParser

# Tensorflow Version
print("Tensorflow Version:", tf.__version__)

###########################################
# Load Data
###########################################
xData = DataParser.get("./Data/UGLY_data_X.txt")
yLabel = DataParser.get("./Data/UGLY_labels_Y.txt")

print("Data Info ---------------------------------------------")
print("Number of Data:", len(xData))
print("Channels of Data:", len(xData[0]))
print("Number of Labels:", len(yLabel))
print("-------------------------------------------------------")

###########################################
# Prepare Data
###########################################


###########################################
# Model
###########################################


###########################################
# Evaluate
###########################################


###########################################
# Run Workflow
###########################################
