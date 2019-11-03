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

database = pickle.load(open('userData/database.p'))
nameEntered = False

controller = Leap.Controller()

#
# coordinate variables
x = 250
y = 250
hand = 'images/hand.jpg'
handImage = pygame.image.load(hand)
hand = pygame.transform.scale(handImage, (pygameWindowWidth / 2, pygameWindowDepth / 2))

zero = 'images/zero.jpg'
newImage2 = pygame.image.load(zero)
newImage2 = pygame.transform.scale(newImage2, (pygameWindowWidth / 2, pygameWindowDepth / 2))

aslZero = 'images/aslZero.png'
aslImage = pygame.image.load(aslZero)
aslImage = pygame.transform.scale(aslImage, (pygameWindowWidth / 2, pygameWindowDepth / 2))

one = 'images/one.png'
newImage = pygame.image.load(one)
newImage = pygame.transform.scale(newImage, (pygameWindowWidth / 2, pygameWindowDepth / 2))

aslOne = 'images/aslOne.jpg'
aslImage1 = pygame.image.load(aslOne)
aslImage1 = pygame.transform.scale(aslImage1, (pygameWindowWidth / 2, pygameWindowDepth / 2))

two = 'images/two.png'
twoImage = pygame.image.load(two)
twoImage = pygame.transform.scale(twoImage, (pygameWindowWidth / 2, pygameWindowDepth / 2))

aslTwo = 'images/aslTwo.jpg'
aslImage2 = pygame.image.load(aslTwo)
aslImage2 = pygame.transform.scale(aslImage2, (pygameWindowWidth / 2, pygameWindowDepth / 2))

three = 'images/three.jpg'
threeImage = pygame.image.load(three)
threeImage = pygame.transform.scale(threeImage, (pygameWindowWidth / 2, pygameWindowDepth / 2))

aslThree = 'images/aslThree.jpg'
aslImage3 = pygame.image.load(aslThree)
aslImage3 = pygame.transform.scale(aslImage3, (pygameWindowWidth / 2, pygameWindowDepth / 2))

five = 'images/five.png'
newImage3 = pygame.image.load(five)
newImage3 = pygame.transform.scale(newImage3, (pygameWindowWidth / 2, pygameWindowDepth / 2))

aslFive = 'images/aslFive.jpg'
aslFive = pygame.image.load(aslFive)
aslFive = pygame.transform.scale(aslFive, (pygameWindowWidth / 2, pygameWindowDepth / 2))

eight = 'images/eight.jpg'
eightImage = pygame.image.load(eight)
eightImage = pygame.transform.scale(eightImage, (pygameWindowWidth / 2, pygameWindowDepth / 2))

aslEight = 'images/aslEight.jpg'
aslImage8 = pygame.image.load(aslEight)
aslImage8 = pygame.transform.scale(aslImage8, (pygameWindowWidth / 2, pygameWindowDepth / 2))

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

wrong = 'images/wrong.png'
wrongImage = pygame.image.load(wrong)
wrongImage = pygame.transform.scale(wrongImage, (pygameWindowWidth / 2, pygameWindowDepth / 2))

white = 'images/whiteBg.png'
whiteImage = pygame.image.load(white)
whiteImage = pygame.transform.scale(whiteImage, (pygameWindowWidth / 2, pygameWindowDepth / 2))

framesHeld = 0
currentImage = ''
seconds = 0
counter = 0
errorCounter = 0
signedCorrect = 0
signedWrong = 0
totalCorrect = 0
# randomNum = random.randint(1, 6)
randomNum = 1
programState = 0

