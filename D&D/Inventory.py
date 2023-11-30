import json

class Inventory:
    def __init__(self, character_class):
        self.character_class = character_class
        self.loadouts = self.load_loadouts()
        self.inventory = {}

    def load_loadouts(self):
        with open('loadouts.json') as file:
            loadouts_data = json.load(file)
            return loadouts_data.get(self.character_class, [])

    def initialize_inventory(self):
        for loadout in self.loadouts:
            for category in loadout:
                if category not in self.inventory:
                    self.inventory[category] = []
                self.inventory[category].extend(loadout[category])

    def save_to_characters_json(self):
        try:
            save_directory = 'Games/Characters/'
            filename = f"{self.name}_character.json"
            full_path = os.path.join(save_directory, filename)
            with open(full_path , 'r+') as file:
                characters_data = json.load(file)
                if self.character_class in characters_data:
                    characters_data[self.character_class]['INVENTORY'] = self.inventory
                    file.seek(0)
                    json.dump(characters_data, file, indent=4)
                    print(f"Inventory for {self.character_class} saved to characters.json")
                else:
                    print(f"{self.character_class} not found in characters.json")
        except FileNotFoundError:
            print("characters.json file not found.")
