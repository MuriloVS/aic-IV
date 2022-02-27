from threading import Thread
import pygame as pg
import time

from scenes.game_singleplayer import GameSingleplayer
from sprites.player_online import PlayerOnline
from sprites.player_guest import PlayerGuest
from connection.client import Client
from util.tools import generate_walls_sprites_group
from config import *

vector = pg.math.Vector2


class GameMultiplayerGuest(GameSingleplayer):

    def __init__(self, game, window: pg.display):
        super().__init__(game, window)    

    def load(self):
        # carregano música
        self.music = self.get_sound() 

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
        self.player = PlayerOnline(self, self.client)

        self.music.play()

    def update_maze(self, maze_list=None):
        if maze_list:
            walls = generate_walls_sprites_group(maze_list)
        else:
            walls = generate_walls_sprites_group(self.maze_list)
        
        # adicionando sprites aos grupos
        for wall in walls:
            self.walls.add(wall)
            self.scenario_dinamic.add(wall)
            self.all_sprites.add(wall)


    def create_guest(self, data):
        print(data)
        guest = GameMultiplayerGuest(self, self.window,) # continuar aqui

    def close(self):
        self.client.desconnect()

