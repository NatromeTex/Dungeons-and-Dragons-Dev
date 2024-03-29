from pygame import *
import string
import configparser
from MenuGUI import *
from play1 import *

import random
import os
import json

class GameGUI():
    def __init__(self):
        pygame.init()
        self.running    = True
        self.playing    = False
        self.START_KEY, self.DOWN_KEY, self.UP_KEY, self.BACK_KEY, self.LEFT_KEY, self.RIGHT_KEY, self.BACKSPC, self.ANY_KEY = False, False, False, False, False, False, False, False
        self.LEX_KEY    = ''
        self.DISPLAY_W, self.DISPLAY_H = 1920, 1080
        self.display    = pygame.Surface((self.DISPLAY_W,self.DISPLAY_H))
        self.window     = pygame.display.set_mode(((self.DISPLAY_W,self.DISPLAY_H)))
        self.font_name  = "BreatheFire.ttf"
        self.assets     = os.path.join(self.getGamePath(),'Assets')
        self.butsfx     = pygame.mixer.Sound(os.path.join(self.assets,'BNA_UI19.wav'))
        self.menuch     = pygame.mixer.Sound(os.path.join(self.assets,'BNA_UI49.wav'))
        self.clock      = pygame.time.Clock()
        self.BLACK, self.WHITE = (0,0,0),(220,220,220)
        self.intro      = Intro(self)
        self.mainmenu   = MainMenu(self)
        self.start      = StartGame(self)
        self.options    = OptionsMenu(self)
        self.credits    = CreditsMenu(self)
        self.exit       = ExitMenu(self)
        self.create     = CreateChar(self)
        self.currMenu   = Intro(self)
        self.gintro     = gameIntro(self)
        self.currGMenu  = gameIntro(self)
        
    def checkEvent(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running, self.playing = False, False
                self.currMenu.runDisp = False
            if event.type == pygame.KEYDOWN:
                self.ANY_KEY = True
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
                if event.key == pygame.K_BACKSPACE:
                    self.BACKSPC = True
                if event.unicode.isalpha() or event.unicode.isdigit():
                    self.LEX_KEY = chr(event.key)                
    
    def drawText(self, text, size, x, y):
        font = pygame.font.Font(self.font_name, size)
        textSurface = font.render(text, True, self.WHITE)
        textRect = textSurface.get_rect()
        textRect.center = (x,y)
        self.display.blit(textSurface,textRect)
    
    def drawTextTab(self, text, size, x, y):
        font = pygame.font.Font(self.font_name, size)
        textSurface = font.render(text, True, self.WHITE)
        textRect = textSurface.get_rect()
        textRect.midleft = (x,y)
        self.display.blit(textSurface,textRect)
    
    def drawTextCol(self, text, size, x, y, color):
        font = pygame.font.Font(self.font_name, size)
        textSurface = font.render(text, True, color)
        textRect = textSurface.get_rect()
        textRect.center = (x,y)
        self.display.blit(textSurface,textRect)
    
    def fadeIn(self, text, size, x, y, color):
        for i in range(color):
            self.drawTextCol(text, size, x, y, (0,0,0))
            self.drawTextCol(text, size, x, y, (i,i,i))
            self.window.blit(self.display,(0,0))
            pygame.display.update()            
        self.clock.tick(144)
    
    def fadeOut(self, text, size, x, y, color):
        for i in range(color,0,-1):
            self.drawTextCol(text, size, x, y, (0,0,0))
            self.drawTextCol(text, size, x, y, (i,i,i))
            self.window.blit(self.display,(0,0))
            pygame.display.update()            
        self.clock.tick(144)
            
    
    def drawRect(self, color, x1, y1, x2, y2):
        pygame.draw.rect(self.window, color, pygame.Rect(x1, y1, x2, y2))

    def resetKeys(self):
        self.START_KEY, self.DOWN_KEY, self.UP_KEY, self.BACK_KEY, self.LEFT_KEY, self.RIGHT_KEY, self.BACKSPC, self.ANY_KEY = False, False, False, False, False, False, False, False
        self.LEX_KEY = ''

    def setGamePath(self, path):
        config = configparser.ConfigParser()
        config['GAME'] = {'selected_game_path': path}
        with open('config.ini', 'w') as configfile:
            config.write(configfile)
    
    def getGamePath(self):
        config = configparser.ConfigParser()
        config.read('config.ini')
        return config['GAME'].get('selected_game_path', '')
    
    def getGameName(self, name):
        if name == 'Games\\Default Game':
            return 'Default Game'
    
    def getCharName(self,dic,ind):
        files = [file for file in os.listdir(dic) if file.endswith(".json")]
        names = ['                  <Create Character>']
        for file in files:
            name = file.split(".")[0]
            names.append(name)
        if ind == 0:
            return names[0]
        else:    
            ind = ind % len(names)
            return names[ind]

    def getRace(self, ind):
        wd = f"Character\stat_modifiers.json"
        gamePath = self.getGamePath()
        cgwd = os.path.join(gamePath, wd)         # Loading the current game working directory
        with open(cgwd) as file:
            self.race = json.load(file)
        races = list(self.race.keys())
        if ind == 0:
            return races[0]
        else:
            ind = ind%len(races)
            return races[ind]

    def getClass(self, ind):
        wd = f"Character\stat_ranges.json"
        gamePath = self.getGamePath()
        cgwd = os.path.join(gamePath, wd)         # Loading the current game working directory
        with open(cgwd) as file:
            self.Class = json.load(file)
        classes = list(self.Class.keys())
        if ind == 0:
            return classes[0]
        else:
            ind = ind%len(classes)
            return classes[ind]        

    def getStatRanges(self):
        wd = f"Character\stat_ranges.json"
        gamePath = self.getGamePath()
        cgwd = os.path.join(gamePath, wd)         # Loading the current game working directory
        with open(cgwd) as file:
            return json.load(file)
    
    def getStatModifiers(self):
        wd = f"Character\stat_modifiers.json"
        gamePath = self.getGamePath()
        cgwd = os.path.join(gamePath, wd )      # Loading the current game working directory
        with open(cgwd) as file:
            return json.load(file)
    
    def getCharStats(self, name):
        cf = f"Current Games\Characters\{name}.json"
        with open(cf) as file:
            return json.load(file)


    def genStats(self, gender, name, Class, race):                                        # Creating Random Stats from Ranges specified in game and adding the modifiers for all classes and races
        self.ranges    = self.getStatRanges()
        self.modifiers = self.getStatModifiers()
        self.gender    = gender
        self.name      = name
        statRanges     = self.ranges[Class]
        statModifiers  = self.modifiers[race]

        self.strength       = random.randint(statRanges['strength']['min'], statRanges['strength']['max']) + statModifiers['strength']
        self.dexterity      = random.randint(statRanges['dexterity']['min'], statRanges['dexterity']['max']) + statModifiers['dexterity']
        self.constitution   = random.randint(statRanges['constitution']['min'], statRanges['constitution']['max']) + statModifiers['constitution']
        self.intelligence   = random.randint(statRanges['intelligence']['min'], statRanges['intelligence']['max']) + statModifiers['intelligence']
        self.wisdom         = random.randint(statRanges['wisdom']['min'], statRanges['wisdom']['max']) + statModifiers['wisdom']
        self.charisma       = random.randint(statRanges['charisma']['min'], statRanges['charisma']['max']) + statModifiers['charisma']
        self.level          = (self.strength + self.dexterity + self.constitution + self.intelligence + self.wisdom + self.charisma) // 6

        character_data = {
            "Name"          : self.name,
            "Gender"        : self.gender,
            "Class"         : Class,
            "Race"          : race,
            "Strength"      : self.strength,
            "Dexterity"     : self.dexterity,
            "Constitution"  : self.constitution,
            "Intelligence"  : self.intelligence,
            "Wisdom"        : self.wisdom,
            "Charisma"      : self.charisma,
            "Level"         : self.level
        }
        save_directory = 'Current Games/Characters/'
        filename = f"{self.name}.json"
        full_path = os.path.join(save_directory, filename)

        os.makedirs(save_directory, exist_ok=True)                           # Create directory if it doesn't exist

        with open(full_path, "w") as file:
            json.dump(character_data, file, indent=4)
        print(f"Character stats saved to {full_path}")

    def displayStats(self):                                                # Displaying all created stats on
        print(f"Name        : {self.name}")
        print(f"Gender      : {self.gender}")
        print(f"Class       : {self.character_class}")
        print(f"Strength    : {self.strength}")
        print(f"Dexterity   : {self.dexterity}")
        print(f"Constitution: {self.constitution}")
        print(f"Intelligence: {self.intelligence}")
        print(f"Wisdom      : {self.wisdom}")
        print(f"Charisma    : {self.charisma}")        
            