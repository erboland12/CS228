from pygameWindow import PYGAME_WINDOW
import random
pygameWindow = PYGAME_WINDOW()

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

# infinite loop
while True:
    pygameWindow.prepare()
    pygameWindow.drawBlackCircle(x, y)
    perturbCirclePosition()
    pygameWindow.reveal()
