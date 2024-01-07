import pygame

class Menu():
    def __init__(self, gui):
        self.gui = gui
        self.mid_w, self.mid_h = self.gui.DISPLAY_W/2, self.gui.DISPLAY_W/2
        self.runDisp = True
        self.cursorRect = pygame.Rect(0, 0, 50, 50)
        self.offset = -300

    def drawCursor(self):
        self.gui.drawText('x', 50, self.cursorRect.x, self.cursorRect.y)

    def blitScreen(self):
        self.gui.window.blit(self.gui.display, (0, 0))
        pygame.display.update()
        self.gui.resetKeys()

class MainMenu(Menu):
    def __init__(self, gui):
        Menu.__init__(self, gui)
        self.state = "Start"
        self.startx, self.starty = self.mid_w, self.mid_h - 500
        self.optionsx, self.optionsy = self.mid_w, self.mid_h - 400
        self.creditsx, self.creditsy = self.mid_w, self.mid_h - 300
        self.cursorRect.midtop = (self.startx + self. offset, self.starty)

    def dispMenu(self):
        self.runDisp = True
        print("we here")
        while self.runDisp:
            self.gui.checkEvent()
            self.checkIO()
            self.gui.display.fill(self.gui.BLACK)
            self.gui.drawText('Dungeons and Dragons-Dev', 75, self.gui.DISPLAY_W/2, self.gui.DISPLAY_H/5)
            self.gui.drawText('Start Game', 50, self.startx, self.starty)
            self.gui.drawText('Options', 50, self.optionsx, self.optionsy)
            self.gui.drawText('Credits', 50, self.creditsx, self.creditsy)
            self.drawCursor()
            self.blitScreen()

    def moveCursor(self):
        if self.gui.DOWN_KEY:
            if self.state == 'Start':
                self.cursorRect.midtop = (self.optionsx + self.offset, self.optionsy)
                self.state = 'Options'
            elif self.state == 'Options':    
                self.cursorRect.midtop = (self.creditsx + self.offset, self.creditsy)
                self.state = 'Credits'
            elif self.state == 'Credits':
                self.cursorRect.midtop = (self.startx + self.offset, self.starty)
                self.state = 'Start'
        if self.gui.UP_KEY:
            if self.state == 'Start':
                self.cursorRect.midtop = (self.creditsx + self.offset, self.creditsy)
                self.state = 'Credits'
            elif self.state == 'Options':    
                self.cursorRect.midtop = (self.startx + self.offset, self.starty)
                self.state = 'Start'
            elif self.state == 'Credits':
                self.cursorRect.midtop = (self.optionsx + self.offset, self.optionsy)
                self.state = 'Options'
    
    def checkIO(self):
        self.moveCursor()
        if self.state == "Start":
            self.gui.playing = True
        elif self.state == "Options":
            pass
        elif self.state == "Credits":
            pass
        self.run_display = False
        
