class DynamicArray:
    """
    A dynamic array implementation that automatically resizes when needed
    """
    def __init__(self, initial_capacity=4):
        self.capacity = initial_capacity    # Total space allocated
        self.size = 0                      # Current number of elements
        self.data = [None] * self.capacity # Internal storage array

    def is_empty(self):
        """Check if the array is empty"""
        return self.size == 0

    def __len__(self):
        """Return the number of elements in the array"""
        return self.size

    def get(self, index):
        """Get element at specified index"""
        if not (0 <= index < self.size):
            raise IndexError(f"Index {index} out of bounds")
        return self.data[index]

    def set(self, index, value):
        """Set element at specified index to new value"""
        if not (0 <= index < self.size):
            raise IndexError(f"Index {index} out of bounds")
        self.data[index] = value

    def _resize(self):
        """Double the capacity when array becomes full"""
        old_capacity = self.capacity
        self.capacity *= 2
        old_data = self.data
        self.data = [None] * self.capacity
        
        # Copy elements to new array
        for i in range(self.size):
            self.data[i] = old_data[i]
        
        print(f"Resized array from capacity {old_capacity} to {self.capacity}")

    def append(self, value):
        """Add element to the end of the array"""
        if self.size >= self.capacity:
            self._resize()
        
        self.data[self.size] = value
        self.size += 1

    def insert(self, index, value):
        """Insert element at specified index"""
        if not (0 <= index <= self.size):
            raise IndexError(f"Index {index} out of bounds")
        
        if self.size >= self.capacity:
            self._resize()
        
        # Shift elements to the right
        for i in range(self.size, index, -1):
            self.data[i] = self.data[i - 1]
        
        self.data[index] = value
        self.size += 1

    def delete(self, index):
        """Remove element at specified index"""
        if not (0 <= index < self.size):
            raise IndexError(f"Index {index} out of bounds")
        
        deleted_value = self.data[index]
        
        # Shift elements to the left
        for i in range(index, self.size - 1):
            self.data[i] = self.data[i + 1]
        
        self.size -= 1
        self.data[self.size] = None  # Clear the last element
        return deleted_value

    def remove(self, value):
        """Remove first occurrence of the specified value"""
        for i in range(self.size):
            if self.data[i] == value:
                return self.delete(i)
        raise ValueError(f"Value {value} not found")

    def search(self, value):
        """Search for value and return its index, -1 if not found"""
        for i in range(self.size):
            if self.data[i] == value:
                return i
        return -1

    def print_array(self):
        """Display the array contents"""
        elements = [str(self.data[i]) for i in range(self.size)]
        print(f"Array: [{', '.join(elements)}]")
        print(f"Size: {self.size}, Capacity: {self.capacity}")

    def print_internal_state(self):
        """Show internal array state including unused slots"""
        print(f"Internal state (capacity {self.capacity}):")
        for i in range(self.capacity):
            marker = " <-- current size" if i == self.size else ""
            status = "used" if i < self.size else "unused"
            print(f"  Index {i}: {self.data[i]} ({status}){marker}")


class Stack:
    """
    A stack implementation using dynamic array (LIFO - Last In First Out)
    """
    def __init__(self):
        self.items = []  # Using Python list for simplicity

    def is_empty(self):
        """Check if stack is empty"""
        return len(self.items) == 0

    def push(self, data):
        """Add element to top of stack"""
        self.items.append(data)
        print(f"Pushed {data} onto stack")

    def pop(self):
        """Remove and return top element from stack"""
        if self.is_empty():
            raise IndexError("Stack is empty - cannot pop")
        
        popped_item = self.items.pop()
        print(f"Popped {popped_item} from stack")
        return popped_item

    def peek(self):
        """Return top element without removing it"""
        if self.is_empty():
            raise IndexError("Stack is empty - cannot peek")
        return self.items[-1]

    def size(self):
        """Return number of elements in stack"""
        return len(self.items)

    def print_stack(self):
        """Display stack contents from top to bottom"""
        if self.is_empty():
            print("Stack is empty")
            return
        
        print("Stack (top to bottom):")
        for i in range(len(self.items) - 1, -1, -1):
            marker = " <-- TOP" if i == len(self.items) - 1 else ""
            print(f"  {self.items[i]}{marker}")

    def print_operations_demo(self):
        """Show how stack operations work step by step"""
        print("\n--- Stack Operations Demo ---")
        print("Stack follows LIFO (Last In, First Out) principle")
        print("Elements are added and removed from the TOP only")


