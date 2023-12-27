from GameGUI import GameGUI

game = GameGUI()

while game.running:
    game.playing = True
    game.game_loop()