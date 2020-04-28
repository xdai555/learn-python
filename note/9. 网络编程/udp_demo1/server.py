import socket

sk = socket.socket(type=socket.SOCK_DGRAM)
sk.bind(("127.0.0.1",9888))

# msg = sk.recv(1111)
# print(msg)
# 单个
# msg , addr = sk.recvfrom(11111)
# print(msg)  # (b'123123', ('127.0.0.1', 62003))
# sk.sendto(b'to_client',addr)

# 多条消息
while True:
    msg, addr = sk.recvfrom(1024)
    print(f"收到了{addr[0]}的消息",msg.decode('utf-8'))
    send_msg = input("要发送的信息>>>")
    print(f"向{addr[0]}发送信息")
    sk.sendto(send_msg.encode('utf-8'),addr)
