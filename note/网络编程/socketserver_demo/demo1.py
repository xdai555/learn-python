import socketserver
import time

class Myserver(socketserver.BaseRequestHandler):
    def handle(self):
        conn = self.request
        while True:
            try:
                content = conn.recv(1024).decode('utf-8')
                conn.send(content.upper().encode('utf-8'))
                time.sleep(1)
            except ConnectionResetError:
                break

server = socketserver.ThreadingTCPServer(('127.0.0.1',9999),Myserver)
server.serve_forever()
