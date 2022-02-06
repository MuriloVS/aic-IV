import socket
import threading
import pickle

from scenes.maze import Maze
from util.config import LOCALHOST, PORT


def generate_maze():
    maze = Maze()
    maze.build()
    maze_list = []

    for i in range(maze.rows):
        maze_list.append([])
        for j in range(maze.cols):
            maze_list[i].append(maze.grid[i][j].__dict__['walls'])

    return maze_list


maze = generate_maze()
clients = []


def broadcast(message):  # ainda não é usada
    for client in clients:
        client.send(message)


def client_handler(client, current_player):
    while True:
        try:
            # recebe a mensagem enviada por um cliente
            message = pickle.loads(client.recv(2048))
            print(message['msg_id'])

            if message['msg_id'] == 'player_position':
                print(f'Player {current_player} - position {message["data"]}')

            elif message['msg_id'] == 'player':
                client.send(pickle.dumps(len(clients) - 1))

            elif message['msg_id'] == 'load_maze':
                client.sendall(pickle.dumps(maze))
        except KeyboardInterrupt:
            client.close()
            break

        except:
            # removendo o cliente das listas
            print('Cliente se desconectou.')
            index = clients.index(client)
            clients.pop(index)

            # e finalizando a conexão
            client.close()
            break


def receive(server):
    current_player = len(clients)

    while True:
        try:
            # accept inicia a conexão com o servidor
            # retornando dados do cliente e endereço/porta usados
            client, address = server.accept()
            clients.append(client)

            # feita a conexão com o cliente iniciamos uma thread para
            # lidar com esta conexão
            thread = threading.Thread(
                target=client_handler, args=(client, current_player))
            thread.start()

            current_player += 1
        except KeyboardInterrupt:
            print('aqui')
            for c in clients:
                c.close()
            server.close()
            break
        except:
            exit(0)


def create_server():
    # AF_INET se refere ao IPV4 e o SOCK_STREAM ao protocolo TCP
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # o bind vincula o servidor ao endereço e porta fornecidos
    server.bind((LOCALHOST, PORT))

    # listen para esperar as conexões
    server.listen(2)

    print(f'Servidor rodando em {LOCALHOST} na porta {PORT}')

    return server


if __name__ == '__main__':
    # cria o servidor
    server = create_server()

    # e espera as conexões
    receive(server)
