class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.key = value

    def traverse(self):
        """
        In-order traversal: left subtree, node itself, right subtree.
        """
        if self.left:
            self.left.traverse()
        print(self.key, end=' ')
        if self.right:
            self.right.traverse()

    def insert(self, value):
        """
        Insert a new value into the BST. Recursively places it in the correct position.
        """
        if value < self.key:
            if self.left:
                self.left.insert(value)
            else:
                self.left = Node(value)
        elif value > self.key:
            if self.right:
                self.right.insert(value)
            else:
                self.right = Node(value)
        # If value == self.key, do nothing (no duplicates)

    def search(self, value):
        """
        Search for a value in the BST. Returns True if found, False otherwise.
        """
        if value == self.key:
            return True
        elif value < self.key:
            if self.left:
                return self.left.search(value)
            else:
                return False
        else:
            if self.right:
                return self.right.search(value)
            else:
                return False


if __name__ == "__main__":
    # Activity: build and test the BST
    values_to_insert = [20, 40, 10, 4, 15, 50, 35, 55, 60]

    # Create an empty BST by initializing the root with the first value
    root = Node(values_to_insert[0])
    for val in values_to_insert[1:]:
        root.insert(val)

    print("In-order traversal of the BST:")
    root.traverse()
    print("\n")

    # Search tests
    tests = [15, 52]
    for t in tests:
        result = root.search(t)
        print(f"Search for {t}: {result}")
