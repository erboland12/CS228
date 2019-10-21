import sys
import pygame
from pygameWindow import PYGAME_WINDOW
import threading
import random
import time
import random
import numpy as np
import pickle
from constants import pygameWindowDepth, pygameWindowWidth

clf = pickle.load(open('classifier.p', 'rb'))
testData = np.zeros((1, 30), dtype='f')

sys.path.insert(0, '../../../../')
from x86 import Leap

database = pickle.load(open('userData/database.p', 'rb'))
nameEntered = False

controller = Leap.Controller()

#
# coordinate variables
x = 250
y = 250
one = 'images/hand.jpg'
newImage = pygame.image.load(one)
newImage = pygame.transform.scale(newImage, (pygameWindowWidth / 2, pygameWindowDepth / 2))
zero = 'images/zero.jpg'
newImage2 = pygame.image.load(zero)
newImage2 = pygame.transform.scale(newImage2, (pygameWindowWidth / 2, pygameWindowDepth / 2))
aslZero = 'images/aslZero.png'
aslImage = pygame.image.load(aslZero)
aslImage = pygame.transform.scale(aslImage, (pygameWindowWidth / 2, pygameWindowDepth / 2))
five = 'images/five.jpg'
newImage3 = pygame.image.load(five)
newImage3 = pygame.transform.scale(newImage3, (pygameWindowWidth / 2, pygameWindowDepth / 2))
aslFive = 'images/aslFive.jpg'
aslFive = pygame.image.load(aslFive)
aslFive = pygame.transform.scale(aslFive, (pygameWindowWidth / 2, pygameWindowDepth / 2))
left = 'images/leftArrow.png'
leftImage = pygame.image.load(left)
leftImage = pygame.transform.scale(leftImage, (pygameWindowWidth / 2, pygameWindowDepth / 2))

right = 'images/rightArrow.png'
rightImage = pygame.image.load(right)
rightImage = pygame.transform.scale(rightImage, (pygameWindowWidth / 2, pygameWindowDepth / 2))

up = 'images/upArrow.png'
upImage = pygame.image.load(up)
upImage = pygame.transform.scale(upImage, (pygameWindowWidth / 2, pygameWindowDepth / 2))

down = 'images/downArrow.png'
downImage = pygame.image.load(down)
downImage = pygame.transform.scale(downImage, (pygameWindowWidth / 2, pygameWindowDepth / 2))

thumbsUp = 'images/thumbsUp.jpg'
thumbsUpImage = pygame.image.load(thumbsUp)
thumbsUpImage = pygame.transform.scale(thumbsUpImage, (pygameWindowWidth / 2, pygameWindowDepth / 2))

success = 'images/success.png'
successImage = pygame.image.load(success)
successImage = pygame.transform.scale(successImage, (pygameWindowWidth / 2, pygameWindowDepth / 2))

recording = 'images/redDot.png'
recordingImage = pygame.image.load(recording)
recordingImage = pygame.transform.scale(recordingImage, (pygameWindowWidth / 2, pygameWindowDepth / 2))
framesHeld = 0
currentImage = ''
seconds = 0
counter = 0
randomNum = 1

programState = 0



def HandleState0():
    global controller, programState
    pygameWindow.setImage(newImage)
    frame = controller.frame()
    if len(frame.hands) > 0:
        programState = 1


def HandleState1():
    global controller, programState
    frame = controller.frame()
    pygameWindow.setImage(leftImage)
    hand = frame.hands[0]
    fingers = hand.fingers
    for finger in fingers:
        handleFinger(finger, k)

    if len(frame.hands) == 0:
        programState = 0