def HandleState0():
    global controller, programState
    pygameWindow.setImage(handImage)
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
    global controller, k, framesHeld, userName, totalCorrect, counter, errorCounter, signedCorrect, signedWrong, randomNum, programState, testData

    setSigns(randomNum)

    frame = controller.frame()
    hand = frame.hands[0]
    if len(frame.hands) == 0:
        programState = 0
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

    if randomNum == 1:
        if predictedClass == 5:
            counter += 1
            errorCounter = 0
        else:
            counter = 0
            errorCounter += 1
    elif randomNum == 2:
        if predictedClass == 0:
            counter += 1
            errorCounter = 0
        else:
            counter = 0
            errorCounter += 1
    elif randomNum == 3:
        if predictedClass == 1:
            counter += 1
            errorCounter = 0
        else:
            counter = 0
            errorCounter += 1
    elif randomNum == 4:
        if predictedClass == 2:
            counter += 1
            errorCounter = 0
        else:
            counter = 0
            errorCounter += 1
    elif randomNum == 5:
        if predictedClass == 3:
            counter += 1
            errorCounter = 0
        else:
            counter = 0
            errorCounter += 1
    elif randomNum == 6:
        if predictedClass == 8:
            counter += 1
            errorCounter = 0
        else:
            counter = 0
            errorCounter += 1

    if counter >= 5 and totalCorrect > 0:
        pygameWindow.setSign(whiteImage)

    if counter >= 3 and totalCorrect > 1:
        pygameWindow.setSign(whiteImage)

    if counter >= 0 and totalCorrect > 2:
        pygameWindow.setSign(whiteImage)

    if (counter >= 10 and totalCorrect == 0):
        handleCorrectResponse(randomNum)
    elif counter >= 8 and totalCorrect > 0:
        handleCorrectResponse(randomNum)
    elif counter >= 6 and totalCorrect > 1:
        handleCorrectResponse(randomNum)
    elif counter >= 4 and totalCorrect > 2:
        handleCorrectResponse(randomNum)

    if errorCounter >= 20:
        if randomNum == 1:
            database[userName]['digit5attempted'] += 1
            print database[userName]['digit5attempted']
        elif randomNum == 2:
            database[userName]['digit0attempted'] += 1
            print database[userName]['digit0attempted']
        elif randomNum == 3:
            database[userName]['digit1attempted'] += 1
            print database[userName]['digit1attempted']
        elif randomNum == 4:
            database[userName]['digit2attempted'] += 1
            print database[userName]['digit2attempted']
        elif randomNum == 5:
            database[userName]['digit3attempted'] += 1
            print database[userName]['digit3attempted']
        elif randomNum == 6:
            database[userName]['digit8attempted'] += 1
            print database[userName]['digit8attempted']

        pygameWindow.setImage(wrongImage)
        programState = 3
        counter = 0
        errorCounter = 0
        signedWrong += 1
        pickle.dump(database, open('userData/database.p', 'wb'))

    myfont = pygame.font.SysFont('Comic Sans MS', 20)
    title = myfont.render('Attempts', False, (0, 0, 0))
    pygameWindow.screen.blit(title, (pygameWindowWidth / 10, pygameWindowDepth / 2))
    zero = myfont.render('Zero - ' + str(database[userName]['digit0attempted']), False, (0, 0, 0))
    pygameWindow.screen.blit(zero, (pygameWindowWidth / 10, pygameWindowDepth / 2 + 20))
    one = myfont.render('One - ' + str(database[userName]['digit1attempted']), False, (0, 0, 0))
    pygameWindow.screen.blit(one, (pygameWindowWidth / 10, pygameWindowDepth / 2 + 40))
    two = myfont.render('Two - ' + str(database[userName]['digit2attempted']), False, (0, 0, 0))
    pygameWindow.screen.blit(two, (pygameWindowWidth / 10, pygameWindowDepth / 2 + 60))
    three = myfont.render('Three - ' + str(database[userName]['digit3attempted']), False, (0, 0, 0))
    pygameWindow.screen.blit(three, (pygameWindowWidth / 10, pygameWindowDepth / 2 + 80))
    four = myfont.render('Four - ' + str(database[userName]['digit4attempted']), False, (0, 0, 0))
    pygameWindow.screen.blit(four, (pygameWindowWidth / 10, pygameWindowDepth / 2 + 100))
    five = myfont.render('Five - ' + str(database[userName]['digit5attempted']), False, (0, 0, 0))
    pygameWindow.screen.blit(five, (pygameWindowWidth / 10, pygameWindowDepth / 2 + 120))
    six = myfont.render('Six - ' + str(database[userName]['digit6attempted']), False, (0, 0, 0))
    pygameWindow.screen.blit(six, (pygameWindowWidth / 10, pygameWindowDepth / 2 + 140))
    seven = myfont.render('Seven - ' + str(database[userName]['digit7attempted']), False, (0, 0, 0))
    pygameWindow.screen.blit(seven, (pygameWindowWidth / 10, pygameWindowDepth / 2 + 160))
    eight = myfont.render('Eight - ' + str(database[userName]['digit8attempted']), False, (0, 0, 0))
    pygameWindow.screen.blit(eight, (pygameWindowWidth / 10, pygameWindowDepth / 2 + 180))
    nine = myfont.render('Nine - ' + str(database[userName]['digit9attempted']), False, (0, 0, 0))
    pygameWindow.screen.blit(nine, (pygameWindowWidth / 10, pygameWindowDepth / 2 + 200))

