import pygame as pg
from math import ceil

from scenes.game_base import GameBase
from sprites.player import Player
from sprites.target import Target
from sprites.text import Text
from util.maze import Maze
from util.config import *

vector = pg.math.Vector2


class GameSingleplayer(GameBase):
    def __init__(self, game, window: pg.display):
        super().__init__(game, window)

    def load(self):
        # carregano música
        #self.music_file = None
        #self.music = self.get_sound(self.music_file)
        self.music = self.get_sound() 

        # mensagem de vitória
        msg = 'VOCÊ GANHOU!'
        self.win_text = Text(msg, 40, MIDSCREEN_X, MIDSCREEN_Y, color=BLACK, background=WHITE)

        # recebendo nível

        # cria o labirinto
        self.maze = Maze(level=GAME_DIFFICULTY, numPlayers=2)
        self.maze.build()
        self.maze.build_walls_sprites()
        # recebendo posição inicial do player
        x, y = self.maze.get_player_position()

        # cria linha de partida e chegada
        self.finish = Target(self, 0, 0, GREEN)
        self.start = Target(self, self.maze.rows-1, self.maze.cols-1, RED)

        # cria o player 1
        self.player = Player(self, MIDSCREEN_X, MIDSCREEN_Y)

        # adicionando sprites aos grupos
        self.scenario_dinamic.add(self.finish, self.start)
        for wall in self.maze.walls:
            self.walls.add(wall)
            self.scenario_dinamic.add(wall)
        
        self.set_camera_position(x, y)

        self.music.play(loops=-1)

    def winner(self):
        self.win = True
        self.scenario_static.add(self.win_text)
        #self.play = False
        #self.g.currentScene = self.g.menuInicial

    def close(self):
        self.win = False
        self.reset_scene()
