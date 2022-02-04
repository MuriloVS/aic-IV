from cmath import pi
import socket
import threading
import pickle

LOCALHOST = '127.0.0.1'
PORT = 6789

clients = []


def broadcast(message):
    for client in clients:
        client.send(message)


def client_handler(client):
    while True:
        try:
            # recebe a mensagem enviada por um cliente
            message = client.recv(4096)
            data = pickle.loads(message)
            broadcast(data)
        except:
            # removendo o cliente das listas
            index = clients.index(client)
            clients.pop(index)

            # e finalizando a conexão
            client.close()
            break


def receive(server):
    while True:
        try:
            # accept inicia a conexão com o servidor
            # retornando dados do cliente e endereço/porta usados
            client, address = server.accept()
            clients.append(client)

            client.send('POS'.encode('utf-8'))
            message = pickle.loads(client.recv(4096))
            print(f'{message} se conectou')

            # feita a conexão com o cliente iniciamos uma thread para
            # lidar com esta conexão
            thread = threading.Thread(target=client_handler, args=(client,))
            thread.start()
        except:
            exit(0)


def create_server():
    # AF_INET se refere ao IPV4 e o SOCK_STREAM ao protocolo TCP
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # o bind vincula o servidor ao endereço e porta fornecidos
    server.bind((LOCALHOST, PORT))
    # listen para esperar as conexões - limitadas a 15
    # no caso de uma hipotética 16ª conexão esta seria rejeitada
    server.listen(15)
    print(f'Servidor rodando em {LOCALHOST} na porta {PORT}')
    return server


if __name__ == '__main__':
    # cria o servidor
    server = create_server()
    # e espera as conexões
    receive(server)
