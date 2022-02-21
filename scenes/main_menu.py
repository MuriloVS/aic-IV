import pygame_menu as pg_menu
import pygame as pg

from util.config import *


class Menu(pg_menu.Menu):
    def __init__(self, game, window):
        super().__init__(TITLE, SCREENWIDTH/3, SCREENHEIGHT/2)
        self.game = game
        self.window = window

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
        self.add.button('Sobre')
        self.add.button('Sair', pg_menu.events.EXIT)

    def start_singleplayer(self):
        self.game.currentScene = self.game.singleplayer
        self.game.play = True
        self.run = False

    def start_menu_multiplayer(self):
        self.game.currentScene = self.game.multiplayer_host
        self.game.play = True
        self.run = False 

    def start_options(self): # continuar aqui
        self.game.currentScene = self.options
        self.run = False   


class Options(Menu):
    def __init__(self, game, window):
        super().__init__(game, window)

        self.run = False

    def load(self):
        self.clear(True)

        self.add.text_input('Name :', default='John Doe', font=pg_menu.font.FONT_COMIC_NEUE)
        self.add.selector('Difficulty :', [('Hard', 1), ('Easy', 2)], onchange=self.set_difficulty)

    def set_difficulty(self, value, difficulty):
        print(value, difficulty)


class Credits(Menu):
    def __init__(self, game, window):
        super().__init__(game, window)

        self.run = False

    def load(self):
        self.clear(True)

        # continuar aqui


if __name__ == '__main__':

    pg.init()
    window = pg.display.set_mode((SCREENWIDTH, SCREENHEIGHT), pg.RESIZABLE)
    menu = MainMenu(window)
    menu.load()
    menu.loop()