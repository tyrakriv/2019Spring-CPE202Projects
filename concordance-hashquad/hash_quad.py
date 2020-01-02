class Hash:

    def __init__(self, key, value):
        self.key = key
        self.value = value


class HashTable:

    def __init__(self, table_size = 191):   # can add additional attributes
        self.table_size = table_size        # initial table size
        self.hash_table = [None]*table_size # hash table
        self.num_items = 0                  # empty hash table

    def insert(self, key, value=None):
        ''' Inserts an entry into the hash table (using Horner hash function to determine index, 
        and quadratic probing to resolve collisions).
        The key is a string (a word) to be entered, and value is any object (e.g. Python List).
        If the key is not already in the table, the key is inserted along with the associated value
        If the key is is in the table, the new value replaces the existing value.
        If load factor is greater than 0.5 after an insertion, hash table size should be increased (doubled + 1).'''
        hash = Hash(key,value)
        index = self.horner_hash(key)

        self.hash_table[index] = hash
        
        self.num_items += 1
        
        factor = self.get_load_factor()

        if factor >= 0.5:
            old = HashTable(self.table_size)
            old.table_size = self.table_size
            old.hash_table = self.hash_table
            old.num_items = self.num_items

            self.table_size = self.table_size*2 + 1
            self.num_items = 0
            self.hash_table = [None]*self.table_size # hash table

            for i in range(old.table_size):
                if old.hash_table[i] is not None:
                    self.insert(old.hash_table[i].key, old.hash_table[i].value)

            


    def horner_hash(self, key):
        ''' Compute and return an integer from 0 to the (size of the hash table) - 1
        Compute the hash value by using Horner’s rule, as described in project specification.'''
        sum = index = origindex = 0
        count = 1
        n = len(key)
        if n > 8:
            n = 8
        for i in range(n):
            sum += ord(str(key[i])) * (31 ** (n-1-i))
        index = sum % self.table_size

        origindex = index
        while self.hash_table[index] is not None:
            if self.hash_table[index].key == key:
                break

            index = count**2 + origindex
            count += 1
            if (index) >= self.table_size:
                index = (index) % self.table_size 

        return index

    def in_table(self, key):
        ''' Returns True if key is in an entry of the hash table, False otherwise.'''
        index = self.horner_hash(key)
        if self.hash_table[index] is not None:
            if key == self.hash_table[index].key:
                return True
        return False

    def get_index(self, key):
        ''' Returns the index of the hash table entry containing the provided key. 
        If there is not an entry with the provided key, returns None.'''
        index = self.horner_hash(key)
        if self.hash_table[index] is None:
            return None
        if self.hash_table[index].key is key:
            return index
        # return None
        

    def get_all_keys(self):
        ''' Returns a Python list of all keys in the hash table.'''
        key_list = []
        for i in range(len(self.hash_table)):
            if self.hash_table[i] is not None:
                key_list.append(self.hash_table[i].key)
        return key_list

    def get_value(self, key):
        ''' Returns the value associated with the key. 
        If key is not in hash table, returns None.'''
        index = self.horner_hash(key)
        if self.hash_table[index] is not None:
            if self.hash_table[index].key == key:
                return self.hash_table[index].value
        return None

    def get_num_items(self):
        ''' Returns the number of entries in the table.'''
        return self.num_items

    def get_table_size(self):
        ''' Returns the size of the hash table.'''
        return self.table_size

    def get_load_factor(self):
        ''' Returns the load factor of the hash table (entries / table_size).'''
        return self.num_items / self.table_size

