from Vegenere import Vegenere
from LineCode import B8ZS
from Server import Server
from Client import Client
from Interface import selectorWindow

import matplotlib.pyplot as plt

if __name__ == "__main__":
    crypt = Vegenere()
    b8 = B8ZS()
    ip = '127.0.0.1'
    port = 3012

    

    print("Press 's' for Server or 'c' for Client")
    choice = input()
        
    if choice == 's':
        server = Server()
        server.start(ip, port)
        while True:
            signal = server.receiveMessage()
            signal = crypt.stringToSignal(signal)
            bin = b8.decode(signal)
            crypt.decodeVegenere(bin)
            binStr = ''.join([str(item) for item in bin])
            veg = crypt.convertToString()
            inp = crypt.getDecryptographedMessage()
            print('Sinal: \n', signal)
            print('Forma Binária: \n', binStr)
            print('Criptografia de Vegenere: \n', veg)
            print('Entrada: \n', inp)

            # plt.step(list(range(len(signal))), signal)
            # plt.show()

    elif choice == 'c':
        client = Client()
        client.start(ip, port)
        while True:
            message = input(' -> ')
            crypt.encodeVegenere(message)
            vegenere = crypt.getCryptographedMessage()
            binary = crypt.convertBinary()
            binaryString = ''.join([str(item) for item in binary])
            sig = b8.encode(binary)
            client.sendMessage(crypt.signalToString(sig))
            print('Entrada: \n', message)
            print('Criptografia de Vegenere: \n', vegenere)
            print('Forma Binária: \n', binaryString)
            print('Sinal: \n', sig)
            client.sendMessage(crypt.signalToString(sig))
    
    app = selectorWindow()
    app.run()
    
