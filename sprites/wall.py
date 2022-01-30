import pygame as pg
from pathlib import Path

from util.config import *


vector = pg.math.Vector2


class Wall(pg.sprite.Sprite):
    def __init__(self, x, y, orientacao, posicao):
        pg.sprite.Sprite.__init__(self)

        self.x = x*30+50
        self.y = y*30+100

        path = Path("media", "images", "tv.png")
        self.image = pg.image.load(path).convert()
        #self.image = pg.Surface()

        if orientacao == 'v':
            self.image = pg.transform.scale(self.image, (50,25))
            self.image = pg.transform.rotate(self.image, 90)
        else:
            self.image = pg.transform.scale(self.image, (25,50))

#        if posicao == 'n':


        self.rect = self.image.get_rect()

        self.rect.midbottom = (self.x, self.y)
        self.pos = vector(self.rect.midbottom)

    def update(self):
        pass
