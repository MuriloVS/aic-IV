import pygame as pg

from sprites.player import Player
from util.config import *

vector = pg.math.Vector2


class PlayerOnline(Player):
    def __init__(self, game, client, pos_x, pos_y):
        super().__init__(game, pos_x, pos_y)

        self.client = client

    def update(self, walls):
        # armazena posição inicial
        pos_inicial = vector(self.pos.x, self.pos.y)

        # atualiza posição
        super().update(walls)

        # verifica se a posição foi alterada para enviar ao servidor
        if self.pos != pos_inicial:
            self.send_position()

    def send_position(self):
        message = {'id': 'player_position',
                   'data': {
                       'player_id': self.client.id,
                       'x': self.pos.x - self.game.compass.x ,
                       'y': self.pos.y - self.game.compass.y
                           }
                   }

        self.client.send_message(message)