def HandleState3():
    global controller, programState, seconds, frame, randomNum
    time.sleep(3)
    if len(frame.hands) == 1:
        programState = 2
    elif len(frame.hands) == 0:
        programState = 1


xMin = 1000.0
xMax = -1000.0
yMin = 1000.0
yMax = -1000.0

def handleCorrectResponse(randomNumber):
    global controller, k, framesHeld, userName, totalCorrect, counter, errorCounter, signedCorrect, signedWrong, randomNum, programState, testData
    if randomNum == 1:
        database[userName]['digit5attempted'] += 1
        print database[userName]['digit5attempted']
    elif randomNum == 2:
        database[userName]['digit0attempted'] += 1
        print database[userName]['digit0attempted']
    elif randomNum == 3:
        database[userName]['digit1attempted'] += 1
        print database[userName]['digit1attempted']
    elif randomNum == 4:
        database[userName]['digit2attempted'] += 1
        print database[userName]['digit2attempted']
    elif randomNum == 5:
        database[userName]['digit3attempted'] += 1
        print database[userName]['digit3attempted']
    elif randomNum == 6:
        database[userName]['digit8attempted'] += 1
        print database[userName]['digit8attempted']

    pygameWindow.setImage(successImage)
    signedCorrect += 1
    totalCorrect += 1
    programState = 3
    counter = 0
    errorCounter = 0
    if signedWrong >= 3:
        if signedCorrect >= 3:
            # randomNum = random.randint(1, 6)
            signedCorrect = 0
            signedWrong = 0
    elif signedWrong < 3 and signedCorrect > 0:
        # randomNum = random.randint(1, 6)
        signedCorrect = 0
        signedWrong = 0

    pickle.dump(database, open('userData/database.p', 'wb'))

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
    if programState == 1:
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
            pygameWindow.setImage(recordingImage)
            framesHeld += 1
        if 3500 <= framesHeld < 3750:
            pygameWindow.setImage(thumbsUpImage)
        if framesHeld >= 3750:
            framesHeld = 0
            programState = 2

    return pygameX, pygameY

def setSigns(randomNum):
    if randomNum == 1:
        pygameWindow.setSign(aslFive)
        pygameWindow.setImage(newImage3)
    elif randomNum == 2:
        pygameWindow.setSign(aslImage)
        pygameWindow.setImage(newImage2)
    elif randomNum == 3:
        pygameWindow.setSign(aslImage1)
        pygameWindow.setImage(newImage)
    elif randomNum == 4:
        pygameWindow.setSign(aslImage2)
        pygameWindow.setImage(twoImage)
    elif randomNum == 5:
        pygameWindow.setSign(aslImage3)
        pygameWindow.setImage(threeImage)
    elif randomNum == 6:
        pygameWindow.setSign(aslImage8)
        pygameWindow.setImage(eightImage)


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
    database[userName]['logins'] += 1
    nameEntered = True

    print 'welcome back ' + userName + '.'
else:
    database[userName] = {}
    database[userName]['logins'] = 1
    database[userName]['digit0attempted'] = 0
    database[userName]['digit1attempted'] = 0
    database[userName]['digit2attempted'] = 0
    database[userName]['digit3attempted'] = 0
    database[userName]['digit4attempted'] = 0
    database[userName]['digit5attempted'] = 0
    database[userName]['digit6attempted'] = 0
    database[userName]['digit7attempted'] = 0
    database[userName]['digit8attempted'] = 0
    database[userName]['digit9attempted'] = 0
    print 'welcome ' + userName + '.'
    nameEntered = True
print randomNum
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