def HandleState2():
    global controller, k, framesHeld, counter, randomNum, programState, testData
    framesHeld = 0

    if randomNum == 1:
        pygameWindow.setImage(aslFive)
        pygameWindow.setSign(newImage3)
    elif randomNum == 2:
        pygameWindow.setImage(aslImage)
        pygameWindow.setSign(newImage2)
    frame = controller.frame()
    hand = frame.hands[0]
    fingers = hand.fingers
    for finger in fingers:
        handleFinger(finger, k)
        for b in range(0, 4):
            tip = finger.bone(b).next_joint
            if b == 0 or b == 3:
                testData[0, k] = tip[0]
                testData[0, k + 1] = tip[1]
                testData[0, k + 2] = tip[2]
                k += 3
    testData = CenterData(testData)
    predictedClass = clf.Predict(testData)
    print(predictedClass)
    for i in range(0, 10):
        if random == i:
            if predictedClass == i:
                counter += 1
            else:
                counter == 0

    if counter >= 10:
        pygameWindow.setImage(successImage)
        randomNum = random.randint(1, 10)
        print random
        programState = 3
        counter = 0


def HandleState3():
    global controller, programState, seconds, frame
    time.sleep(3)
    if len(frame.hands) == 1:
        programState = 0
    elif len(frame.hands) == 0:
        programState = 1


xMin = 1000.0
xMax = -1000.0
yMin = 1000.0
yMax = -1000.0


def handleFrame():
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
            return scaledValue / 2
        else:
            scaledValue = (((value - dMin) * newRange) / oldRange) + min
            return scaledValue / 2

    else:
        oldRange = dMax - dMin
        newRange = max - min
        if dMin == dMax:
            scaledValue = min
            return scaledValue / 2
        else:
            scaledValue = (((value - dMin) * newRange) / oldRange) + min
            return scaledValue / 2


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
    global x, y, xMin, xMax, yMin, yMax, tip, random, seconds, start_ticks, programState, framesHeld, currentImage, seconds
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

    now = pygame.time.get_ticks()

    if pygameX > pygameWindowWidth / 3 + pygameWindowWidth / 6:
        pygameWindow.setImage(leftImage)
        currentImage = leftImage
    elif pygameX < pygameWindowWidth / 4:
        pygameWindow.setImage(rightImage)
        currentImage = rightImage
    elif pygameY > pygameWindowDepth / 4:
        pygameWindow.setImage(upImage)
        currentImage = upImage
    elif pygameY < pygameWindowDepth / 3 - pygameWindowDepth / 5:
        pygameWindow.setImage(downImage)
        currentImage = downImage
    else:
        framesHeld += 1
        pygameWindow.setImage(recordingImage)
        currentImage = recordingImage
    if 5000 <= framesHeld < 5250:
        pygameWindow.setImage(thumbsUpImage)
    elif framesHeld == 5250:
        programState = 2
        seconds = 10
        framesHeld = 0
    if programState == 2:
        if random == 1:
            pygameWindow.setImage(aslFive)
        else:
            pygameWindow.setImage(aslImage)
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
frame = controller.frame()
start_ticks = pygame.time.get_ticks()

userName = raw_input('Please enter your name: ')
if userName in database:
    logs = database[userName]['logins']
    temp = logs + 1
    database[userName]['logins'] = temp
    nameEntered = True

    print 'welcome back ' + userName + '.'
else:
    database[userName] = {}
    database[userName]['logins'] = 1
    print 'welcome ' + userName + '.'
    nameEntered = True

print database

pickle.dump(database, open('userData/database.p', 'wb'))
# infinite loop
while True:
    if nameEntered:
        pygameWindow = PYGAME_WINDOW()
        pygameWindow.prepare()
        if programState == 0:
            HandleState0()
        elif programState == 1:
            HandleState1()
        elif programState == 2:
            HandleState2()
        elif programState == 3:
            HandleState3()
        frame = controller.frame()
        if len(frame.hands) > 0:
            k = 0

        pygameWindow.drawGreenLine((0, pygameWindowDepth / 2), (pygameWindowWidth, pygameWindowDepth / 2), 4)
        pygameWindow.drawGreenLine((pygameWindowDepth / 2, 0), (pygameWindowDepth / 2, pygameWindowDepth / 2), 4)
        pygameWindow.reveal()
    # print programState
