import pygame as pg

from sprites.player import Player
from util.config import *

vector = pg.math.Vector2


class PlayerGuest(Player):
    def __init__(self, game, client, pos_x=MIDSCREEN_X, pos_y=MIDSCREEN_Y):
        super().__init__(game, pos_x, pos_y)

        self.client = client

    def update(self):
        pass
          
    def move(self, pos_x, pos_y):
        self.pos.x = pos_x + self.game.compass.x 
        self.pos.y = pos_y + self.game.compass.y
        self.rect.center = self.pos