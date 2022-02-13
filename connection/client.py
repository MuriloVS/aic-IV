import pickle
import socket

from util.config import *


class Client:

    # Inicilizando cliente socket
    def __init__(self, address, port):

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
                    print(f'[CLIENTE] Mensagem recebida {msg}')

                    # Chama função para lidar com mensagem
                    self.handle_msg(msg)

            except:
                # Se houver erro ou falha de conexão
                # seta cliente como offline
                self.online = False

    def send_message(self, message):
        print('cliente msm ',message)
        msg = pickle.dumps(message)
        send_length = pickle.dumps(len(msg))

        self.conn.send(send_length)
        self.conn.send(msg)


    def handle_msg(self, message):
        pass

    def desconnect(self):
        self.conn.close()