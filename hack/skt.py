import socket 
client = socket.socket()
try:
    client.connect(('google.com', 22))
    print(client.recv(1024))
except Exception as e:
    print("Error: {}".format(e))