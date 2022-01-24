import socket
import threading

pos = [(0, 0), (100, 100)]
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


def read_pos(data):
    # recebe a posição na tela como uma string e retorna uma tupla
    data = data.split(',')
    return int(data[0]), int(data[1])


def set_pos(data):
    # recebe uma tupla de devolve uma string com as posições
    return str(data[0]) + ',' + str(data[1])


def threaded_client(conn, current_player):
    conn.send(str.encode(set_pos(pos[current_player])))
    reply = ""

    while True:
        try:
            data = conn.recv(2048).decode()
            data = read_pos(data)
            pos[current_player] = data

            if not data:
                print('Disconnected')
                break
            else:
                if current_player == 1:
                    reply = pos[0]
                else:
                    reply = pos[1]

                # print(f'Received: {data}')
                # print(f'Sending: {reply}')

            conn.sendall(str.encode(set_pos(reply)))
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
