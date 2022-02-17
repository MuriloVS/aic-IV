import pygame as pg

from scenes.game_guest import GameMultiplayerGuest
from util.config import *


if __name__ == '__main__':

    pg.init()

    #window = pg.display.set_mode((SCREENWIDTH, SCREENHEIGHT), pg.FULLSCREEN)
    window = pg.display.set_mode((SCREENWIDTH, SCREENHEIGHT), pg.RESIZABLE)

    g = GameMultiplayerGuest(window)
    
    g.load()
    #g.load_scene(MENU_PRINCIPAL)
    g.loop()
