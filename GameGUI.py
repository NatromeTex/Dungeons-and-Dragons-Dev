import pygame
from MenuGUI import *

class GameGUI():
    def __init__(self):
        pygame.init()
        self.running = True
        self.playing = False
        self.START_KEY, self.DOWN_KEY, self.UP_KEY, self.BACK_KEY, self.LEFT_KEY, self.RIGHT_KEY = False, False, False, False, False, False
        self.DISPLAY_W, self.DISPLAY_H = 1920, 1080
        self.display = pygame.Surface((self.DISPLAY_W,self.DISPLAY_H))
        self.window = pygame.display.set_mode(((self.DISPLAY_W,self.DISPLAY_H)))
        self.font_name = "BreatheFire.ttf"
        self.BLACK, self.WHITE = (0,0,0),(255,255,255)
        self.mainmenu = MainMenu(self)
        self.options = OptionsMenu(self)
        self.credits = CreditsMenu(self)
        self.exit = ExitMenu(self)
        self.currMenu = MainMenu(self)

    def checkEvent(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running, self.playing = False, False
                self.currMenu.runDisp = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.START_KEY = True
                if event.key == pygame.K_ESCAPE:
                    self.BACK_KEY = True
                if event.key == pygame.K_UP:
                    self.UP_KEY = True
                if event.key == pygame.K_DOWN:
                    self.DOWN_KEY = True
                if event.key == pygame.K_LEFT:
                    self.LEFT_KEY = True
                if event.key == pygame.K_RIGHT:
                    self.RIGHT_KEY = True
    
    def drawText(self, text, size, x, y):
        font = pygame.font.Font(self.font_name, size)
        textSurface = font.render(text, True, self.WHITE)
        textRect = textSurface.get_rect()
        textRect.center = (x,y)
        self.display.blit(textSurface,textRect)
    
    def drawRect(self, color, x1, y1, x2, y2):
        pygame.draw.rect(self.window, color, pygame.Rect(x1, y1, x2, y2))

    def resetKeys(self):
        self.START_KEY, self.DOWN_KEY, self.UP_KEY, self.BACK_KEY, self.LEFT_KEY, self.RIGHT_KEY = False, False, False, False, False, False
            