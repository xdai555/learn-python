import socket
import time


sk = socket.socket()
server = ("127.0.0.1",9999)
sk.connect(server)
while True:
    sk.send('hello'.encode('utf-8'))
    msg = sk.recv(1024)
    print(msg)
    time.sleep(1)