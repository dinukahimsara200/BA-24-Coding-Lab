from collections import deque

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, root_value):
        self.root = TreeNode(root_value)
    
    # Depth-First Search (DFS) Traversals
    
    def pre_order(self, node=None):
        if node is None:
            node = self.root
        result = []
        def traverse(current):
            if current:
                result.append(current.value)  # Visit root
                traverse(current.left)       # Traverse left
                traverse(current.right)      # Traverse right
        traverse(node)
        return result
    
    def in_order(self, node=None):
        if node is None:
            node = self.root
        result = []
        def traverse(current):
            if current:
                traverse(current.left)       # Traverse left
                result.append(current.value) # Visit root
                traverse(current.right)     # Traverse right
        traverse(node)
        return result
    
    def post_order(self, node=None):
        if node is None:
            node = self.root
        result = []
        def traverse(current):
            if current:
                traverse(current.left)      # Traverse left
                traverse(current.right)    # Traverse right
                result.append(current.value) # Visit root
        traverse(node)
        return result
    
    # Breadth-First Search (BFS) Traversal
    def level_order(self):
        if not self.root:
            return []
        
        result = []
        queue = deque([self.root])
        
        while queue:
            current = queue.popleft()
            result.append(current.value)
            
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
        
        return result

# Example Usage
if __name__ == "__main__":
    # Create a binary tree
    #       1
    #      / \
    #     2   3
    #    / \
    #   4   5
    tree = BinaryTree(1)
    tree.root.left = TreeNode(2)
    tree.root.right = TreeNode(3)
    tree.root.left.left = TreeNode(4)
    tree.root.left.right = TreeNode(5)
    
    print("Pre-order traversal:  ", tree.pre_order())   # [1, 2, 4, 5, 3]
    print("In-order traversal:   ", tree.in_order())    # [4, 2, 5, 1, 3]
    print("Post-order traversal: ", tree.post_order())  # [4, 5, 2, 3, 1]
    print("Level-order traversal:", tree.level_order()) # [1, 2, 3, 4, 5]