import pickle
import os
from pygameWindowDe103 import PYGAME_WINDOW
import sys
sys.path.insert(0, '..')
import Leap

controller = Leap.Controller()
pygameWindow = PYGAME_WINDOW()


class READER:
    def __init__(self, pygameWindow):
        self.pygameWindow = pygameWindow
        self.Read_Gesture()

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
        for i in range(0, 4):
            for j in range(0, 3):
                currentBone = gestureData[i]
                xBaseNotYetScaled = currentBone[0]
                yBaseNotYetScaled = currentBone[1]
                xTipNotYetScaled = currentBone[2]
                yTipNotYetScaled = currentBone[3]
                xBase = self.Scale(xBaseNotYetScaled, -100000, 100000, -1000000, 100000)
                yBase = self.Scale(yBaseNotYetScaled, -100000, 100000, -1000000, 100000)
                xTip = self.Scale(xTipNotYetScaled, -100000, 100000, -1000000, 100000)
                yTip = self.Scale(yTipNotYetScaled, -1000, 1000, -10000, 10000)
                pygameWindow.drawBlueLine((xBaseNotYetScaled, yBaseNotYetScaled), (xTipNotYetScaled, yTipNotYetScaled), i)
        pygameWindow.reveal()

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