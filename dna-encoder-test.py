import dnaEncoder as de
import pytest
class TestDnaEncoder():
    
    def testNormalize(self):
        normalizeTest1 = de.DNAEncoder()
        normalizeTest1.normalize("h")
        assert normalizeTest1.normalize("h") == ['01', '10', '10', '00']
        assert normalizeTest1.getBinaryArray() == ['01', '10', '10', '00']
    
    def testConvert(self):
        convertTest1 = de.DNAEncoder()
        convertTest1.normalize("h")
        assert convertTest1.convert() == ['G', 'C', 'C', 'A']
        assert convertTest1.getNucleotideArray() == ['G', 'C', 'C', 'A']