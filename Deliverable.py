from pygameWindowDe103 import PYGAME_WINDOW
from constants import pygameWindowWidth, pygameWindowDepth
import sys
import numpy as np
import os
import shutil

sys.path.insert(0, '..')
import Leap

x = 250
y = 250
xMin = 1000.0
xMax = -1000.0
yMin = 1000.0
yMax = -1000.0
controller = Leap.Controller()
pygameWindow = PYGAME_WINDOW()

xCord = 0
yCord = 0
zCord = 0


class DELIVERABLE:
    import pickle
    numberOfHands = 0
    previousNumberOfHands = 0
    currentNumberOfHands = 0

    def __init__(self, controller, pygameWindow, x, y, xMin, xMax, yMin, yMax, prev, curr):
        self.controller = controller
        self.pygameWindow = pygameWindow
        self.x = x
        self.y = y
        self.xMin = xMin
        self.xMax = xMax
        self.yMin = yMin
        self.yMax = yMax
        self.previousNumberOfHands = prev
        self.currentNumberOfHands = curr
        self.gestureData = np.zeros((5, 4, 6), dtype='f')
        self.gestI = 0

    def handleFrame(self, i):
        self.currentNumberOfHands = i
        # global x, y, xMin, xMax, yMin, yMax, tip, pygameWindowWidth, pygameWindowDepth
        # x = int(tip[0])
        # y = int(tip[2])
        #
        # if x < xMin:
        #     xMin = x
        # if x > xMax:
        #     xMax = x
        # if y < yMin:
        #     yMin = y
        # if y > yMax:
        #     yMax = y

        if self.Recording_Is_Ending():
            print self.gestureData[0]
            self.Save_Gesture()

        self.previousNumberOfHands = self.currentNumberOfHands

    def Scale(self, value, dMin, dMax, min, max):
        if dMin > value > dMax:
            oldRange = dMax - dMin
            newRange = max - min
            if dMin == dMax:
                scaledValue = min
                return scaledValue
            else:
                scaledValue = (((value - dMin) * newRange) / oldRange) + min
                return scaledValue
        else:
            oldRange = dMax - dMin
            newRange = max - min
            if dMin == dMax:
                scaledValue = min
                return scaledValue
            else:
                scaledValue = (((value - dMin) * newRange) / oldRange) + min
                return scaledValue

    def handleFinger(self, f):
        for b in range(0, 4):
            if b == 0:
                self.handleBone(f.bone(b), 4)
            elif b == 1:
                self.handleBone(f.bone(b), 3)
            elif b == 2:
                self.handleBone(f.bone(b), 2)
            elif b == 3:
                self.handleBone(f.bone(b), 1)

    def handleBone(self, bone, b):
        base = bone.prev_joint
        tip = bone.next_joint

        rawBone = base
        rawTip = tip
        pygameWindow.drawLine(self.handleVectorFromLeap(base), self.handleVectorFromLeap(tip), b,
                              self.currentNumberOfHands)
        for i in range(0, 5):
            self.gestureData[i, -b + 4, 0] = base[0]
            self.gestureData[i, -b + 4, 1] = base[1]
            self.gestureData[i, -b + 4, 2] = base[2]
            self.gestureData[i, -b + 4, 3] = tip[0]
            self.gestureData[i, -b + 4, 4] = tip[1]
            self.gestureData[i, -b + 4, 5] = tip[2]

    def handleVectorFromLeap(self, v):
        global x, y, xCord, yCord, zCord, xMin, xMax, yMin, yMax, tip
        x = v[0]
        y = -v[2]

        xCord = v[0]
        yCord = v[1]
        zCord = v[2]

        if x < xMin:
            xMin = x
        if x > xMax:
            xMax = x
        if y < yMin:
            yMin = y
        if y > yMax:
            yMax = y

        pygameX = int(self.Scale(x, xMin, xMax, 0, pygameWindowWidth))
        pygameY = int(self.Scale(y, yMax, yMin, 0, pygameWindowDepth))
        xCord = pygameX
        yCord = pygameY
        zCord = v[2]

        return pygameX, pygameY

    def Recording_Is_Ending(self):
        if self.previousNumberOfHands > self.currentNumberOfHands:
            return True

    def Save_Gesture(self):
        self.pickle_out = open("userData/gesture" + str(self.gestI) + ".p", "wb")
        self.pickle.dump(self.gestureData[0], self.pickle_out)
        self.pickle_out.close()
        self.gestI += 1

    def delDirectory(self):
        shutil.rmtree("userData")
        os.mkdir("userData")

    def Run_Once(self):
        pygameWindow.prepare()
        frame = controller.frame()
        if len(frame.hands) > 0:
            if len(frame.hands) == 1:
                self.handleFrame(1)
                hand = frame.hands[0]
                fingers = hand.fingers
                for finger in fingers:
                    self.handleFinger(finger)
            elif len(frame.hands) == 2:
                self.handleFrame(2)
                hand = frame.hands[0]
                fingers = hand.fingers
                for finger in fingers:
                    self.handleFinger(finger)
        pygameWindow.reveal()

    def Run_Forever(self):
        while True:
            self.Run_Once()
            self.previousNumberOfHands = self.currentNumberOfHands
