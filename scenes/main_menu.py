from pathlib import Path

import pygame as pg
import pygame_menu as pg_menu
from pygame_menu import sound, themes

from config import *


class Menu(pg_menu.Menu):
    def __init__(self, game, window, theme=themes.THEME_BLUE, width=SCREENWIDTH/3, height=SCREENHEIGHT/2):

        self.game = game
        self.window = window
        self._theme = theme.copy()
        #self._theme.background_color = (0, 25, 200, 180)
        self.width = width
        self.height = height

        super().__init__(TITLE, self.width, self.height, theme=self._theme)

        # som
        self.engine = sound.Sound()
        self.engine.set_sound(sound.SOUND_TYPE_KEY_ADDITION,
                              Path('media', 'sounds', 'Menu Selection Click.wav'))
        self.set_sound(self.engine, recursive=True)

        self.loaded = False
        self.run = False

    def loop(self):
        global SCREENWIDTH, SCREENHEIGHT

        self.enable()
        self.run = True

        while self.run:
            events = pg.event.get()
            for event in events:

                if event.type == pg.QUIT:
                    exit()

                if event.type == pg.VIDEORESIZE:
                    SCREENWIDTH = event.w
                    SCREENHEIGHT = event.h
                    self.on_resize()

                if event.type == pg.KEYDOWN:
                
                    if event.key == pg.K_ESCAPE:
                        self.game.currentScene = self.game.menuInicial
                        self.run = False

            if self.is_enabled():
                self.update(events)
                self.draw(self.window, True)

            pg.display.update()
        self.disable()

    def on_resize(self):
        new_w, new_h = self.window.get_size()
        self.set_absolute_position(new_w/2-self.width/2, new_h/2-self.height/2)

    def get_back(self):
        self.game.currentScene = self.game.menuInicial
        self.run = False

class MainMenu(Menu):
    def __init__(self, game, window):
        super().__init__(game, window)

    def load(self):
        if not self.loaded:
            self.add.button('Singleplayer', self.start_singleplayer)
            self.add.button('Multiplayer', self.start_menu_multiplayer)
            self.add.button('Options', self.start_options)
            self.add.button('About', self.start_credits)
            self.add.vertical_margin(10)
            self.add.button('Exit', pg_menu.events.EXIT)

            self.loaded = True

        self.on_resize()
        self.force_surface_update()

    def start_singleplayer(self):
        self.game.currentScene = self.game.singleplayer
        self.run = False

    def start_menu_multiplayer(self):
        self.game.currentScene = self.game.menuMultiplayer
        self.run = False

    def start_options(self):
        self.game.currentScene = self.game.options
        self.run = False

    def start_credits(self):
        self.game.currentScene = self.game.credits
        self.run = False

class MultiplayerMenu(Menu):
    def __init__(self, game, window):
        super().__init__(game, window)

    def load(self):
        if not self.loaded:
            self.add.label('Multiplayer')
            self.add.vertical_margin(20)
            self.add.button('Create Room', self.start_host)
            self.add.button('Conect Room', self.start_guest)
            self.add.button('Local', self.start_multiplayer_local)
            self.add.vertical_margin(20)
            self.add.button('Return to menu', self.get_back)

            self.loaded = True

        self.on_resize()
        self.force_surface_update()

    def start_host(self):
        self.game.currentScene = self.game.multiplayer_host
        self.run = False

    def start_guest(self):
        self.game.currentScene = self.game.multiplayer_guest
        self.run = False

    def start_multiplayer_local(self): # continuar aqui
        # self.game.currentScene = self.game.singleplayer
        # self.run = False
        pass

class Options(Menu):
    def __init__(self, game, window):
        super().__init__(game, window)

    def load(self):
        if not self.loaded:
            self.add.label('Options')
            self.add.vertical_margin(20)
            self.add.text_input('Name :', default='Mr Ball',
                                font=pg_menu.font.FONT_COMIC_NEUE)
            self.add.selector(
                'Difficulty :', [('Easy', 1), ('Normal', 2), ('Hard', 3), ('Very Hard', 4), ('Impossible', 5)], onchange=self.set_difficulty)
            self.add.vertical_margin(20)
            self.add.button('Back', self.get_back)

            self.loaded = True

        self.on_resize()
        self.force_surface_update()

    def set_difficulty(self, value, difficulty):
        self.game.lvl = int(difficulty)

class Credits(Menu):
    def __init__(self, game, window):
        super().__init__(game, window)

    def load(self):
        if not self.loaded:
            self.add.label('About')
            self.add.label(
                '''Jogo desenvolvido por Augusto Cardoso Setti
                e Murilo Vitória da Silva como tarefa da
                disciplina de AIC IV, do Curso de 
                Engenharia de Computação, entre
                2021 e 2022.''', font_size=16)
            self.add.button('Back', self.get_back)

            self.loaded = True

        self.on_resize()

    def get_back(self):
        self.game.currentScene = self.game.menuInicial
        self.run = False


if __name__ == '__main__':

    pg.init()
    window = pg.display.set_mode((SCREENWIDTH, SCREENHEIGHT), pg.RESIZABLE)
    menu = MainMenu(window)
    menu.load()
    menu.loop()
