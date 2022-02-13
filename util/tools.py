import pygame as pg

from util.maze import Maze
from sprites.wall import Wall
from util.config import FPS


def wait_for_key() -> bool:
    waiting = True
    while waiting:
        pg.clock.tick(FPS)
        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_RETURN:
                    return True

def generate_maze():
    maze = Maze()
    maze.build()
    maze_list = []

    for i in range(maze.rows):
        maze_list.append([])
        for j in range(maze.cols):
            maze_list[i].append(maze.grid[i][j].__dict__['walls'])

    return maze_list

def generate_walls_sprites(maze_list):

    size = 100
    walls_list = []

    for i in range(len(maze_list[0])):
        for j in range(len(maze_list[1])):

            # parede superior
            if maze_list[i][j][0] == True and j % 2 == 0:
                pos = [i*size + size/2, j*size]
                w = Wall(pos=pos, size=size, orientacao=0)
                walls_list.append(w)

            # parede direita
            if maze_list[i][j][1] == True and i % 2 == 0:
                pos = [i*size + size, j*size + size/2]
                w = Wall(pos=pos, size=size, orientacao=1)
                walls_list.append(w)

            # parede inferior
            if maze_list[i][j][2] == True and j % 2 == 0:
                pos = [i*size + size/2, j*size+size]
                w = Wall(pos=pos, size=size, orientacao=0)
                walls_list.append(w)

            # parede esquerda
            if maze_list[i][j][3] == True and i % 2 == 0:
                pos = [i*size, j*size+size/2]
                w = Wall(pos=pos, size=size, orientacao=1)
                walls_list.append(w)

    return walls_list
