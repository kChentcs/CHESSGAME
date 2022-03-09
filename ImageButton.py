import pygame
from textButton import textButton

class ImageButton(textButton):
    def __init__(self, onClick, s, image, x, y, w, h, bc=(255, 255, 255)):
        textButton.__init__(self, onClick, s, "", x, y, w, h, pygame.font.Font(None, 0), (0, 0, 0 ), bc)
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, (self.width, self.height))

    def update(self):
        textButton.update(self)
        self.screen.blit(self.image, (self.x, self.y))

    def handleEvent(self, event):
        textButton.handleEvent(self, event)


    def changeImage(self, newFile):
        self.image = pygame.image.load(newFile)
        self.image = pygame.transform.scale(self.image, (self.width, self.height))