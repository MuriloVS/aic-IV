from game import Game
from util.config import *

if __name__ == '__main__':

    g = Game()
    g.load_scene(scene=MAZE, level=2)
    g.loop()