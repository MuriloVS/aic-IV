import time
import socket
import threading
from multiprocessing import Manager
import pickle

from connection.server_client import ServerClient
from config import LOCALHOST, PORT


class Server():
    def __init__(self):

        # AF_INET se refere ao IPV4 e o SOCK_STREAM ao protocolo TCP
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # o bind vincula o servidor ao endereço e porta fornecidos
        self.s.bind((LOCALHOST, PORT))

        # listen para esperar as conexões
        self.s.listen(2)

        print(f'Servidor rodando em {LOCALHOST} na porta {PORT}')

        self.clients = []
        self.playerID = 1

        manenger = Manager()
        self.maze_list = manenger.Value(typecode=dict, value={})
        self.initial_player_position = manenger.Value(typecode=tuple, value=(0, 0))
        self.targets = manenger.Value(typecode=tuple, value=(0, 0))

        self.online = True

    def subscribe(self):
        while self.online:
            try:
                # accept inicia a conexão com o servidor
                # retornando dados do cliente e endereço/porta usados
                client, address = self.s.accept()

                # print(f'[NOVA CONEXÃO] Player {self.playerID}')
                c = ServerClient(self, client, self.playerID, self.maze_list)
                self.clients.append(c)

                # Cria thread para receber msgns do cliente
                thread = threading.Thread(target=c.start, args=())
                thread.start()

                self.playerID += 1

            except:
                self.online = False

    # Realiza desinscrição de um usuário
    def unsubscribe(self, client):
        # Remova usuário das listas de clientes conectados
        self.clients.remove(client)

        print(f'[SERVIDOR] DESCONEXÃO: Player {client.id}')

        # Encerra socket do cliente
        client.conn.close()

    def personal_message(self, conn, message):
        # Recebendo variáveis já codificados para envio
        message, send_length = pickle_message(message)

        # Envia mensagem a todos clientes conectados
        conn.send(send_length)
        time.sleep(0.1)
        conn.send(message)

    def broadcast(self, conn, message):
        # Recebendo variáveis já codificados para envio
        message, send_length = pickle_message(message)

        for client in self.clients:
            if client.conn != conn:
                client.conn.send(send_length)
                client.conn.send(message)

    def close_server(self):
        self.online = False
        self.s.close()        

def pickle_message(message):
    message = pickle.dumps(message)
    send_length = pickle.dumps(len(message))
    return message, send_length

if "__main__" == __name__:
    
    s = Server()
    s.subscribe()