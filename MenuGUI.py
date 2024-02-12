import pygame
import time

class Menu():
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

class Intro(Menu):
    def __init__(self,gui):
        Menu.__init__(self,gui)

    def dispMenu(self):
        color = (0,0,0)
        i = 0
        while i <= 160:
            self.gui.display.fill(self.gui.BLACK)
            self.gui.drawTextCol('Pure Black Studios', 75, self.mid_w, self.mid_h, color)
            self.blitScreen()
            self.showFps()
            self.blitScreen()
            self.gui.clock.tick(144)
            i += 1
            color = (i,i,i)
            time.sleep(0.02)
        while i >= 0:
            self.gui.display.fill(self.gui.BLACK)
            self.gui.drawTextCol('Pure Black Studios', 75, self.mid_w, self.mid_h, color)
            self.blitScreen()
            self.showFps()
            self.blitScreen()
            self.gui.clock.tick(144)
            i -= 1
            color = (i,i,i)
            time.sleep(0.001)
        self.gui.currMenu = self.gui.mainmenu    
            
class MainMenu(Menu):
    def __init__(self, gui):
        Menu.__init__(self, gui)
        self.state = "Start"
        self.startx, self.starty = self.mid_w, self.mid_h/5 + 300
        self.optionsx, self.optionsy = self.mid_w, self.mid_h/5 + 400
        self.creditsx, self.creditsy = self.mid_w, self.mid_h/5 + 500
        self.exitx, self.exity = self.mid_w, self.mid_h/5 + 600
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
            self.showFps()
            self.blitScreen()
            self.gui.clock.tick(144)

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
        elif self.gui.UP_KEY:
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
        elif self.gui.BACK_KEY:
            self.gui.currMenu = self.gui.exit
            self.runDisp = False     
    
    def checkIO(self):
        self.moveCursor()
        if self.gui.START_KEY:
            if self.state == "Start":
                self.gui.currMenu = self.gui.start
            elif self.state == "Options":
                self.gui.currMenu = self.gui.options
            elif self.state == "Credits":
                self.gui.currMenu = self.gui.credits
            elif self.state == "Exit":
                self.gui.currMenu = self.gui.exit
            self.runDisp = False

class StartGame(Menu):
    def __init__(self, gui):
        Menu.__init__(self, gui)
        self.state = "SelGame"
        self.selGamex, self.selGamey = self.mid_w - 300, self.mid_h/4 + 300
        self.selCharx, self.selChary = self.mid_w - 250, self.mid_h/4 + 450
        self.cursorRect.midtop = (self.selGamex + self.offset, self.selGamey)
        self.gamePath = self.gui.getGamePath()
        self.gameName = self.gui.getGameName(self.gamePath)
        self.index = 0
        self.charName = self.gui.getCharName("Current Games\\Characters", self.index)
        
    
    def dispMenu(self):
        self.runDisp = True
        while self.runDisp:
            self.gui.checkEvent()
            self.checkIO()
            self.gui.display.fill(self.gui.BLACK)
            self.gui.drawText('Start Game', 60, self.gui.DISPLAY_W/2, self.gui.DISPLAY_H/4)
            self.gui.drawText('Selected Game:', 50, self.selGamex, self.selGamey)
            self.gui.drawText(self.gameName, 50, self.selGamex + 400, self.selGamey)
            self.gui.drawText('Selected Character:', 50, self.selCharx, self.selChary)
            self.gui.drawText(self.charName, 50, self.selCharx + 350, self.selChary)
            self.drawCursor()
            self.showFps()
            self.blitScreen()
            self.gui.clock.tick(144)

    def checkIO(self):
        if self.gui.BACK_KEY:
            self.gui.currMenu = self.gui.mainmenu
            self.runDisp = False
        elif self.gui.UP_KEY or self.gui.DOWN_KEY:
            if self.state == "SelGame":
                self.state = "SelChar"
                self.cursorRect.midtop = (self.selCharx + self.offset - 50, self.selChary)
            elif self.state == "SelChar":
                self.state = "SelGame"
                self.cursorRect.midtop = (self.selGamex + self.offset, self.selGamey) 
        elif self.gui.LEFT_KEY:
            if self.state == 'SelGame':
                pass
            elif self.state == 'SelChar':
                self.index -= 1
                self.charName = self.gui.getCharName("Current Games\\Characters", self.index)
                print(self.charName)
        elif self.gui.RIGHT_KEY:
            if self.state == 'SelGame':
                pass
            elif self.state == 'SelChar':
                self.index += 1
                self.charName = self.gui.getCharName("Current Games\\Characters", self.index)
                print(self.charName)              
        elif self.gui.START_KEY:
            if self.state == 'SelChar' and self.charName == '                  <Create Character>':
                self.gui.currMenu = self.gui.create
                self.runDisp = False


