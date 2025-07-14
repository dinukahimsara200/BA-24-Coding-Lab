class Node:
    """
    A single node in the linked list containing data and a reference to the next node
    """
    def __init__(self, data):
        self.data = data      # Store the actual value/data
        self.next = None      # Reference to the next node (initially None)

class LinkedList:
    """
    A singly linked list implementation with basic operations
    """
    def __init__(self):
        self.head = None      # Reference to the first node (initially empty list)

    def is_empty(self):
        """Check if the list is empty by testing if head is None"""
        return self.head is None

    def append(self, data):
        """Add a new node at the end of the list"""
        new_node = Node(data)

        # If list is empty, make the new node the head
        if self.is_empty():
            self.head = new_node
            return

        # Otherwise, traverse to the end and attach the new node
        current = self.head
        while current.next:        # Keep going until we find a node with no next
            current = current.next
        current.next = new_node    # Link the last node to our new node

    def prepend(self, data):
        """Add a new node at the beginning of the list"""
        new_node = Node(data)
        new_node.next = self.head  # Point new node to current head
        self.head = new_node       # Make new node the new head

    def insert_after(self, target, data):
        """Insert a new node after the first occurrence of target value"""
        current = self.head

        # Traverse the list looking for the target value
        while current:
            if current.data == target:
                new_node = Node(data)
                # Insert between current and current.next
                new_node.next = current.next  # New node points to what current was pointing to
                current.next = new_node       # Current now points to new node
                return
            current = current.next

        # If we get here, target wasn't found
        raise ValueError(f"Target {target} not found")

    def delete(self, data):
        """Remove the first occurrence of the specified data"""
        if self.is_empty():
            raise ValueError("List is empty")

        # Special case: deleting the head node
        if self.head.data == data:
            self.head = self.head.next  # Move head to next node
            return

        # General case: find the node before the one to delete
        current = self.head
        while current.next:
            if current.next.data == data:
                # Skip over the node to delete by linking around it
                current.next = current.next.next
                return
            current = current.next

        # If we get here, data wasn't found
        raise ValueError(f"Data {data} not found")

    def search(self, data):
        """Search for a value in the list, return True if found"""
        current = self.head

        # Traverse the entire list
        while current:
            if current.data == data:
                return True
            current = current.next

        return False  # Not found

    def size(self):
        """Count and return the number of nodes in the list"""
        count = 0
        current = self.head

        # Traverse the entire list, counting nodes
        while current:
            count += 1
            current = current.next

        return count

    def print_list(self):
        """Display the list in a readable format"""
        elements = []
        current = self.head

        # Collect all data values into a list
        while current:
            elements.append(str(current.data))
            current = current.next

        # Print with arrows showing the linking structure
        print(" -> ".join(elements))

    def print_list_with_addresses(self):
        """Display the list showing both data and memory addresses of nodes"""
        if self.is_empty():
            print("Empty list")
            return

        current = self.head
        print(f"Head points to: {hex(id(self.head))}")
        print("Node details:")

        # Traverse and show each node's data, address, and next pointer
        while current:
            next_addr = hex(id(current.next)) if current.next else "None"
            print(f"  Data: {current.data} | Node address: {hex(id(current))} | Next points to: {next_addr}")
            current = current.next

# Example Usage:
ll = LinkedList()
ll.append(1)                 # List: 1
ll.append(2)                 # List: 1 -> 2
ll.prepend(0)               # List: 0 -> 1 -> 2 (0 added at beginning)
ll.insert_after(1, 1.5)     # List: 0 -> 1 -> 1.5 -> 2 (1.5 inserted after 1)
ll.delete(1)                # List: 0 -> 1.5 -> 2 (removed the 1)
print(ll.search(1.5))       # True (1.5 exists in the list)
ll.print_list()             # Output: 0 -> 1.5 -> 2

# Show the internal pointer structure
print("\nPointer details:")
ll.print_list_with_addresses() # Shows memory addresses and how nodes link together
