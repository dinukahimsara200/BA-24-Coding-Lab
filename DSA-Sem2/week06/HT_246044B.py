class Pair:
    def __init__(self, k, val):
        self.key = k
        self.value = val

class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size
    
    # Activity 1: Basic hash function (k mod m)
    def hash(self, k):
        return k % self.size
    
    # Activity 2: Insert without collision handling
    def insert(self, k, val):
        index = self.hash(k)
        if self.table[index] is None:
            self.table[index] = Pair(k, val)
    
    # Activity 3: Search method
    def search(self, k):
        index = self.hash(k)
        if self.table[index] is None:
            return False
        elif self.table[index].key == k:
            return self.table[index].value
        return False
    
    # Activity 4: Delete method
    def delete(self, k):
        index = self.hash(k)
        if self.table[index] is not None and self.table[index].key == k:
            self.table[index] = None


# Activity 5: Create hash table and insert data
ht = HashTable(20)
ht.insert(246044, "Dinuka")
ht.insert(246060, "Thisath")
ht.insert(246148, "Pasan")
ht.insert(246059, "Manulya")
ht.insert(246066, "Nisira")

ht.insert(246104, "Rithesh") # Collison ( 44 <-> 104 same hash)

# Activity 6: Search for index number
print("Search 246044:", ht.search(246044))

print("Search 246104:", ht.search(246104)) # False (Coliision when inserting)

# Deletion
ht.delete(246060)
print(ht.search(246060))