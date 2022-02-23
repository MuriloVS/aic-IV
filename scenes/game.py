import pygame as pg

from scenes.main_menu import MainMenu, Options, Credits
from scenes.game_singleplayer import GameSingleplayer
from scenes.game_host import GameMultiplayerHost
from scenes.game_guest import GameMultiplayerGuest
from util.config import *

vector = pg.math.Vector2


class Game:
    def __init__(self, window: pg.display):

        self.window = window
        self.rect = self.window.get_rect()
        self.rect.center = (SCREENWIDTH/2, SCREENHEIGHT/2)
        pg.display.set_caption(TITLE)

        self.lvl = ''

        # menus
        self.menuInicial = MainMenu(self, self.window)
        self.options = Options(self, self.window)
        self.credits = Credits(self, self.window)

        # modos de jogo
        self.singleplayer = GameSingleplayer(self, self.window)
        self.multiplayer_host = GameMultiplayerHost(self, self.window)
        self.multiplayer_guest = GameMultiplayerGuest(self, self.window)

        self.currentScene = self.menuInicial

        self.run = True