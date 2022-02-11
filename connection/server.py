from audioop import add
import socket
import threading
import pickle

import util.tools as tool
from connection.server_client import ServerClient
from util.config import LOCALHOST, PORT


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
        self.playerID = 0
        self.maze = tool.generate_maze() # AQUI

        self.online = True

        # Inicializa thread que capta uma entrada para encerrar servidor
        TQuit = threading.Thread(target=self.close_server, args=())
        TQuit.start()

    def subscribe(self):
        while self.online:
            try:
                # accept inicia a conexão com o servidor
                # retornando dados do cliente e endereço/porta usados
                client, address = self.s.accept()
                #print(client, address)

                c = ServerClient(self, client, self.playerID)
                self.clients.append(client)

                # Cria thread para receber msgns do cliente
                thread = threading.Thread(target=c.start, args=())
                thread.start()

                self.personal_message(client, self.playerID)

                self.playerID += 1
            except:
                exit(0)

    # Realiza desinscrição de um usuário
    def unsubscribe(self, client):
        print(f'Cliente [{client.id}] se desconectou.')
        # Remova usuário das listas de clientes conectados
        self.clients.remove(client.conn)

        # Encerra socket do cliente
        client.conn.close()

    def personal_message(self, conn, message):
        # Recebendo variáveis já codificados para envio
        message = pickle.dumps(message)
        send_length = len(message)

        # Envia mensagem a todos clientes conectados
        conn.send(send_length)
        conn.send(message)

    def broadcast(self, message):  # ainda não é usada
        for client in self.clients:
            client.conn.send(message)

    def close_server(self):
        # Espera input no terminal do servidor para encerrar aplicação
        input("Pressione [ENTER] para encerrar o servidor\n")

        # Ao receber, seta variável para offline, encerra o socket e fecha app
        self.online = False
        self.s.close()        


if "__main__" == __name__:
    
    s = Server()
    s.subscribe()