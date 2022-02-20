import pygame_menu as pg_menu
import pygame as pg

from util.config import *


class MainMenu(pg_menu.Menu):
    def __init__(self, window) -> None:
        super().__init__(TITLE, SCREENWIDTH/3, SCREENHEIGHT/2)

        self.window = window
        self.run = False

    def load(self):
        self.add.button('Singleplayer', self.start_singleplayer)
        self.add.button('Multiplayer', self.start_multiplayer)
        self.add.button('Opções')
        self.add.button('Sobre')
        self.add.button('Sair', pg_menu.events.EXIT)

        # self.add.dropselect('Nível', [('Hard', 1), ('Easy', 2)])
        # self.add.text_input('Name :', default='John Doe', font=pg_menu.font.FONT_COMIC_NEUE)
        # self.add.selector('Difficulty :', [('Hard', 1), ('Easy', 2)], onchange=self.set_difficulty)
        
    def loop(self):
        self.run = True
        while self.run:
            self.update(pg.event.get())
            self.draw(self.window)
            pg.display.flip()

    def set_difficulty(self, value, difficulty):
        print(value, difficulty)
        pass

    def start_singleplayer(self):
        # Do the job here !
        pass

    def start_multiplayer(self):
        # Do the job here !
        pass    

if __name__ == '__main__':

    pg.init()
    window = pg.display.set_mode((SCREENWIDTH, SCREENHEIGHT), pg.RESIZABLE)
    menu = MainMenu(window)
    menu.load()
    menu.loop()