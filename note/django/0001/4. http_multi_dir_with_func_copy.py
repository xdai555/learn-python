
# 根据不同的路径返回不同的数据，如果路径过多，通过 if 添加过于麻烦，可以通过反射来实现
import socket
import time

sk = socket.socket()
sk.bind(("127.0.0.1",88))
sk.listen()


def __init__(self,url):
    url = url
def page1(url):
    return f"This is {url}"
def page2(url):
    return f"This is {url}"
def page3(url):
    return f"This is {url}"
def home(url):
    with open("index.html",'r', encoding='utf-8') as f:
        return f.read()

lis = [
    ("/page1", page1),
    ("/page2", page2),
    ("/page3", page3),
    ("/", home),
]



while True:
    conn, addr = sk.accept()
    # 获取到请求头
    data = conn.recv(2048).decode("utf-8")
    # 获取请求头中的目录
    url = data.split()[1]
    print(url)
    # 发送请求头
    conn.send(b"HTTP/1/1 200 OK\r\n\r\n")
    # 根据不同的请求目录，通过执行不通的函数来返回不同的数据
    func = None
    for i in lis:
        if url == i[0]:
            func = i[1]
            break
    if func:
        ret = func(url)
    else:
        ret = "Page Not Found"
    conn.send(ret.encode('utf-8'))
    conn.close()
    