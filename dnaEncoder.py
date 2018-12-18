#Software to encode binary information to DNA nucleotides
import binascii
import re
class DNAEncoder:
    def __init__(self):
        self.binaryArray = []
        self.nucleotideArray = []

    #This section of code is used for the express purpose of encoding binary information
    #Creates a demilited binary array
    def normalize(self, stringIn):
        binary =  str(bin(int.from_bytes(stringIn.encode(), 'big')))
        binary = re.sub('b', '', binary)
        self.binaryArray = [binary[i:i+2] for i in range(0, len(binary), 2)]
        return self.binaryArray

    #Converts to nucleotides
    def convert(self):
        for x in self.binaryArray:
            if x == '00':
                self.nucleotideArray.append('A')
            elif x == '11':
                self.nucleotideArray.append('T')
            elif x == '01':
                self.nucleotideArray.append('G')
            elif x == '10':
                self.nucleotideArray.append('C')
            else:
                print("Error")
        return self.nucleotideArray

    def getBinaryArray(self):
        return self.binaryArray

    def getNucleotideArray(self):
        return self.nucleotideArray