import pygame
from constants import pygameWindowDepth, pygameWindowWidth

white = [255, 255, 255]
black = [0, 0, 0]
green = [30, 255, 30]

addButton = pygame.Rect((pygameWindowWidth / 2) - 60, pygameWindowDepth / 2, pygameWindowWidth / 4,
                        pygameWindowDepth / 8)
subButton = pygame.Rect((pygameWindowWidth / 2) - 60, (pygameWindowDepth / 2) + 80, pygameWindowWidth / 4,
                        pygameWindowDepth / 8)

backButton = pygame.Rect((pygameWindowWidth / 6) - 60, (pygameWindowDepth / 6) + 320, pygameWindowWidth / 4, pygameWindowDepth / 8)


class PYGAME_WINDOW:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((pygameWindowWidth, pygameWindowDepth))
        self.font = pygame.font.SysFont('Arial', 18)

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

    def setButton(self):
        pygame.draw.rect(self.screen, black, addButton)
        self.screen.blit(self.font.render('Addition', True, (255, 0, 0)),
                         ((pygameWindowWidth / 2) - 60, pygameWindowDepth / 2))

        pygame.draw.rect(self.screen, black, subButton)
        self.screen.blit(self.font.render('Subtraction', True, (255, 0, 0)),
                         ((pygameWindowWidth / 2) - 60, (pygameWindowDepth / 2) + 80))

        pygame.display.update()

    def setBackButton(self):
        pygame.draw.rect(self.screen, black, backButton)
        self.screen.blit(self.font.render('Back', True, (255, 0, 0)),
                         ((pygameWindowWidth / 6) - 60, (pygameWindowDepth / 6) + 320))

    def checkMouseEventsAdd(self):
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                pos = pygame.mouse.get_pos()
                if addButton.collidepoint(pos):
                    return "add"
                if subButton.collidepoint(pos):
                    return "sub"
                if backButton.collidepoint(pos):
                    return "back"

