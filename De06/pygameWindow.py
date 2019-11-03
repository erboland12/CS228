import pygame
from constants import pygameWindowDepth, pygameWindowWidth

white = [255, 255, 255]
black = [0, 0, 0]
green = [30, 255, 30]


class PYGAME_WINDOW:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((pygameWindowWidth, pygameWindowDepth))

    def prepare(self):
        self.screen.fill(white)

    def reveal(self):
        pygame.display.update()

    def drawBlackCircle(self, x, y):
        pygame.draw.circle(self.screen, black, (x, y), 10)

    def drawBlackLine(self, (xBase, yBase), (xTip, yTip), b):
        pygame.draw.line(self.screen, black, (xBase, yBase), (xTip, yTip), b)

    def drawGreenLine(self, (xBase, yBase), (xTip, yTip), b):
        pygame.draw.line(self.screen, green, (xBase, yBase), (xTip, yTip), b)

    def setImage(self, image):
        self.screen.blit(image, (pygameWindowWidth / 2, 0))

    def setSign(self, image):
        self.screen.blit(image, (pygameWindowWidth / 2, pygameWindowDepth / 2))


