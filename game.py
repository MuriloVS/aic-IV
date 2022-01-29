import pygame as pg

from util.game_base import GameBase
from util.config import *


class Game(GameBase):

    def __init__(self):
        super().__init__()

        pg.init()
        pg.mixer.init()
        pg.display.set_caption(TITLE)

        self.window = pg.display.set_mode((WIDTH, HEIGHT))
        self.clock = pg.time.Clock()

        self.scene = ''
        self.load_scene(scene=MENU_PRINCIPAL)

    def loop(self):

        self.run = True
        while self.run:
            self.clock.tick(FPS)

            for event in pg.event.get():
                self.quit_check(event)
                #self.get_input(event)

            self.update()
            self.draw()
        pg.quit()

    def update(self):
        #self.sprites.update()
        self.player.update()

    def draw(self):
        self.window.fill(BLACK)

        self.sprites.draw(self.window)

        self.window.blit((self.player.image), (self.player.rect))
        # self.player.draw() # TESTE
        
        pg.display.flip()


if __name__ == '__main__':

    g = Game()
    g.load_scene(scene=MAZE, lvl=0)
    g.loop()