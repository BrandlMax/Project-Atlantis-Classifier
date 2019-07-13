# Project Atlantis: Signal Classifier

---

## What is this?

This project is a signal classifier, that can be used to classify frequency data streams from an Arduino. It is build on tensorflow. When working properly, you can even control a dolphin with only your hand and a bowl of water (see the Unity demo). For more information on why this exists, see the related [article](http://philippkaltofen.com/signalClassifier).

## Disclaimer

If you want to use this classifier with realtime data, you have to build a sensor and setup *[Is this touch](https://github.com/BrandlMax/is-this-touch).* This project was build to *only* use the data from the Arduino, so if you want to use it in another way, maybe without the fitting hardware, you will have to rewrite the data generation part.

Also, this project is still heavily in progress and probably riddled with bugs.

## Setup

First, you have to get your python environment ready. This project was only tested with python 3.7. 

    pip install tensorflow matplotlib numpy pyplot BytesIo Pillow 

Then, you can clone this repository.

    git clone https://github.com/BrandlMax/Project-Atlantis-Classifier.git

Currently, *ImageClassifier_test.py* is the entrance point of the classifier. You'll most likely have to change the "Port" variable in line 19 to fit to whichever port you have connected your Arduino to.

If everything is setup correctly, you should see a plotting window. There you can generate datasets and train the model. After the training, the prediction starts automatically.