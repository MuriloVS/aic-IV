import pygame as pg
from multiplayer_guest import Game

from util.config import *


if __name__ == '__main__':

    pg.init()

    #window = pg.display.set_mode((SCREENWIDTH, SCREENHEIGHT), pg.FULLSCREEN)
    window = pg.display.set_mode((SCREENWIDTH, SCREENHEIGHT), pg.RESIZABLE)

    g = Game(window)
    
    g.load_scene(MAZE)
    #g.load_scene(MENU_PRINCIPAL)
    g.loop()