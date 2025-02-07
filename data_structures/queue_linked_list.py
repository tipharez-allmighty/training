class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next
    
    def __repr__(self):
        return f"Node(value={self.value}, next={self.next})"

class Queue:
    def __init__(self):
        self.queue = None
    
    def __repr__(self):
        return str(self.queue) if self.queue else ""
    
    def isEmpty(self):
        return self.queue == None
    
    def enqueue(self, value):
        new_element = Node(value)
        if self.isEmpty():
            self.queue = new_element
        else:
            current = self.queue
            while current.next:
                current = current.next
            current.next = new_element
    
    def dequeue(self):
        if self.isEmpty():
            raise IndexError("Queue is empty")
        elif not self.queue.next:
            self.queue = None
        else:
            dequeue_element = self.queue.value
            self.queue = self.queue.next
            return dequeue_element
    
    def peek(self):
        if self.isEmpty():
            raise IndexError("Queue is empty")
        else:
            return self.queue.value
