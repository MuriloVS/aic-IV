import pickle
import time

from config import *

# Classe worker
# - recebe msgns do cliente
# - lida com solicitações e se comunica com a classe principal

class ServerClient:

    # Inicializa a instância do cliente no server
    def __init__(self, server, conn, id):

        self.id = id

        # Armazena a referência ao servidor para realizar comunicação
        self.s = server

        # recebe o socket do cliente
        self.conn = conn

        # Define cliente como online para loop principal
        self.clientOnline = True

        print(f'[SERVIDOR] Nova conexão: Player {self.id}')

        # Enviando mensagem com ID do player e infos sobre o labirinto
        if self.id > 1:
            self.send_maze()
        time.sleep(1)
        self.send_id()
        self.send_clients()


    # Aguarda o recebimento de uma mensagem do cliente
    def start(self):
        # Enquanto o cliente estiver online recebe mensagem dele
        while self.clientOnline and self.s.online:
            try:
                # espera receber mensagem do servidor
                msg_lenght = pickle.loads(self.conn.recv(HEADER))
                if msg_lenght: # se tam for recebido
                    msg_lenght = int(msg_lenght) # armazena valor em int
                    msg = pickle.loads(self.conn.recv(msg_lenght))
                    #print(f'[SERVIDOR] Mensagem recebida:{msg["id"]}')
                    
                    # Chama função para lidar com mensagem
                    self.handle_msg(msg)
                
            except Exception as e:
                # print(f'[SERVIDOR] [Player {self.id}] Erro ao receber mensagem: {e}')
                pass

    # Lida com mensagem recebida
    def handle_msg(self, message):
        try:
            if message['id'] == 'player_position':
                self.s.broadcast(self.conn, message)

            elif message['id'] == 'player_id':
                self.s.personal_message(self.conn, self.id)

            elif message['id'] == 'load_maze':
                self.s.maze_list.value = message['data']
            
            elif message['id'] == 'win':
                msg = {'id': 'win',
                        'data': {
                            'player_id': self.id
                                }
                    }        
                self.s.broadcast(self.conn, msg)

            elif message['id'] == 'desconnect':
                self.s.unsubscribe(self)
                self.clientOnline = False

            else:
                pass

            # elif message['id'] == 'get_maze':
            #     msg = {'id': 'load_maze',
            #             'data': self.s.maze_list.value
            #             }
            #     self.s.personal_message(self.conn, msg)

        except Exception as e:
            #print(f'[SERVER] [Player {self.id}] Erro ao ler mensagem: {e}')
            pass

    def send_id(self):
        message = {'id': 'player_id',
                   'data': self.id
                  }
        self.s.personal_message(self.conn, message)    
        time.sleep(0.2)            

    def send_maze(self):
        message = {'id': 'load_maze',
                   'data': self.s.maze_list.value
                }
        self.s.personal_message(self.conn, message)

    def send_clients(self):
        for client in self.s.clients:
            message = {'id': 'player_guest',
                       'data': client.id
                      }
            self.s.personal_message(self.conn, message)
        time.sleep(0.2)
