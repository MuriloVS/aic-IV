import pygame
from network import Network

# tamanho da tela
width = 500
height = 500

# variável que controle a tela
window = pygame.display.set_mode((width, height))
# título da tela
pygame.display.set_caption("Cliente")

# controle dos clientes
clientNumber = 0


class Player():
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color

        self.rect = (x, y, width, height)
        self.velocity = 3

    def draw(self, window):
        pygame.draw.rect(window, self.color, self.rect)

    def move(self):
        keys = pygame.key.get_pressed()

        # movimentação - ifs separados para movimentos combinados (diagonal)
        if keys[pygame.K_LEFT]:
            self.x -= self.velocity
        if keys[pygame.K_RIGHT]:
            self.x += self.velocity
        if keys[pygame.K_UP]:
            self.y -= self.velocity
        if keys[pygame.K_DOWN]:
            self.y += self.velocity

        # atualizando a posição na tela
        self.update()

    def update(self):
        self.rect = (self.x, self.y, self.width, self.height)


def read_pos(data):
    # recebe a posição na tela como uma string (ou lista?) e retorna uma tupla
    data = data.split(',')
    return int(data[0]), int(data[1])


def set_pos(data):
    return str(data[0]) + ',' + str(data[1])


def redraw_window(window, p1, p2):
    window.fill((255, 255, 255))
    p1.draw(window)
    p2.draw(window)
    pygame.display.update()


def main():
    run = True
    n = Network()

    start_pos = read_pos(n.get_pos())
    p1 = Player(start_pos[0], start_pos[1], 50, 50, (0, 255, 0))
    p2 = Player(0, 0, 50, 50, (0, 0, 255))

    clock = pygame.time.Clock()

    while run:
        # 60 fps
        clock.tick(60)

        # atualizando as posições dos jogadores
        # p1_pos = read_pos(n.send(set_pos(p1.x, p1.y)))
        p2_pos = read_pos(n.send(set_pos((p1.x, p1.y))))
        p2.x = p2_pos[0]
        p2.y = p2_pos[1]
        p2.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

        p1.move()
        redraw_window(window, p1, p2)


if __name__ == '__main__':
    main()
