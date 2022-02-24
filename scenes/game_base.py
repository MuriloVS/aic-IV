from abc import abstractclassmethod
import pygame as pg
from pathlib import Path
from math import ceil

from config import *

vector = pg.math.Vector2


class GameBase:

    def __init__(self, game, window: pg.display):

        self.g = game
        self.window = window

        self.clock = pg.time.Clock()
        self.music_file = None

        self.players = pg.sprite.Group()
        self.walls = pg.sprite.Group()
        self.scenario_dinamic = pg.sprite.Group()
        self.scenario_static = pg.sprite.Group()
        self.all_sprites = pg.sprite.Group()

        # bússola para controlar posição dos objetos
        self.compass = vector(0, 0)

        self.actions = {"left": False, "right": False, "up" : False, "down" : False, "action1" : False, "action2" : False, "start" : False}

        self.win = False

    def loop(self):
        self.play = True
        while self.play:
            self.clock.tick(FPS)

            self.event_check()
            self.update()
            self.draw()
            pg.display.flip()
        self.close()

    @abstractclassmethod
    def load(self):
        pass

    @abstractclassmethod
    def winner(self):
        pass

    @abstractclassmethod
    def close(self):
        pass

    def event_check(self):
        global SCREENWIDTH, SCREENHEIGHT
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.play = False
                self.g.run = False
                
            if event.type == pg.VIDEORESIZE:
                SCREENWIDTH = event.w
                SCREENHEIGHT = event.h
                self.window = pg.display.set_mode((event.w, event.h), pg.RESIZABLE)   

            if event.type == pg.KEYDOWN:
            
                if event.key == pg.K_ESCAPE:
                    self.reset_scene()
                    
                if event.key == pg.K_LEFT:
                    self.actions['left'] = True
                if event.key == pg.K_RIGHT:
                    self.actions['right'] = True
                if event.key == pg.K_UP:
                    self.actions['up'] = True
                if event.key == pg.K_DOWN:
                    self.actions['down'] = True
                if event.key == pg.K_SPACE:
                    self.actions['action1'] = True
                if event.key == pg.K_LCTRL:
                    self.actions['action2'] = True    
                if event.key == pg.K_RETURN:
                    self.actions['start'] = True  

            if event.type == pg.KEYUP:
                if event.key == pg.K_LEFT:
                    self.actions['left'] = False
                if event.key == pg.K_RIGHT:
                    self.actions['right'] = False
                if event.key == pg.K_UP:
                    self.actions['up'] = False
                if event.key == pg.K_DOWN:
                    self.actions['down'] = False
                if event.key == pg.K_SPACE:
                    self.actions['action1'] = False
                if event.key == pg.K_LCTRL:
                    self.actions['action2'] = False
                if event.key == pg.K_RETURN:
                    self.actions['start'] = False                 

    def update(self):
        self._move_camera()
        
        # verifica se jogador completou o labirinto
        win = pg.sprite.collide_rect(self.player, self.finish)
        if win:
            self.winner()

        self.player.update(self.walls)

    def draw(self):
        # cor de fundo
        self.window.fill((150, 200, 145))

        # desenha todos os objetos na tela
        self.scenario_dinamic.draw(self.window)
        self.players.draw(self.window)
        self.window.blit(self.player.image, self.player.rect)
        self.scenario_static.draw(self.window)

    def reset_scene(self):
        self.music.stop()

        self.play = False
        self.win = False
        self.g.currentScene = self.g.menuInicial
        self.compass = vector(0, 0)

        for sprite in self.all_sprites:
            sprite.kill()

    def get_sound(self, music='music_intro.wav', volume=0.15) -> pg.mixer.Sound:
        path = Path('media', 'sounds', music)
        music = pg.mixer.Sound(path)
        music.set_volume(volume)
        return music

    def set_camera_position(self, pos_x, pos_y):
        self.compass.x -= pos_x - MIDSCREEN_X
        self.compass.y -= pos_y - MIDSCREEN_Y
        for player in self.players:
            player.rect.x += self.compass.x      
            player.rect.y += self.compass.y
        for elem in self.scenario_dinamic:
            elem.rect.x += self.compass.x
            elem.rect.y += self.compass.y

    def _move_camera(self):
        # ao atingir os limites inferiores e superiores
        # a posição dos objetos se reajusta

        # controle da câmera em y
        move = ceil(abs(self.player.vel.y))
        if self.player.rect.top <= SCREENHEIGHT * (1/3):
            self.player.pos.y += move
            self.compass.y += move
            for player in self.players:
                player.rect.y += move
            for elem in self.scenario_dinamic:
                elem.rect.y += move
        elif self.player.rect.bottom >= SCREENHEIGHT * (2/3):
            self.player.pos.y -= move
            self.compass.y -= move
            for player in self.players:
                player.rect.y -= move            
            for elem in self.scenario_dinamic:
                elem.rect.y -= move

        # controle da câmera em x
        move = ceil(abs(self.player.vel.x))
        if self.player.rect.left <= SCREENWIDTH * (1/3):
            self.player.pos.x += move
            self.compass.x += move
            for player in self.players:
                player.rect.x += move            
            for elem in self.scenario_dinamic:
                elem.rect.x += move

        elif self.player.rect.right >= SCREENWIDTH * (2/3):
            self.player.pos.x -= move
            self.compass.x -= move
            for player in self.players:
                player.rect.x -= move                 
            for elem in self.scenario_dinamic:
                elem.rect.x -= move
