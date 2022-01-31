import pygame as pg
from pathlib import Path

from util.config import *


vector = pg.math.Vector2


class Player(pg.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        pg.sprite.Sprite.__init__(self)

        path = Path("media", "images", "tv.png")
        self.image = pg.image.load(path).convert()
        self.rect = self.image.get_rect()

        self.rect.midbottom = (SCREENWIDTH/2, SCREENHEIGHT/2)
        self.pos = vector(self.rect.midbottom)
        self.vel = vector(0, 0)
        self.acc = vector(0, 0)
        self.x = pos_x
        self.y = pos_y

    def update(self):
        self.acc = vector(0, 0)
        key = pg.key.get_pressed()

        # movimento
        if key[pg.K_LEFT]:
            self.acc.x = -PLAYER_ACC
        if key[pg.K_RIGHT]:
            self.acc.x = PLAYER_ACC
        if key[pg.K_DOWN]:
            self.acc.y = PLAYER_ACC
        if key[pg.K_UP]:
            self.acc.y = -PLAYER_ACC

        # atrito
        self.acc.x += self.vel.x * PLAYER_FRICTION
        self.vel.x += self.acc.x
        self.pos.x += self.vel.x + 0.5 * self.acc.x
        self.acc.y += self.vel.y * PLAYER_FRICTION
        self.vel.y += self.acc.y
        self.pos.y += self.vel.y + 0.5 * self.acc.y

        # atualização da posição
        self.rect.midbottom = self.pos
