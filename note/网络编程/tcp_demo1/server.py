import socket

sk = socket.socket()
sk.bind(('172.17.144.1',6666))
sk.listen()

conn,addr = sk.accept()
conn.send(b'asdasdasd')

conn.close()
sk.close()