class OptionsMenu(Menu):
    def __init__(self, gui):
        Menu.__init__(self,gui)
        self.state = "Graphics"
        self.graphx, self.graphy = self.mid_w, self.mid_h - 100
        self.controlsx, self.controlsy = self.mid_w, self.mid_h 
        self.volx, self.voly = self.mid_w, self.mid_h + 100
        self.cursorRect.midtop = (self.graphx + self.offset, self.graphy)

    def dispMenu(self):
        self.runDisp = True
        while self.runDisp:
            self.gui.checkEvent()
            self.checkIO()
            self.gui.display.fill(self.gui.BLACK)
            self.gui.drawText("Options", 70, self.gui.DISPLAY_W / 2, self.gui.DISPLAY_H / 4)
            self.gui.drawText("Graphics", 50, self.graphx, self.graphy)
            self.gui.drawText("Sounds", 50, self.volx, self.voly)
            self.gui.drawText("Controls", 50, self.controlsx, self.controlsy)
            self.drawCursor()
            self.showFps()
            self.blitScreen()
            self.gui.clock.tick(144)
    
    def checkIO(self):
        if self.gui.BACK_KEY:
            self.gui.currMenu = self.gui.mainmenu
            self.runDisp = False
        elif self.gui.UP_KEY:
            if self.state == "Graphics":
                self.state = "Sounds"
                self.cursorRect.midtop = (self.volx + self.offset, self.voly)
            elif self.state == "Sounds":
                self.state = "Controls"
                self.cursorRect.midtop = (self.controlsx + self.offset, self.controlsy)
            elif self.state == "Controls":
                self.state = "Graphics"
                self.cursorRect.midtop = (self.graphx + self.offset, self.graphy)                 
        elif self.gui.DOWN_KEY:
            if self.state == "Graphics":
                self.state = "Controls"
                self.cursorRect.midtop = (self.controlsx + self.offset, self.controlsy)
            elif self.state == "Sounds":
                self.state = "Graphics"
                self.cursorRect.midtop = (self.graphx + self.offset, self.graphy)
            elif self.state == "Controls":
                self.state = "Sounds"
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
            self.gui.drawText('Credits', 70, self.mid_w, self.mid_h/2)
            self.gui.drawText('Coding By Natrome Tex', 50, self.mid_w, self.mid_h)
            self.showFps()
            self.blitScreen()
            self.gui.clock.tick(144)

class ExitMenu(Menu):
    def __init__(self, gui):
        Menu.__init__(self,gui)
        self.state = "Yes"
        self.yesx, self.yesy = self.mid_w - 150, self.mid_h + 50
        self.nox, self.noy = self.mid_w + 150, self.mid_h + 50
        self.cursorRect.midtop = (self.yesx -100, self.yesy)
    
    def dispMenu(self):
        self.runDisp = True
        while self.runDisp:
            self.gui.checkEvent()
            self.checkIO()
            self.showFps()
            self.gui.display.fill(self.gui.BLACK)
            self.gui.drawText('Dungeons and Dragons-Dev', 75, self.gui.DISPLAY_W/2, self.gui.DISPLAY_H/5)
            self.gui.drawText('Do you really want to quit?', 55, self.mid_w, self.mid_h - 150)
            self.gui.drawText('Yes', 40, self.yesx, self.yesy)
            self.gui.drawText('No', 40, self.nox, self.noy)
            self.drawCursor()
            self.showFps()
            self.blitScreen()
            self.gui.resetKeys()
            self.gui.clock.tick(144)
            

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

