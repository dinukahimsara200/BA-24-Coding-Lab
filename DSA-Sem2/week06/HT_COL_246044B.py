class Pair:
    def __init__(self, k, val):
        self.key = k
        self.value = val

class HashTable:
    def __init__(self, size, m2):
        self.size = size
        self.m2 = m2  # Last 2 digits of index number (44)
        self.table = [None] * size
    
    def hash(self, k):
        return k % self.size
    
    def probeHash(self, k):
        return 1 + (k % self.m2)
    
    def insert(self, k, val):
        start_index = self.hash(k)
        step = self.probeHash(k)
        
        for i in range(self.size):
            index = (start_index + i * step) % self.size
            if self.table[index] is None:
                self.table[index] = Pair(k, val)
                return
            elif self.table[index].key == k:
                return  # Key already exists
        print("Hash table is full!")
    
    def search(self, k):
        start_index = self.hash(k)
        step = self.probeHash(k)
        
        for i in range(self.size):
            index = (start_index + i * step) % self.size
            if self.table[index] is None:
                return False
            elif self.table[index].key == k:
                return self.table[index].value
        return False
    
    def delete(self, k):
        start_index = self.hash(k)
        step = self.probeHash(k)
        
        for i in range(self.size):
            index = (start_index + i * step) % self.size
            if self.table[index] is None:
                return  # Key not found
            elif self.table[index].key == k:
                self.table[index] = None
                return

# Test the corrected implementation
last_two_digits = 44 

ht = HashTable(20, last_two_digits)
ht.insert(246044, "Dinuka")
ht.insert(246104, "Rithesh")  # This will now work with collision handling
ht.insert(246060, "Thisath")
ht.insert(246148, "Pasan")
ht.insert(246059, "Manulya")
ht.insert(246066, "Nisira")

print("Search 246044:", ht.search(246044))  # Should return "Dinuka"
print("Search 246104:", ht.search(246104))  # Should return "Rithesh"

# Display table contents
print("\nHash table contents:")
for i, pair in enumerate(ht.table):
    if pair is not None:
        print(f"Index {i}: Key={pair.key}, Value={pair.value}")