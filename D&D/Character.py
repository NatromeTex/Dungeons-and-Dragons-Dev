import json
import random
import os
import Inventory

class DnDCharacter:
    def __init__(self, gender, name, character_class, character_race):
        self.name = name
        self.gender = gender
        self.character_class = character_class
        self.character_race = character_race
        self.stats = self.load_stat_ranges()
        self.modifiers = self.load_stat_modifiers()
        self.level = 0
        
        if self.character_class in self.stats :
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
        with open('stat_ranges.json') as file:
            return json.load(file)
    
    def load_stat_modifiers(self):
        with open('stat_modifiers.json') as file:
            return json.load(file)

    def generate_random_stats(self):
        stat_ranges     = self.stats[self.character_class]
        stat_modifiers  = self.modifiers[self.character_race]

        self.strength       = random.randint(stat_ranges['strength']['min'], stat_ranges['strength']['max']) + stat_modifiers['strength']
        self.dexterity      = random.randint(stat_ranges['dexterity']['min'], stat_ranges['dexterity']['max']) + stat_modifiers['dexterity']
        self.constitution   = random.randint(stat_ranges['constitution']['min'], stat_ranges['constitution']['max']) + stat_modifiers['constitution']
        self.intelligence   = random.randint(stat_ranges['intelligence']['min'], stat_ranges['intelligence']['max']) + stat_modifiers['intelligence']
        self.wisdom         = random.randint(stat_ranges['wisdom']['min'], stat_ranges['wisdom']['max']) + stat_modifiers['wisdom']
        self.charisma       = random.randint(stat_ranges['charisma']['min'], stat_ranges['charisma']['max']) + stat_modifiers['charisma']
        self.level          = self.strength + self.dexterity + self.constitution + self.intelligence + self.wisdom + self.charisma

    def display_stats(self):
        print(f"Name        : {self.name}")
        print(f"Gender      : {self.gender}")
        print(f"Class       : {self.character_class}")
        print(f"Strength    : {self.strength}")
        print(f"Dexterity   : {self.dexterity}")
        print(f"Constitution: {self.constitution}")
        print(f"Intelligence: {self.intelligence}")
        print(f"Wisdom      : {self.wisdom}")
        print(f"Charisma    : {self.charisma}")

    def save_to_json(self):
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
        save_directory = 'Games/Characters/'
        filename = f"{self.name}_character.json"
        full_path = os.path.join(save_directory, filename)

        os.makedirs(save_directory, exist_ok=True)  # Create directory if it doesn't exist

        with open(full_path, "w") as file:
            json.dump(character_data, file, indent=4)
        print(f"Character stats saved to {full_path}")

    def init_loadout(self, character_class):
        character_class = self.character_class
        inventory = Inventory(character_class)
        inventory.initialize_inventory()
        inventory.save_to_characters_json()