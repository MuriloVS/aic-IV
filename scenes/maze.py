import pygame as pg
from pathlib import Path
import random

from sprites.wall import Wall
from util.config import *


class Spot:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.neighbors = []
        self.visited = False
        self.walls = [True, True, True, True]

    def add_neighbors(self, grid, rows, cols):
        if self.x > 0:
            self.neighbors.append(grid[self.x - 1][self.y])
        if self.y > 0:
            self.neighbors.append(grid[self.x][self.y - 1])
        if self.x < rows - 1:
            self.neighbors.append(grid[self.x + 1][self.y])
        if self.y < cols - 1:
            self.neighbors.append(grid[self.x][self.y + 1])


class Maze():
    def __init__(self, level=10, dimension=False, numPlayers=1):

        self.level = level
        self.numPlayers = numPlayers

        if not dimension:
            self.rows = level*5
            self.cols = level*5
        else:
            self.rows = dimension[0]
            self.cols = dimension[1]
        
        self.completed = False
        self.walls = []
        self.grid = [[Spot(i, j) for j in range(self.cols)] for i in range(self.rows)]

        for i in range(self.rows):
            for j in range(self.cols):
                self.grid[i][j].add_neighbors(self.grid, self.rows, self.cols)

    def print_maze(self):
        for i in range(self.rows):
            for j in range(self.cols):
                print(f'{i} {j} {self.grid[i][j].walls}')

    def build(self, init=(0,0)):

        if not self.completed:

            x, y = init
            current = self.grid[x][y]
            self.visited = [current]

            while not self.completed:
                self.grid[current.x][current.y].visited = True
                got_new = False
                temp = 10

                while not got_new and not self.completed:
                    r = random.randint(0, len(current.neighbors)-1)
                    Tempcurrent = current.neighbors[r]
                    if not Tempcurrent.visited:
                        self.visited.append(current)
                        current = Tempcurrent
                        got_new = True
                    if temp == 0:
                        temp = 10
                        if len(self.visited) == 0:
                            self.completed = True
                            break
                        else:
                            current = self.visited.pop()
                    temp = temp - 1

                if not self.completed:
                    self._break_walls(current, self.visited[len(self.visited)-1])

                current.visited = True  

    def _break_walls(self, a, b):
        if a.y == b.y and a.x > b.x:
            self.grid[b.x][b.y].walls[1] = False
            self.grid[a.x][a.y].walls[3] = False
        if a.y == b.y and a.x < b.x:
            self.grid[a.x][a.y].walls[1] = False
            self.grid[b.x][b.y].walls[3] = False
        if a.x == b.x and a.y < b.y:
            self.grid[b.x][b.y].walls[0] = False
            self.grid[a.x][a.y].walls[2] = False
        if a.x == b.x and a.y > b.y:
            self.grid[a.x][a.y].walls[0] = False
            self.grid[b.x][b.y].walls[2] = False

    def build_walls(self):
        self.dist_x = SCREENWIDTH/self.cols
        self.dist_y = SCREENWIDTH/self.rows
        mazeBlock = [self.dist_x, self.dist_y]


        for i in range(self.cols):
            for j in range(self.rows):
                if self.grid[i][j].walls[0] == True:
                    position = [i*self.dist_x, j*self.dist_y]
                    w = Wall(pos=position, size=mazeBlock, orientacao=0)
                    self.walls.append(w)
                if self.grid[i][j].walls[1] == True:
                    position = [i*self.dist_x+self.dist_x, j*self.dist_y]
                    w = Wall(pos=position, size=mazeBlock, orientacao=1)
                    self.walls.append(w)
                if self.grid[i][j].walls[2] == True:
                    position = [i*self.dist_x+self.dist_x, j*self.dist_y+self.dist_y]
                    w = Wall(pos=position, size=mazeBlock, orientacao=0)
                    self.walls.append(w)
                if self.grid[i][j].walls[3] == True:
                    position = [i*self.dist_x+self.dist_x, j*self.dist_y+self.dist_y]
                    w = Wall(pos=position, size=mazeBlock, orientacao=1)
                    self.walls.append(w)

                # if self.walls[0]:
                #     pygame.draw.line(screen, color, [self.x*hr, self.y*wr],       [self.x*hr+hr, self.y*wr], 2)
                # if self.walls[1]:
                #     pygame.draw.line(screen, color, [self.x*hr+hr, self.y*wr],    [self.x*hr+hr, self.y*wr + wr], 2)
                # if self.walls[2]:
                #     pygame.draw.line(screen, color, [self.x*hr+hr, self.y*wr+wr], [self.x*hr, self.y*wr+wr], 2)
                # if self.walls[3]:
                #     pygame.draw.line(screen, color, [self.x*hr, self.y*wr+wr],    [self.x*hr, self.y*wr], 2)

                                                                   
    #pensar no online