class CreateChar(Menu):
    def __init__(self, gui):
        Menu.__init__(self,gui)
        self.state = "Gender"
        self.genderx, self.gendery = self.mid_w - 500, self.mid_h - 250
        self.classx, self.classy = self.mid_w - 500, self.mid_h - 150
        self.racex, self. racey = self.mid_w - 500, self.mid_h - 50
        self.createx, self.createy = self.mid_w, self.mid_h + 200
        self.raceIndex = 0
        self.classIndex = 0
        self.gender = 'Male'
        self.clas = self.gui.getClass(self.classIndex)
        self.race = self.gui.getRace(self.raceIndex)
        self.cursorRect.midtop = (self.genderx - 100, self.gendery)

    def dispMenu(self):
        self.gui.checkEvent()
        self.checkIO()
        self.showFps()
        self.gui.display.fill(self.gui.BLACK)
        self.gui.drawText('Character Creation', 50, self.mid_w, self.mid_h - 350)
        self.gui.drawText('Gender: ', 50, self.genderx, self.gendery)
        self.gui.drawText(self.gender, 50, self.genderx + 200, self.gendery)
        self.gui.drawText('Class: ', 50, self.classx, self.classy)
        self.gui.drawText(self.clas, 50, self.classx + 200, self.classy)
        self.gui.drawText('Race: ', 50, self.racex, self.racey)
        self.gui.drawText(self.race, 50, self.racex + 200, self.racey)
        self.gui.drawText('Create Character', 50, self.createx, self.createy)
        self.drawCursor()
        self.showFps()
        self.blitScreen()
        self.gui.resetKeys()
        self.gui.clock.tick(144)

    def checkIO(self):
        if self.gui.BACK_KEY:
            self.gui.currMenu = self.gui.mainmenu
            self.runDisp = False
        elif self.gui.UP_KEY:
            if self.state == 'Gender':
                self.state = 'Create'
                self.cursorRect.midtop = (self.createx - 200, self.createy)
            elif self.state == 'Class':
                self.state = 'Gender'
                self.cursorRect.midtop = (self.genderx - 100, self.gendery)
            elif self.state == 'Race':
                self.state = 'Class'
                self.cursorRect.midtop = (self.classx - 100, self.classy)
            elif self.state == 'Create':
                self.state = 'Race'
                self.cursorRect.midtop = (self.racex - 100, self.racey)
        elif self.gui.DOWN_KEY:
            if self.state == 'Gender':
                self.state = 'Class'
                self.cursorRect.midtop = (self.classx - 100, self.classy)
            elif self.state == 'Class':
                self.state = 'Race'
                self.cursorRect.midtop = (self.racex - 100, self.racey)
            elif self.state == 'Race':
                self.state = 'Create'
                self.cursorRect.midtop = (self.createx - 200, self.createy)
            elif self.state == 'Create':
                self.state = 'Gender'
                self.cursorRect.midtop = (self.genderx - 100, self.gendery) 
        elif self.gui.RIGHT_KEY:
            if self.state == 'Gender':
                if self.gender == 'Male':
                    self.gender = 'Female'
                else:
                    self.gender = 'Male'
            elif self.state == 'Race':
                self.raceIndex += 1
                self.race = self.gui.getRace(self.raceIndex)
            elif self.state == 'Class':
                self.classIndex += 1
                self.clas = self.gui.getClass(self.classIndex)
        elif self.gui.LEFT_KEY:
            if self.state == 'Gender':
                if self.gender == 'Male':
                    self.gender = 'Female'
                else:
                    self.gender = 'Male'
            elif self.state == 'Race':
                self.raceIndex -= 1
                self.race = self.gui.getRace(self.raceIndex)
            elif self.state == 'Class':
                self.classIndex -= 1
                self.clas = self.gui.getClass(self.classIndex)
        elif self.gui.START_KEY:
            if self.state == 'Create':
                self.gui.genStats(self.gender, self.clas, self.race)