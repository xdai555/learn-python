
# 根据不同的路径返回不同的数据
import socket


sk = socket.socket()
sk.bind(("127.0.0.1",88))
sk.listen()

def page1(url):
    return f"This is {url}"
def page2(url):
    return f"This is {url}"

while True:
    conn, addr = sk.accept()
    # 获取到请求头
    data = conn.recv(2048).decode("utf-8")
    # 获取请求头中的目录
    url = data.split()[1]
    print(url)
    # 根据不同的请求目录，通过执行不通的函数来返回不同的数据
    conn.send(b"HTTP/1/1 200 OK\r\n\r\n")
    if url == "/page1":
        ret = page1(url)
    elif url == "/page2":
        ret = page2(url)
    else:
        ret = "Page Not Found"
    conn.send(ret.encode('utf-8'))
    conn.close()
    