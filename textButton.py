import pygame


class textButton:
    def __init__(self, onClick, s, label, x, y, w, h, font, tc = (0,0,0), bc = (255,255,255)):
        #if not pygame.get_init(): pygame.init()
        self.onClick = onClick
        self.screen = s
        self.label = label
        self.x = x
        self.y = y
        self.width = w
        self. height = h
        self.textColor = tc
        self.backgroundColor = bc
        self.buttonText = font.render(self.label, True, self.textColor)
        self.buttonTextRect = self.buttonText.get_rect()

    def update(self):
        pygame.draw.rect(self.screen, self.backgroundColor, [self.x, self.y, self.width, self.height])
        self.buttonTextRect.center = (self.x + self.width / 2, self.y + self.height / 2)
        self.screen.blit(self.buttonText, self.buttonTextRect)

    def handleEvent(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouseX, mouseY = event.pos
            object = pygame.Rect((self.x, self.y), (self.width, self.height))
            if object.collidepoint(mouseX, mouseY):
                self.onClick()
