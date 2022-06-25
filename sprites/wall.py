import pygame as pg
from pathlib import Path

from config import *


vector = pg.math.Vector2

class Wall(pg.sprite.Sprite):
    def __init__(self, pos, size, orientacao=0):
        pg.sprite.Sprite.__init__(self)

        # recebendo posição
        self.pos = vector(0, 0)
        self.pos.x = pos[0]
        self.pos.y = pos[1]

        # ajustando dimensões da parede
        self.size_x = size * 1.25
        self.size_y = size * 0.25

        # criando superfície
        path = Path("media", "images", "wall.gif")
        self.image = pg.image.load(path).convert()
        pg.transform.scale(self.image, (self.size_x, self.size_y))
        # self.image = pg.Surface((self.size_x, self.size_y))
        # self.image.fill((45,45,45))

        # definindo orientação da parede
        if orientacao == 1:
            self.image = pg.transform.rotate(self.image, 90)

        # definindo posição do objeto
        self.rect = self.image.get_rect()
        self.rect.center = (self.pos.x, self.pos.y)
        self.pos = vector(self.rect.center)

    def update(self):
        pass

