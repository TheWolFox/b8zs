import math

class Vegenere:
    def __init__(self):
        self.inputC = ''
        self.binaryC = []
        self.outputC = ''
        self.inputD = ''
        self.binaryD = []
        self.outputD = ''

        self.keyword = 'crystalgems'

        self.charToIndex = {
            'c': 2,
            'r': 17,
            'y': 24,
            's': 18,
            't': 19,
            'a': 0,
            'l': 11,
            'g': 6,
            'e': 4,
            'm': 12
        }
    
    def getCryptographedLetter(self, index, letter):
        alphabet = 'abcdefghijklmnopqrstuvwxyzàáãâéêóôõíúçABCDEFGHIJKLMNOPQRSTUVWXYZÀÁÃÂÉÊÓÕÍÚÇ'

        if letter not in alphabet:
            return letter

        i = alphabet.index(letter) + self.charToIndex[index]
        if i >= len(alphabet):
            i-= len(alphabet)
        
        return alphabet[i]

    def fitKeyword(self):
        times = math.floor(len(self.inputC)/len(self.keyword))
        rest = len(self.inputC) - times*len(self.keyword)
        return self.keyword*times + self.keyword[:rest]
    
    def getCryptographedMessage(self):

        keyword = self.fitKeyword()
        
        for i, letter in enumerate(self.inputC):
            self.outputC+= self.getCryptographedLetter(keyword[i], letter)
        
        return self.outputC
    
    def convertBinary(self):
        binaryC = ''
        for letter in self.outputC:
            binaryC += bin(ord(letter))[2:].zfill(8)

        for letter in binaryC:
            i = 0
            if letter == '1':
                i = 1
            self.binaryC.append(i)

        return self.binaryC

    def encodeVegenere(self, inputC):
        self.inputC = inputC

    def decodeVegenere(self, inputD):
        self.inputD = inputD
    
    
    






    