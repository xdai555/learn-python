# # HTTP 请求方法
# 根据 HTTP 标准，HTTP 请求可以使用多种请求方法。
# HTTP1.0 定义了三种请求方法： GET, POST 和 HEAD方法。
# HTTP1.1 新增了六种请求方法：OPTIONS、PUT、PATCH、DELETE、TRACE 和 CONNECT 方法。
# 1   GET	请求指定的页面信息，并返回实体主体。
# 2   HEAD	类似于 GET 请求，只不过返回的响应中没有具体的内容，用于获取报头
# 3   POST	向指定资源提交数据进行处理请求（例如提交表单或者上传文件）。数据被包含在请求体中。POST 请求可能会导致新的资源的建立和/或已有资源的修改。
# 4   PUT	从客户端向服务器传送的数据取代指定的文档的内容。
# 5   DELETE	请求服务器删除指定的页面。
# 6   CONNECT	HTTP/1.1 协议中预留给能够将连接改为管道方式的代理服务器。
# 7   OPTIONS	允许客户端查看服务器的性能。
# 8   TRACE	回显服务器收到的请求，主要用于测试或诊断。
# 9   PATCH	是对 PUT 方法的补充，用来对已知资源进行局部更新 。

# # 状态码
# 1xx 消息：请求被服务器接收，继续处理
# 2xx 成功：请求已经被服务器接收、理解并接受
# 3xx 重定向：需要后续操作才能完成当前的请求
# 4xx 请求错误：请求含有错误或请求无法被执行
# 5xx 服务器错误：服务器在处理某个正确请求时发生错误
# 一般情况下，RFC 2616 中定义了常用状态的状态码，开发人员也可以自定义
# 常见的相应代码 https://www.runoob.com/http/http-status-codes.html

# # URL 基本元素
# 协议
# 层级URL标记符号
# 访问资源所需凭证（可选）
# 服务器地址，IP 或域名
# 端口号
# 路径，以 / 为分隔符
# 查询，GET 模式的参数，以 ? 为起点，每个参数以 & 隔开，再以 key=value 表示数据
# 片段，类似于目录标题，以 # 为起点

import socket

sk = socket.socket()
sk.bind(("127.0.0.1",88))
sk.listen()

while True:
    conn, addr = sk.accept()
    data = conn.recv(2048).decode("utf-8")
    # 给客户端发送 HTTP 请求头，即可正常显示
    conn.send(b"HTTP/1.1 200 OK\r\n\r\n hello web")
    print(data)
    conn.close()

# 请求头
# GET / HTTP/1.1            --> 请求方法 URL 版本，GET /aaa HTTP/1.1，用户请求不同目录时，请求头会变， / 表示根目录
# Host: 127.0.0.1:88        
# Connection: keep-alive
# DNT: 1
# Upgrade-Insecure-Requests: 1
# User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36
# Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
# Sec-Fetch-Site: none
# Sec-Fetch-Mode: navigate
# Sec-Fetch-User: ?1
# Sec-Fetch-Dest: document
# Accept-Encoding: gzip, deflate, br
# Accept-Language: zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7      --> 下方应当为请求数据

# 请求格式 request
# "请求方法 路径 HTTP/1.1
# k1=v1
# k2=v2
# 
# 
# 请求体" --> get 请求没有请求体

# 响应格式 response
# "HTTP/1.1 状态码 状态描述符
# k1=v1
# k2=v2
# 
# 
# 响应体（响应数据）"
