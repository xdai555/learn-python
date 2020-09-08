
# 根据不同的路径返回不同的数据
import socket


sk = socket.socket()
sk.bind(("127.0.0.1",88))
sk.listen()

while True:
    conn, addr = sk.accept()
    # 获取到请求头
    data = conn.recv(2048).decode("utf-8")
    # 获取请求头中的目录
    url = data.split()[1]
    print(url)
    # 根据不同的请求目录，返回不同的数据
    if url == "/page1":
        conn.send(b"HTTP/1.1 200 OK\r\n\r\n <h1>Page 1</h1>")
    elif url == "/page2":
        conn.send(b"HTTP/1.1 200 OK\r\n\r\n <h1>Page 2</h1>")
    else:
        conn.send(b"HTTP/1.1 404 NOT FOUND\r\n\r\n <h1>Page Not Found</h1>")
    conn.close()
    