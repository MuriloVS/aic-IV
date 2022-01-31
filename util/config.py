# Arquivo de configuração
import pygame as pg
import time

# janela
TITLE = 'A Maze'
FPS = 30

# tamanho da tela inteira
pg.init() 
screen = pg.display.set_mode() 
SCREENWIDTH, SCREENHEIGHT = screen.get_size() 
pg.display.quit() 

# player property
PLAYER_ACC = 1
PLAYER_FRICTION = -0.2

# scene's name
MENU_PRINCIPAL = 0
LOBBY = 1
MAZE = 2
GAME_OVER = 3
PAUSE = 4

# measures
FLOOR = (SCREENHEIGHT * 7) // 8
FLOOR_OBJ = FLOOR + 10
MIDSCREEN_Y = SCREENHEIGHT / 2
MIDSCREEN_X = SCREENWIDTH / 2
QUARTERSCREEN_X = SCREENWIDTH / 4
QUARTERSCREEN_Y = SCREENHEIGHT / 4

# define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
PURPLE = (255, 0, 255)
EBONY = (33, 36, 31)
