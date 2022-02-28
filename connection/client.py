import pickle
import socket
from uuid import uuid4

from config import *


class Client:

    # Inicilizando cliente socket
    def __init__(self, game, address, port):

        self.id = 0
        self.game = game

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
                    #print(f'[PLAYER] Mensagem recebida: {msg}')

                    # Chama função para lidar com mensagem
                    self.handle_msg(msg)

            except:
                # Se houver erro ou falha de conexão
                # seta cliente como offline
                self.online = False

    # Lida com mensagem recebida
    def handle_msg(self, message):
        try:
            if message['id'] == 'player_position':
                pos_x = message['data']['x']
                pos_y = message['data']['y']
                for client in self.game.players:
                    if client.client == message['data']['player_id']:
                        client.move(pos_x, pos_y)        
            
            elif message['id'] == 'load_maze':
                rows, cols = message['data']['size']
                self.game.set_targets(rows, cols)
                maze_list = message['data']['list']
                self.game.update_maze(maze_list)                    
                pos_x, pos_y = message['data']['position']
                self.game.set_camera_position(pos_x, pos_y)                

            elif message['id'] == 'player_guest':
                self.game.create_guest(message['data'])

            elif message['id'] == 'player_id':
                self.id = message['data']

            elif message['id'] == 'win':
                self.game.win = True
                if self.id == message['data']['player_id']:
                    self.game.winner()
                else:
                    self.game.loser()

            else:
                print(f'[CLIENTE] ERRO: id de msgm recebida não identificada. Mensagem: {message}')

        except Exception as e:
            print(f'ERRO HANDLE MSG: {e}\n{message}')

    def send_message(self, message):
        try:
            #print('[PLAYER] Enviando msg: ', message['id'])
            msg = pickle.dumps(message)
            send_length = pickle.dumps(len(msg))

            self.conn.send(send_length)
            self.conn.send(msg)

        except Exception as e:
            print(f'[PLAYER] Erro send_message -> {e}')

    def desconnect(self):
        self.conn.close()