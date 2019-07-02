from ImageClassifier import ImageClassifier
from Serial2Plot.MFramework import Serial
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation
import PIL
from io import BytesIO
from Serial2Plot.MFramework import CSV
from matplotlib.widgets import Button

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

def addNoFinger(e):
    global NoFingerID
    NoFingerID += 1
    saveImage('noFinger', NoFingerID)

def addOneFinger(e):
    global OneFingerID
    OneFingerID += 1 
    saveImage('OneFinger', OneFingerID)

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

axF = plt.axes([0.44, 0.01, 0.2, 0.05])
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
        x = np.linspace(0, 1, 160)     

        extent = [x[0]-(x[1]-x[0])/2., x[-1]+(x[1]-x[0])/2.,0,1]       

        ax.cla()
        im = ax.imshow(y[np.newaxis,:], cmap="inferno", aspect="auto", extent=extent)
        
        if(state == 'takeImage'):
            global ID                        
            path = './Data/images/training/' + label + '/' + str(ID) + '.jpeg'
            plt.savefig(path, format = "jpeg", bbox_inches = 'tight', pad_inches = 0 )
            state = 'nothing'
        elif(state == 'predict'):
            buffer_ = BytesIO()
            # path = './RTData/img.jpg'
            plt.savefig(buffer_, format = "jpeg", bbox_inches = 'tight', pad_inches = 0 )
            buffer_.seek(0)
            # image = PIL.Image.open( buffer_ )
            # img = PIL.Image.frombytes('RGB', (224, 224), buffer_, 'raw')

            b = BytesIO()

            image = PIL.Image.open(buffer_)
            image = image.resize((224, 224), PIL.Image.BICUBIC)
            image.save(b, format='jpeg')

            buffer_.close()

            IC.predictFrame(image)

        # try:
        #     IC.predictFrame(image)
        # except Exception as e:
        #     print(e)
        #     r = 'error'
        #     pass

        plt.pause(0.001)
        return im


anim = animation.FuncAnimation(fig, animate, interval = 1)
plt.show()

# def main():    
#     while(0 < 1):
#         print("1: Add noFinger\n2: Add oneFinger\n3: Train\n4:Predict")
#         inp = input('-->')
#         if(inp == 1){
#             CSV.LUKE_CSVWRITER(BufferLength)
#             for i in range(0, 20):
#                 CSV.writeFreq(
#                     'Session_' + str(1) + '.csv'
#                 )
#         }

# IC.trainModel()
# IC.validateModel()

# IC.predictFrame(animate())