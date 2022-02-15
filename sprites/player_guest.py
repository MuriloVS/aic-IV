import pygame as pg
from pathlib import Path

from util.config import *

vector = pg.math.Vector2


class PlayerGuest(pg.sprite.Sprite):
    def __init__(self, game, client, pos_x, pos_y):
        pg.sprite.Sprite.__init__(self)

        self.game = game
        self.client = client

        path = Path("media", "images", "tv.png")
        self.image = pg.image.load(path).convert()
        self.rect = self.image.get_rect()

        self.rect.center = (pos_x, pos_y)
        self.pos = vector(self.rect.center)
        self.x = pos_x
        self.y = pos_y

    def update(self):
        pass
          
    def move(self, pos_x, pos_y):
        self.pos.x = pos_x + self.game.compass.x 
        self.pos.y = pos_y + self.game.compass.y
        self.rect.center = self.pos