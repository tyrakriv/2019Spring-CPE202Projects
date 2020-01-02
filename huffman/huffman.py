from huffman_bit_writer import *
from huffman_bit_reader import *

class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char   # stored as an integer - the ASCII character code value
        self.freq = freq   # the freqency associated with the node
        self.left = None   # Huffman tree (node) to the left
        self.right = None  # Huffman tree (node) to the right

    def set_left(self, node):
        self.left = node

    def set_right(self, node):
        self.right = node

    def __lt__(self,other):
        return comes_before(self,other)
    
def comes_before(a, b):
    """Returns True if tree rooted at node a comes before tree rooted at node b, False otherwise"""
    if a.freq < b.freq:
        return True
    elif a.freq > b.freq:
        return False
    else:
        if a.char < b.char:
            return True
        else:
            return False
    
def combine(a, b):
    """Creates and returns a new Huffman node with children a and b, with the "lesser node" on the left
    The new node's frequency value will be the sum of the a and b frequencies
    The new node's char value will be the lesser of the a and b char ASCII values"""
    newfreq = a.freq + b.freq
    if a.char < b.char:
        newchar = a.char
    else:
        newchar = b.char
    newnode = HuffmanNode(newchar,newfreq)
    newnode.set_right(b)
    newnode.set_left(a)

    return newnode

def cnt_freq(filename):
    """Opens a text file with a given file name (passed as a string) and counts the 
    frequency of occurrences of all the characters within that file"""
    lstfreq = [0]*256
    fin = open(filename, 'r')
    for line in fin:
        for i in range(len(line)):
            ch = line[i]
            lstfreq[ord(ch)] = 1 + lstfreq[ord(ch)]
    fin.close()
    return lstfreq


            
def create_huff_tree(char_freq):
    """Create a Huffman tree for characters with non-zero frequency
    Returns the root node of the Huffman tree"""
    lstnode = []
    if char_freq == [0]*256:
        return None
    for i in range(len(char_freq)):
        if char_freq[i] != 0:
            node = HuffmanNode(i,char_freq[i])
            lstnode.append(node)
    lstnode.sort()
        
    while len(lstnode) > 1:
        left = lstnode.pop(0)
        right = lstnode.pop(0)
        newnode = combine(left,right)
        lstnode.append(newnode)
        lstnode.sort()
    return lstnode[0]
    
def create_code(node):
    """Returns an array (Python list) of Huffman codes. For each character, use the integer ASCII representation 
    as the index into the arrary, with the resulting Huffman code for that character stored at that location"""
    lst = ['']*256
    return create_code_helper(node,lst,'')
            
def create_code_helper(node,lst,code):

    if node is None:
        return lst
    if node.left is not None:
        create_code_helper(node.left,lst,code+'0')
    if node.right is not None:
        create_code_helper(node.right,lst,code+'1')    
    else:
        lst[node.char] = code
    
    return lst
    
        
def create_header(freqs):
    """Input is the list of frequencies. Creates and returns a header for the output file
    Example: For the frequency list asscoaied with "aaabbbbcc, would return “97 3 98 4 99 2” """
    retstr = ''
    for i in range(len(freqs)):
        if freqs[i] is not 0:
            retstr = retstr + str(i) + ' ' + str(freqs[i]) + ' '
    
    return retstr[:-1]

def huffman_encode(in_file, out_file):
    """Takes inout file name and output file name as parameters - both files will have .txt extensions
    Uses the Huffman coding process on the text from the input file and writes encoded text to output file
    Also creates a second output file which adds _compressed before the .txt extension to the name of the file.
    This second file is actually compressed by writing individual 0 and 1 bits to the file using the utility methods 
    provided in the huffman_bits_io module to write both the header and bits.
    Take not of special cases - empty file and file with only one unique character"""
    codelist = []
    end = code = ''
    count = 0
    try:
        fin = open(in_file,'r')
        
        lstfreq = cnt_freq(in_file)
        head = create_header(lstfreq)
        node = create_huff_tree(lstfreq)
        codelist = create_code(node)
        
        for line in fin:
            count += 1
            for i in range(len(line)):
                ch = line[i]
                code = codelist[ord(ch)]
                end = end + code
                
        fout = open(out_file,'w')

        if head == '':
            fin.close()
            fout.close()
            
        else:
            fout.write(head + '\n')

            fout.write(end)

            newname = in_file[:-4] + '_out_compressed.txt'
            comp = HuffmanBitWriter(newname)
            
            comp.write_str(head + '\n')

            comp.write_code(end)

            comp.close()
            
            fin.close()
            fout.close()

    except FileNotFoundError:
        raise FileNotFoundError

def huffman_decode(encoded_file, decode_file):
    try:
        fout = open(decode_file, 'w')
        dec = HuffmanBitReader(encoded_file)
        header = dec.read_str()
        head_freq = parse_header(header)
        node = create_huff_tree(head_freq)

        numofchar = 0
        header_list = header.split()
 
        
        count = 1
        while count < (len(header_list)):
            numofchar = numofchar + int(header_list[count])
            count += 2
        
        count = 0
        current = node
        while count < numofchar:
            if current.right == None and current.left == None:
                fout.write(chr(current.char))
                count += 1
                current = node
            
            else:
                boo = dec.read_bit()
                if boo:
                    current = current.right
                else:
                    current = current.left

        dec.close()
        fout.close()
                
    except FileNotFoundError:
        raise FileNotFoundError

def parse_header(header):
    print(header)
    header_list = header.split()
    head_freq = [0]*256
    loop = (len(header_list))
    for i in range(0,loop, 2):
        head_freq[int(header_list[i])] = int(header_list[i+1])
    print(head_freq)
    return head_freq
