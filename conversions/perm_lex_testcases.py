import unittest
import perm_lex

class TestAssign1(unittest.TestCase):

    def test_perm_gen_lex(self):
        #tests general alphabetical format
        self.assertEqual(perm_lex.perm_gen_lex('ab'),['ab','ba'])
        #tests empty string
        self.assertEqual(perm_lex.perm_gen_lex(''),[])
        #tests a string with one character
        self.assertEqual(perm_lex.perm_gen_lex('a'),['a'])
        #tests a string with multiple characters
        self.assertEqual(perm_lex.perm_gen_lex('abc'),['abc','acb','bac','bca','cab','cba'])
        #tests uppercase
        self.assertEqual(perm_lex.perm_gen_lex('AB'),['AB','BA'])
        #tests with a number
        self.assertEqual(perm_lex.perm_gen_lex('ab1'),['ab1','a1b','ba1','b1a','1ab','1ba'])
        #tests letters at the end of the alphabet
        self.assertEqual(perm_lex.perm_gen_lex('xy'),['xy','yx'])
        #tests letters out of order
        self.assertEqual(perm_lex.perm_gen_lex('di'),['di','id'])


if __name__ == "__main__":
        unittest.main()
