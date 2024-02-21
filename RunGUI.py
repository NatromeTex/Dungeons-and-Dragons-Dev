from GameGUI import GameGUI

gui = GameGUI()

while gui.running:
    gui.currMenu.dispMenu()
while gui.playing:
    gui.currGMenu.dispGame()