import pygame as pg
from config import *


vector = pg.math.Vector2


class Player(pg.sprite.Sprite):
    def __init__(self, game, x, y, color):
        pg.sprite.Sprite.__init__(self)

        self.game = game

        self.image = pg.image.load(os.path.join(
            ROOT, 'media', 'images', 'tv.png')).convert()
        self.rect = self.image.get_rect()

        self.rect.midbottom = (MIDSCREEN_X, MIDSCREEN_Y)
        self.pos = vector(self.rect.midbottom)
        self.vel = vector(0, 0)
        self.acc = vector(0, 0)
        self.x = x
        self.y = y

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
