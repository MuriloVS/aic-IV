import pygame as pg
from pathlib import Path

from config import *


vector = pg.math.Vector2

class Text(pg.sprite.Sprite):
    def __init__(self, text, size, pos_x, pos_y, color=WHITE, font=pg.font.get_default_font(), background=None):
        pg.sprite.Sprite.__init__(self)
        self.font = pg.font.Font(font, size)

        self.image = self.font.render(text, True, color, background)
        self.rect = self.image.get_rect()
        self.rect.center = (pos_x, pos_y)

    def update(self):
        pass

