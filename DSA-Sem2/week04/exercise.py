class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

    def insert(self, value):
        """Inserts a new value in the BST"""
        if value < self.value:
            if self.left is None:
                self.left = Node(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = Node(value)
            else:
                self.right.insert(value)

    def in_order_traversal(self):
        """Left -> Root -> Right"""
        if self.left:
            self.left.in_order_traversal()
        print(self.value, end=" ")
        if self.right:
            self.right.in_order_traversal()

    def pre_order_traversal(self):
        """Root -> Left -> Right"""
        print(self.value, end=" ")
        if self.left:
            self.left.pre_order_traversal()
        if self.right:
            self.right.pre_order_traversal()

    def post_order_traversal(self):
        """Left -> Right -> Root"""
        if self.left:
            self.left.post_order_traversal()
        if self.right:
            self.right.post_order_traversal()
        print(self.value, end=" ")


# Let's build a BST from scratch
print("Building a BST...")
root = Node(50)  # This becomes our root node
values_to_insert = [30, 70, 20, 40, 60, 80]

for value in values_to_insert:
    root.insert(value)

# Visual representation of the BST we built:
#        50
#      /    \
#    30      70
#   /  \    /  \
# 20   40 60   80

print("\nIn-order traversal (sorted order):", end=" ")
root.in_order_traversal()  # Output: 20 30 40 50 60 70 80

print("\nPre-order traversal:", end=" ")
root.pre_order_traversal()  # Output: 50 30 20 40 70 60 80

print("\nPost-order traversal:", end=" ")
root.post_order_traversal()  # Output: 20 40 30 60 80 70 50
print()