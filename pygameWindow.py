import pygame

from constants import pygameWindowDepth, pygameWindowWidth

white = [255, 255, 255]
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




