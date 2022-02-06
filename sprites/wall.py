from re import X
import pygame as pg
from pathlib import Path

from util.config import *


vector = pg.math.Vector2


class Wall(pg.sprite.Sprite):
    def __init__(self, pos, size, orientacao=0):
        pg.sprite.Sprite.__init__(self)

        self.x = pos[0]
        self.y = pos[1]
        # ajustando dimensões da parede
        self.size_x = size * 1.25
        self.size_y = size * 0.25

        path = Path("media", "images", "tv.png")
        #self.image = pg.image.load(path).convert()
        self.image = pg.Surface((self.size_x, self.size_y))
        self.image.fill((45,45,45))

        if orientacao == 1:
            self.image = pg.transform.rotate(self.image, 90)

        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)
        self.pos = vector(self.rect.center)

    def update(self):
        pass

