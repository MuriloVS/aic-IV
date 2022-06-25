import pygame as pg

from scenes.menus import MainMenu, MultiplayerMenu, Options, Credits
from scenes.singleplayer import Singleplayer
from scenes.host import Host
from scenes.guest import Guest
from config import *

vector = pg.math.Vector2


class Builder:
    def __init__(self, window: pg.display):

        self.window = window
        self.rect = self.window.get_rect()
        self.rect.center = (SCREENWIDTH/2, SCREENHEIGHT/2)
        pg.display.set_caption(TITLE)

        self.lvl = 1

        # menus
        self.menuInicial = MainMenu(self, self.window)
        self.menuMultiplayer = MultiplayerMenu(self, self.window)
        self.options = Options(self, self.window)
        self.credits = Credits(self, self.window)

        # modos de jogo
        self.singleplayer = Singleplayer(self, self.window)
        self.multiplayer_host = Host(self, self.window)
        self.multiplayer_guest = Guest(self, self.window)

        self.currentScene = self.menuInicial

        self.run = True