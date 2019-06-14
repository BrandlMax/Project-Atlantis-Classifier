# Load MobileNet as FeatureGen
from keras.applications.mobilenet import MobileNet, preprocess_input, decode_predictions
from keras.models import Model

layer = 'conv_pw_13_relu'
def LoadFeatureModel():
    print('LoadFeatureModel ###############################')
    base_model = MobileNet(weights='imagenet')
    model = Model(inputs=base_model.input, outputs=base_model.get_layer(layer).output)
    model.summary()
    return model