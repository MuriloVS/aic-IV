import pygame as pg

from scenes.menu import Menu
from util.config import *

class MenuInicial(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = "Start"
        self.startx, self.starty = SCREENWIDTH * (3/4), SCREENHEIGHT * (3/4) + 30
        self.optionsx, self.optionsy = SCREENWIDTH * (3/4), SCREENHEIGHT * (3/4) + 50
        self.creditsx, self.creditsy = SCREENWIDTH * (3/4), SCREENHEIGHT * (3/4) + 70
        self.cursor_rect.midtop = (self.startx + self.offset, self.starty)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.check_events()
            self.game.window.fill(BLACK)
            self.game.draw_text("A Maze'n Game", 30, SCREENWIDTH * (3/4), SCREENHEIGHT * (3/4) - 20)
            self.game.draw_text("Start Game", 20, self.startx, self.starty)
            self.game.draw_text("Options", 20, self.optionsx, self.optionsy)
            self.game.draw_text("Credits", 20, self.creditsx, self.creditsy)
            self.draw_cursor()
            self.blit_screen()

    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.run_display = False
                
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_RETURN:
                    self.check_input()
                if event.key == pg.K_DOWN:
                    self.move_cursor('down')
                if event.key == pg.K_UP:
                    self.move_cursor('up')

    def check_input(self):
        if self.state == 'Start':
            self.game.load_scene(MAZE)
        elif self.state == 'Options':
            self.game.curr_menu = self.game.options
        elif self.state == 'Credits':
            self.game.curr_menu = self.game.credits

        self.run_display = False

    def move_cursor(self, key):
        if key == "down":
            if self.state == 'Start':
                self.cursor_rect.midtop = (self.optionsx + self.offset, self.optionsy)
                self.state = 'Options'
            elif self.state == 'Options':
                self.cursor_rect.midtop = (self.creditsx + self.offset, self.creditsy)
                self.state = 'Credits'
            elif self.state == 'Credits':
                self.cursor_rect.midtop = (self.startx + self.offset, self.starty)
                self.state = 'Start'
   
        elif key == "up":
            if self.state == 'Start':
                self.cursor_rect.midtop = (self.creditsx + self.offset, self.creditsy)
                self.state = 'Credits'
            elif self.state == 'Options':
                self.cursor_rect.midtop = (self.startx + self.offset, self.starty)
                self.state = 'Start'
            elif self.state == 'Credits':
                self.cursor_rect.midtop = (self.optionsx + self.offset, self.optionsy)
                self.state = 'Options'