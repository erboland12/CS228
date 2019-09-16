import sys
from Deliverable import DELIVERABLE, pygameWindow, x, y, xMax, xMin, yMax, yMin
from Deliverable import controller

deliv = DELIVERABLE(controller, pygameWindow,
                    x, y, xMin,
                    xMax, yMin, yMax,
                    DELIVERABLE.previousNumberOfHands, DELIVERABLE.currentNumberOfHands)
try:
    deliv.delDirectory()
except OSError:
    deliv.delDirectory()
deliv.Run_Forever()
