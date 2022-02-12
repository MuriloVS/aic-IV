import pickle
import socket
from threading import Thread
import pygame as pg
from pathlib import Path
from math import ceil

from connection.server import Server
from connection.client import Client
from scenes.menu_inicial import MenuInicial
# from scenes.options import OptionsMenu
# from scenes.credits import CreditsMenu
from sprites.player_online import PlayerOnline
from sprites.player_guest import PlayerGuest
from util.tools import build_walls, generate_maze
from util.maze import Maze
from util.config import *

vector = pg.math.Vector2

class Game():

    def __init__(self, window: pg.display):

        self.window = window
        self.rect = self.window.get_rect()
        self.rect.center = (SCREENWIDTH/2, SCREENHEIGHT/2)

        pg.display.set_caption(TITLE)

        self.clock = pg.time.Clock()

        self.players = pg.sprite.Group()
        self.walls = pg.sprite.Group()

        # bússola para controlar posição dos objetos
        self.compass = vector(0, 0)

        self.walls_list = []

        self.menu_incial = MenuInicial(self)
        # self.options = OptionsMenu(self)
        # self.credits = CreditsMenu(self)
        self.lobby = ''
        self.carregamento = ''

        self.run = True
        self.play = False

    def loop(self):
        self.play = True
        while self.play:
            self.clock.tick(FPS)

            self.event_check()
            self.update()
            self.move_camera()
            self.draw()

            pg.display.flip()

        pg.quit()
        self.client.desconnect()
        self.server.close_server()

    def event_check(self):
        global SCREENWIDTH, SCREENHEIGHT
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.run = False
                self.play = False
            if event.type == pg.VIDEORESIZE:
                SCREENWIDTH = event.w
                SCREENHEIGHT = event.h
                self.window = pg.display.set_mode((event.w, event.h), pg.RESIZABLE)                 

    def update(self):
        self.walls.update()

        self.players.update(self.walls)

    def draw(self):
        self.window.fill((150, 200, 145))

        # desenha todos os objetos na tela
        self.walls.draw(self.window)

        # self.players.draw(self.window)
        self.window.blit((self.player.image),
                         (self.player.rect))  # não necessário

    def load_scene(self, scene=MENU_PRINCIPAL, **kwargs):
        self.scene = scene
        self.walls.empty()
        self.players.empty()

        if self.scene == MENU_PRINCIPAL:
            self.menu_incial.display_menu()

        elif self.scene == LOBBY:
            pass

        elif self.scene == MAZE:
            # criando servidor multiplayer
            self.server = Server()
            self.TServer = Thread(target=self.server.subscribe)
            self.TServer.start()

            # criando cliente para conectar no servidor
            self.client = Client(LOCALHOST, PORT)
            self.TClient = Thread(target=self.client.receive_message)
            self.TClient.start()
            print('4186456')
            # solicitando o número do jogador ao servidor
            message = {'msg_id': 'player'}
            self.client.send_message(message)
            print('dskioapdi')
            # envia o labirinto ao servidor
            self.maze_list = generate_maze()
            self.maze = build_walls(self.maze_list)
            message = {'msg_id': 'load_maze'}

            # if player == 0:
            #     self.player = Player(MIDSCREEN_X, MIDSCREEN_Y)
            # else:
            #     self.player = Player(QUARTERSCREEN_X, QUARTERSCREEN_Y)
            self.player = PlayerOnline(MIDSCREEN_X, MIDSCREEN_Y, self.client)
            self.players.add(self.player)
            #self.player1 = Player(SCREENWIDTH/2+100, SCREENHEIGHT/2)
            #self.player2 = Player(self, MIDSCREEN_X, MIDSCREEN_Y, RED)

            # adicionando sprites aos grupos
            for wall in self.maze:
                self.walls.add(wall)

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
            self.compass.y += move
            for elem in self.walls:
                elem.rect.y += move
        elif self.player.rect.bottom >= SCREENHEIGHT * (2/3):
            self.player.pos.y -= move
            self.compass.y -= move
            for elem in self.walls:
                elem.rect.y -= move

        # controle da câmera em x
        move = ceil(abs(self.player.vel.x))
        if self.player.rect.left <= SCREENWIDTH * (1/3):
            self.player.pos.x += move
            self.compass.x += move
            for elem in self.walls:
                elem.rect.x += move

        elif self.player.rect.right >= SCREENWIDTH * (2/3):
            self.player.pos.x -= move
            self.compass.x -= move
            for elem in self.walls:
                elem.rect.x -= move

    def draw_text(self, text, size, x, y, font=pg.font.get_default_font()):
        font = pg.font.Font(font,size)
        text_surface = font.render(text, True, WHITE)
        text_rect = text_surface.get_rect()
        text_rect.center = (x,y)
        self.window.blit(text_surface,text_rect)

    def play_music(self):
        # podemos passar um parâmetro no método para quando tivermos outras músicas (intro, gameplay)
        path = Path('media', 'music', 'music_intro.wav')
        self.intro_music = pg.mixer.Sound(path)
        self.intro_music.set_volume(0.15)
        self.intro_music.play(loops=-1)
