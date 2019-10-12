import pickle
import os
from pygameWindowDe103 import PYGAME_WINDOW
import sys
import numpy as np
import time

sys.path.insert(0, '..')
from x86 import Leap

controller = Leap.Controller()
pygameWindow = PYGAME_WINDOW()


class READER:
    def __init__(self, pygameWindow):
        self.pygameWindow = pygameWindow
        self.Read_Gesture()
        self.gestureData = np.zeros((5, 4, 6), dtype='f')

    def Read_Gesture(self):
        path, dirs, files = next(os.walk('userData'))
        self.numGestures = len(files)

    def Print_Gestures(self):
        for i in range(0, self.numGestures):
            pickle_in = open("userData/gesture" + str(i) + ".p", "rb")
            newData = pickle.load(pickle_in)
            print newData

    def Draw_Gesture(self, i):
        pygameWindow.prepare()
        pickle_in = open("userData/gesture" + str(i) + ".p", "rb")
        gestureData = pickle.load(pickle_in)
        for i in range(0, 5):
            for j in range(0, 4):
                currentBone = gestureData[i, j, :]
                print i, j, currentBone
                xBaseNotYetScaled = currentBone[0]
                yBaseNotYetScaled = currentBone[2]
                xTipNotYetScaled = currentBone[3]
                yTipNotYetScaled = currentBone[5]
                xBase = self.Scale(xBaseNotYetScaled, -250, 250, 0, 300)
                yBase = self.Scale(yBaseNotYetScaled, -250, 250, 0, 300)
                xTip = self.Scale(xTipNotYetScaled, -250, 250, 0, 300)
                yTip = self.Scale(yTipNotYetScaled, -250, 250, 0, 300)
                pygameWindow.drawBlueLine((xBase, yBase), (xTip, yTip),
                                          i)
        # pickle_in = open("userData/gesture1.p", "rb")
        # gestureData = pickle.load(pickle_in)
        # print gestureData

        pygameWindow.reveal()
        time.sleep(0.5)

    def Scale(self, value, dMin, dMax, min, max):
        if dMin > value.any() > dMax:
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

    def Draw_Each_Gesture_Once(self):
        for i in range(0, self.numGestures):
            self.Draw_Gesture(i)

    def Draw_Gestures(self):
        while True:
            self.Draw_Each_Gesture_Once()
