import pickle
import socket
import pygame as pg
from pathlib import Path
from math import ceil

from scenes.menu_inicial import MenuInicial
from util.tools import build_walls
from sprites.player import Player
from sprites.wall import Wall

from util.config import *


class Game():

    def __init__(self, window: pg.display):

        self.window = window
        self.rect = self.window.get_rect()
        self.rect.center = (SCREENWIDTH/2, SCREENHEIGHT/2)

        pg.display.set_caption(TITLE)
        # pg.mixer.init()

        self.clock = pg.time.Clock()

        self.players = pg.sprite.Group()
        self.walls = pg.sprite.Group()

        # bússola para controlar posição dos objetos
        self.x = 0
        self.y = 0

        self.scene = MENU_PRINCIPAL
        self.walls_list = []

    def loop(self):

        self.run = True
        while self.run:
            self.clock.tick(FPS)

            self.event_check()
            self.move_camera()
            self.update()
            self.draw()

            pg.display.flip()

        pg.quit()

    def event_check(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.run = False

    def update(self):
        self.walls.update()
        self.players.update()

        self.player.collides = pg.sprite.spritecollide(
            self.player, self.walls, False)

    def draw(self):
        self.window.fill(WHITE)

        # desenha todos os objetos na tela
        self.walls.draw(self.window)
        self.players.draw(self.window)
        # self.window.blit((self.player.image), (self.player.rect)) # não necessário

    def load_scene(self, scene=MENU_PRINCIPAL, **kwargs):
        self.scene = scene
        self.walls.empty()
        self.players.empty()

        if self.scene == MENU_PRINCIPAL:
            pass

        elif self.scene == LOBBY:
            pass

        elif self.scene == MAZE:
            # estabelecendo a conexão com o servidor
            self.game_socket = socket.socket(
                socket.AF_INET, socket.SOCK_STREAM)
            self.game_socket.connect((LOCALHOST, PORT))

            # solicitando o número do jogador ao servidor
            message = {'msg_id': 'player'}
            self.game_socket.send(pickle.dumps(message))
            player = pickle.loads(self.game_socket.recv(2048))

            # # solicitando o labirinto ao servidor
            message = {'msg_id': 'load_maze'}
            self.game_socket.send(pickle.dumps(message))
            self.maze_list = pickle.loads(self.game_socket.recv(4096 * 5))
            self.maze = build_walls(self.maze_list)

            if player == 0:
                self.player = Player(MIDSCREEN_X, MIDSCREEN_Y)
            else:
                self.player = Player(QUARTERSCREEN_X, QUARTERSCREEN_Y)

            self.players.add(self.player)

            # adicionando sprites aos grupos
            for wall in self.maze:
                self.walls.add(wall)

            # finalizando a conexão com o servidor
            self.game_socket.close()

            # self.play_music()

        elif self.scene == PAUSE:
            pass

        elif self.scene == GAME_OVER:
            pass

    def move_camera(self):
        # ao atingir os limites inferiores e superiores
        # a posição dos objetos se reajusta

        # controle da câmera em y
        move = ceil(abs(self.player.vel.y))
        if self.player.rect.top <= SCREENHEIGHT * (1/3):
            self.player.pos.y += move
            self.y += move
            for elem in self.walls:
                elem.rect.y += move
        elif self.player.rect.bottom >= SCREENHEIGHT * (2/3):
            self.player.pos.y -= move
            self.y -= move
            for elem in self.walls:
                elem.rect.y -= move

        # controle da câmera em x
        move = ceil(abs(self.player.vel.x))
        if self.player.rect.left <= SCREENWIDTH * (1/3):
            self.player.pos.x += move
            self.x += move
            for elem in self.walls:
                elem.rect.x += move

        elif self.player.rect.right >= SCREENWIDTH * (2/3):
            self.player.pos.x -= move
            self.x -= move
            for elem in self.walls:
                elem.rect.x -= move

    def play_music(self):
        # podemos passar um parâmetro no método para quando tivermos outras músicas (intro, gameplay)
        path = Path('media', 'music', 'music_intro.wav')
        self.intro_music = pg.mixer.Sound(path)
        self.intro_music.set_volume(0.15)
        self.intro_music.play(loops=-1)
