from GameGUI import GameGUI

gui = GameGUI()

while gui.running:
    gui.currMenu.dispMenu()
    gui.game_loop()

    