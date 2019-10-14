import sys
import pygame
from pygameWindow import PYGAME_WINDOW
import random
import numpy as np
import pickle
from constants import pygameWindowDepth, pygameWindowWidth

clf = pickle.load(open('classifier.p', 'rb'))
testData = np.zeros((1, 30), dtype='f')

sys.path.insert(0, '../../../../')
from x86 import Leap

controller = Leap.Controller()

pygameWindow = PYGAME_WINDOW()
#
# coordinate variables
x = 250
y = 250
programState = 0
one = 'images/number1.jpg'
newImage = pygame.image.load(one)
newImage = pygame.transform.scale(newImage, (pygameWindowWidth/2, pygameWindowDepth/2))

left = 'images/leftArrow.png'
leftImage = pygame.image.load(left)
leftImage = pygame.transform.scale(leftImage, (pygameWindowWidth/2, pygameWindowDepth/2))

right = 'images/rightArrow.png'
rightImage = pygame.image.load(right)
rightImage = pygame.transform.scale(rightImage, (pygameWindowWidth/2, pygameWindowDepth/2))

up = 'images/upArrow.png'
upImage = pygame.image.load(up)
upImage = pygame.transform.scale(upImage, (pygameWindowWidth/2, pygameWindowDepth/2))

down = 'images/downArrow.png'
downImage = pygame.image.load(down)
downImage = pygame.transform.scale(downImage, (pygameWindowWidth/2, pygameWindowDepth/2))

def HandleState0():
    global controller, programState
    pygameWindow.setImage(newImage)
    frame = controller.frame()
    if len(frame.hands) > 0:
        programState = 1

def HandleState1():
    global controller, programState
    frame = controller.frame()
    # pygameWindow.setImage(leftImage)
    hand = frame.hands[0]
    fingers = hand.fingers
    for finger in fingers:
        handleFinger(finger, k)
        # for b in range(0, 4):
        #     tip = finger.bone(b).next_joint
            # if b == 0 or b == 3:
            #     testData[0, k] = tip[0]
            #     testData[0, k + 1] = tip[1]
            #     testData[0, k + 2] = tip[2]
            #     k += 3
    # testData = CenterData(testData)
    # predictedClass = clf.Predict(testData)
    # print(predictedClass)
    if len(frame.hands) == 0:
        programState = 0

def perturbCirclePosition():
    global x, y
    fourSidedDieRoll = random.randint(1, 4)
    if fourSidedDieRoll == 1:
        x -= 1
    elif fourSidedDieRoll == 2:
        x += 1
    elif fourSidedDieRoll == 3:
        y -= 1
    else:
        y += 1


xMin = 1000.0
xMax = -1000.0
yMin = 1000.0
yMax = -1000.0


def handleFrame(frame):
    global x, y, xMin, xMax, yMin, yMax, tip, pygameWindowWidth, pygameWindowDepth
    x = int(tip[0])
    y = int(tip[2])

    if x < xMin:
        xMin = x
    if x > xMax:
        xMax = x
    if y < yMin:
        yMin = y
    if y > yMax:
        yMax = y


def Scale(value, dMin, dMax, min, max):
    if dMin > value > dMax:
        oldRange = dMax - dMin
        newRange = max - min
        if dMin == dMax:
            scaledValue = min
            return scaledValue/2
        else:
            scaledValue = (((value - dMin) * newRange) / oldRange) + min
            return scaledValue/2

    else:
        oldRange = dMax - dMin
        newRange = max - min
        if dMin == dMax:
            scaledValue = min
            return scaledValue/2
        else:
            scaledValue = (((value - dMin) * newRange) / oldRange) + min
            return scaledValue/2



def handleFinger(f, k):
    for b in range(0, 4):
        if b == 0:
            handleBone(f.bone(b), 4, k)
        elif b == 1:
            handleBone(f.bone(b), 3, k)
        elif b == 2:
            handleBone(f.bone(b), 2, k)
        elif b == 3:
            handleBone(f.bone(b), 1, k)


def handleBone(bone, b, k):
    global testData
    base = bone.prev_joint
    tip = bone.next_joint

    pygameWindow.drawBlackLine(handleVectorFromLeap(base), handleVectorFromLeap(tip), b)


def handleVectorFromLeap(v):
    global x, y, xMin, xMax, yMin, yMax, tip
    x = v[0]
    y = -v[2]

    if x < xMin:
        xMin = x
    if x > xMax:
        xMax = x
    if y < yMin:
        yMin = y
    if y > yMax:
        yMax = y

    pygameX = int(Scale(x, xMin, xMax, 0, pygameWindowWidth))
    pygameY = int(Scale(y, yMax, yMin, 0, pygameWindowDepth))

    if pygameX > pygameWindowWidth/3 + 40:
        pygameWindow.setImage(leftImage)
    elif pygameX < pygameWindowDepth/4 - 30:
        pygameWindow.setImage(rightImage)
    elif pygameY > pygameWindowDepth/4 + 60:
        pygameWindow.setImage(upImage)
    elif pygameY < pygameWindowDepth/3 - 100:
        pygameWindow.setImage(downImage)

    return pygameX, pygameY

def CenterData(data):
    allXCoordinates = data[0, ::3]
    meanValue = allXCoordinates.mean()
    data[0, ::3] = allXCoordinates - meanValue

    allYCoordinates = data[0, 1::3]
    meanValue2 = allYCoordinates.mean()
    data[0, 1::3] = allYCoordinates - meanValue2

    allZCoordinates = data[0, 2::3]
    meanValue3 = allZCoordinates.mean()
    data[0, 2::3] = allZCoordinates - meanValue3

    return data


controller = Leap.Controller()

# infinite loop
while True:
    pygameWindow.prepare()
    if programState == 0:
        HandleState0()
    elif programState == 1:
        HandleState1()
    frame = controller.frame()
    if len(frame.hands) > 0:
        k = 0

    pygameWindow.drawGreenLine((0, pygameWindowDepth / 2), (pygameWindowWidth, pygameWindowDepth / 2), 4)
    pygameWindow.drawGreenLine((pygameWindowDepth / 2, 0), (pygameWindowDepth / 2, pygameWindowDepth / 2), 4)
    pygameWindow.reveal()

