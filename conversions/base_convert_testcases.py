import unittest
from  base_convert import *

class TestBaseConvert(unittest.TestCase):

    #tests base 2
    def test_base2(self):
        self.assertEqual(convert(45,2),"101101")

    #tests base 3 with small number
    def test_base3(self):
        self.assertEqual(convert(4,3),"11")

    #tests base 4
    def test_base4(self):
        self.assertEqual(convert(30,4),"132")

    #tests base 5 with a number smaller than the base
    def test_base5(self):
        self.assertEqual(convert(1,5),"1")

    #tests base 6
    def test_base6(self):
        self.assertEqual(convert(363,6),"1403")

    #tests base 7 with 0
    def test_base7(self):
        self.assertEqual(convert(0,7),"0")

    #tests base 8 with same integer value
    def test_base8(self):
        self.assertEqual(convert(8,8),"10")

    #tests base 9 with large value
    def test_base9(self):
        self.assertEqual(convert(10000,9),"14641")

    #tests base 10 with same integer value
    def test_base10(self):
        self.assertEqual(convert(0,10),"0")

    #tests A remainder
    def test_base11(self):
        self.assertEqual(convert(2900,11),"21A7")

    #tests B remainder
    def test_base12(self):
        self.assertEqual(convert(671,12),"47B")

    #tests C remainder
    def test_base13(self):
        self.assertEqual(convert(500,13),"2C6")

    #tests D remainder        
    def test_base14(self):
        self.assertEqual(convert(184,14),"D2")

    #tests E remainder
    def test_base15(self):
        self.assertEqual(convert(210,15),"E0")

    #tests F remainder  
    def test_base16(self):
        self.assertEqual(convert(783,16),"30F")        

    
        
if __name__ == "__main__":
        unittest.main()
