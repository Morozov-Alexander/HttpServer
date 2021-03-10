import os
import argparse

from MyHttpServer import MyHttpServer

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Set server params')
    parser.add_argument("--directory", "-d", type=str, help='set server directory', default=os.getcwd())
    parser.add_argument("--port", '-p', type=int, help='set server port', default=8000)
    args = parser.parse_args()
    print("Arguments --- ",args)
    my_server = MyHttpServer(port=args.port, path=args.directory)
    my_server.run()


