import pygame as pg

# Arquivo de configuração

# janela
TITLE = 'A Maze'
FPS = 30

# conexão
LOCALHOST = '127.0.0.1'
PORT = 6789

# tamanho da tela
SCREENWIDTH = 1200
SCREENHEIGHT = 700

# player property
PLAYER_ACC = 2
PLAYER_FRICTION = -0.4

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

# conexão
LOCALHOST = '127.0.0.1'
PORT = 6789

