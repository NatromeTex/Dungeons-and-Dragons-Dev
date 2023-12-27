import pygame

class GameGUI():
    def __init__(self):
        self.running = True
        self.playing = False
        self.START_KEY, self.DOWN_KEY, self.UP_KEY, self.BACK_KEY = False, False, False,False
        self.DISPLAY_W, self.DISPLAY_H = 1280, 720
        self.display = pygame.Surface((self.DISPLAY_W,self.DISPLAY_H))
        self.window = pygame.display.set_mode(((self.DISPLAY_W,self.DISPLAY_H)))
        self.font_name = "Assets/BreathFire.ttf"
        self.BLACK, self.WHITE = (0,0,0),(255,255,255)

    def game_loop(self):
        while self.playing:
            self.checkEvent()
            if self.START_KEY:
                self.playing = False
            self.display.fill(self.BLACK)
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
    def resetKeys(self):
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False
            