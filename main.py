import pygame as pg

from scenes.game import Game
from util.config import *


if __name__ == '__main__':

    pg.init()

    #window = pg.display.set_mode((SCREENWIDTH, SCREENHEIGHT), pg.FULLSCREEN)
    window = pg.display.set_mode((SCREENWIDTH, SCREENHEIGHT), pg.RESIZABLE)

    g = Game(window)

    while g.run:
        g.currentScene.load()
        g.currentScene.loop()
    pg.quit()