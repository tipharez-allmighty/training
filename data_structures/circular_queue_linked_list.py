class Node:
    def __init__(self, value=None, prev=None, next=None):
        self.value = value
        self.next = next
        self.prev = prev
            
    def __repr__(self):
        result = []
        current = self
        while True:
            result.append(current.value)
            current = current.next
            if current == self:
                break
        return ' '.join([str(node) for node in result])

class CircularQueue:
    def __init__(self, max_size: int):
        self.max_size = max_size
        self.space = self.max_size
        self.start = None
        self.top = None
    
    def __repr__(self):
        return str(self.start) if self.start else 'Queue is empty'
    
    def isEmpty(self):
        return self.start is None and self.top is None
    
    def isFull(self):
        return self.space == 0
    
    def enqueu(self, value):
        if self.isFull():
            raise IndexError('Queue is full')
        new_element = Node(value=value)
        if self.isEmpty():
            self.start = new_element
            self.top = new_element
            self.start.prev = self.start
            self.start.next = self.start
        else:
            new_element.prev = self.top
            new_element.next = self.start
            self.top.next = new_element
            self.start.prev = new_element
            self.top = new_element
        
        self.space -=1
    
    def dequeu(self):
        if self.isEmpty():
            raise IndexError('Queue is empty')
        element_to_dequeu = self.start.value
        if self.start == self.top:
            self.start = None
            self.top = None
        else:
            self.start = self.start.next
            self.top.next = self.start
            self.start.prev = self.top
        
        self.space += 1
        
        return element_to_dequeu
    
    def peek(self):
        if self.isEmpty():
            raise IndexError('Queue is empty')
        else:
            return self.start.value
    
    def delete(self):
        self.space = self.max_size
        self.start = None
        self.top = None
