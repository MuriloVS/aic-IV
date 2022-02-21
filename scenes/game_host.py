from threading import Thread
import pygame as pg
import time

from scenes.game_singleplayer import GameSingleplayer
from sprites.player_online import PlayerOnline
from sprites.player_guest import PlayerGuest
from connection.server import Server
from connection.client import Client
from util.maze import Maze
from util.config import *

vector = pg.math.Vector2


class GameMultiplayerHost(GameSingleplayer):

    def __init__(self, game, window: pg.display):
        super().__init__(game, window)

    def loop(self):
        super().loop()
        self.client.desconnect()
        self.server.close_server()              
        self.g.currentScene = self.g.menuInicial

    def update(self):
        self.walls.update()
        self.players.update()
        self.player.update(self.walls)

    def draw(self):
        self.window.fill((150, 200, 145))

        # desenha todos os objetos na tela
        self.walls.draw(self.window)

        self.players.draw(self.window)
        self.window.blit((self.player.image), (self.player.rect))

    def load(self, scene=MENU_PRINCIPAL):
        self.scene = scene
        self.walls.empty()
        self.players.empty()

        # criando servidor multiplayer
        self.server = Server()
        self.TServer = Thread(target=self.server.subscribe)
        self.TServer.start()

        # criando cliente para conectar no servidor
        self.client = Client(self, LOCALHOST, PORT)
        self.TClient = Thread(target=self.client.receive_message)
        self.TClient.start()
        time.sleep(1)

        # lobby

        # cria o labirinto e envia ao servidor
        self.maze = Maze(level=2, numPlayers=2)
        self.maze.build()
        self.maze.build_walls_sprites()
        
        # adicionando sprites do lab ao seu grupo
        for wall in self.maze.walls:
            self.walls.add(wall)
        
        # recebendo posição inicial do player
        x, y = self.maze.get_player_position()

        # enviando lab ao servidor
        message = {'id': 'load_maze', 'data': {
                                                'list': self.maze.get_walls_list(),
                                                'position': (x, y)
                                              }
        }      
        self.client.send_message(message)

        # geração dos jogadores convidados
        self.player2 = PlayerGuest(self, 2)
        self.players.add(self.player2)

        # gerações do player atual
        self.player = PlayerOnline(self, self.client)

        self.set_camera_position(x, y)

        self.play_music()