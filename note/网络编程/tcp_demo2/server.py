import socket

sk = socket.socket()
sk.bind(("127.0.0.1", 9999))
sk.listen()

# 可以依次接收多个客户端的连接
while True:
    conn, addr = sk.accept()
    print("当前连接：", conn)
    # 可以和客户端一直保持连接
    while True:
        send_msg = input("要发送的内容>>>")
        conn.send(send_msg.encode('utf-8'))
        msg = conn.recv(1111).decode('utf-8')
        if send_msg.lower() == "q" or msg.lower() == "q":
            break
        print(msg)
    print("已关闭：",conn)
    conn.close()  # 断开连接

sk.close()  # 终止服务