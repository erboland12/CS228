import sys
import pygame
from pygameWindow import PYGAME_WINDOW
import threading
import random
import time
import random
import numpy as np
import pickle
import atexit
from constants import pygameWindowDepth, pygameWindowWidth

clf = pickle.load(open('classifier.p', 'rb'))
testData = np.zeros((1, 30), dtype='f')

sys.path.insert(0, '../../../../')
from x86 import Leap

database = pickle.load(open('userData/database.p','rb'))

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

four = 'images/four.png'
fourImage = pygame.image.load(four)
fourImage = pygame.transform.scale(fourImage, (pygameWindowWidth / 2, pygameWindowDepth / 2))

aslFour = 'images/aslFour.jpg'
aslFourImage = pygame.image.load(aslFour)
aslFourImage = pygame.transform.scale(aslFourImage, (pygameWindowWidth / 2, pygameWindowDepth / 2))

five = 'images/five.png'
newImage3 = pygame.image.load(five)
newImage3 = pygame.transform.scale(newImage3, (pygameWindowWidth / 2, pygameWindowDepth / 2))

aslFive = 'images/aslFive.jpg'
aslFive = pygame.image.load(aslFive)
aslFive = pygame.transform.scale(aslFive, (pygameWindowWidth / 2, pygameWindowDepth / 2))

six = 'images/six.png'
sixImage = pygame.image.load(six)
sixImage = pygame.transform.scale(sixImage, (pygameWindowWidth / 2, pygameWindowDepth / 2))

aslSix = 'images/aslSix.jpg'
aslSixImage = pygame.image.load(aslSix)
aslSixImage = pygame.transform.scale(aslSixImage, (pygameWindowWidth / 2, pygameWindowDepth / 2))

seven = 'images/seven.png'
sevenImage = pygame.image.load(seven)
sevenImage = pygame.transform.scale(sevenImage, (pygameWindowWidth / 2, pygameWindowDepth / 2))

aslSeven = 'images/aslSeven.png'
aslSevenImage = pygame.image.load(aslSeven)
aslSevenImage = pygame.transform.scale(aslSevenImage, (pygameWindowWidth / 2, pygameWindowDepth / 2))

eight = 'images/eight.jpg'
eightImage = pygame.image.load(eight)
eightImage = pygame.transform.scale(eightImage, (pygameWindowWidth / 2, pygameWindowDepth / 2))

aslEight = 'images/aslEight.jpg'
aslImage8 = pygame.image.load(aslEight)
aslImage8 = pygame.transform.scale(aslImage8, (pygameWindowWidth / 2, pygameWindowDepth / 2))

nine = 'images/nine.png'
nineImage = pygame.image.load(nine)
nineImage = pygame.transform.scale(nineImage, (pygameWindowWidth / 2, pygameWindowDepth / 2))

aslNine = 'images/aslNine.jpg'
aslNineImage = pygame.image.load(aslNine)
aslNineImage = pygame.transform.scale(aslNineImage, (pygameWindowWidth / 2, pygameWindowDepth / 2))

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
sessionCorrect = 0.0
sessionTotal = 0.0
careerCorrect = 0.0
careerAttempts = 0.0
averageRight = 0.0
averageTotal = 0.0
totalCorrect = 0
randomNum = random.randint(1, 10)
programState = -1
userName = raw_input('Please enter your name: ')
selection = ""

def HandleStateStart():
    global selection, programState
    pygameWindow.setButton()

    selected = pygameWindow.checkMouseEventsAdd()

    if selected == "add":
        selection = "addition"
        programState = 0

    if selected == "sub":
        selection = "subtraction"
        programState = 0

def HandleState0():
    global controller, programState, selection
    pygameWindow.drawGreenLine((0, pygameWindowDepth / 2), (pygameWindowWidth, pygameWindowDepth / 2), 4)
    pygameWindow.drawGreenLine((pygameWindowDepth / 2, 0), (pygameWindowDepth / 2, pygameWindowDepth / 2), 4)
    pygameWindow.setBackButton()
    back = pygameWindow.checkMouseEventsAdd()
    if back == "back":
        HandleStateStart()
        programState = -1
    font = pygameWindow.font
    mode = font.render('You are currently in ' + selection + ' mode', False, (0, 0, 0))
    pygameWindow.screen.blit(mode, (pygameWindowWidth / 25, pygameWindowDepth / 2 + 100))
    goBack = font.render('Click the button below to return to the selection screen', False, (0, 0, 0))
    pygameWindow.screen.blit(goBack, (pygameWindowWidth / 25, pygameWindowDepth / 2 + 120))
    pygameWindow.setImage(handImage)
    frame = controller.frame()
    saveSessionStats()
    print selection
    if len(frame.hands) > 0:
        programState = 1


