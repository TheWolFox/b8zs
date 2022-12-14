import socket

class Client:
    def __init__(self):
        self.host = ''
        self.port = 3000
        self.client_socket =''

    def setup(self, host, port):
        self.host = host
        if port != None:
            self.port = port

    def connect(self):
        self.client_socket = socket.socket()
        self.client_socket.connect((self.host, self.port))

    def sendMessage(self):
        print('Send Message')
        message = input(" -> ")

        while True:
            self.client_socket.send(message.encode())
            message = input(" -> ")

    def start(self, host, port):
        self.setup(host, port)
        self.connect()
        self.sendMessage()
