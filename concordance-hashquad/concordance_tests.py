import unittest
import filecmp
from concordance import *
from hash_quad import*

class TestList(unittest.TestCase):

    def test_01(self):
        # Tests stop words with file1
       conc = Concordance()
       conc.load_stop_table("stop_words.txt")
       conc.load_concordance_table("file1.txt")
       conc.write_concordance("file1_con.txt")
       self.assertTrue(filecmp.cmp("file1_con.txt", "file1_sol.txt"))

    def test_02(self):
        # Tests stop words with file2
       conc = Concordance()
       conc.load_stop_table("stop_words.txt")
       conc.load_concordance_table("file2.txt")
       conc.write_concordance("file2_con.txt")
       self.assertTrue(filecmp.cmp("file2_con.txt", "file2_sol.txt"))

    def test_03(self):
        # Tests stop words with declaration
       conc = Concordance()
       conc.load_stop_table("stop_words.txt")
       conc.load_concordance_table("declaration.txt")
       conc.write_concordance("declaration_con.txt")
       self.assertTrue(filecmp.cmp("declaration_con.txt", "declaration_sol.txt"))
    
    # def test_04(self):
    #     conc = Concordance()
    #     conc.load_stop_table('stop_words.txt')
    #     conc.load_concordance_table("War_And_Peace.txt")
    #     conc.write_concordance("War_And_Peace_con.txt")

    def test_05(self):
        # Tests if file does not exist
        conc = Concordance()
        with self.assertRaises (FileNotFoundError):
            conc.load_stop_table('stop_words_not_found.txt')
        with self.assertRaises (FileNotFoundError):
            conc.load_concordance_table('filenothere.txt')

    # def test_06(self):
    #     conc = Concordance()
    #     conc.load_stop_table('stop_words.txt')
    #     conc.load_concordance_table("dictionary_a-c.txt")
    #     conc.write_concordance("dictionary_a-c_con.txt")

    def test_07(self):
        # Tests if file is all numbers
        conc = Concordance()
        conc.load_stop_table('stop_words.txt')
        conc.load_concordance_table("digits.txt")
        conc.write_concordance("digits_con.txt")

    def test_08(self):
        # Tests if file is all punctuation characters
        conc = Concordance()
        conc.load_stop_table('stop_words.txt')
        conc.load_concordance_table("punctuation.txt")
        conc.write_concordance("punctuation_con.txt")

    # def test_09(self):
    #     conc = Concordance()
    #     conc.load_stop_table('stop_words2.txt')
    #     conc.load_concordance_table("the.txt")
    #     conc.write_concordance("the_con.txt")

    def test_01a(self):
        ht = HashTable(7)
        ht.insert("cat", 5)
        self.assertEqual(ht.get_table_size(), 7)

    def test_01b(self):
        ht = HashTable(7)
        ht.insert("cat", 5)
        self.assertEqual(ht.get_num_items(), 1)

    def test_01c(self):
        ht = HashTable(7)
        ht.insert("cat", 5)
        self.assertAlmostEqual(ht.get_load_factor(), 1/7)

    def test_01d(self):
        ht = HashTable(7)
        ht.insert("cat", 5)
        self.assertEqual(ht.get_all_keys(), ["cat"])

    def test_01e(self):
        ht = HashTable(7)
        ht.insert("cat", 5)
        self.assertEqual(ht.in_table("cat"), True)

    def test_01f(self):
        ht = HashTable(7)
        ht.insert("cat", 5)
        self.assertEqual(ht.get_value("cat"), 5)

    def test_01g(self):
        ht = HashTable(7)
        ht.insert("cat", 5)
        self.assertEqual(ht.get_index("cat"), 3)

    def test_01h(self):
        ht = HashTable(7)
        ht.insert("cat", 5)
        ht.insert('dog', 4)
        ht.insert('bird', 3)
        ht.insert('chicken', 2)
        self.assertEqual(ht.get_index("cat"), 13)

    def test_01i(self):
        ht = HashTable(7)
        ht.insert("biggerthaneight", 5)
        self.assertEqual(ht.get_index("biggerthaneight"), 1)
        self.assertFalse(ht.in_table('cat'))
        self.assertEqual(ht.get_index('cat'), None)
        self.assertEqual(ht.get_value('cat'), None)

if __name__ == '__main__':
   unittest.main()
