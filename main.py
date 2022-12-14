from Vegenere import Vegenere
from LineCode import B8ZS

if __name__ == "__main__":
    crypt = Vegenere()
    b8 = B8ZS()
    crypt.encodeVegenere('Y!')
    print(crypt.getCryptographedMessage())
    a = crypt.convertBinary()

    print(b8.encode(a))

    s = ''.join([str(item) for item in a])
    print(s)
    crypt.decodeVegenere(a)
    print(crypt.convertToString())
    print(crypt.getDecryptographedMessage())
    
