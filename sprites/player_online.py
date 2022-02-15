import pygame as pg
from pathlib import Path
import socket
import pickle

from util.config import *

vector = pg.math.Vector2


class PlayerOnline(pg.sprite.Sprite):
    def __init__(self, game, client, pos_x, pos_y):
        pg.sprite.Sprite.__init__(self)

        self.game = game
        self.client = client

        path = Path("media", "images", "tv.png")
        self.image = pg.image.load(path).convert()
        self.rect = self.image.get_rect()

        self.rect.center = (pos_x, pos_y)
        self.pos = vector(self.rect.center)
        self.vel = vector(0, 0)
        self.acc = vector(0, 0)
        self.x = pos_x
        self.y = pos_y

    def update(self, walls):
        self.acc = vector(0, 0)
        key = pg.key.get_pressed()

        pos_inicial = vector(self.pos.x, self.pos.y)

        # movimento
        if key[pg.K_LEFT]:
            self.acc.x = -PLAYER_ACC
        if key[pg.K_RIGHT]:
            self.acc.x = PLAYER_ACC
        if key[pg.K_DOWN]:
            self.acc.y = PLAYER_ACC
        if key[pg.K_UP]:
            self.acc.y = -PLAYER_ACC

        # equações para movimento
        acc_x = self.vel.x * PLAYER_FRICTION
        self.acc.x += acc_x
        vel_x = self.acc.x
        self.vel.x += vel_x
        pos_x = self.vel.x + 0.5 * self.acc.x
        self.pos.x += pos_x

        acc_y = self.vel.y * PLAYER_FRICTION
        self.acc.y += acc_y
        vel_y = self.acc.y
        self.vel.y += vel_y
        pos_y = self.vel.y + 0.5 * self.acc.y
        self.pos.y += pos_y

        self.rect.center = self.pos  

        collides = pg.sprite.spritecollide(self, walls, False)

        if collides:
            tolerance = 10
            collide_t = False
            collide_b = False
            collide_r = False
            collide_l = False

            for collide in collides:

                dist_t = abs(self.rect.top - collide.rect.bottom)
                dist_b = abs(self.rect.bottom - collide.rect.top)
                if dist_t <= tolerance and self.acc.y < 0 and not collide_t:
                    collide_t = True
                    self.pos.y -= pos_y
                    self.vel.y = 0           
                elif dist_b <= tolerance and self.acc.y > 0 and not collide_b:
                    collide_b = True
                    self.pos.y -= pos_y
                    self.vel.y = 0 
                
                dist_l = abs(self.rect.left - collide.rect.right)
                dist_r = abs(self.rect.right - collide.rect.left)
                if dist_l <= tolerance and self.acc.x < 0 and not collide_l:
                    collide_l = True
                    self.pos.x -= pos_x
                    self.vel.x = 0       
                elif dist_r <= tolerance and self.acc.x > 0 and not collide_r:
                    collide_r = True
                    self.pos.x -= pos_x
                    self.vel.x = 0    


        # condition to stop (to print standing_frames)
        if abs(self.vel.x) <= 1:
            self.vel.x = 0
            self.acc.y = 0
            self.walking = False
        if abs(self.vel.y) <= 1:
            self.vel.y = 0
            self.acc.y = 0
            self.walking = False

        if self.pos != self.rect.center:
            self.rect.center = self.pos  

        if self.pos != pos_inicial:
            self.send_position()

    def send_position(self):
        message = {'id': 'player_position',
                   'data': {
                       'player_id': self.client.id,
                       'x': self.pos.x - self.game.compass.x ,
                       'y': self.pos.y - self.game.compass.y
                           }
                   }

        self.client.send_message(message)