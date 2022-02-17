from threading import Thread
import pygame as pg
import time

from scenes.game import *
from sprites.player_online import PlayerOnline
from sprites.player_guest import PlayerGuest
from connection.client import Client
from util.tools import generate_walls_sprites_group

vector = pg.math.Vector2


class GameMultiplayerGuest(Game):

    def __init__(self, window: pg.display):
        super().__init__(window)

    def loop(self):
        super().loop()
        self.client.desconnect()               

    def update(self):
        self.walls.update()
        self.players.update()
        self.player.update(self.walls)

    def draw(self):
        self.window.fill((150, 200, 145))

        # desenha todos os objetos na tela
        self.walls.draw(self.window)

        # self.players.draw(self.window)
        self.window.blit((self.player.image), (self.player.rect))  # não necessário

    def load(self):
        self.walls.empty()
        self.players.empty()

        # criando cliente para conectar no servidor
        self.client = Client(self, LOCALHOST, PORT)
        self.TClient = Thread(target=self.client.receive_message)
        self.TClient.start()
        time.sleep(1)

        # geração das posições dos player

        # criação dos players convidados
        #self.player2 = PlayerGuest(MIDSCREEN_X, MIDSCREEN_Y) #continuar aqui
        # self.players.add(self.player)

        # criação do player atual
        self.player = PlayerOnline(self, self.client, MIDSCREEN_X, MIDSCREEN_Y)

        self.play_music()

    def update_maze(self, maze_list=None):
        if maze_list:
            walls = generate_walls_sprites_group(maze_list)
        else:
            walls = generate_walls_sprites_group(self.maze_list)
        
        # adicionando sprites aos grupos
        self.walls.empty()
        for wall in walls:
            self.walls.add(wall)


