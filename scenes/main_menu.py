from pathlib import Path
import pygame_menu as pg_menu
from pygame_menu import sound
import pygame as pg

from util.config import *

# engine = sound.Sound()
# engine.set_sound(sound.SOUND_TYPE_OPEN_MENU, Path(
#     'media', 'menu', 'misc_menu_4.wav'))


class Menu(pg_menu.Menu):
    def __init__(self, game, window, theme=pg_menu.themes.THEME_BLUE):
        super().__init__(TITLE, SCREENWIDTH/3, SCREENHEIGHT/2)
        self.game = game
        self.window = window
        self._theme = theme

        # som
        self.engine = sound.Sound()
        self.engine.set_sound(sound.SOUND_TYPE_KEY_ADDITION,
                              Path('media', 'menu', 'Menu Selection Click.wav'))
        self.set_sound(self.engine, recursive=True)

    def loop(self):
        self.run = True
        self.enable()
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

        self.options = Options(game, self.window)
        self.credits = Credits(game, self.window)

        pg_menu.Menu.in_submenu(self, self.options)
        pg_menu.Menu.in_submenu(self, self.credits)

        self.run = False

    def load(self):
        self.clear(True)

        self.add.button('Singleplayer', self.start_singleplayer)
        self.add.button('Multiplayer', self.start_menu_multiplayer)
        self.add.button('Opções', self.start_options)
        self.add.button('Sobre', self.start_credits)
        self.add.button('Sair', pg_menu.events.EXIT)

    def start_singleplayer(self):
        self.game.currentScene = self.game.singleplayer
        self.game.play = True
        self.run = False

    def start_menu_multiplayer(self):
        self.game.currentScene = self.game.multiplayer_host
        self.game.play = True
        self.run = False

    def start_options(self):  # continuar aqui
        self.game.currentScene = self.options
        self.run = False

    def start_credits(self):  # continuar aqui
        self.game.currentScene = self.credits
        self.run = False


class Options(Menu):
    def __init__(self, game, window):
        super().__init__(game, window)

        self.run = False

    def load(self):
        self.clear(True)

        # self.add.text_input('Name :', default='John Doe',
        #                     font=pg_menu.font.FONT_COMIC_NEUE)
        self.add.selector(
            'Difficulty :', [('Hard', 1), ('Easy', 2)], onchange=self.set_difficulty)
        self.add.button('Back', pg_menu.events.BACK)

    def set_difficulty(self, value, difficulty):
        print(value, difficulty)


class Credits(Menu):
    def __init__(self, game, window):
        super().__init__(game, window)

        self.run = False

    def load(self):
        self.clear(True)

        self.add.label(
            '''  Jogo desenvolvido por
            Augusto Cardoso Setti e
            Murilo Vitória da Silva
            (há controvérsias) como tarefa
            da disciplina de AIC IV,
            do Curso de Engenharia de Computação,
            entre 2021 e 2022.''', font_size=16)
        self.add.button('Back', )

        # continuar aqui


if __name__ == '__main__':

    pg.init()
    window = pg.display.set_mode((SCREENWIDTH, SCREENHEIGHT), pg.RESIZABLE)
    menu = MainMenu(window)
    menu.load()
    menu.loop()
