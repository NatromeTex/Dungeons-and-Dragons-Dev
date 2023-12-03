import os
import json
import Create
import configparser
selected_game_path = ""

def set_selected_game_path(path):                           # Took me around 3 hours to figure out this routine because python caching causes the null value in selected_game_path to be passed not the actual path
    config = configparser.ConfigParser()
    config['GAME'] = {'selected_game_path': path}
    with open('config.ini', 'w') as configfile:
        config.write(configfile)

def get_selected_game_path():
    config = configparser.ConfigParser()
    config.read('config.ini')
    return config['GAME'].get('selected_game_path', '')
    
def display_menu():
    print("Welcome to the Game Menu!")
    print("1. Select a Game")
    print("2. Create Characters")
    print("3. Start the Game")
    print("4. Exit")

def select_game():
    global selected_game_path
    game_folder = "Games"    
    games = os.listdir(game_folder)    
    print("\nAvailable Games:")
    for index, game in enumerate(games, start=1):
        print(f"{index}. {game}")
    
    game_choice = int(input("Enter the number of the game you want to select: "))
    selected_game = games[game_choice - 1] if 0 < game_choice <= len(games) else None    
    if selected_game:
        print(f"You've selected '{selected_game}'.")
        selected_game_path = os.path.join(game_folder, selected_game)
        print(selected_game_path)
        set_selected_game_path(selected_game_path)
        Create.main()  
    else:
        print("Invalid selection. Please choose a valid game.")

def create_characters():
    print("\nCreating Characters...")

def start_game():
    print("\nStarting the Game...")
    
def main():
    while True:
        display_menu()
        choice = input("\nEnter your choice (1-4): ")
        
        if choice == '1':
            select_game()
        elif choice == '2':
            create_characters()
        elif choice == '3':
            start_game()
        elif choice == '4':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
