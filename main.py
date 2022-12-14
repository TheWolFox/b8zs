from Crypto import Vegenere

if __name__ == "__main__":
    crypt = Vegenere()
    crypt.encodeVegenere('olá tudo bem?')
    print(crypt.getCryptographedMessage())
    a = crypt.convertBinary()
    s = ''.join([str(item) for item in a])
    print(s)