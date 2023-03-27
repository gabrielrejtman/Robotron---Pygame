from game import Game
from config import *

pygame.init()

pygame.display.set_caption("Robotron")

play = Game(screen)
Game.game_loop(play)