import pygame
network import Network
from player import Player

# tamanho da tela
width = 500
height = 500

# variável que controle a tela
window = pygame.display.set_mode((width, height))
# título da tela
pygame.display.set_caption("Cliente")


def redraw_window(window, p1, p2):
    window.fill((255, 255, 255))
    p1.draw(window)
    p2.draw(window)
    pygame.display.update()


def main():
    run = True
    n = Network()
    p1 = n.get_p()

    clock = pygame.time.Clock()

    while run:
        # 60 fps
        clock.tick(60)
        p2 = n.send(p1)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

        p1.move()
        redraw_window(window, p1, p2)


if __name__ == '__main__':
    main()
