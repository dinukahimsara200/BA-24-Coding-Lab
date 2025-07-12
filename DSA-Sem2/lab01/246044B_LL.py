class Node:
    def __init__(self, dataval):
        self.dataval = dataval
        self.next = None



class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_head(self, dataval):
        new_node = Node(dataval)
        new_node.next = self.head
        self.head = new_node

    def traverse(self):
        n = self.head
        while n is not None:
            print(n.dataval, end=' ')
            n = n.next

    def insert_at_end(self, dataval):
        new_node = Node(dataval)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

