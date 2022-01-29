# Arquivo de configuração
import os
ROOT = os.getcwd()

# janela
TITLE = 'A Maze'
FPS = 30
WIDTH = 400
HEIGHT = 400

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
FLOOR = (HEIGHT * 7) // 8
FLOOR_OBJ = FLOOR + 10
MIDSCREEN_Y = HEIGHT / 2
MIDSCREEN_X = WIDTH / 2
QUARTERSCREEN_X = WIDTH / 4
QUARTERSCREEN_Y = HEIGHT / 4

# define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
PURPLE = (255, 0, 255)
EBONY = (33, 36, 31)
