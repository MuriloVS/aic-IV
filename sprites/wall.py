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
        self.size_x = size[0]
        self.size_y = size[1]/4
        print(f'pos: ({self.x, self.y}) - size: ({self.size_x, self.size_y})')

        path = Path("media", "images", "tv.png")
        #self.image = pg.image.load(path).convert()
        self.image = pg.Surface((self.size_x, self.size_y))
        self.image.fill(RED)

        if orientacao == 1:
            self.image = pg.transform.rotate(self.image, 90)

        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)
        self.pos = vector(self.rect.midbottom)

    def update(self):
        pass

