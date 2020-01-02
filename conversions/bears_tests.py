import unittest
from bears import *

class TestAssign1(unittest.TestCase):
    #tests high, true number value
    def test_bear_01(self):
        self.assertTrue(bears(208))
        self.assertTrue(bears(250))

    #tests 42 bears
    def test_bear_02(self):
        self.assertTrue(bears(42))

    #tests prime number
    def test_bear_03(self):
        self.assertFalse(bears(53))

    #tests number less than 42
    def test_bear_04(self):
        self.assertFalse(bears(41))

    #tests 0 bears
    def test_bear_05(self):
        self.assertFalse(bears(0))

    #tests non-prime number
    def test_bear_07(self):
        self.assertFalse(bears(4))

    #tests true statement with large number
    def test_bear_08(self):
        self.assertTrue(bears(7344000))

    #tests with very small, prime number
    def test_bear_09(self):
        self.assertFalse(bears(1))
        
if __name__ == "__main__":
    unittest.main()
