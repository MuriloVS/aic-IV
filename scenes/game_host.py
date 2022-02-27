from threading import Thread
import pygame as pg
import time

from scenes.game_base import GameBase
from sprites.target import Target
from sprites.player_online import PlayerOnline
from sprites.player_guest import PlayerGuest
from sprites.target import Target
from sprites.text import Text
from connection.server import Server
from connection.client import Client
from util.maze import Maze
from config import *

vector = pg.math.Vector2


class GameMultiplayerHost(GameBase):

    def __init__(self, game, window: pg.display):
        super().__init__(game, window)

    def load(self):
        # carregano música
        #self.music_file = None
        #self.music = self.get_sound(self.music_file)
        self.music = self.get_sound()

        # criando servidor multiplayer
        self.server = Server()
        self.TServer = Thread(target=self.server.subscribe)
        self.TServer.start()

        # criando cliente para conectar no servidor
        self.client = Client(self, LOCALHOST, PORT)
        self.TClient = Thread(target=self.client.receive_message)
        self.TClient.start()
        time.sleep(1)

        # cria o labirinto e envia ao servidor
        self.maze = Maze(level=self.g.lvl, numPlayers=2)
        self.maze.build()
        self.maze.build_walls_sprites()
        # recebendo posição inicial do player
        x, y = self.maze.get_player_position()

        # cria linha de partida e chegada # continuar aqui
        self.set_targets(self.maze.rows, self.maze.cols)

        # enviando lab ao servidor
        message = {'id': 'load_maze', 'data': {
            'list': self.maze.get_walls_list(),
            'position': (x, y),
            'size': (self.maze.rows, self.maze.rows)
        }
        }
        self.client.send_message(message)

        # geração dos jogadores convidados
        self.player2 = PlayerGuest(self, 2)

        # gerações do player atual
        self.player = PlayerOnline(self, self.client)

        # adicionando sprites aos grupos
        self.players.add(self.player2)
        self.scenario_dinamic.add(self.player2)

        for wall in self.maze.walls:
            self.walls.add(wall)
            self.scenario_dinamic.add(wall)
            self.all_sprites.add(wall)

        self.set_camera_position(x, y)

        self.music.play(loops=-1)

    def winner(self): # continuar aqui
        # mensagem de vitória
        msg = 'VOCÊ GANHOU!'
        self.win_text = Text(msg, 40, MIDSCREEN_X, MIDSCREEN_Y, color=BLACK, background=WHITE)

        self.scenario_static.add(self.win_text)
        self.all_sprites.add(self.win_text)

        self.win = True
        #self.play = False
        #self.g.currentScene = self.g.menuInicial

    def close(self):
        self.client.desconnect()
        self.server.close_server()  