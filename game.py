import pygame as pg

from scenes.menu_inicial import MenuInicial
from scenes.maze import Maze
from sprites.player import Player

from util.config import *


class Game():

    def __init__(self, window:pg.display):

        self.window = window     
        self.rect = self.window.get_rect()
        self.rect.center = (SCREENWIDTH, SCREENHEIGHT)

        pg.display.set_caption(TITLE)
        # pg.mixer.init()

        self.clock = pg.time.Clock()

        self.players = pg.sprite.Group()
        self.walls = pg.sprite.Group()

        self.scene = MENU_PRINCIPAL

    def loop(self):

        self.run = True
        while self.run:
            self.clock.tick(FPS)

            self.event_check()
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

    def draw(self):
        self.window.fill(BLACK)

        # desenha todos os objetos na tela
        self.walls.draw(self.window)
        self.players.draw(self.window)
        #self.window.blit((self.player1.image), (self.player1.rect)) # não necessário

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

        elif self.scene == PAUSE:
            pass

        elif self.scene == GAME_OVER:
            pass     