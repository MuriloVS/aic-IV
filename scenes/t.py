import pygame_menu
import pygame

pygame.init()
surface = pygame.display.set_mode()
def set_difficulty(value, difficulty):
    # Do the job here !
    pass

def start_the_game():
    # Do the job here !
    pass

menu = pygame_menu.Menu("MENU", 400, 300, 
                       )
menu.set_absolute_position()
menu.add.text_input('Name :', default='John Doe', font=pygame_menu.font.FONT_COMIC_NEUE)
menu.add.selector('Difficulty :', [('Hard', 1), ('Easy', 2)], onchange=set_difficulty)
menu.add.button('Play', start_the_game)
menu.add.button('Quit', pygame_menu.events.EXIT)

menu.mainloop(surface)

