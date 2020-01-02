import unittest
from hash_quad import *

class TestList(unittest.TestCase):

    def test_01a(self):
        # Tests if implementation of hash table is correct
        ht = HashTable(7)
        ht.insert("cat", 5)
        self.assertEqual(ht.get_table_size(), 7)

    def test_01b(self):
        # Tests for number of items in hash table
        ht = HashTable(7)
        ht.insert("cat", 5)
        self.assertEqual(ht.get_num_items(), 1)

    def test_01c(self):
        # Tests for correct load factor
        ht = HashTable(7)
        ht.insert("cat", 5)
        self.assertAlmostEqual(ht.get_load_factor(), 1/7)

    def test_01d(self):
        # Tests for all key values
        ht = HashTable(7)
        ht.insert("cat", 5)
        self.assertEqual(ht.get_all_keys(), ["cat"])

    def test_01e(self):
        # Tests if a key is in the table
        ht = HashTable(7)
        ht.insert("cat", 5)
        self.assertEqual(ht.in_table("cat"), True)

    def test_01f(self):
        # Tests if value of cat is correct
        ht = HashTable(7)
        ht.insert("cat", 5)
        self.assertEqual(ht.get_value("cat"), 5)

    def test_01g(self):
        # Tests if the index is correct
        ht = HashTable(7)
        ht.insert("cat", 5)
        self.assertEqual(ht.get_index("cat"), 3)

    def test_01h(self):
        # Tests for load factor overload
        ht = HashTable(7)
        ht.insert("cat", 5)
        ht.insert('dog', 4)
        ht.insert('bird', 3)
        ht.insert('chicken', 2)
        self.assertEqual(ht.get_index("cat"), 13)

    def test_01i(self):
        # Tests when key is larger than eight characters
        ht = HashTable(7)
        ht.insert("biggerthaneight", 5)
        self.assertEqual(ht.get_index("biggerthaneight"), 1)
        self.assertFalse(ht.in_table('cat'))
        self.assertEqual(ht.get_index('cat'), None)
        self.assertEqual(ht.get_value('cat'), None)

if __name__ == '__main__':
   unittest.main()
