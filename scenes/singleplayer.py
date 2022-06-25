import pygame as pg

from scenes.game import Game
from sprites.player import Player
from sprites.target import Target
from sprites.text import Text
from util.maze import Maze
from config import *

vector = pg.math.Vector2


class Singleplayer(Game):
    def __init__(self, game, window: pg.display):
        super().__init__(game, window)

    def load(self):
        # carregano música
        #self.music_file = None
        #self.music = self.get_sound(self.music_file)
        self.music = self.get_sound() 

        # cria o labirinto
        self.maze = Maze(level=self.g.lvl, numPlayers=2)
        self.maze.build()
        self.maze.build_walls_sprites()
        # recebendo posição inicial do player
        x, y = self.maze.get_player_position()

        # cria linha de partida e chegada
        self.set_targets(self.maze.rows, self.maze.cols)

        # cria o player 1
        self.player = Player(self, MIDSCREEN_X, MIDSCREEN_Y)

        # adicionando sprites aos grupos
        for wall in self.maze.walls:
            self.walls.add(wall)
            self.scenario_dinamic.add(wall)
            self.all_sprites.add(wall)
        
        self.set_camera_position(x, y)

        self.music.play(loops=-1)

    def maze_complete(self):
        # mensagem de vitória
        msg = 'VOCÊ GANHOU!'
        self.win_text = Text(msg, 40, MIDSCREEN_X, MIDSCREEN_Y, color=BLACK, background=WHITE)

        self.scenario_static.add(self.win_text)
        self.all_sprites.add(self.win_text)

        self.win = True
        #self.play = False
        #self.g.currentScene = self.g.menuInicial