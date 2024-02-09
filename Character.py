import json
import random
import os
import Inventory
import importlib
import Menu

game_path = Menu.get_selected_game_path()

class DnDCharacter:
    def __init__(self, gender, name, character_class, character_race):      # Receive Data from Create.py
        self.name = name
        self.gender = gender
        self.character_class = character_class
        self.character_race = character_race
        self.stats = self.load_stat_ranges()
        self.modifiers = self.load_stat_modifiers()
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

    def display_stats(self):                                                # Displaying all created stats once
        print(f"Name        : {self.name}")
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
            "Name"          : self.name,
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

    def init_loadout(self, character_class):                                 # Add the default loadouts for each characters per class              
        character_class = self.character_class
        inventory = Inventory(character_class)
        inventory.initialize_inventory()
        inventory.save_to_characters_json()