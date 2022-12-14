from Vegenere import Vegenere
from LineCode import B8ZS
from Server import Server
from Client import Client

if __name__ == "__main__":
    # crypt = Vegenere()
    # b8 = B8ZS()
    # crypt.encodeVegenere('Y!')
    # print(crypt.getCryptographedMessage())
    # a = crypt.convertBinary()

    # print(b8.encode(a))

    # s = ''.join([str(item) for item in a])
    # print(s)
    # crypt.decodeVegenere(a)
    # print(crypt.convertToString())
    # print(crypt.getDecryptographedMessage())
    print("Press 's' for Server or 'c' for Client")
    choice = input()
        
    if choice == 's':
        server = Server()
        server.start('127.0.0.1', 3000)
    elif choice == 'c':
        client = Client()
        client.start('127.0.0.1', 3000)
    
