class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.key = value

    def traverse(self): # Activity 1: In-order traversal
        if self.left is not None:
            self.left.traverse()       
        print(self.key)       
        if self.right is not None:
            self.right.traverse()      

    def insert(self, value): # Activity 2: Insert values into the BST
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

    def search(self, value): # Activity 4: Search for a value in the BST
        if value == self.key:
            return True
        elif value < self.key:
            if self.left is None:
                return False
            else:
                return self.left.search(value)
        else:
            if self.right is None:
                return False
            else:
                return self.right.search(value)


root = None

values = [20, 40, 10, 4, 15, 50, 35, 55, 60]
for i in values: # Activity 3: Insert all the values
    if root is None:
        root = Node(i)
    else:
        root.insert(i)

print("In-order traversal:")
if root is not None: # Activity 3: Traverse the tree
    root.traverse()

print("Search for 15:", root.search(15))  
print("Search for 52:", root.search(52))  