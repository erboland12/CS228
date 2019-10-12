import sys
from pygameWindow import PYGAME_WINDOW
import random

sys.path.insert(0, '../..')
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

def handleFinger(f):
    for b in range(0, 4):
        if b == 0:
            handleBone(f.bone(b), 4)
        elif b == 1:
            handleBone(f.bone(b), 3)
        elif b == 2:
            handleBone(f.bone(b), 2)
        elif b == 3:
            handleBone(f.bone(b), 1)

def handleBone(bone, b):
    base = bone.prev_joint
    tip = bone.next_joint

    pygameWindow.drawBlackLine(handleVectorFromLeap(base), handleVectorFromLeap(tip), b)


def handleVectorFromLeap(v):
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

    pygameX = int(Scale(x, xMin, xMax, 0, pygameWindowWidth))
    pygameY = int(Scale(y, yMax, yMin, 0, pygameWindowDepth))

    return pygameX, pygameY


controller = Leap.Controller()

# infinite loop
while True:
    pygameWindow.prepare()
    frame = controller.frame()
    if len(frame.hands) > 0:
        hand = frame.hands[0]
        fingers = hand.fingers
        for finger in fingers:
            handleFinger(finger)

    pygameWindow.reveal()
