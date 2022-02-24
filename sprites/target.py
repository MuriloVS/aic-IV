import pygame as pg
from pathlib import Path

from config import *

vector = pg.math.Vector2


class Target(pg.sprite.Sprite):
    def __init__(self, game, pos_x, pos_y, file=GREEN):
        pg.sprite.Sprite.__init__(self)

        self.game = game

        #path = Path("media", "images", file)
        #self.image = pg.image.load(path).convert()
        self.image = pg.Surface((SIZE, SIZE))
        self.image.fill(file)
        self.rect = self.image.get_rect()

        self.rect.topleft = (pos_x*SIZE, pos_y*SIZE)
        self.pos = vector(self.rect.center)

    def update(self):
        pass