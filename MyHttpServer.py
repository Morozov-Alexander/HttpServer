import socket
import yaml
import os

class MyHttpServer:
    __slots__ = ('_domain', '_port', '_path', 'server_socket')

    def __init__(self,port=8000, path='/home/alex', domain = "localhost"):
        self._domain = domain
        self._port = port
        self._path = path

    @property
    def domain(self):
        return self._domain

    @domain.setter
    def domain(self, value):
        self._domain = value

    @property
    def port(self):
        return self._port

    @port.setter
    def port(self, value):
        if isinstance(value, int):
            self._port = value

    def makeResponse(self,request):
        type, new_path = self.parseRequest(request)
        try:
            file = open("index.html",'rb') # open file , r => read , b => byte format
            response = file.read()
            file.close()
 
            header = 'HTTP/1.1 200 OK\n'
            mimetype = 'text/html'
 
            header += 'HTTP/1.0 200 OK\r\n' + 'Content-Type: text/html\r\n\r\n' 
 
        except Exception as e:
            header = 'HTTP/1.1 404 Not Found\n\n'
            response = '<html><body><center><h3>Error 404: File not found</h3><p>Python HTTP Server</p></center></body></html>'.encode('utf-8')
 

        final_response = header.encode('utf-8')
        final_response += response
        return final_response

    def run(self)->None:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s: #ipv_4 tcp
            s.bind((self._domain, self._port))
            s.listen()
            while True:
                client_socket, addres = s.accept()
                request = client_socket.recv(1024)
                print({addres})
                #client_socket.sendall(response)
                print(request)
                response = self.makeResponse(request)
                client_socket.send(response)
