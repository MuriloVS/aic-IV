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
                # Recebe o tamanha da mensagem a ler
                message = pickle.loads(self.conn.recv(HEADER))
                print(message['msg_id'])

                # Chama função para lidar com mensagem
                self.handleMsg(message)
                
            except: # Se houver erro ou falha de conexão
                # Desconecta cliente
                self.s.unsubscribe(self)
                self.clientOnline = False
                return

    # Lida com mensagem recebida
    def handleMsg(self, message):
        if message['msg_id'] == 'player_position':
            print(f'Player {self.id} - position {message["data"]}')

        elif message['msg_id'] == 'player':
            self.conn.send(pickle.dumps(len(self.s.clients) - 1))

        elif message['msg_id'] == 'load_maze':
            self.s.broadcast(pickle.dumps(self.s.maze))