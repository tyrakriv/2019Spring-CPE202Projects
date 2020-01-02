import unittest
import filecmp
from huffman import *
import subprocess

class TestList(unittest.TestCase):
    def test_01a_test_file1_parse_header(self):
        f = open('file1_compressed_soln.txt', 'rb')
        header = f.readline()      
        f.close()
        expected = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, \
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, \
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 3, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, \
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, \
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, \
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, \
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.compare_freq_counts(parse_header(header), expected)
        
    def test_01_test_file1_decode(self):
        # Test declaration compressed file as the in fie
        huffman_decode("declaration_compressed_soln.txt", "declaration_decoded.txt")
        err = subprocess.call("diff -wb declaration.txt declaration_decoded.txt", shell = True)
        self.assertEqual(err, 0)

        # Test file 1 compressed file as the in fie
        huffman_decode("file1_compressed_soln.txt", "file1_decoded.txt")
        err = subprocess.call("diff -wb file1.txt file1_decoded.txt", shell = True)
        self.assertEqual(err, 0)

        # Test file2 compressed file as the in fie
        huffman_decode("file2_compressed_soln.txt", "file2_decoded.txt")
        err = subprocess.call("diff -wb file2.txt file2_decoded.txt", shell = True)
        self.assertEqual(err, 0)

        # Test multiline compressed file as the in fie
        huffman_decode("multiline_compressed_soln.txt", "multiline_decoded.txt")
        err = subprocess.call("diff -wb multiline.txt multiline_decoded.txt", shell = True)
        self.assertEqual(err, 0)

        # Test one char out compressed file as the in fie
        huffman_decode("one_char_out_compressed.txt", "one_char_out_decoded.txt")
        err = subprocess.call("diff -wb one_char.txt one_char_out_decoded.txt", shell = True)
        self.assertEqual(err, 0)

        # # Test empty file compressed file as the in fie
        # huffman_decode("empty_file_out.txt", "empty_decoded.txt")
        # err = subprocess.call("diff -wb empty_file_out.txt empty_decoded.txt", shell = True)
        # self.assertEqual(err, 0)

    def compare_freq_counts(self, freq, exp):
        for i in range(256):
            stu = 'Frequency for ASCII ' + str(i) + ': ' + str(freq[i])
            ins = 'Frequency for ASCII ' + str(i) + ': ' + str(exp[i])
            self.assertEqual(stu, ins)
                
if __name__ == '__main__': 
   unittest.main()
