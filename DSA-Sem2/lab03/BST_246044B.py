class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.key = value  # Fixed the syntax error from original code
    
    def traverse(self):
        """
        Activity 1: In-order traversal of the tree
        In-order: Left -> Root -> Right
        This will give us sorted order for BST
        """
        result = []
        
        # Traverse left subtree
        if self.left:
            result.extend(self.left.traverse())
        
        # Visit root (current node)
        result.append(self.key)
        
        # Traverse right subtree
        if self.right:
            result.extend(self.right.traverse())
        
        return result
    
    def insert(self, value):
        """
        Activity 2: Insert a value into the BST
        BST property: left child < parent < right child
        """
        if value < self.key:
            # Insert to the left
            if self.left is None:
                self.left = Node(value)
            else:
                self.left.insert(value)
        else:
            # Insert to the right (includes equal values)
            if self.right is None:
                self.right = Node(value)
            else:
                self.right.insert(value)
    
    def search(self, value):
        """
        Activity 4: Search for a value in the BST
        Returns True if found, False otherwise
        """
        if value == self.key:
            return True
        elif value < self.key:
            # Search in left subtree
            if self.left:
                return self.left.search(value)
            else:
                return False
        else:
            # Search in right subtree
            if self.right:
                return self.right.search(value)
            else:
                return False
    
    def print_tree(self, level=0, prefix="Root: "):
        """
        Helper function to visualize the tree structure
        """
        print(" " * (level * 4) + prefix + str(self.key))
        if self.left:
            self.left.print_tree(level + 1, "L--- ")
        if self.right:
            self.right.print_tree(level + 1, "R--- ")


print("=== Binary Search Tree Implementation ===\n")

# 1. Create an empty BST (start with root node)
print("1. Creating BST with root node...")
root = Node(20)  # First value becomes root
print(f"Root created with value: {root.key}\n")

# 2. Insert the remaining values
print("2. Inserting values: 40, 10, 4, 15, 50, 35, 55, 60")
values_to_insert = [40, 10, 4, 15, 50, 35, 55, 60]

for value in values_to_insert:
    root.insert(value)
    print(f"Inserted: {value}")

print("\nTree structure:")
root.print_tree()

# 3. Traverse the tree (in-order traversal)
print("\n3. In-order traversal of the tree:")
traversal_result = root.traverse()
print(f"Traversal result: {traversal_result}")
print("Note: In-order traversal of BST gives sorted order")

# 4. Search for values 15 and 52
print("\n4. Searching for values:")

search_value_1 = 15
found_1 = root.search(search_value_1)
print(f"Search for {search_value_1}: {'Found' if found_1 else 'Not Found'}")

search_value_2 = 52
found_2 = root.search(search_value_2)
print(f"Search for {search_value_2}: {'Found' if found_2 else 'Not Found'}")

# Additional demonstration
print("\n=== Additional Demonstrations ===")

# Activity 3: Create a separate tree and test
print("\nActivity 3: Creating a separate small tree for testing:")
test_root = Node(10)
test_root.insert(5)
test_root.insert(15)
test_root.insert(3)
test_root.insert(7)

print("Small test tree structure:")
test_root.print_tree()

print(f"Small tree traversal: {test_root.traverse()}")

# Test edge cases
print("\n=== Edge Case Testing ===")
single_node = Node(42)
print(f"Single node traversal: {single_node.traverse()}")
print(f"Search in single node (42): {single_node.search(42)}")
print(f"Search in single node (99): {single_node.search(99)}")