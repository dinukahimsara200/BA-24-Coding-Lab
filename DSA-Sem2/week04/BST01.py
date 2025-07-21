# funtions outside the class
class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.key = value

# Activity 1: In-order traversal (Left -> Root -> Right)
def traverse(node):
    if node is not None:
        traverse(node.left)       # Visit left child
        print(node.key, end=" ")  # Print current node
        traverse(node.right)      # Visit right child

# Activity 2: Insert values into the BST
def insert(node, value):
    if node is None:
        new_node = Node(value)
        return new_node
    else:
        if value < node.key:
            node.left = insert(node.left, value)
        else:
            node.right = insert(node.right, value)
        return node

# Activity 4: Search for a value in the BST
def search(node, value):
    if node is None:
        return False
    else:
        if value == node.key:
            return True
        else:
            if value < node.key:
                return search(node.left, value)
            else:
                return search(node.right, value)

# Step 1: Start with an empty tree
root = None

# Step 2: Insert all the values
values = [20, 40, 10, 4, 15, 50, 35, 55, 60]
for v in values:
    root = insert(root, v)

# Step 3: Traverse the tree (should print in sorted order)
print("In-order traversal:", end=" ")
traverse(root)
print()  # For a new line after traversal

# Step 4: Search for two values
print("Search for 15:", search(root, 15))  # Should return True
print("Search for 52:", search(root, 52))  # Should return False