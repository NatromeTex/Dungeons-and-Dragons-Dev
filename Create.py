from Character import DnDCharacter
from Inventory import Inventory

def main():
    gender = input("Enter character gender: ")
    name = input("Enter character name: ")
    character_class = input("Enter character class: ")
    character_race = input("Enter character race: ")

    try:
        new_character = DnDCharacter(gender, name, character_class, character_race)
        new_character.display_stats()
        new_character.save_to_json()
    except ValueError as e:
        print(f"Error creating character: {e}")

if __name__ == "__main__":
    main()