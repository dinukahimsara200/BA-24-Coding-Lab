class Pair:
    def __init__(self, k, val):
        self.key = k
        self.value = val

class HashTable:
    def __init__(self, size, m2):
        self.size = size
        self.m2 = m2  # Last 2 digits of your index (44)
        self.table = [None] * size
    
    def hash(self, k):
        return k % self.size  # Primary hash: maps key to initial index
    
    def probeHash(self, k):
        return 1 + (k % self.m2)  # Step size for collision resolution
    
    def insert(self, k, val):
        start_index = self.hash(k)  # Initial position
        step = self.probeHash(k)    # Probe step size
        
        for i in range(self.size):
            # Double hashing: (start_index + i*step) mod table_size
            index = (start_index + i * step) % self.size
            # Example for 246104: 
            #   i=0: (4 + 0*13) % 20 = 4 -> occupied
            #   i=1: (4 + 1*13) % 20 = 17 -> empty (store here)
            if self.table[index] is None:
                self.table[index] = Pair(k, val)
                return
            elif self.table[index].key == k:
                return  # Key exists (no duplicate)
        print("Hash table is full!")
    
    def search(self, k):
        start_index = self.hash(k)
        step = self.probeHash(k)
        
        # Probe until empty slot or key found
        for i in range(self.size):
            index = (start_index + i * step) % self.size
            # Empty slot means key not present
            if self.table[index] is None:
                return False
            # Return value if key matches
            elif self.table[index].key == k:
                return self.table[index].value
        # Exhausted all slots, key not found
        return False
    
    def delete(self, k):
        start_index = self.hash(k)
        step = self.probeHash(k)
        
        # Probe to find the key for deletion
        for i in range(self.size):
            index = (start_index + i * step) % self.size
            # Empty slot means key not present
            if self.table[index] is None:
                return
            # If key matches, remove it by setting to None
            elif self.table[index].key == k:
                self.table[index] = None
                return


# Test with your data
last_two_digits = 44  # From your index 246044

ht = HashTable(20, last_two_digits)
ht.insert(246044, "Dinuka")    # Primary hash: 246044%20=4 → stored at 4
ht.insert(246104, "Rithesh")   # Collision resolved: stored at 17
ht.insert(246060, "Thisath")   # 246060%20=0 → stored at 0
ht.insert(246148, "Pasan")     # 246148%20=8 → stored at 8
ht.insert(246059, "Manulya")   # 246059%20=19 → stored at 19
ht.insert(246066, "Nisira")    # 246066%20=6 → stored at 6

# Verify searches
print("Search 246044:", ht.search(246044))  # "Dinuka" at index 4
print("Search 246104:", ht.search(246104))  # "Rithesh" at index 17

# Display table contents
print("\nHash table contents:")
for i, pair in enumerate(ht.table):
    if pair is not None:
        print(f"Index {i}: Key={pair.key}, Value={pair.value}")