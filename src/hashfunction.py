# implement a simple hash
class HashTable(object):            # create an empty HashTable()
    def __init__(self):
        self.hash_table = {}
    def __str__(self):              # nice printing
        string = ""
        for key,val in self.hash_table.items():
            string += str(key) + ": " + str(val) + "\n"
        return string

class HashFunction(object):         # Make changes to the HashTable()
    def __init__(self, ht, key, val):
        self.ht = ht
        self.key_str = str(key)
        self.val = val
        self.key = self.fnv_hash_key()
        self.add_entry()
    def __str__(self):              # call HashTable() print
        return str(self.ht)
    def fnv_hash_key(self):         # use FNV algorithm
        h = 2166136261
        for i in self.key_str:
            h = (h * 16777619) ^ ord(i)
        return h
    def add_entry(self):            # add an entry to the HashTable()
        self.ht.hash_table[str(self.key)] = self.val
      
# some examples      
def main():
    ht = HashTable()
    HashFunction(ht, "one", "one")
    HashFunction(ht, "two", "two")
    HashFunction(ht, "three", "three")
    HashFunction(ht, 15, 30)
    HashFunction(ht, 200000, 2)
    HashFunction(ht, 200000, 2)    # silently ignores dual entries
    HashFunction(ht, 3.456, 9)     # works over many types
  #  HashFunction(ht, ht, "hashtable obj")   # will hash objects (key is ridiculously long hence commented out)
    print(str(ht))

main()