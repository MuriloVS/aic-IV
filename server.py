import socket
import threading
import pickle

from util.maze import Maze
from util.tools import generate_maze
from util.config import LOCALHOST, PORT


class Server():
    def __init__(self):

        # AF_INET se refere ao IPV4 e o SOCK_STREAM ao protocolo TCP
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # o bind vincula o servidor ao endereço e porta fornecidos
        self.server.bind((LOCALHOST, PORT))
        # listen para esperar as conexões
        self.server.listen(2)

        print(f'Servidor rodando em {LOCALHOST} na porta {PORT}')

        self.clients = []
        self.online = True

        self.maze = generate_maze()

        # Inicializa thread que capta uma entrada para encerrar servidor
        TQuit = threading.Thread(target=self.close_server, args=())
        TQuit.start()

    def broadcast(self, message):  # ainda não é usada
        for client in self.clients:
            client.send(message)

    def client_handler(self, client, current_player):
        while True:
            try:
                # recebe a mensagem enviada por um cliente
                message = pickle.loads(client.recv(2048))
                print(message['msg_id'])

                if message['msg_id'] == 'player_position':
                    print(f'Player {current_player} - position {message["data"]}')

                elif message['msg_id'] == 'player':
                    client.send(pickle.dumps(len(self.clients) - 1))

                elif message['msg_id'] == 'load_maze':
                    client.sendall(pickle.dumps(self.maze))

            except:
                # removendo o cliente das listas
                print('Cliente se desconectou.')
                index = self.clients.index(client)
                self.clients.pop(index)

                # e finalizando a conexão
                client.close()
                break


    def receive(self):
        current_player = len(self.clients)

        while self.online:
            try:
                # accept inicia a conexão com o servidor
                # retornando dados do cliente e endereço/porta usados
                client, address = self.server.accept()
                self.clients.append(client)

                # feita a conexão com o cliente iniciamos uma thread para
                # lidar com esta conexão
                thread = threading.Thread(
                    target=self.client_handler, args=(client, current_player))
                thread.start()

                current_player += 1
            except:
                exit(0)

    def close_server(self):
        # Espera input no terminal do servidor para encerrar aplicação
        input("Pressione [ENTER] para encerrar o servidor\n")

        # Ao receber, seta variável para offline, encerra o socket e fecha app
        self.online = False
        self.server.close()        

if __name__ == '__main__':

    # cria o servidor
    server = Server()

    # e espera as conexões
    server.receive()
