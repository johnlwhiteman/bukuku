from Server import Server




from http.server import HTTPServer, BaseHTTPRequestHandler
import logging

HOST = 'localhost'
PORT = 7777

def getPublicParameters():
    g = 5
    p = 23
    return [g, p]

class Server(BaseHTTPRequestHandler):

    def sendResponse(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.send_header('g', g)
        self.send_header('p', p)
        self.end_headers()

    def do_GET(self):
        self.sendResponse()
        self.wfile.write(b'Check the headers, Sir')

if __name__ == "__main__":
    g = 5
    p = 23
    server = HTTPServer((HOST, PORT), Server)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    server.server_close()
