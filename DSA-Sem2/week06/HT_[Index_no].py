class Pair:
    def __init__(self, k, val):
        # Store a key and its associated value
        self.key = k
        self.value = val

class HashTable:
    def __init__(self, size):
        # Total number of slots in the table
        self.size = size
        # Initialize all slots to None (empty)
        self.table = [None] * size
    
    # Activity 1: Basic hash function (k mod size)
    def hash(self, k):
        # Compute index by taking remainder of key divided by table size
        return k % self.size
    
    # Activity 2: Insert without collision handling
    def insert(self, k, val):
        # Determine slot index for this key
        index = self.hash(k)
        # Only insert if slot is empty
        if self.table[index] is None:
            self.table[index] = Pair(k, val)
    
    # Activity 3: Search method
    def search(self, k):
        index = self.hash(k)
        # If slot is empty, key is not present
        if self.table[index] is None:
            return False
        # If key matches, return its value
        elif self.table[index].key == k:
            return self.table[index].value
        # In case of mismatch (collision), also return False
        return False
    
    # Activity 4: Delete method
    def delete(self, k):
        index = self.hash(k)
        # Remove key only if it matches at computed slot
        if self.table[index] is not None and self.table[index].key == k:
            self.table[index] = None


# Activity 5: Create and populate hash table
ht = HashTable(20)
ht.insert(246044, "Dinuka")
ht.insert(246060, "Thisath")
ht.insert(246148, "Pasan")
ht.insert(246059, "Manulya")
ht.insert(246066, "Nisira")

# Attempt to insert key that hashes to an occupied slot
ht.insert(246104, "Rithesh")  # Collision: same index as 246044

# Activity 6: Demonstrate search and deletion
print("Search 246044:", ht.search(246044))  # Should find "Dinuka"
print("Search 246104:", ht.search(246104))  # Fails due to no collision handling
ht.delete(246060)                         # Remove entry with key 246060
print(ht.search(246060))                  # Now returns False