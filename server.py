import socket
import threading
import pickle
from player import Player

players = [Player(0, 0, 50, 50, (255, 0, 0)),
           Player(100, 100, 50, 50, (0, 0, 255))]
current_player = 0

server = "192.168.56.1"
port = 5555


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    print(e)

# no máximo dois jogadores podem se conectar ao servidor
s.listen(2)
print('Esperando conexão. Sever funcionando.')


def threaded_client(conn, current_player):
    conn.send(pickle.dumps(players[current_player]))
    reply = ""

    while True:
        try:
            data = pickle.loads(conn.recv(2048))
            players[current_player] = data

            if not data:
                print('Disconnected')
                break
            else:
                if current_player == 1:
                    reply = players[0]
                else:
                    reply = players[1]

                # print(f'Received: {data}')
                # print(f'Sending: {reply}')

            conn.sendall(pickle.dumps(reply))
        except:
            break

    print('Lost connection.')
    print(current_player)
    conn.close()


def main(current_player):
    while True:
        conn, addr = s.accept()
        print(f'Connected to: {addr}')

        t = threading.Thread(target=threaded_client,
                             args=(conn, current_player))
        t.start()
        current_player += 1


if __name__ == '__main__':
    main(current_player)
