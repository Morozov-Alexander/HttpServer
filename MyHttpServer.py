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

    # @my_logger
    # def get_url_method(self, request):
    #     parsed = request.split(' ')
    #     method = parsed[0]
    #     url = parsed[1]
    #     return method, url

    def run(self)->None:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s: #ipv_4 tcp
            s.bind((self._domain, self._port))
            s.listen()
            while True:
                client_socket, addres = s.accept()
                request = client_socket.recv(1024)
                # if not request:
                #     break
                response = "hello"
                print({addres})
                client_socket.send(bytes(response,"utf-8"))
                #client_socket.sendall(response)


    def generateGetResponse():
        try:
            file = open("index.html",'rb') # open file , r => read , b => byte format
            response = file.read()
            file.close()
 
            header = 'HTTP/1.1 200 OK\n'
 
            if(myfile.endswith(".jpg")):
                mimetype = 'image/jpg'
            elif(myfile.endswith(".css")):
                mimetype = 'text/css'
            else:
                mimetype = 'text/html'
 
            header += 'Content-Type: '+str(mimetype)+'<strong>\n\n</strong>'
 
        except Exception as e:
            header = 'HTTP/1.1 404 Not Found\n\n'
            response = '<html>
                          <body>
                            <center>
                             <h3>Error 404: File not found</h3>
                             <p>Python HTTP Server</p>
                            </center>
                          </body>
                        </html>'.encode('utf-8')