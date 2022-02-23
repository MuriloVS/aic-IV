from pathlib import Path

import pygame as pg
import pygame_menu as pg_menu
from pygame_menu import sound, themes

from util.config import *


class Menu(pg_menu.Menu):
    def __init__(self, game, window, theme=themes.THEME_BLUE):

        self.game = game
        self.window = window
        self._theme = theme.copy()
        #self._theme.background_color = (0, 25, 200, 180)

        super().__init__(TITLE, SCREENWIDTH/2, SCREENHEIGHT/2, theme=self._theme)

        # som
        self.engine = sound.Sound()
        self.engine.set_sound(sound.SOUND_TYPE_KEY_ADDITION,
                              Path('media', 'menu', 'Menu Selection Click.wav'))
        self.set_sound(self.engine, recursive=True)

        self.run = False

    def loop(self):
        self.enable()
        self.run = True
        while self.run:
            events = pg.event.get()
            for event in events:
                if event.type == pg.QUIT:
                    exit()
            if self.is_enabled():
                self.update(events)
                self.draw(self.window, True)

            pg.display.update()
        self.disable()


class MainMenu(Menu):
    def __init__(self, game, window):
        super().__init__(game, window)

    def load(self):
        self.clear(True)

        self.add.button('Singleplayer', self.start_singleplayer)
        self.add.button('Multiplayer', self.start_menu_multiplayer)
        self.add.button('Opções', self.start_options)
        self.add.button('Sobre', self.start_credits)
        self.add.button('Sair', pg_menu.events.EXIT)

        self.add.clock()

    def start_singleplayer(self):
        self.game.currentScene = self.game.singleplayer
        self.run = False

    def start_menu_multiplayer(self):
        self.game.currentScene = self.game.multiplayer_host
        self.run = False

    def start_options(self):  # continuar aqui
        self.game.currentScene = self.game.options
        self.run = False

    def start_credits(self):  # continuar aqui
        self.game.currentScene = self.game.credits
        self.run = False


class Options(Menu):
    def __init__(self, game, window):
        super().__init__(game, window)

    def load(self):
        self.clear(True)

        self.add.text_input('Name :', default='Murilo Dev Master',
                            font=pg_menu.font.FONT_COMIC_NEUE)
        self.add.selector(
            'Difficulty :', [('Easy', 1), ('Hard', 2)], onchange=self.set_difficulty)
        self.add.button('Back', self.get_back)

    def set_difficulty(self, value, difficulty):
        global GAME_DIFFICULTY
        GAME_DIFFICULTY = difficulty
        print(GAME_DIFFICULTY)

    def get_back(self):
        self.game.currentScene = self.game.menuInicial
        self.run = False


class Credits(Menu):
    def __init__(self, game, window):
        super().__init__(game, window)

    def load(self):
        self.clear(True)

        self.add.label(
            '''Jogo desenvolvido por Augusto Cardoso Setti e
            Murilo Vitória da Silva (há controvérsias)
            como tarefa da disciplina de AIC IV, do 
            Curso de Engenharia de Computação, entre
            2021 e 2022.''', font_size=16)
        self.add.button('Back', self.get_back)

    def get_back(self):
        self.game.currentScene = self.game.menuInicial
        self.run = False


if __name__ == '__main__':

    pg.init()
    window = pg.display.set_mode((SCREENWIDTH, SCREENHEIGHT), pg.RESIZABLE)
    menu = MainMenu(window)
    menu.load()
    menu.loop()
