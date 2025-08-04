class Pair:
    def __init__(self, k, val):
        self.key = k
        self.value = val

class HashTable:
    def __init__(self, size, m2):
        self.size = size
        self.m2 = m2  
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
                return  
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
                return  
            elif self.table[index].key == k:
                self.table[index] = None
                return


last_two_digits = 60

ht = HashTable(20, last_two_digits)
ht.insert(246060, "Thisath")
ht.insert(246044, "Dinuka")
ht.insert(246148, "Pasan")
ht.insert(246059, "Manulya")
ht.insert(246100, "Vihanga") # Collision

print("Search 246060:", ht.search(246060))  
print("Search 246100:", ht.search(246100))  