import numpy as np
from keras.preprocessing.image import ImageDataGenerator
from keras.preprocessing import image
from keras.applications.mobilenet import MobileNet, preprocess_input, decode_predictions
import tensorflow as tf
from tensorflow import keras
import math as Math
from PIL import Image

'''
def convert(img_path, IMAGE_SIZE):
    img = image.load_img(img_path, target_size=(IMAGE_SIZE, IMAGE_SIZE))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)
    return x
'''

def convert(img_path, IMAGE_SIZE):
    img = image.load_img(img_path, target_size=(IMAGE_SIZE, IMAGE_SIZE))    
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)
    return x

def convertFrame(frame):
    print('covertFrame')        
    print(frame)
    x = image.img_to_array(frame)
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)
    return x