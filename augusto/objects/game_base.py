import pygame as pg
from multiprocessing import Process
from config import *

class GameBase():
        def __init__(self): # initialize game window, etc.

            QuitThread = Process(target=self.close())
            QuitThread.start()

            QuitThread = Process(target=self.getEvent())
            QuitThread.start()

        def load_scene(self, scene):
            self.scene = scene
            self.scenes[scene]()

        def getEvent(self):
            for event in pg.event.get():
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        if self.playing:
                            self.playing = False
                        self.running = False
                    if event.key == pg.K_UP:
                        self.player.jump()
                    if event.key == pg.K_d and self.lvl.get_book:
                        self.lvl.read_book()
                if event.type == pg.KEYUP:
                    if event.key == pg.K_UP:
                        self.player.jump_cut()
                if event.type == pg.KEYUP:
                    if event.key == pg.K_a or event.key == pg.K_s:
                        self.lvl.update_scenario(event.key)

        def close(self):
            while self.run:
                for event in pg.event.get():
                    if event.type == pg.QUIT:
                        self.run = False
                        pg.quit()


if __name__ == "__main__":
    g = Game()
    g.load_scene('menu_inicial')