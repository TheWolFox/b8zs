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
            # receive data stream. it won't accept data packet greater than 1024 bytes
            data = self.conn.recv(1024).decode()
            if not data:
                break
            print("from connected user: " + str(data))

    def start(self, host, port):
        self.setup(host, port)
        self.connect()
        self.receiveMessage()
