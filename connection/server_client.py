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

        # Recebe informações do cliente
        self.conn = conn # recebe o socket do cliente

        # Define cliente como online para loop principal
        self.clientOnline = True

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

                print(f'[SERVER] Mensagem recebida:{msg}')
                # Chama função para lidar com mensagem
                self.handleMsg(msg)
                
            except:
                # Se houver erro ou falha de conexão
                # Desconecta cliente
                self.s.unsubscribe(self)
                self.clientOnline = False

    # Lida com mensagem recebida
    def handleMsg(self, message):
        if message['msg_id'] == 'player_position':
            print(f'Player {self.id} - position {message["data"]}')
            # self.s.broadcast(message)

        elif message['msg_id'] == 'player':
            self.s.personal_message(self.conn, self.id)

        elif message['msg_id'] == 'load_maze':
            self.s.broadcast(self.s.maze)