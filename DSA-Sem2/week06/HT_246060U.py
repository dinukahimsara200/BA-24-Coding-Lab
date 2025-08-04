class Pair:
    def __init__(self, k, val):
        self.key = k
        self.value = val

class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size
    
    def hash(self, k):
        return k % self.size
    
    def insert(self, k, val):
        index = self.hash(k)
        if self.table[index] is None:
            self.table[index] = Pair(k, val)
    
    def search(self, k):
        index = self.hash(k)
        if self.table[index] is None:
            return False
        elif self.table[index].key == k:
            return self.table[index].value
        return False
    
    def delete(self, k):
        index = self.hash(k)
        if self.table[index].key == k:
            self.table[index] = None


ht = HashTable(20)
ht.insert(246060, "Thisath")
ht.insert(246044, "Dinuka")
ht.insert(246148, "Pasan")
ht.insert(246059, "Manulya")
ht.insert(246019, "Hasala")

print("Search 246060:", ht.search(246060))

ht.delete(246060)
print("Search 246060:", ht.search(246060)) 