import pygame as pg

from scenes.menu_inicial import MenuInicial
from scenes.maze import Maze
from sprites.player import Player

from config import *


class GameBase():
    def __init__(self):
        self.lock_input = True
        self.sprites = pg.sprite.Group()

    def load_scene(self, scene, **kwargs):
        self.scene = scene
        self.sprites.empty()

        if self.scene == MENU_PRINCIPAL:
            pass

        elif self.scene == LOBBY:
            pass

        elif self.scene == MAZE:
            lvl = kwargs.get('lvl')
            numeroPlayers = kwargs.get('numeroPlayers')

            self.maze = Maze(game=self, level=lvl, numeroPlayers=numeroPlayers)
            #x, y = self.maze.get_player_position()

            #self.player = Player(self, x, y, RED)
            self.player = Player(self, MIDSCREEN_X, MIDSCREEN_Y, RED)

            #self.sprites.add(self.player, self.maze)
            self.sprites.add(self.player)

        elif self.scene == PAUSE:
            pass

        elif self.scene == GAME_OVER:
            pass                        

    def quit_check(self, event):
        if event.type == pg.QUIT:
            self.run = False
