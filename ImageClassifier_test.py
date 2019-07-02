from ImageClassifier import ImageClassifier
from Serial2Plot.MFramework import Serial
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation
import PIL
from io import BytesIO
from Serial2Plot.MFramework import CSV
from matplotlib.widgets import Button
from PIL import ImageOps

# SERIAL DATA
Port = "COM3"
Baud = 115200
BufferLength = 160
Divider = "999"

SERIAL = Serial.CONNECTION(Port, Baud, BufferLength, Divider)

# PLOT
fig, ax = plt.subplots()

IC = ImageClassifier.IMAGECLASSIFIER()

# Dirty af
ID = 0
NoFingerID = 0 
OneFingerID = 0
TwoFingerID = 0

def addNoFinger(e):
    global NoFingerID
    NoFingerID += 1
    saveImage('noFinger', NoFingerID)

def addOneFinger(e):
    global OneFingerID
    OneFingerID += 1 
    saveImage('OneFinger', OneFingerID)
    
def addTwoFinger(e):
    global TwoFingerID
    TwoFingerID += 1 
    saveImage('TwoFinger', TwoFingerID)

def start(e):
    global state
    IC.trainModel()
    state = 'predict'

# GUI
# L, B, W, H
axStart = plt.axes([0.01, 0.01, 0.2, 0.05])
startButton = Button(axStart, 'No Finger')
startButton.on_clicked(addNoFinger)

axEnd = plt.axes([0.22, 0.01, 0.2, 0.05])
endButton = Button(axEnd, 'One Finger')
endButton.on_clicked(addOneFinger)

axT = plt.axes([0.44, 0.01, 0.2, 0.05])
tButton = Button(axT, 'Two Fingers')
tButton.on_clicked(addTwoFinger)

axF = plt.axes([0.66, 0.01, 0.2, 0.05])
fButton = Button(axF, 'Start')
fButton.on_clicked(start)

state = 'nothing'
label = 'noLabel'

def saveImage(l, iid):
    print('saveImage')
    global label
    global state
    global ID
    label = l
    state = 'takeImage'
    ID = iid

def animate(i):    
    global state
    if (SERIAL.ready):
        SERIAL.READ()

        y = np.array(SERIAL.doneBUFFER.copy())
        x = np.linspace(0, 160, 160)     

        extent = [x[0]-(x[1]-x[0])/2., x[-1]+(x[1]-x[0])/2.,0,1]       

        ax.cla()
        im = ax.imshow(y[np.newaxis,:], cmap="inferno", aspect="auto", extent=extent)        
        ax.set_title("frame {}".format(i))
        if(state == 'takeImage'):

            global ID              

            path = './Data/images/training/' + label + '/' + str(ID) + '.jpeg'
            plt.savefig(path, format = "jpeg", bbox_inches = 'tight', pad_inches = 0 )
            state = 'nothing'

        elif(state == 'predict'):

            buffer_ = BytesIO()
            plt.savefig(buffer_, format = "jpeg", bbox_inches = 'tight', pad_inches = 0 )
            buffer_.seek(0)
            b = BytesIO()

            # OPEN AS IMAGE
            image = PIL.Image.open(buffer_)

            # SET BORDER THAT GETS CROPPED
            # left, up, right, bottom
            border = (70, 0, 0, 70)

            # CROP
            image = ImageOps.crop(image, border)

            # SAVE IMAGE
            image.save(b, format='jpeg')
            # image.save('./RTData/image.jpg', format='jpeg')

            buffer_.close()

            # PREDICT
            IC.predictFrame(image)

        plt.pause(0.001)
        return im


anim = animation.FuncAnimation(fig, animate, interval = 1)
plt.show()