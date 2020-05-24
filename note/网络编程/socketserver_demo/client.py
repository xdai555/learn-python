import socket

sk = socket.socket()
sk.connect(('127.0.0.1',9999))

while True:
    sk.send(b'hello')
    content = sk.recv(1024).decode('utf-8')
    print(content)