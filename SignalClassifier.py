
# PART II

# Preparation
# UI Select
# -> Train(mode) // mode = 'heatmap' oder 'spectrogram'

# prepareData()
# Nimmt die CSV Dateien aus dem data-Folder
# generiert daraus Labels und Images aus den Plots: Label_train_01.jpg / Label_test_01.jpg
# 80% Testdaten + 20% Validation in extra train_data Folder.

# Classifier
# trainModel()
# Nimmt die Daten und trainiert das netzwerk
# ImageClassifier(labels[]) -> returns Loss

# validateModel()
# nimmt die Testdaten und predicted
# returns accuracy

# PART II

# Port, // Serial Port
# baudRate, // Baudrate from Arduino
# freqLength=160, // Number of related values for Plotting
# startValue='999' // start value (kind of start bit)
# -> Predict(mode, serialPort, baudRate, freqLength, startValue) // mode = 'heatmap' oder 'spectrogram'
# Get Serial Stream
# Ploting()
# ImageClassifier_Predict(ImageAsBase64) -> Label + Probability

from ImageGenerator import ImageGenerator as IG


def train():
    image.prepareData('heatmap')


def main():
    print('Signal Classifier')

    # Create Image Generator
    global
    imageGenerator = IG.ImageGenerator(0)


if __name__ == '__main__':
    main()
