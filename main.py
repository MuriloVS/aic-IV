import pygame as pg
import time
from game import Game

from util.config import *


if __name__ == '__main__':

    pg.init()

    #window = pg.display.set_mode((SCREENWIDTH, SCREENHEIGHT), pg.FULLSCREEN)
    window = pg.display.set_mode((SCREENWIDTH, SCREENHEIGHT), pg.RESIZABLE)

    g = Game(window)
    start = time.time()
    g.load_scene(MAZE)
    #g.load_scene(MENU_PRINCIPAL)
    while time.time() - start < 0.5:
        continue
    g.loop()
