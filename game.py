import pygame as pg
from pathlib import Path
from math import ceil

from scenes.menu_inicial import MenuInicial
from scenes.maze import Maze
from sprites.player import Player

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

        self.player1.collides = pg.sprite.spritecollide(self.player1, self.walls, False)

    def draw(self):
        self.window.fill(WHITE)

        # desenha todos os objetos na tela
        self.walls.draw(self.window)
        self.players.draw(self.window)
        # self.window.blit((self.player1.image), (self.player1.rect)) # não necessário

    def load_scene(self, scene=MENU_PRINCIPAL, **kwargs):
        self.scene = scene
        self.walls.empty()
        self.players.empty()

        if self.scene == MENU_PRINCIPAL:
            pass

        elif self.scene == LOBBY:
            pass

        elif self.scene == MAZE:
            # recebendo parâmetros do labirinto
            level = kwargs.get('level')
            numPlayers = kwargs.get('numeroPlayers')

            # criando o labirinto
            self.maze = Maze(level, numPlayers)
            self.maze.build()
            self.maze.build_walls()
            #x, y = self.maze.get_player_position()

            self.player1 = Player(SCREENWIDTH/2, SCREENHEIGHT/2)
            #self.player2 = Player(self, MIDSCREEN_X, MIDSCREEN_Y, RED)

            # adicionando sprites aos grupos
            for wall in self.maze.walls:
                self.walls.add(wall)
            self.players.add(self.player1)

            self.play_music()

        elif self.scene == PAUSE:
            pass

        elif self.scene == GAME_OVER:
            pass

    def move_camera(self):
        # ao atingir os limites inferiores e superiores
        # a posição dos objetos se reajusta

        # controle da câmera em y
        move = ceil(abs(self.player1.vel.y))
        if self.player1.rect.top <= SCREENHEIGHT * (1/3):
            self.player1.pos.y += move
            self.y += move
            for elem in self.walls:
                elem.rect.y += move
        elif self.player1.rect.bottom >= SCREENHEIGHT * (2/3):
            self.player1.pos.y -= move
            self.y -= move
            for elem in self.walls:
                elem.rect.y -= move

        # controle da câmera em x   
        move = ceil(abs(self.player1.vel.x))
        if self.player1.rect.left <= SCREENWIDTH * (1/3):
            self.player1.pos.x += move
            self.x += move
            for elem in self.walls:
                elem.rect.x += move

        elif self.player1.rect.right >= SCREENWIDTH * (2/3):
            self.player1.pos.x -= move
            self.x -= move
            for elem in self.walls:
                elem.rect.x -= move

    def play_music(self):
        pass
        # podemos passar um parâmetro no método para quando tivermos outras músicas (intro, gameplay)
        # path = Path('media', 'music', 'music_intro.wav')
        # self.intro_music = pg.mixer.Sound(path)
        # self.intro_music.set_volume(0.15)
        # self.intro_music.play(loops=-1)
