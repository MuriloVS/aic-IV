import pickle

from util.config import *

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

        # Enviando mensagem com ID do player
        message = {'id': 'player_id',
                   'data': self.id
                  }
        self.s.personal_message(self.conn, message)

        if (self.id > 1):
            message = {'id': 'load_maze',
                    'data': self.s.maze
                    }
            self.s.personal_message(self.conn, message)

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
                
            except:
                # Se houver erro ou falha de conexão desconecta cliente
                self.s.unsubscribe(self)
                self.clientOnline = False

    # Lida com mensagem recebida
    def handle_msg(self, message):
        # try:
        if message['id'] == 'player_position':
            self.s.broadcast(self.conn, message)

        elif message['id'] == 'player_id':
            self.s.personal_message(self.conn, self.id)

        elif message['id'] == 'load_maze':
            self.s.maze = message['data']

        elif message['id'] == 'get_maze':
            msg = {'id': 'load_maze',
                       'data': self.s.maze
                      }
            self.s.personal_message(self.conn, msg)
        
        # except:
        # print(f'ERRO HANDLE MSG: {message}')