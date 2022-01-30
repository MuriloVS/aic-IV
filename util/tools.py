import pygame as pg

from config import *


def wait_for_key() -> bool:
    waiting = True
    while waiting:
        pg.clock.tick(FPS)
        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_RETURN:
                    return True