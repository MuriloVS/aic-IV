import pygame as pg

from scenes.main_menu import MainMenu
from scenes.game import Game
from scenes.game_host import  GameMultiplayerHost
from util.config import *


if __name__ == '__main__':

    pg.init()

    #window = pg.display.set_mode((SCREENWIDTH, SCREENHEIGHT), pg.FULLSCREEN)
    window = pg.display.set_mode((SCREENWIDTH, SCREENHEIGHT), pg.RESIZABLE)

    g = GameMultiplayerHost(window)
    #g = MainMenu(window)

    while g.run:
        g.load()
        #g.load_scene(MENU_PRINCIPAL)
        g.loop()
