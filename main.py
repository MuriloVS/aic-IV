import pygame as pg
from scenes.game import Game
from scenes.game_multiplayer_host import  GameMultiplayerHost

from util.config import *


if __name__ == '__main__':

    pg.init()

    #window = pg.display.set_mode((SCREENWIDTH, SCREENHEIGHT), pg.FULLSCREEN)
    window = pg.display.set_mode((SCREENWIDTH, SCREENHEIGHT), pg.RESIZABLE)

    g = Game(window)
    
    g.load()
    #g.load_scene(MENU_PRINCIPAL)
    g.loop()
