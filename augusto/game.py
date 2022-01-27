import pygame as pg
from multiprocessing import Process
from config import *

class Game():
        def __init__(self): # initialize game window, etc.

            pg.init()
            pg.mixer.init()
            pg.display.set_caption(TITLE)
            
            self.window = pg.display.set_mode((WIDTH, HEIGHT))
            self.clock = pg.time.Clock()
            self.run = True
            self.scene = ''

            self.scenes = {
                'menu_inicial' : ''
            }

        def main_loop(self):
            while self.run:
                self.clock.tick(FPS)
                self.events()
                self.update()
                self.draw()


if __name__ == "__main__":
    g = Game()
    g.load_scene('menu_inicial')