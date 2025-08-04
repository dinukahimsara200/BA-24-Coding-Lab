class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

    def insert(self, value):
        """Insert a new value in the BST (uses recursion)."""
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

    def search(self, value):
        """Search for a value (returns True if found, uses recursion)."""
        if self.value == value:
            return True
        elif value < self.value and self.left:
            return self.left.search(value)
        elif value > self.value and self.right:
            return self.right.search(value)
        else:
            return False

    def in_order_traversal(self):
        """Print values in sorted order: Left -> Root -> Right (recursive)."""
        if self.left:
            self.left.in_order_traversal()
        print(self.value, end=" ")
        if self.right:
            self.right.in_order_traversal()

    def pre_order_traversal(self):
        """Root -> Left -> Right (recursive)."""
        print(self.value, end=" ")
        if self.left:
            self.left.pre_order_traversal()
        if self.right:
            self.right.pre_order_traversal()

    def post_order_traversal(self):
        """Left -> Right -> Root (recursive)."""
        if self.left:
            self.left.post_order_traversal()
        if self.right:
            self.right.post_order_traversal()
        print(self.value, end=" ")

    def find_min(self):
        """Find the smallest value (go left until no more left)."""
        current = self
        while current.left:
            current = current.left
        return current.value

    def delete(self, value):
        """
        Delete a value from BST.
        Returns the modified subtree (or None if value not found).
        """
        if value < self.value:
            if self.left:
                self.left = self.left.delete(value)
            else:
                print(f"Warning: Value {value} not found in the tree.")
        elif value > self.value:
            if self.right:
                self.right = self.right.delete(value)
            else:
                print(f"Warning: Value {value} not found in the tree.")
        else:
            # Found the node to delete
            # Case 1: No children (leaf node)
            if not self.left and not self.right:
                return None
            # Case 2: One child
            if not self.left:
                return self.right
            if not self.right:
                return self.left
            # Case 3: Two children
            # Replace with smallest value from right subtree
            self.value = self.right.find_min()
            self.right = self.right.delete(self.value)
        return self


# Example usage
def main():
    # Create BST from a single list
    values = [50, 30, 70, 20, 40, 60, 80]
    root = Node(values[0])
    for value in values[1:]:
        root.insert(value)

    print("\nIn-order traversal (sorted order):", end=" ")
    root.in_order_traversal()

    print("\n\nPre-order traversal:", end=" ")
    root.pre_order_traversal()

    print("\n\nPost-order traversal:", end=" ")
    root.post_order_traversal()

    print("\n\nSearching for values:")
    print(f"Search 40: {root.search(40)}")  # True
    print(f"Search 99: {root.search(99)}")  # False

    print("\nMinimum value in the tree:", root.find_min())

    print("\nDeleting 20 (leaf node)...")
    root = root.delete(20)
    print("After deletion (in-order):", end=" ")
    root.in_order_traversal()

    print("\n\nDeleting 30 (node with two children)...")
    root = root.delete(30)
    print("After deletion (in-order):", end=" ")
    root.in_order_traversal()

    print("\n\nAttempting to delete non-existent value (99)...")
    root = root.delete(99)  # Will print a warning

if __name__ == "__main__":
    main()