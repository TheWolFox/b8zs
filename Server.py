import socket

class Server:
    def __init__(self):
        self.host = ''
        self.port = 3000
        self.conn =''


    def setup(self, host, port):
        self.host = host
        if port != None:
            self.port = port

    def connect(self):
        server_socket = socket.socket()
        server_socket.bind((self.host, self.port))
        server_socket.listen(2)
        self.conn, address = server_socket.accept()
        print("Connection from: " + str(address))

    def receiveMessage(self):
        while True:
            data = self.conn.recv(1024).decode()
            if data != '':
                return data
                print("from connected user: " + str(data))
                break
            

    def start(self, host, port):
        self.setup(host, port)
        self.connect()
        #self.receiveMessage()
