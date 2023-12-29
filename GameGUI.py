import pygame

class GameGUI():
    def __init__(self):
        pygame.init()
        self.running = True
        self.playing = False
        self.START_KEY, self.DOWN_KEY, self.UP_KEY, self.BACK_KEY = False, False, False,False
        self.DISPLAY_W, self.DISPLAY_H = 1280, 720
        self.display = pygame.Surface((self.DISPLAY_W,self.DISPLAY_H))
        self.window = pygame.display.set_mode(((self.DISPLAY_W,self.DISPLAY_H)))
        self.font_name = "BreatheFire.ttf"
        self.BLACK, self.WHITE = (0,0,0),(255,255,255)

    def game_loop(self):
        while self.playing:
            self.checkEvent()
            if self.START_KEY:
                self.playing = False
            self.display.fill(self.BLACK)
            self.drawText('Thanks for playing',80,self.DISPLAY_W/2,self.DISPLAY_H/2)
            self.window.blit(self.display, (0,0))
            pygame.display.update()
            self.resetKeys

    def checkEvent(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running, self.playing = False, False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.START_KEY = True
                if event.key == pygame.K_ESCAPE:
                    self.BACK_KEY = True
                if event.key == pygame.K_UP:
                    self.UP_KEY = True
                if event.key == pygame.K_DOWN:
                    self.DOWN_KEY = True
    
    def drawText(self, text, size, x, y):
        font = pygame.font.Font(self.font_name, size)
        textSurface = font.render(text, True, self.WHITE)
        textRect = textSurface.get_rect()
        textRect.center = (x,y)
        self.display.blit(textSurface,textRect)

    def resetKeys(self):
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False
            