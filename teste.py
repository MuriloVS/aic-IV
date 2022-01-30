import imp
from game import Game
from scenes.maze import Maze


if __name__ == '__main__':

    game = Game()
    m = Maze(game)
    m._build(init=(0,0))
    #m.print_maze()
