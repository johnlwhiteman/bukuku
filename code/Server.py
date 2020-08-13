import json
import pprint
import random
import re
import socket
import sys

class Server(object):

    def __init__(self, cfgPath='server.json'):
        self.cfgPath = cfgPath

    def init(self):
        with open(self.cfgPath) as fd:
            try:
                with open(self.cfgPath, "r",  encoding="utf-8") as fd:
                    self.cfg = json.load(fd)
                    self.host = self.cfg['host']
                    self.port = int(self.cfg['port'])
                    self.listen = int(self.cfg['listen'])
                    self.headers = 'HTTP/1.1 200 OK\r\n'
                    for name, value in self.cfg['headers'].items():
                        self.headers += f'{name}: {value}\r\n'
                    self.headers += '\r\n\r\n'
            except IOError as e:
                print(f'Error: {e}')
                sys.exit(1)

    def run(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            sock.bind((self.host, self.port))
            sock.listen(self.listen)
            print (f'Listening @ http://{self.host}:{self.port}')
            while True:
                content = f'\n<html><h1>Dog Will Hunt {random.randint(0, 100)}</h1></html>\n'
                try:
                    conn, adx = sock.accept()
                    request = conn.recv(1024)
                    print(request.decode(encoding='utf-8'))
                    conn.send(self.headers.encode(encoding='utf-8'))
                    conn.send(content.encode(encoding='utf-8'))
                    conn.close()
                except KeyboardInterrupt as e:
                    print(f'Keyboard Interrupted by YOU!')
                    conn.close()
                    sock.close()
                    sys.exit(1)

if __name__ == "__main__":
    server = Server()
    server.init()
    server.run()