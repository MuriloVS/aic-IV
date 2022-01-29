import pygame as pg


class Maze(pg.sprite.Sprite):
    def __init__(self, game, level=1, numeroPlayers=1):
        pg.sprite.Sprite.__init__(self)

        self.game = game
        self.level = level
        self.numeroPlayers = numeroPlayers

        self.generate_maze()

    def load_data(self):
        pass

    def generate_maze(self, lvl=False):
        if lvl:
            self.level = lvl

        tam = lvl*5

        if self.level == 1:
            pass
        if self.level == 2:
            pass
        if self.level == 3:
            pass
        if self.level == 4:
            pass
        if self.level == 5:
            pass
        

    def get_player_position(self):
        pass
        