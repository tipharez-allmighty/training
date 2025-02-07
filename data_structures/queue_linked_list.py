class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next
    
    def __repr__(self):
        return f"Node(value={self.value}, next={self.next})"

class Queue:
    def __init__(self):
        self.start = None
        self.top = None
        
    def __repr__(self):
        return str(self.start) if self.start else ""
    
    def isEmpty(self):
        return self.start is None and self.top is None
    
    def enqueue(self, value):
        new_element = Node(value)
        if self.isEmpty():
            self.start = new_element
            self.top = new_element
        else:
            self.top.next = new_element
            self.top = self.top.next
                
    def dequeue(self):
        if self.isEmpty():
            raise IndexError("Queue is empty")
            
        dequeue_element = self.start.value
        if self.start == self.top:
            self.start = None
            self.top = None
            return dequeue_element
        else:
            self.start = self.start.next
            return dequeue_element
    
    def peek(self):
        if self.isEmpty():
            raise IndexError("Queue is empty")
        else:
            return self.start.value
    
    def delete(self):
        self.start = None
        self.top = None   
