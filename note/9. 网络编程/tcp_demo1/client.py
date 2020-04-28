import socket

sk = socket.socket()
sk.connect((('172.17.144.1',6666)))

msg = sk.recv(111)
print(msg)