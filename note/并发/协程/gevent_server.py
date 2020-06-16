import gevent
from gevent import monkey
monkey.patch_all()
import socket
import time

server = ("127.0.0.1",9999)
sk = socket.socket()
sk.bind(server)
sk.listen()
# 未使用协程时，只能连接一个客户端
# while True:
#     conn,_ = sk.accept()
#     while True:
#         msg = conn.recv(1024).decode('utf-8')
#         MSG = msg.upper()
#         conn.send(MSG.encode('utf-8'))

# 使用协程
def server(conn):
    while True:
        msg = conn.recv(1024).decode('utf-8')   # 阻塞
        MSG = msg.upper()
        conn.send(MSG.encode('utf-8'))
while True:
    conn,_ = sk.accept()    # 阻塞
    gevent.spawn(server,conn)

# accept 和 recive 都会阻塞，gevent 协程会不断在这两处之间切换，所以可以接收多个客户端的信息，接受多个客户端的连接
# 当连接了多个客户端后，协程会不断在各个阻塞之间快速切换