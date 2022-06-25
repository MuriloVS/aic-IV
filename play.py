import pygame as pg

from builder import Builder
from config import *


if __name__ == '__main__':

    pg.init()

    #window = pg.display.set_mode((SCREENWIDTH, SCREENHEIGHT), pg.FULLSCREEN)
    window = pg.display.set_mode((SCREENWIDTH, SCREENHEIGHT), pg.RESIZABLE)

    g = Builder(window)

    while g.run:
        g.currentScene.load()
        g.currentScene.loop()
    pg.quit()