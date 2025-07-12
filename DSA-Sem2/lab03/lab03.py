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
        
        HOW IT WORKS:
        1. Recursively visit left subtree first
        2. Then visit current node (root)
        3. Finally recursively visit right subtree
        
        Example: For tree with root=10, left=5, right=15
        - First: traverse(5) -> visits 5
        - Then: visit 10
        - Finally: traverse(15) -> visits 15
        Result: [5, 10, 15] (sorted order)
        """
        result = []
        
        # STEP 1: Traverse left subtree first
        # This ensures all smaller values are visited before current node
        if self.left:
            result.extend(self.left.traverse())  # Recursive call to left child
        
        # STEP 2: Visit current node (root of this subtree)
        # Add current node's value to result
        result.append(self.key)
        
        # STEP 3: Traverse right subtree last
        # This ensures all larger values are visited after current node
        if self.right:
            result.extend(self.right.traverse())  # Recursive call to right child
        
        return result
    
    def insert(self, value):
        """
        Activity 2: Insert a value into the BST
        BST property: left child < parent < right child
        
        HOW IT WORKS:
        1. Compare new value with current node's key
        2. If smaller -> go left, if larger/equal -> go right
        3. If target position is empty -> create new node
        4. If target position has a node -> recursively insert there
        
        Example: Inserting 7 into tree with root=10
        - 7 < 10, so go left
        - If left is empty -> create Node(7) as left child
        - If left has Node(5) -> call insert(7) on Node(5)
        """
        if value < self.key:
            # CASE 1: New value is smaller - goes to LEFT subtree
            if self.left is None:
                # Base case: no left child exists, create new node here
                self.left = Node(value)
                print(f"    Inserted {value} as left child of {self.key}")
            else:
                # Recursive case: left child exists, insert into left subtree
                print(f"    {value} < {self.key}, going left to node {self.left.key}")
                self.left.insert(value)
        else:
            # CASE 2: New value is larger or equal - goes to RIGHT subtree
            if self.right is None:
                # Base case: no right child exists, create new node here
                self.right = Node(value)
                print(f"    Inserted {value} as right child of {self.key}")
            else:
                # Recursive case: right child exists, insert into right subtree
                print(f"    {value} >= {self.key}, going right to node {self.right.key}")
                self.right.insert(value)
    
    def search(self, value):
        """
        Activity 4: Search for a value in the BST
        Returns True if found, False otherwise
        
        HOW IT WORKS:
        1. Compare search value with current node's key
        2. If equal -> found! return True
        3. If smaller -> search left subtree (if exists)
        4. If larger -> search right subtree (if exists)
        5. If subtree doesn't exist -> not found, return False
        
        Example: Searching for 7 in tree with root=10, left=5, right=15
        - 7 != 10, and 7 < 10, so search left
        - At node 5: 7 != 5, and 7 > 5, so search right of 5
        - If right of 5 has Node(7) -> return True
        - If right of 5 is None -> return False
        
        TIME COMPLEXITY: O(h) where h is height of tree
        - Best case (balanced): O(log n)
        - Worst case (skewed): O(n)
        """
        print(f"    Searching for {value}, currently at node {self.key}")
        
        if value == self.key:
            # BASE CASE: Found the value!
            print(f"    Found {value} at node {self.key}")
            return True
        elif value < self.key:
            # CASE 1: Search value is smaller - search LEFT subtree
            print(f"    {value} < {self.key}, searching left subtree")
            if self.left:
                return self.left.search(value)  # Recursive call to left child
            else:
                print(f"    No left child of {self.key}, {value} not found")
                return False
        else:
            # CASE 2: Search value is larger - search RIGHT subtree
            print(f"    {value} > {self.key}, searching right subtree")
            if self.right:
                return self.right.search(value)  # Recursive call to right child
            else:
                print(f"    No right child of {self.key}, {value} not found")
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


def main():
    """
    Submission Requirements:
    1. Create an empty BST
    2. Insert values: 20, 40, 10, 4, 15, 50, 35, 55, 60
    3. Traverse the tree
    4. Search for values 15 and 52
    """
    
    print("=== Binary Search Tree Implementation ===\n")
    
    # 1. Create an empty BST (start with root node)
    print("1. Creating BST with root node...")
    root = Node(20)  # First value becomes root
    print(f"Root created with value: {root.key}\n")
    
    # 2. Insert the remaining values
    print("2. Inserting values: 40, 10, 4, 15, 50, 35, 55, 60")
    values_to_insert = [40, 10, 4, 15, 50, 35, 55, 60]
    
    for value in values_to_insert:
        print(f"\nInserting {value}:")
        root.insert(value)
    
    print("\nTree structure:")
    root.print_tree()
    
    # 3. Traverse the tree (in-order traversal)
    print("\n3. In-order traversal of the tree:")
    print("--- Starting traversal process ---")
    print("In-order means: Left subtree -> Current node -> Right subtree")
    print("For BST, this gives us values in sorted order!")
    
    traversal_result = root.traverse()
    print(f"\nTraversal result: {traversal_result}")
    print("✓ Notice how the values are in ascending order!")
    print("✓ This is the key property of in-order traversal on BST")
    
    # 4. Search for values 15 and 52
    print("\n4. Searching for values:")
    
    print(f"\n--- Searching for 15 ---")
    search_value_1 = 15
    found_1 = root.search(search_value_1)
    print(f"Final result: Search for {search_value_1}: {'Found' if found_1 else 'Not Found'}")
    
    print(f"\n--- Searching for 52 ---")
    search_value_2 = 52
    found_2 = root.search(search_value_2)
    print(f"Final result: Search for {search_value_2}: {'Found' if found_2 else 'Not Found'}")
    
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


if __name__ == "__main__":
    main()