import pygame

from constants import pygameWindowDepth, pygameWindowWidth

white = [255, 255, 255]
green = [0, 128, 0]
red = [255, 0, 0]
black = [0, 0, 0]

class PYGAME_WINDOW:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((pygameWindowWidth,pygameWindowDepth))

    def prepare(self):
        self.screen.fill(white)

    def reveal(self):
        pygame.display.update()

    def drawBlackCircle(self, x, y):
        pygame.draw.circle(self.screen, black, (x, y), 10)

    def drawLine(self, (xBase, yBase), (xTip, yTip), b, i):
        if i == 1:
            pygame.draw.line(self.screen, green, (xBase, yBase), (xTip, yTip), b)
        elif i == 2:
            pygame.draw.line(self.screen, red, (xBase, yBase), (xTip, yTip), b)


