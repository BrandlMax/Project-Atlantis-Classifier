import random
import zmq
import threading
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

import time
start_time = time.time()

# SERVER

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")
RESP = [""]

# SERIAL DATA
# Port = "COM3"
Port = '/dev/cu.usbmodem14101'
Baud = 115200
BufferLength = 160
Divider = "999"

SERIAL = Serial.CONNECTION(Port, Baud, BufferLength, Divider, start_time)

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
    # IC.validateModel()
    state[0] = 'predict'


def translate(value, leftMin, leftMax, rightMin, rightMax):
    # Figure out how 'wide' each range is
    leftSpan = leftMax - leftMin
    rightSpan = rightMax - rightMin

    # Convert the left range into a 0-1 range (float)
    valueScaled = float(value - leftMin) / float(leftSpan)

    # Convert the 0-1 range into a value in the right range.
    return rightMin + (valueScaled * rightSpan)


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

state = ['nothing']
label = 'noLabel'


def saveImage(l, iid):
    print('saveImage')
    global label
    global state
    global ID
    label = l
    state[0] = 'takeImage'
    ID = iid


def animate(i):
    global state
    if (SERIAL.ready):
        curTime = time.time() - start_time

        dataPartArray = []

        while(len(dataPartArray) < 100):
            rawData = SERIAL.doneBUFFER.copy()
            dataPart = []
            # Filter
            maxborder = 350
            for i, d in enumerate(rawData):
                if(d < maxborder):
                    dataPart.append(0)
                else:
                    val = translate(d, maxborder, 700, 0, 100)
                    dataPart.append(val)

            dataPart = dataPart[60:]
            dataPart = dataPart[:40]

            dataPartArray.append(dataPart)

        y1 = np.array(dataPartArray)
        # print(y1.shape())
        y = np.random.random((16, 16))
        # print(y.shape())
        x = np.linspace(0, 60, 60)

        extent = [x[0]-(x[1]-x[0])/2., x[-1]+(x[1]-x[0])/2., 0, 1]

        ax.cla()
        im = ax.imshow(y1, cmap="nipy_spectral",
                       aspect="auto", extent=extent)
        # ax.set_title("frame {}".format(i))
        if(state[0] == 'takeImage'):

            global ID

            path = './Data/images/training/' + label + '/' + str(ID) + '.jpeg'
            plt.savefig(path, format="jpeg", bbox_inches='tight', pad_inches=0)
            state[0] = 'nothing'

        elif(state[0] == 'predict'):

            buffer_ = BytesIO()
            plt.savefig(buffer_, format="jpeg",
                        bbox_inches='tight', pad_inches=0)
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
            global RESP
            res = IC.predictFrame(image)
            RESP[0] = res
            # message = socket.recv()
            # try:
            #     socket.send_string(str(res))
            # except:
            #     print('Nope')
            #     pass

        plt.pause(0.001)
        return im


def read_from_port(socket, ser, state, res):
    while True:
        ser.READ()


def comUnity(socket, ser, state, res):
    while True:
        message = socket.recv()
        # print("Received request: %s" % message)
        time.sleep(1)
        val = random.randint(0, 1)
        val = str(val)
        socket.send_string(res[0])


thread = threading.Thread(target=read_from_port,
                          args=(socket, SERIAL, state, RESP))
thread.daemon = True

threadUnity = threading.Thread(target=comUnity,
                               args=(socket, SERIAL, state, RESP))
threadUnity.daemon = True

thread.start()
threadUnity.start()
anim = animation.FuncAnimation(fig, animate, interval=1)
plt.show()
print('Bye')
# plt.close()
# print("CLOSE")
# thread.interrupt_main()
# threadUnity.interrupt_main()
# print("CLOSED")
