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
            self.scene = HOME

            self.scenes = {
                'HOME' : ''
            }

            QuitThread = Process(target=self.close())
            QuitThread.start()



            self.load_scene(HOME)

        def load_scene(self, scene):
            self.scene = scene
            pass

        def main_loop(self):
            # loop principal
            pass

        def getEvent(self):
            pass

        def close(self):
            while self.run:
                for event in pg.event.get():
                    if event.type == pg.QUIT:
                        self.run = False
                        pg.quit()


if __name__ == "__main__":
    g = Game()