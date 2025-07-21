class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.key = value

    def in_order_traversal(self):
        if self.left is not None:
            self.left.in_order_traversal()       
        print(self.key, end=" ")       
        if self.right is not None:
            self.right.in_order_traversal()

    def pre_order_traversal(self):
        print(self.key, end=" ")       
        if self.left is not None:
            self.left.pre_order_traversal()       
        if self.right is not None:
            self.right.pre_order_traversal()

    def post_order_traversal(self):
        if self.left is not None:
            self.left.post_order_traversal()       
        if self.right is not None:
            self.right.post_order_traversal()       
        print(self.key, end=" ")
    
root = Node(7)
root.left = Node(3)
root.right = Node(8)
root.left.left = Node(4)
root.left.right = Node(12)
root.left.left.left = Node(11)
root.left.left.right = Node(2)
root.left.right.left = Node(6)
root.left.right.right = Node(5)
root.right.left = Node(1)
root.right.right = Node(9)

print("In-order traversal:", end=" ")
root.in_order_traversal()  # Output: 11 4 2 3 6 5 12 7 1 8 9
print()

print("Pre-order traversal:", end=" ")
root.pre_order_traversal() # Output: 7 3 4 11 2 12 6 5 8 1 9
print()

print("Post-order traversal:", end=" ")
root.post_order_traversal() # Output: 11 2 4 6 5 12 3 1 9 8 7
print()