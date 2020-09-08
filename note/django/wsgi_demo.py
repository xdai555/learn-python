# Python web 程序分为两部分：服务器程序和应用程序
# 服务器负责对 socket 服务端进行封装，并处理各类请求数据，应用程序负责具体的逻辑处理，不同的框架如 Django、Flask 开发
# 出来的应用程序需要和服务器来进行交互，此时需要一个规范，来使得服务器可以支持不同框架开发的应用程序

# WSGI(Web Server Gateway Interface) 是一种规范，定义了 Python 编写的 web 应用程序与 web 服务器之间的接口，实现解耦
# 常用的 WSGI 服务器有 uWSGI Gunicorn , Python 标准库中有独立的 WSGI 叫做 wsgiref
# HTTP请求--> Nginx --> WSGI --> Django