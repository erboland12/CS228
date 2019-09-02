import sys
sys.path.insert(0, '..')
import Leap

controller = Leap.Controller()


from pygameWindow import PYGAME_WINDOW
import random
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
    global x, y, xMin, xMax, yMin, yMax, tip
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
    print frame
    print xMax, xMin, yMax, yMin

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
    pygameWindow.drawBlackCircle(x, y)
    # perturbCirclePosition()
    pygameWindow.reveal()
