from game import Game
from util.config import *

if __name__ == '__main__':

    pg.init()
    window = pg.display.set_mode((0,0), pg.RESIZABLE)   

    g = Game(window)
    g.load_scene(scene=MAZE, level=2)
    g.loop()