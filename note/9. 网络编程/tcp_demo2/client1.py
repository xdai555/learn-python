import socket

# client 运行多次，观察服务器端
# sk = socket.socket()
# sk.connect(("127.0.0.1", 9999))
# msg = sk.recv(1111).decode('utf-8')
# sk.send(b'bye')
# print(msg)
# sk.close()

# 可以和端一直保持连接,交互信息
sk = socket.socket()
sk.connect(("127.0.0.1", 9999))
while True:
    msg = sk.recv(1111).decode('utf-8')
    print(msg)
    if msg.lower() == "q": break
    send_msg = input("要发送的内容>>>")
    sk.send(send_msg.encode('utf-8'))
    if send_msg.lower() == "q":break

sk.close()
