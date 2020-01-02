from hash_quad import *
import string

class Concordance:

    def __init__(self):
        self.stop_table = None  # hash table for stop words
        self.concordance_table = None  # hash table for concordance

    def load_stop_table(self, filename):
        """ Read stop words from input file (filename) and insert each word as a key into the stop words hash table.
        Starting size of hash table should be 191: self.stop_table = HashTable(191)
        If file does not exist, raise FileNotFoundError"""
        try:
            # for loop 
            fin = open(filename, 'r')
            # lines = fin.readlines()
            # self.stop_table = HashTable()

            # for i in lines:
            #     i = i.strip()
            #     self.stop_table.insert(str(i))

            self.stop_table = HashTable()
            for line in fin:
                line = line.strip()
                self.stop_table.insert(str(line))


            
            fin.close()
        except FileNotFoundError:
            raise FileNotFoundError

    def load_concordance_table(self, filename):
        """ Read words from input text file (filename) and insert them into the concordance hash table, 
        after processing for punctuation, numbers and filtering out words that are in the stop words hash table.
        Do not include duplicate line numbers (word appearing on same line more than once, just one entry for that line)
        Starting size of hash table should be 191: self.concordance_table = HashTable(191)
        If file does not exist, raise FileNotFoundError"""

        try:
            fin = open(filename, 'r')

            self.concordance_table = HashTable()

            count = 0
            word_list = []

            for line in fin:
                line = line.lower() 
                line = line.strip()
                
                count += 1

                stringpunc = '!#$%&"()*+,-./:;<=>?@[\]^_`{|}~'
                stringnum = '0123456789'

                translatorpunc = line.maketrans(stringpunc,' '* len(stringpunc))
                translatordig = line.maketrans(stringnum,' '*len(stringnum))

                line = line.translate(translatorpunc)
                line = line.translate(translatordig)

                if "'" in line:
                    line = line.replace("'", '')

                word_list = line.split(' ')
                
                word_list = set(word_list)
                word_list = list(word_list)

                for i in range(len(word_list)):    
                    if self.concordance_table.in_table(word_list[i]) == True:
                        if str(count) not in str(self.concordance_table.get_value(word_list[i])):
                            self.concordance_table.insert(word_list[i], ((str(self.concordance_table.get_value(word_list[i]))) + ' ' + str(count)))
                    elif not self.stop_table.in_table(word_list[i]) and word_list[i] is not '':
                        self.concordance_table.insert(word_list[i], str(count))                        
                    
            fin.close()

        except FileNotFoundError:
            raise FileNotFoundError


    def write_concordance(self, filename):
        """ Write the concordance entries to the output file(filename)
        See sample output files for format."""
        fout = open(filename, 'w')

        list_alph= []
                
        for i in range(self.concordance_table.table_size):
            if self.concordance_table.hash_table[i] is not None:
                list_alph.append(str(self.concordance_table.hash_table[i].key))

        list_alph.sort()
        for i in range(len(list_alph)):
            if i == len(list_alph) - 1 and list_alph[i] is not '':
                fout.write(list_alph[i] + ': ' + self.concordance_table.get_value(list_alph[i]) )
            elif list_alph[i] is not None:
                fout.write(list_alph[i] + ': ' + self.concordance_table.get_value(list_alph[i]) + '\n')
                
        fout.close()


