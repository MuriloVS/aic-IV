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
    def __init__(self, level=10, numPlayers=1):

        self.level = level
        self.numPlayers = numPlayers

        self.rows = level*5
        self.cols = level*5
        self.completed = False

        self.walls = []

    def print_maze(self):
        for i in range(self.cols):
            for j in range(self.rows):
                print(f'{i} {j} {self.grid[i][j].walls}')

    def build(self, init=(0,0)):

        self.grid = [[Spot(i, j) for j in range(self.cols)] for i in range(self.rows)]

        for i in range(self.rows):
            for j in range(self.cols):
                self.grid[i][j].add_neighbors(self.grid, self.rows, self.cols)

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

            return True

        else:
            return False      

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

    # def _build_walls(self):
    #     for i in range(self.cols):
    #         for j in range(self.rows):
    #             if self.grid[i][j].walls[0] == True:
    #                 w = Wall(self.game, i, j, 'h', 'n')
    #                 self.walls.add(w)
    #             if self.grid[i][j].walls[1] == True:
    #                 w = Wall(self.game, i, j, 'v', 'l')
    #                 self.walls.add(w)
    #             if self.grid[i][j].walls[2] == True:
    #                 w = Wall(self.game, i, j, 'h', 's')
    #                 self.walls.add(w)
    #             if self.grid[i][j].walls[3] == True:
    #                 w = Wall(self.game, i, j, 'v', 'o')
    #                 self.walls.add(w)

                                                                   
    #pensar no online