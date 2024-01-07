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
        self.startx, self.starty = self.gui.DISPLAY_W/2, self.gui.DISPLAY_H/5 + 150
        self.optionsx, self.optionsy = self.gui.DISPLAY_W/2, self.gui.DISPLAY_H/5 + 250
        self.creditsx, self.creditsy = self.gui.DISPLAY_W/2, self.gui.DISPLAY_H/5 + 350
        self.cursorRect.midtop = (self.startx + self. offset, self.starty)

    def dispMenu(self):
        self.runDisp = True
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
            self.gui.currMenu = self.gui.options
        elif self.state == "Credits":
            self.gui.currMenu = self.gui.credits
        self.runDisp = False

class OptionsMenu(Menu):
    def __init__(self, gui):
        Menu.__init__(self,gui)
        self.state = "Volume"
        self.volx, self.voly = self.mid_w, self.mid_h - 200
        self.controlsx, self.controlsy = self.mid_w, self.mid_h - 100
        self.cursorRect.midtop = (self.volx + self.offset, self.voly)

    def dispMenu(self):
        self.runDisp = True
        while self.runDisp:
            self.gui.checkEvent()
            self.checkIO()
            self.gui.display.fill(self.gui.BLACK)
            self.gui.drawText("Options", 70, self.gui.DISPLAY_W / 2, self.gui.DISPLAY_H / 4)
            self.gui.drawText("Volume", 50, self.volx, self.voly)
            self.gui.drawText("Controls", 50, self.controlsx, self.controlsy)
            self.drawCursor()
            self.blitScreen()
    
    def checkIO(self):
        if self.gui.BACK_KEY:
            self.gui.currMenu = self.gui.mainmenu
            self.runDisp = False
        elif self.gui.UP_KEY or self.gui.DOWN_KEY:
            if self.state == "Volume":
                self.state = "Controls"
                self.cursorRect.midtop = (self.controlsx - self.offset, self.controlsy)
            elif self.state == "Controls":
                self.state = "Volume"
                self.cursorRect.midtop = (self.volx - self.offset, self.voly)                 
        elif self.gui.START_KEY:
            pass

class CreditsMenu(Menu):
    def __init__(self, gui):
        Menu.__init__(self,gui)

    def dispMenu(self):
        self.runDisp = True
        while self.runDisp:
            self.gui.checkEvent()
            if self.gui.START_KEY or self.gui.BACK_KEY:
                self.gui.currMenu = self.gui.mainmenu
                self.runDisp = False
            self.gui.display.fill(self.gui.BLACK)
            self.gui.drawText("Credits", 70, self.gui.DISPLAY_W/2, self.gui.DISPLAY_H/4)
            self.gui.drawText("All coding by Natrome Tex", 60, self.gui.DISPLAY_W/2, self.gui.DISPLAY_H/2)
            self.blitScreen()
