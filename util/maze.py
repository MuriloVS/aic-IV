import random

from sprites.wall import Wall
from config import *


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
    def __init__(self, level=2, numPlayers=1):

        self.level = level
        self.numPlayers = numPlayers

        self.rows = self.level*6+1
        self.cols = self.level*6+1
        # self.rows = 3
        # self.cols = 3

        self.completed = False
        self.walls = []
        self.grid = [[Spot(i, j) for j in range(self.cols)]
                     for i in range(self.rows)]

        for i in range(self.rows):
            for j in range(self.cols):
                self.grid[i][j].add_neighbors(self.grid, self.rows, self.cols)

    def build(self, init=(0, 0)):

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
                    self._break_walls(
                        current, self.visited[len(self.visited)-1])

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

    def get_walls_list(self):
        walls_list = []

        for i in range(self.rows):
            walls_list.append([])
            for j in range(self.cols):
                walls_list[i].append(self.grid[i][j].walls)

        return walls_list        

    def build_walls_sprites(self):
        self.walls.clear()

        for i in range(len(self.grid[0])):
            for j in range(len(self.grid[1])):

                # parede superior
                if self.grid[i][j].walls[0] == True and j % 2 == 0:
                    pos = [i*SIZE + SIZE/2, j*SIZE]
                    w = Wall(pos=pos, size=SIZE, orientacao=0)
                    self.walls.append(w)

                # parede direita
                if self.grid[i][j].walls[1] == True and i % 2 == 0:
                    pos = [i*SIZE + SIZE, j*SIZE + SIZE/2]
                    w = Wall(pos=pos, size=SIZE, orientacao=1)
                    self.walls.append(w)

                # parede inferior
                if self.grid[i][j].walls[2] == True and j % 2 == 0:
                    pos = [i*SIZE + SIZE/2, j*SIZE+SIZE]
                    w = Wall(pos=pos, size=SIZE, orientacao=0)
                    self.walls.append(w)

                # parede esquerda
                if self.grid[i][j].walls[3] == True and i % 2 == 0:
                    pos = [i*SIZE, j*SIZE+SIZE/2]
                    w = Wall(pos=pos, size=SIZE, orientacao=1)
                    self.walls.append(w)

    def get_player_position(self):
        x = (self.rows * SIZE) - (0.5 * SIZE)
        y = (self.cols * SIZE) - (0.5 * SIZE)
        return x, y