def HandleState1():
    global controller, programState
    pygameWindow.drawGreenLine((0, pygameWindowDepth / 2), (pygameWindowWidth, pygameWindowDepth / 2), 4)
    pygameWindow.drawGreenLine((pygameWindowDepth / 2, 0), (pygameWindowDepth / 2, pygameWindowDepth / 2), 4)
    frame = controller.frame()
    pygameWindow.setImage(leftImage)
    hand = frame.hands[0]
    fingers = hand.fingers
    saveSessionStats()
    for finger in fingers:
        handleFinger(finger, k)

    if len(frame.hands) == 0:
        programState = 0


def HandleState2():
    global controller, k, framesHeld, userName, sessionTotal, sessionCorrect, totalCorrect, counter, errorCounter, \
        signedCorrect, signedWrong, randomNum, programState, testData, lastSessionCorrect, lastSessionTotal, careerCorrect, \
        careerAttempts, averageTotal, averageRight
    pygameWindow.drawGreenLine((0, pygameWindowDepth / 2), (pygameWindowWidth, pygameWindowDepth / 2), 4)
    pygameWindow.drawGreenLine((pygameWindowDepth / 2, 0), (pygameWindowDepth / 2, pygameWindowDepth / 2), 4)

    setSigns(randomNum)
    myfont = pygame.font.SysFont('Comic Sans MS', 14)

    saveSessionStats()
    if sessionTotal == 0:
        currSesh = myfont.render('Current Session Accuracy: 0.0%', False, (0, 0, 0))
        pygameWindow.screen.blit(currSesh, (pygameWindowWidth / 25, pygameWindowDepth / 2+ 100))
    elif sessionTotal > 0:
        currSesh = myfont.render('Current Session Accuracy: ' + str( '%.1f' % ((sessionCorrect / sessionTotal) * 100.0)) + "%", False, (0, 0, 0))
        pygameWindow.screen.blit(currSesh, (pygameWindowWidth / 25, pygameWindowDepth / 2+ 100))
    if lastSessionTotal == 0:
        lastSesh = myfont.render('Last Session Accuracy: 0.0%', False, (0, 0, 0))
        pygameWindow.screen.blit(lastSesh, (pygameWindowWidth / 25, (pygameWindowDepth / 2 + 120)))
    elif lastSessionTotal > 0:
        lastSesh = myfont.render('Last Session Accuracy: ' + str('%.1f' % ((lastSessionCorrect / lastSessionTotal) * 100.0)) + "%", False,
                                 (0, 0, 0))
        pygameWindow.screen.blit(lastSesh, (pygameWindowWidth / 25, (pygameWindowDepth / 2 + 120)))

    if averageTotal == 0:
        ave = myfont.render('Average Accuracy of All Users: 0%', False, (0, 0, 0))
        pygameWindow.screen.blit(ave, (pygameWindowWidth / 25, (pygameWindowDepth / 2 + 140)))
    elif averageTotal > 0:
        ave = myfont.render('Average Accuracy of All Users: ' + str('%1.f' % ((averageRight / averageTotal) * 100.0)) + "%",
                            False, (0, 0, 0))
        pygameWindow.screen.blit(ave, (pygameWindowWidth / 25, (pygameWindowDepth / 2 + 140)))
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
    elif randomNum == 7:
        if predictedClass == 4:
            counter += 1
            errorCounter = 0
        else:
            counter = 0
            errorCounter += 1
    elif randomNum == 8:
        if predictedClass == 6:
            counter += 1
            errorCounter = 0
        else:
            counter = 0
            errorCounter += 1
    elif randomNum == 9:
        if predictedClass == 7:
            counter += 1
            errorCounter = 0
        else:
            counter = 0
            errorCounter += 1
    elif randomNum == 10:
        if predictedClass == 9:
            counter += 1
            errorCounter = 0
        else:
            counter = 0
            errorCounter += 1

    # if counter >= 5 and totalCorrect > 0:
    #     pygameWindow.setSign(whiteImage)
    #
    # if counter >= 3 and totalCorrect > 1:
    #     pygameWindow.setSign(whiteImage)
    #
    # if counter >= 0 and totalCorrect > 2:
    #     pygameWindow.setSign(whiteImage)

    helpFont = pygame.font.SysFont('Comic Sans MS', 20)
    if 0 < counter < 10:
        warmer = helpFont.render("Warmer", False, (255, 0, 0))
        pygameWindow.screen.blit(warmer, (pygameWindowWidth / 25, (pygameWindowDepth / 2)))
    if 0 < errorCounter < 20:
        colder = helpFont.render("Colder", False, (0, 0, 255))
        pygameWindow.screen.blit(colder, (pygameWindowWidth / 25, (pygameWindowDepth / 2)))
    if counter >= 10 and totalCorrect == 0:
        sessionCorrect += 1
        sessionTotal += 1
        database[userName]['totalCorrect'] += 1
        database[userName]['totalAttempted'] += 1
        handleCorrectResponse()
    elif counter >= 8 and totalCorrect > 0:
        sessionCorrect += 1
        sessionTotal += 1
        database[userName]['totalCorrect'] += 1
        database[userName]['totalAttempted'] += 1
        handleCorrectResponse()
    elif counter >= 6 and totalCorrect > 1:
        sessionCorrect += 1
        sessionTotal += 1
        database[userName]['totalCorrect'] += 1
        database[userName]['totalAttempted'] += 1
        handleCorrectResponse()
    elif counter >= 4 and totalCorrect > 2:
        sessionCorrect += 1
        sessionTotal += 1
        database[userName]['totalCorrect'] += 1
        database[userName]['totalAttempted'] += 1
        handleCorrectResponse()

    if errorCounter >= 20:
        sessionTotal += 1
        database[userName]['totalAttempted'] += 1
        logAttempts()
        pygameWindow.setImage(wrongImage)
        programState = 3
        counter = 0
        errorCounter = 0
        signedWrong += 1
        pickle.dump(database, open('userData/database.p', 'wb'))

