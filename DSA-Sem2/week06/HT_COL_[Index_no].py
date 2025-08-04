class Pair:
    def __init__(self, k, val):
        # Store a key and its associated value
        self.key = k
        self.value = val

class HashTable:
    def __init__(self, size, m2):
        # Total number of slots in the table
        self.size = size
        # Secondary modulus for computing probe step (e.g., last two digits)
        self.m2 = m2
        # Initialize all slots to None (empty)
        self.table = [None] * size
    
    def hash(self, k):
        # Primary hash: key mod table size
        return k % self.size
    
    def probeHash(self, k):
        # Secondary hash: 1 + (key mod m2)
        # Ensures non-zero step for probing
        return 1 + (k % self.m2)
    
    def insert(self, k, val):
        # Starting slot based on primary hash
        start_index = self.hash(k)
        # Step size for probing
        step = self.probeHash(k)
        
        # Try up to size times to find an empty slot
        for i in range(self.size):
            index = (start_index + i * step) % self.size
            # If empty slot found, insert new Pair
            if self.table[index] is None:
                self.table[index] = Pair(k, val)
                return
            # If key already exists, exit without inserting
            elif self.table[index].key == k:
                return
        # Table is full if no empty slot after full probing
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

# Test the implementation with collision handling
last_two_digits = 44
ht = HashTable(20, last_two_digits)
ht.insert(246044, "Dinuka")
ht.insert(246104, "Rithesh")  # Now inserted into next available slot
ht.insert(246060, "Thisath")
ht.insert(246148, "Pasan")
ht.insert(246059, "Manulya")
ht.insert(246066, "Nisira")

# Verify successful searches
print("Search 246044:", ht.search(246044))  # Returns "Dinuka"
print("Search 246104:", ht.search(246104))  # Returns "Rithesh"
