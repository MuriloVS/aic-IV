from util.config import *


class Menu():
    def __init__(self, game):
        self.game = game
        self.font_name = pg.font.get_default_font()
        self.run_display = True
        self.mid_w, self.mid_h = SCREENWIDTH / 2, SCREENHEIGHT / 2
        self.cursor_rect = pg.Rect(0, 0, 20, 20)
        self.offset = - 100

    def draw_cursor(self):
        self.game.draw_text('*', 15, self.cursor_rect.x, self.cursor_rect.y)

    def blit_screen(self):
        self.game.window.blit(self.game.window, (0, 0))
        pg.display.update()        