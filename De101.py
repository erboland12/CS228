import sys
from pygameWindow import PYGAME_WINDOW
import random

sys.path.insert(0, '..')
from x86 import Leap

controller = Leap.Controller()


pygameWindow = PYGAME_WINDOW()
#
# coordinate variables
x = 250
y = 250


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
    y = int(tip[1])

    if x < xMin:
        xMin = x
    if x > xMax:
        xMax = x
    if y < yMin:
        yMin = y
    if y > yMax:
        yMax = y

    print x
    print frame
    print xMax, xMin, yMax, yMin




def Scale(value, dMin, dMax, min, max):
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




controller = Leap.Controller()

# # infinite loop
while True:
    pygameWindow.prepare()
    frame = controller.frame()
    if len(frame.hands) > 0:
        hand = frame.hands[0]
        fingers = hand.fingers
        indexFingerList = fingers.finger_type(Leap.Finger.TYPE_INDEX)
        indexFinger = indexFingerList[0]
        print hand
        distalPhalanx = indexFinger.bone(Leap.Bone.TYPE_DISTAL)
        print distalPhalanx
        tip = distalPhalanx.next_joint
        print tip
        handleFrame(frame)
    pygameX = int(Scale(x, xMin, xMax, 0, pygameWindowWidth))
    pygameY = int(Scale(y, yMax, yMin, 0, pygameWindowDepth))
    pygameWindow.drawBlackCircle(pygameX, pygameY)
    # perturbCirclePosition()
    pygameWindow.reveal()
