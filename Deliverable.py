from pygameWindowDe103 import PYGAME_WINDOW
from constants import pygameWindowWidth, pygameWindowDepth
import sys
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


class DELIVERABLE:
    def __init__(self, controller, pygameWindow, x, y, xMin, xMax, yMin, yMax):
        self.controller = controller
        self.pygameWindow = pygameWindow
        self.x = x
        self.y = y
        self.xMin = xMin
        self.xMax = xMax
        self.yMin = yMin
        self.yMax = yMax

    def handleFrame(self, frame):
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

        pygameWindow.drawBlackLine(self.handleVectorFromLeap(base), self.handleVectorFromLeap(tip), b)

    def handleVectorFromLeap(self, v):
        global x, y, xMin, xMax, yMin, yMax, tip
        x = v[0]
        y = -v[2]

        print x, y
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

        return pygameX, pygameY

    def Run_Once(self):
      pygameWindow.prepare()
      frame = controller.frame()

      if len(frame.hands) > 0:
        hand = frame.hands[0]
        fingers = hand.fingers
        for finger in fingers:
          self.handleFinger(finger)
      pygameWindow.reveal()

    def Run_Forever(self):
        while True:
            self.Run_Once()