class Queue:
    """
    A queue implementation using dynamic array (FIFO - First In First Out)
    """
    def __init__(self):
        self.items = []  # Using Python list for simplicity

    def is_empty(self):
        """Check if queue is empty"""
        return len(self.items) == 0

    def enqueue(self, data):
        """Add element to rear of queue"""
        self.items.append(data)
        print(f"Enqueued {data} to queue")

    def dequeue(self):
        """Remove and return front element from queue"""
        if self.is_empty():
            raise IndexError("Queue is empty - cannot dequeue")
        
        dequeued_item = self.items.pop(0)  # Remove from front
        print(f"Dequeued {dequeued_item} from queue")
        return dequeued_item

    def front(self):
        """Return front element without removing it"""
        if self.is_empty():
            raise IndexError("Queue is empty - cannot peek front")
        return self.items[0]

    def rear(self):
        """Return rear element without removing it"""
        if self.is_empty():
            raise IndexError("Queue is empty - cannot peek rear")
        return self.items[-1]

    def size(self):
        """Return number of elements in queue"""
        return len(self.items)

    def print_queue(self):
        """Display queue contents from front to rear"""
        if self.is_empty():
            print("Queue is empty")
            return
        
        print("Queue (front to rear):")
        for i, item in enumerate(self.items):
            front_marker = " <-- FRONT" if i == 0 else ""
            rear_marker = " <-- REAR" if i == len(self.items) - 1 else ""
            print(f"  {item}{front_marker}{rear_marker}")

    def print_operations_demo(self):
        """Show how queue operations work step by step"""
        print("\n--- Queue Operations Demo ---")
        print("Queue follows FIFO (First In, First Out) principle")
        print("Elements are added at REAR and removed from FRONT")


class CircularQueue:
    """
    A circular queue implementation using fixed-size array for better efficiency
    """
    def __init__(self, max_size):
        self.max_size = max_size
        self.queue = [None] * max_size
        self.front = -1  # Points to front element
        self.rear = -1   # Points to rear element
        self.count = 0   # Number of elements

    def is_empty(self):
        """Check if queue is empty"""
        return self.count == 0

    def is_full(self):
        """Check if queue is full"""
        return self.count == self.max_size

    def enqueue(self, data):
        """Add element to rear of circular queue"""
        if self.is_full():
            raise OverflowError("Queue is full - cannot enqueue")
        
        if self.is_empty():
            self.front = 0
            self.rear = 0
        else:
            self.rear = (self.rear + 1) % self.max_size
        
        self.queue[self.rear] = data
        self.count += 1
        print(f"Enqueued {data} at position {self.rear}")

    def dequeue(self):
        """Remove and return front element"""
        if self.is_empty():
            raise IndexError("Queue is empty - cannot dequeue")
        
        dequeued_item = self.queue[self.front]
        self.queue[self.front] = None  # Clear the slot
        
        if self.count == 1:  # Queue becomes empty
            self.front = -1
            self.rear = -1
        else:
            self.front = (self.front + 1) % self.max_size
        
        self.count -= 1
        print(f"Dequeued {dequeued_item}")
        return dequeued_item

    def print_circular_queue(self):
        """Display circular queue state with positions"""
        print(f"Circular Queue (max_size: {self.max_size}, count: {self.count}):")
        print(f"Front index: {self.front}, Rear index: {self.rear}")
        
        for i in range(self.max_size):
            status = ""
            if i == self.front and i == self.rear and not self.is_empty():
                status = " <-- FRONT & REAR"
            elif i == self.front and not self.is_empty():
                status = " <-- FRONT"
            elif i == self.rear and not self.is_empty():
                status = " <-- REAR"
            
            print(f"  Index {i}: {self.queue[i]}{status}")


# Example Usage and Demonstrations:

if __name__ == "__main__":
    print("=" * 50)
    print("DYNAMIC ARRAY DEMONSTRATION")
    print("=" * 50)
    
    # Dynamic Array Demo
    arr = DynamicArray(initial_capacity=2)
    arr.append(10)
    arr.append(20)
    arr.print_array()
    
    arr.append(30)  # This will trigger resize
    arr.append(40)
    arr.print_array()
    
    arr.insert(1, 15)
    arr.print_array()
    arr.print_internal_state()
    
    print("\n" + "=" * 50)
    print("STACK DEMONSTRATION")
    print("=" * 50)
    
    # Stack Demo
    stack = Stack()
    stack.print_operations_demo()
    
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.print_stack()
    
    print(f"Top element (peek): {stack.peek()}")
    stack.pop()
    stack.pop()
    stack.print_stack()
    
    print("\n" + "=" * 50)
    print("QUEUE DEMONSTRATION")
    print("=" * 50)
    
    # Queue Demo
    queue = Queue()
    queue.print_operations_demo()
    
    queue.enqueue("A")
    queue.enqueue("B")
    queue.enqueue("C")
    queue.print_queue()
    
    print(f"Front element: {queue.front()}")
    print(f"Rear element: {queue.rear()}")
    queue.dequeue()
    queue.print_queue()
    
    print("\n" + "=" * 50)
    print("CIRCULAR QUEUE DEMONSTRATION")
    print("=" * 50)
    
    # Circular Queue Demo
    cq = CircularQueue(4)
    cq.enqueue("X")
    cq.enqueue("Y")
    cq.enqueue("Z")
    cq.print_circular_queue()
    
    cq.dequeue()
    cq.enqueue("W")
    cq.print_circular_queue()
    
    print("\nCircular nature - adding one more element:")
    cq.enqueue("V")  # This will wrap around
    cq.print_circular_queue()