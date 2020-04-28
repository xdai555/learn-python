import socket

sk = socket.socket(type=socket.SOCK_DGRAM)

server = ("127.0.0.1",9888)
# sk.sendto(b'to_server',server)
# msg = sk.recv(12314)
# print(msg)




# 多条消息
while True:
    send_msg = input("要发送的信息>>>")
    if send_msg.lower() == "q":break
    sk.sendto(send_msg.encode('utf-8'),server)
    msg = sk.recv(1024).decode('utf-8')
    print(msg)
    if send_msg.lower() == "q" or msg.lower() == "q":
        break