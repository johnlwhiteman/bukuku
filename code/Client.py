import json
import socket
import sys

class Client(object):

    def __init__(self, cfgPath='client.json'):
        self.cfgPath = cfgPath

    def init(self):
        with open(self.cfgPath) as fd:
            try:
                with open(self.cfgPath, "r",  encoding="utf-8") as fd:
                    self.cfg = json.load(fd)
                    self.host = self.cfg['host']
                    self.port = int(self.cfg['port'])
                    self.timeout = int(self.cfg['timeout'])
            except IOError as e:
                print(f'Error: {e}')
                sys.exit(1)

    def get(self, url='/'):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.connect((self.host, self.port))
            request = f'GET / HTTP/1.0\r\nHost: {self.host}:{self.port}\r\n\r\n'
            print(f'Sending request: {request}')
            sock.send(request.encode(encoding='utf-8'))
            response = sock.recv(1024)
            print(response.decode(encoding='utf-8'))

if __name__ == "__main__":
    client = Client()
    client.init()
    client.get()
