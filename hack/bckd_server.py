import socket

def main():
    server = socket.socket()
    server.bind(('localhost', 7777))
    server.listen(1)

    while True:
        v, d = server.accept()
        print('Conected from {}'.format(d))

        view = v.recv(1204)
        if view == "1":
            while True:
                o = raw_input('shell@shell: ')
                v.send(o)
                response = v.recv(2048)
                print(response)
    

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        pass