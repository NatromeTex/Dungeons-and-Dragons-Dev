import pygame
import time

class Game():
    def __init__(self, gui):
        self.gui = gui
        self.mid_w, self.mid_h = self.gui.DISPLAY_W/2, self.gui.DISPLAY_H/2
        self.runDisp = True
        self.cursorRect = pygame.Rect(0, 0, 50, 50)
        self.offset = -200

    def drawCursor(self):
        self.gui.drawText('x', 50, self.cursorRect.x, self.cursorRect.y)

    def blitScreen(self):
        self.gui.window.blit(self.gui.display, (0, 0))
        pygame.display.update()
        self.gui.resetKeys()
    
    def showFps(self):
        fps = str(int(self.gui.clock.get_fps()))
        self.gui.drawText(fps, 20, 10, 10)

class gameIntro(Game):
    def __init__(self,gui):
        Game.__init__(self,gui)

    def dispGame(self):
        self.gui.display.fill(self.gui.BLACK)
        self.gui.fadeIn('In the beginning...', 60, self.mid_w, self.mid_h - 450, 200)
        self.gui.fadeIn('there was just a Conciousness.', 60, self.mid_w, self.mid_h - 350, 200)
        time.sleep(0.1)
        self.gui.fadeIn('The Conciousness dreamt a long dream...', 60, self.mid_w, self.mid_h - 250, 200)
        self.gui.fadeIn('an explosion of imagination and long strings of thougth...', 60, self.mid_w, self.mid_h - 150, 200)
        self.gui.fadeIn('like a dream, worthy of an epic.', 60, self.mid_w, self.mid_h - 50, 200)
        time.sleep(0.1)
        self.gui.fadeIn('It dreamt of creation, a single thought', 60, self.mid_w, self.mid_h + 50, 200)
        self.gui.fadeIn('exploding into a universe...', 60, self.mid_w, self.mid_h + 150, 200)
        self.gui.fadeIn('as the dream continued, all but seconds to the being', 60, self.mid_w, self.mid_h + 250, 200)
        self.gui.fadeIn('Creation took its course, in all of a billion planets which created life...', 60, self.mid_w, self.mid_h + 350, 200)
        self.gui.fadeIn('Near a simple yellow star... a quaint blue planet', 60, self.mid_w, self.mid_h + 450, 200)
        time.sleep(0.1)
        self.gui.fadeOut('In the beginning...', 60, self.mid_w, self.mid_h - 450, 200)
        self.gui.fadeOut('there was just a Conciousness.', 60, self.mid_w, self.mid_h - 350, 200)
        time.sleep(0.1)
        self.gui.fadeOut('The Conciousness dreamt a long dream...', 60, self.mid_w, self.mid_h - 250, 200)
        self.gui.fadeOut('an explosion of imagination and long strings of thougth...', 60, self.mid_w, self.mid_h - 150, 200)
        self.gui.fadeOut('like a dream, worthy of an epic.', 60, self.mid_w, self.mid_h - 50, 200)
        time.sleep(0.1)
        self.gui.fadeOut('It dreamt of creation, a single thought', 60, self.mid_w, self.mid_h + 50, 200)
        self.gui.fadeOut('exploding into a universe...', 60, self.mid_w, self.mid_h + 150, 200)
        self.gui.fadeOut('as the dream continued, all but seconds to the being', 60, self.mid_w, self.mid_h + 250, 200)
        self.gui.fadeOut('Creation took its course, in all of a billion planets which created life...', 60, self.mid_w, self.mid_h + 350, 200)
        self.gui.fadeOut('Near a simple yellow star... a quaint blue planet', 60, self.mid_w, self.mid_h + 450, 200)
        self.gui.display.fill(self.gui.BLACK)
        self.gui.fadeIn('A creature, started to question its existence...', 60, self.mid_w, self.mid_h - 50, 200)
        self.gui.fadeIn('Why here, why now?', 60, self.mid_w, self.mid_h + 50, 200)
        time.sleep(0.5)
        self.gui.fadeOut('A creature, started to question its existence...', 60, self.mid_w, self.mid_h - 50, 200)
        self.gui.fadeOut('Why here, why now?', 60, self.mid_w, self.mid_h + 50, 200)
        self.gui.display.fill(self.gui.BLACK)
        self.gui.fadeIn('Thanks For playing!', 60, self.mid_w, self.mid_h, 200)
        time.sleep(1)
        self.gui.playing = False