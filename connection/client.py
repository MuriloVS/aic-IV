import pickle
import socket
from uuid import uuid4

from util.config import *


class Client:

    # Inicilizando cliente socket
    def __init__(self, game, address, port):

        self.id = 0
        self.g = game

        # Define família e tipo da conexão (AF_INET -> IPV4 | SOCK_STREAM -> TCP)
        self.conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        # Conecta com servidor socket
        ADDR = (address, int(port))
        self.conn.connect(ADDR)

        # Recebe parâmetros
        self.online = True

    # Recebe mensagem
    def receive_message(self):
        # Loop de recebimento de msgm
        while self.online: # enquanto cliente está online
            try:
                # espera receber mensagem do servidor
                msg_lenght = pickle.loads(self.conn.recv(HEADER))
                if msg_lenght: # se tam for recebido
                    msg_lenght = int(msg_lenght) # armazena valor em int
                    msg = pickle.loads(self.conn.recv(msg_lenght))
                    #print(f'[CLIENTE] Mensagem recebida {msg}')

                    # Chama função para lidar com mensagem
                    self.handle_msg(msg)

            except:
                # Se houver erro ou falha de conexão
                # seta cliente como offline
                self.online = False

    def send_message(self, message):
        msg = pickle.dumps(message)
        send_length = pickle.dumps(len(msg))

        self.conn.send(send_length)
        self.conn.send(msg)

    # Lida com mensagem recebida
    def handle_msg(self, message):
        # try:
        if message['id'] == 'player_id':
            self.id = message['data']

        elif message['id'] == 'player':
            self.s.personal_message(self.conn, self.id)

        elif message['id'] == 'load_maze':
            print('labirinto recebido')
            self.g.maze_list = message['data']
            self.g.update_maze()
            print('[CLIENTE] Labirinto recebido')
        else:
            print(f'[CLIENTE] ERRO: id de msgm recebida não identificada. Mensagem: {message}')
        # except:
        # print(f'ERRO HANDLE MSG: {message}')

    def desconnect(self):
        self.conn.close()