import pygame as pg
from pathlib import Path
from math import ceil

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

        self.walking = False
        self.collides = []

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
        tolerance = 10
        print(self.vel.x, self.vel.y)
        if self.collides:
            for collide in self.collides:
                if (abs(self.rect.top - collide.rect.bottom) < tolerance and self.acc.y < 0):
                    self.acc.y = 0
                    self.vel.y = 0                 
                if (abs(self.rect.bottom - collide.rect.top) < tolerance and self.acc.y > 0):
                    self.acc.y = 0
                    self.vel.y = 0
                if (abs(self.rect.right - collide.rect.left) < tolerance and self.acc.x > 0):
                    self.acc.x = 0
                    self.vel.x = 0                    
                if (abs(self.rect.left - collide.rect.right) < tolerance and self.acc.x < 0):
                    self.acc.x = 0
                    self.vel.x = 0                     
                else:
                    if self.acc.x != 0:
                        self.acc.x += self.vel.x * PLAYER_FRICTION
                        self.vel.x += self.acc.x
                        self.pos.x += self.vel.x + 0.5 * self.acc.x
                    if self.acc.y != 0:
                        self.acc.y += self.vel.y * PLAYER_FRICTION
                        self.vel.y += self.acc.y
                        self.pos.y += self.vel.y + 0.5 * self.acc.y                        

        else:
            self.acc.x += self.vel.x * PLAYER_FRICTION
            self.vel.x += self.acc.x
            self.pos.x += self.vel.x + 0.5 * self.acc.x

            self.acc.y += self.vel.y * PLAYER_FRICTION
            self.vel.y += self.acc.y
            self.pos.y += self.vel.y + 0.5 * self.acc.y

            self.walking = True

        # condition to stop (to print standing_frames)
        if abs(self.vel.x) <= 1:
            self.vel.x = 0
            self.acc.y = 0
            self.walking = False
        if abs(self.vel.y) <= 1:
            self.vel.y = 0
            self.acc.y = 0
            self.walking = False  

        # atualização da posição
        self.rect.center = self.pos    


