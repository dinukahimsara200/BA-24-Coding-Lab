class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.key = value

    def traverse(self):
        if self.left is not None:
            self.left.traverse()       
        print(self.key, end=" ")       
        if self.right is not None:
            self.right.traverse()      

    def insert(self, value):
        if value < self.key:
            if self.left is None:
                self.left = Node(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = Node(value)
            else:
                self.right.insert(value)

    def search(self, value):
        if value == self.key:
            return True
        elif value < self.key:
            if self.left: return self.left.search(value)
        elif value > self.key:
            if self.right: return self.right.search(value)
        return False


root = None

values = [20, 40, 10, 4, 15, 50, 35, 55, 60]
for v in values:
    if root is None:
        root = Node(v)
    else:
        root.insert(v)

print("In-order traversal:", end=" ")
if root is not None:
    root.traverse()
print()  

print("Search for 15:", root.search(15))  
print("Search for 52:", root.search(52))  

# https://github.com/dinukahimsara200/BA-24-Coding-Lab/blob/335fcbaaf014193fd0962d1556954f04711fa79e/DSA-Sem2/lab03/BST_246044B.py