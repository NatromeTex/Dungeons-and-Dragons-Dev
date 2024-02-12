import pygame
import configparser
import time
from MenuGUI import *
import os
import json

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
        self.clock = pygame.time.Clock()
        self.BLACK, self.WHITE = (0,0,0),(255,255,255)
        self.intro = Intro(self)
        self.mainmenu = MainMenu(self)
        self.start = StartGame(self)
        self.options = OptionsMenu(self)
        self.credits = CreditsMenu(self)
        self.exit = ExitMenu(self)
        self.create = CreateChar(self)
        self.currMenu = Intro(self)

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
    
    def drawTextCol(self, text, size, x, y, color):
        font = pygame.font.Font(self.font_name, size)
        textSurface = font.render(text, True, color)
        textRect = textSurface.get_rect()
        textRect.center = (x,y)
        self.display.blit(textSurface,textRect)
    
    def drawRect(self, color, x1, y1, x2, y2):
        pygame.draw.rect(self.window, color, pygame.Rect(x1, y1, x2, y2))

    def resetKeys(self):
        self.START_KEY, self.DOWN_KEY, self.UP_KEY, self.BACK_KEY, self.LEFT_KEY, self.RIGHT_KEY = False, False, False, False, False, False

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
        wd = f"Character/stat_modifiers.json"
        game_path = self.getGamePath()
        cgwd = os.path.join(game_path, wd)         # Loading the current game working directory
        with open(cgwd) as file:
            self.race = json.load(file)
        races = list(self.race.keys())
        if ind == 0:
            return races[0]
        else:
            ind = ind%len(races)
            return races[ind]
    def getClass(self, ind):
        wd = f"Character/stat_ranges.json"
        game_path = self.getGamePath()
        cgwd = os.path.join(game_path, wd)         # Loading the current game working directory
        with open(cgwd) as file:
            self.Class = json.load(file)
        classes = list(self.Class.keys())
        if ind == 0:
            return classes[0]
        else:
            ind = ind%len(classes)
            return classes[ind]

class DnDCharacter:
    def __init__(self, gender, character_class, character_race):      # Receive Data from Create.py
        self.gender = gender
        self.character_class = character_class
        self.character_race = character_race
        self.stats = self.load_stat_ranges()
        self.modifiers = self.load_stat_modifiers()
        self.gamePath = GameGUI.getGamePath()
        self.level = 0
        
        if self.character_class in self.stats :                             # Any mismatch with game files will be raised as error here
            if self.character_race in self.modifiers:
                if self.gender == 'Male' or self.gender == 'Female' :
                    self.generate_random_stats()
                else:
                    raise ValueError(f"Invalid Gender: {self.gender}")
            else:
                raise ValueError(f"Invalid Character Race: {self.character_race}")
        else:
                raise ValueError(f"Invalid Character Class: {self.character_class}")        

    def load_stat_ranges(self):
        wd = f"Character/stat_ranges.json"
        cgwd = os.path.join(game_path, wd)         # Loading the current game working directory
        with open(cgwd) as file:
            return json.load(file)
    
    def load_stat_modifiers(self):
        wd = f"Character/stat_modifiers.json"
        cgwd = os.path.join(game_path, wd )      # Loading the current game working directory
        with open(cgwd) as file:
            return json.load(file)

    def generate_random_stats(self):                                        # Creating Random Stats from Ranges specified in game and adding the modifiers for all classes and races
        stat_ranges     = self.stats[self.character_class]
        stat_modifiers  = self.modifiers[self.character_race]

        self.strength       = random.randint(stat_ranges['strength']['min'], stat_ranges['strength']['max']) + stat_modifiers['strength']
        self.dexterity      = random.randint(stat_ranges['dexterity']['min'], stat_ranges['dexterity']['max']) + stat_modifiers['dexterity']
        self.constitution   = random.randint(stat_ranges['constitution']['min'], stat_ranges['constitution']['max']) + stat_modifiers['constitution']
        self.intelligence   = random.randint(stat_ranges['intelligence']['min'], stat_ranges['intelligence']['max']) + stat_modifiers['intelligence']
        self.wisdom         = random.randint(stat_ranges['wisdom']['min'], stat_ranges['wisdom']['max']) + stat_modifiers['wisdom']
        self.charisma       = random.randint(stat_ranges['charisma']['min'], stat_ranges['charisma']['max']) + stat_modifiers['charisma']
        self.level          = (self.strength + self.dexterity + self.constitution + self.intelligence + self.wisdom + self.charisma) // 6

    def display_stats(self):                                                # Displaying all created stats on
        print(f"Gender      : {self.gender}")
        print(f"Class       : {self.character_class}")
        print(f"Strength    : {self.strength}")
        print(f"Dexterity   : {self.dexterity}")
        print(f"Constitution: {self.constitution}")
        print(f"Intelligence: {self.intelligence}")
        print(f"Wisdom      : {self.wisdom}")
        print(f"Charisma    : {self.charisma}")

    def save_to_json(self):                                                 # Saving all the data to a file for retreival
        character_data = {
            "Gender"        : self.gender,
            "Class"         : self.character_class,
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
            