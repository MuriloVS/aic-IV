import pygame as pg
from pathlib import Path

from scenes.main_menu import MainMenu
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

        self.menuInicial = MainMenu(self, self.window)
        self.singleplayer = GameSingleplayer(self, self.window)
        self.multiplayer_host = GameMultiplayerHost(self, self.window)
        self.multiplayer_guest = GameMultiplayerGuest(self, self.window)

        self.currentScene = self.menuInicial

        self.play = False
        self.run = True

    def draw_text(self, text, size, x, y, font=pg.font.get_default_font()):
        font = pg.font.Font(font, size)
        text_surface = font.render(text, True, WHITE)
        text_rect = text_surface.get_rect()
        text_rect.center = (x, y)
        self.window.blit(text_surface, text_rect)

    def play_music(self, music='music_intro.wav', volume=0.15, loops=-1):  # continuar aqui
        path = Path('media', 'music', music)
        self.intro_music = pg.mixer.Sound(path)
        self.intro_music.set_volume(volume)
        self.intro_music.play(loops)
