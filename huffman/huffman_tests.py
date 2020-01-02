import unittest
import filecmp
import subprocess
from huffman import *

class TestList(unittest.TestCase):
    # tests the frequency list returned from cnt_freq function
    def test_cnt_freq(self):
        freqlist	= cnt_freq("file2.txt")
        anslist = [2, 4, 8, 16, 0, 2, 0] 
        self.assertListEqual(freqlist[97:104], anslist)

        freqlist = cnt_freq("empty_file.txt")
        anslist = [0, 0, 0, 0, 0, 0, 0]
        self.assertListEqual(freqlist[97:104], anslist)

    # tests huff tree implementation
    def test_create_huff_tree(self):
        freqlist = cnt_freq("file2.txt")
        hufftree = create_huff_tree(freqlist)
        self.assertEqual(hufftree.freq, 32)
        self.assertEqual(hufftree.char, 97)
        left = hufftree.left
        self.assertEqual(left.freq, 16)
        self.assertEqual(left.char, 97)
        right = hufftree.right
        self.assertEqual(right.freq, 16)
        self.assertEqual(right.char, 100)

    # tests header function with standard file and file with only one character
    def test_create_header(self):
        freqlist = cnt_freq("file2.txt")
        self.assertEqual(create_header(freqlist), "97 2 98 4 99 8 100 16 102 2")

        freqlist = cnt_freq("one_char.txt")
        self.assertEqual(create_header(freqlist), "97 5")

    # tests create_code function where every character has a unique identity
    def test_create_code(self):
        freqlist = cnt_freq("file2.txt")
        hufftree = create_huff_tree(freqlist)
        codes = create_code(hufftree)
        self.assertEqual(codes[ord('d')], '1')
        self.assertEqual(codes[ord('a')], '0000')
        self.assertEqual(codes[ord('f')], '0001')

        freqlist = cnt_freq("empty_file.txt")
        hufftree = create_huff_tree(freqlist)
        codes = create_code(hufftree)
        self.assertEqual(codes[ord('d')], '')

        
    def test_01_textfile(self):
        huffman_encode("file1.txt", "file1_out.txt")
        # capture errors by running 'diff' on your encoded file with a *known* solution file
        err = subprocess.call("diff -wb file1_out.txt file1_soln.txt", shell = True)
        self.assertEqual(err, 0)
        err = subprocess.call("diff -wb file1_out_compressed.txt file1_compressed_soln.txt", shell = True)
        self.assertEqual(err, 0)

        huffman_encode("file2.txt", "file2_out.txt")
        # capture errors by running 'diff' on your encoded file with a *known* solution file
        err = subprocess.call("diff -wb file2_out.txt file2_soln.txt", shell = True)
        self.assertEqual(err, 0)
        err = subprocess.call("diff -wb file2_out_compressed.txt file2_compressed_soln.txt", shell = True)
        self.assertEqual(err, 0)

        huffman_encode("multiline.txt", "multiline_out.txt")
        # capture errors by running 'diff' on your encoded file with a *known* solution file
        err = subprocess.call("diff -wb multiline_out.txt multiline_soln.txt", shell = True)
        self.assertEqual(err, 0)
        err = subprocess.call("diff -wb multiline_out_compressed.txt multiline_compressed_soln.txt", shell = True)
        self.assertEqual(err, 0)
        
        huffman_encode("declaration.txt", "declaration_out.txt")
        # capture errors by running 'diff' on your encoded file with a *known* solution file
        err = subprocess.call("diff -wb declaration_out.txt declaration_soln.txt", shell = True)
        self.assertEqual(err, 0)
        err = subprocess.call("diff -wb declaration_out_compressed.txt declaration_compressed_soln.txt", shell = True)
        self.assertEqual(err, 0)

        # tests if error is raised when no input file is found
        with self.assertRaises(FileNotFoundError):
            huffman_encode("filetest.txt", "filetest_out.txt")

        # capture errors by running 'diff' on your encoded file with a *known* solution file
        huffman_encode("empty_file.txt", "empty_file_out.txt")
##        err = subprocess.call("diff -wb empty_file_out.txt empty_file_soln.txt", shell = True)
##        self.assertEqual(err, 0)

##        # capture errors by running 'diff' on your encoded file with a *known* solution file
##        huffman_encode("one_char.txt", "one_char_out.txt")
##        err = subprocess.call("diff -wb one_char_out.txt one_char_soln.txt", shell = True)
##        self.assertEqual(err, 0)
        
if __name__ == '__main__': 
   unittest.main()
