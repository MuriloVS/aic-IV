from email import message
from threading import Thread
import pygame as pg
import time

from scenes.game_singleplayer import GameSingleplayer
from sprites.player_online import PlayerOnline
from sprites.player_guest import PlayerGuest
from sprites.text import Text
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

        # criação do player atual
        self.player = PlayerOnline(self, self.client)

        self.music.play()

        time.sleep(2)

    def update_maze(self, maze_list=None):
        if maze_list:
            walls = generate_walls_sprites_group(maze_list)
        else:
            pass
            # walls = generate_walls_sprites_group()
        
        # adicionando sprites aos grupos
        for wall in walls:
            self.walls.add(wall)
            self.scenario_dinamic.add(wall)
            self.all_sprites.add(wall)

    def maze_complete(self):
        if self.win == False:
            message = {'id': 'win', 'data': {
                                       'player_id': self.client.id}
            }
            self.client.send_message(message)
            time.sleep(.1)

    def winner(self):
        # mensagem de vitória
        msg = 'VOCÊ GANHOU!'
        self.win_text = Text(msg, 40, MIDSCREEN_X, MIDSCREEN_Y, color=BLACK, background=WHITE)

        self.scenario_static.add(self.win_text)
        self.all_sprites.add(self.win_text)

        self.win = True
        #self.play = False
        #self.g.currentScene = self.g.menuInicial

    def loser(self):
        # mensagem de vitória
        msg = 'VOCÊ PERDEU!'
        self.win_text = Text(msg, 40, MIDSCREEN_X, MIDSCREEN_Y, color=BLACK, background=WHITE)

        self.scenario_static.add(self.win_text)
        self.all_sprites.add(self.win_text)

        self.win = True
        #self.play = False
        #self.g.currentScene = self.g.menuInicial

    def create_guest(self, data):
        guest = PlayerGuest(self, data)
        self.players.add(guest)
        self.scenario_dinamic.add(guest)
        self.all_sprites.add(guest)

    def close(self):
        message = {'id': 'desconnect'}
        self.client.send_message(message)
        self.client.desconnect()

