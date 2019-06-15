from Modules import DATA

class ImageGenerator:
    def __init__(self, parameter_list):
        self.labels = []

    def prepareData(self, type, ):
        # Get folders

        # Generate Labels from folders

        # Generate folders for images
        # Training Data
        # Validation Data

        # Generate Images
        if type='heatmap':
            # Create Heatmap
        elif type='spectrogram':
            # Create Spectrogram
        else:
            print('No image mode found.')