def HandleState3():
    pygameWindow.drawGreenLine((0, pygameWindowDepth / 2), (pygameWindowWidth, pygameWindowDepth / 2), 4)
    pygameWindow.drawGreenLine((pygameWindowDepth / 2, 0), (pygameWindowDepth / 2, pygameWindowDepth / 2), 4)
    global controller, programState, seconds, frame, randomNum, sessionCorrect, sessionTotal, database
    time.sleep(3)
    saveSessionStats()
    if len(frame.hands) == 1:
        programState = 2
    elif len(frame.hands) == 0:
        programState = 1

def saveSessionStats():
    global database, sessionCorrect, sessionTotal
    database[userName]['lastSessionCorrect'] = sessionCorrect
    database[userName]['lastSessionTotal'] = sessionTotal


xMin = 1000.0
xMax = -1000.0
yMin = 1000.0
yMax = -1000.0
def handleCorrectResponse():
    global controller, k, framesHeld, userName, totalCorrect, counter, errorCounter, signedCorrect, signedWrong, randomNum, programState, testData
    logAttempts()
    pygameWindow.setImage(successImage)
    signedCorrect += 1
    totalCorrect += 1
    programState = 3
    counter = 0
    errorCounter = 0
    if signedWrong >= 3:
        if signedCorrect >= 3:
            randomNum = random.randint(1, 10)
            signedCorrect = 0
            signedWrong = 0
    elif signedWrong < 3 and signedCorrect > 0:
        randomNum = random.randint(1, 10)
        signedCorrect = 0
        signedWrong = 0

    pickle.dump(database, open('userData/database.p', 'wb'))

def logAttempts():
    global database, randomNum
    if randomNum == 1:
        database[userName]['digit5attempted'] += 1
    elif randomNum == 2:
        database[userName]['digit0attempted'] += 1
    elif randomNum == 3:
        database[userName]['digit1attempted'] += 1
    elif randomNum == 4:
        database[userName]['digit2attempted'] += 1
    elif randomNum == 5:
        database[userName]['digit3attempted'] += 1
    elif randomNum == 6:
        database[userName]['digit8attempted'] += 1
    elif randomNum == 7:
        database[userName]['digit4attempted'] += 1
    elif randomNum == 8:
        database[userName]['digit6attempted'] += 1
    elif randomNum == 9:
        database[userName]['digit7attempted'] += 1
    elif randomNum == 10:
        database[userName]['digit9attempted'] += 1

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
    elif randomNum == 7:
        pygameWindow.setSign(aslFourImage)
        pygameWindow.setImage(fourImage)
    elif randomNum == 8:
        pygameWindow.setSign(aslSixImage)
        pygameWindow.setImage(sixImage)
    elif randomNum == 9:
        pygameWindow.setSign(aslSevenImage)
        pygameWindow.setImage(sevenImage)
    elif randomNum == 10:
        pygameWindow.setSign(aslNineImage)
        pygameWindow.setImage(nineImage)


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

if userName in database:
    database[userName]['logins'] += 1
    lastSessionCorrect = database[userName]['lastSessionCorrect'] + 1
    lastSessionTotal = database[userName]['lastSessionTotal'] + 1
    for key in database:
        averageRight += database[key]['totalCorrect']
        averageTotal += database[key]['totalAttempted']
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
    database[userName]['lastSessionCorrect'] = 0
    database[userName]['lastSessionTotal'] = 0
    database[userName]['totalCorrect'] = 0.0
    database[userName]['totalAttempted'] = 0.0
    lastSessionCorrect = 0.0
    lastSessionTotal = 0.0
    print 'welcome ' + userName + '.'
    for key in database:
        averageRight += database[key]['totalCorrect']
        averageTotal += database[key]['totalAttempted']
    nameEntered = True
print randomNum
print database

pickle.dump(database, open('userData/database.p', 'wb'))
# infinite loop
while True:
    if nameEntered:
        saveSessionStats()
        pygameWindow = PYGAME_WINDOW()
        pygameWindow.prepare()
        if programState == -1:
            HandleStateStart()
        elif programState == 0:
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

        pygameWindow.reveal()

