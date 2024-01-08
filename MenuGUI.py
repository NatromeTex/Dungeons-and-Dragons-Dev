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
        self.startx, self.starty = self.gui.DISPLAY_W/2, self.gui.DISPLAY_H/5 + 200
        self.optionsx, self.optionsy = self.gui.DISPLAY_W/2, self.gui.DISPLAY_H/5 + 300
        self.creditsx, self.creditsy = self.gui.DISPLAY_W/2, self.gui.DISPLAY_H/5 + 400
        self.exitx, self.exity = self.gui.DISPLAY_W/2, self.gui.DISPLAY_H/5 + 500
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
            self.gui.drawText('Exit', 50, self.exitx, self.exity)
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
                self.cursorRect.midtop = (self.exitx + self.offset, self.exity)
                self.state = 'Exit'
            elif self.state == 'Exit':
                self.cursorRect.midtop = (self.startx + self.offset, self.starty)
                self.state = 'Start'
        if self.gui.UP_KEY:
            if self.state == 'Start':
                self.cursorRect.midtop = (self.exitx + self.offset, self.exity)
                self.state = 'Exit'
            elif self.state == 'Options':    
                self.cursorRect.midtop = (self.startx + self.offset, self.starty)
                self.state = 'Start'
            elif self.state == 'Credits':
                self.cursorRect.midtop = (self.optionsx + self.offset, self.optionsy)
                self.state = 'Options'
            elif self.state == 'Exit':
                self.cursorRect.midtop = (self.creditsx + self.offset, self.creditsy)
                self.state = 'Credits'
    
    def checkIO(self):
        self.moveCursor()
        if self.gui.START_KEY:
            if self.state == "Start":
                self.gui.playing = True
            elif self.state == "Options":
                self.gui.currMenu = self.gui.options
            elif self.state == "Credits":
                self.gui.currMenu = self.gui.credits
            elif self.state == "Exit":
                self.gui.currMenu = self.gui.exit
            self.runDisp = False

class OptionsMenu(Menu):
    def __init__(self, gui):
        Menu.__init__(self,gui)
        self.state = "Volume"
        self.volx, self.voly = self.mid_w, self.mid_h - 400
        self.controlsx, self.controlsy = self.mid_w, self.mid_h - 300
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
                self.cursorRect.midtop = (self.controlsx + self.offset, self.controlsy)
            elif self.state == "Controls":
                self.state = "Volume"
                self.cursorRect.midtop = (self.volx + self.offset, self.voly)                 
        elif self.gui.START_KEY:
            pass

class CreditsMenu(Menu):
    def __init__(self, gui):
        Menu.__init__(self, gui)

    def dispMenu(self):
        self.runDisp = True
        while self.runDisp:
            self.gui.checkEvent()
            if self.gui.START_KEY or self.gui.BACK_KEY:
                self.gui.currMenu = self.gui.mainmenu
                self.runDisp = False
            self.gui.display.fill(self.gui.BLACK)
            self.gui.drawText('Credits', 70, self.gui.DISPLAY_W / 2, self.gui.DISPLAY_H / 4)
            self.gui.drawText('Coding By Natrome Tex', 50, self.gui.DISPLAY_W / 2, self.gui.DISPLAY_H / 2)
            self.blitScreen()

class ExitMenu(Menu):
    def __init__(self, gui):
        Menu.__init__(self,gui)
        self.state = "Yes"
        self.yesx, self.yesy = self.mid_w - 200, self.mid_h - 350
        self.nox, self.noy = self.mid_w + 200, self.mid_h - 350
        self.cursorRect.midtop = (self.yesx -100, self.yesy)
    
    def dispMenu(self):
        self.runDisp = True
        while self.runDisp:
            self.gui.checkEvent()
            self.checkIO()
            self.gui.display.fill(self.gui.BLACK)
            self.gui.drawText('Dungeons and Dragons-Dev', 75, self.gui.DISPLAY_W/2, self.gui.DISPLAY_H/5)
            self.gui.drawText('Do you really want to quit?', 55, self.mid_w, self.mid_h - 546)
            self.gui.drawText('Yes', 40, self.yesx, self.yesy)
            self.gui.drawText('No', 40, self.nox, self.noy)
            self.drawCursor()
            self.blitScreen()
            self.gui.resetKeys()

    def checkIO(self):
        if self.gui.BACK_KEY or self.state == 'No' and self.gui.START_KEY:
            self.gui.currMenu = self.gui.mainmenu
            self.runDisp = False
        elif self.gui.RIGHT_KEY or self.gui.LEFT_KEY:
            if self.state == "Yes":
                self.state = "No"
                self.cursorRect.midtop = (self.nox - 100, self.noy)
            elif self.state == "No":
                self.state = "Yes"
                self.cursorRect.midtop = (self.yesx - 100, self.yesy)                 
        elif self.state == 'Yes' and self.gui.START_KEY:
            self.gui.running, self.gui.playing = False, False
            self.runDisp = False