import socket
import yaml
import os
import re
import json
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

    def parseRequest(self,request):
        request = request.split(' ')
        return request[0], request[1][1:] 

    def generateGetRequest(self,path):
        file_type = {'html': 'text',
                   'jpg': 'image',
                   'jpeg': 'image'}  
        try:
            type1 = path.split(".")[-1]
            print(type1)
            file = open(path,'rb') # open file , r => read , b => byte format
            response = file.read()
            file.close()
            print("File - OK")
            mimetype = file_type[type1] + "/" +type1 
            print("mimetype - OK")
            header = 'HTTP/1.0 200 OK\r\n' + 'Content-Type:' + mimetype + "\r\n\r\n"
            print("header - OK")
        except:
            header = 'HTTP/1.1 404 Not Found\n\n'
            response = '<html><body><center><h3>Error 404: File not found</h3><p>Python HTTP Server</p></center></body></html>'.encode('utf-8')
    

        final_response = header.encode('utf-8') + response
        return final_response

    def getInfoToYML(self, info_list):
        map1 ={}
        for i in info_list:
            param = i.split('=')
            map1[param[0]] = param[1]
        return map1

    def saveYML(self, info_list):
    
        to_yaml = self.getInfoToYML(info_list)

        with open('POSTInfo.yaml', 'w') as f:
            yaml.dump(to_yaml, f)
        return to_yaml

    def generatePostRequest(self,params):
        kv_params = params.split()[-1].decode('utf-8')
        kv_params= kv_params.split('&')
        answer  = self.saveYML(kv_params)
        response = 'HTTP/1.0 200 OK\r\n' + 'Content-Type: text/html\r\n\r\n' + json.dumps(answer)
        return response.encode('utf-8') 


    def makeResponse(self,request):
        method, new_path = self.parseRequest(request.decode('utf-8'))
        final_response = ""
        print(method, "  ",new_path)
        if method == "GET":
            final_response = self.generateGetRequest(new_path)
        elif method == 'OPTIONS':
            final_response = 'Allow: OPTIONS, GET, POST'.encode('utf-8') 
        elif method == 'POST':
            final_response = self.generatePostRequest(request)
            print(final_response)
        return final_response

    def run(self)->None:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s: #ipv_4 tcp
            s.bind((self._domain, self._port))
            s.listen()
            while True:
                while True:
                    client_socket, addres = s.accept()
                    request = client_socket.recv(1024)
                    print({addres})
                    if not request:
                        break
                    response = self.makeResponse(request)
                    client_socket.send(response)
