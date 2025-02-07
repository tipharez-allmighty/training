class CircularQueue:
    def __init__(self, max_size):
        self.queue = [None]*max_size
        self.max_size = max_size
        self.start = -1
        self.top = -1
            
    def __repr__(self):
        values = [str(value) for value in self.queue if value]
        return f'Max size={self.max_size}, Queue: ' + ' '.join(values)

    def isFull(self):
        if (self.top + 1) % self.max_size == self.start:
            return True
        elif self.start == 0 and self.top + 1 == self.max_size:
            return True
        else:
            return False
    
    def isEmpty(self):
        return True if self.top == -1 else False
    
    def enqueue(self, value):
        if not self.isFull():
            if self.start == -1 and self.top == -1:
                self.start += 1
                self.top += 1
                self.queue[self.top] = value

            else:
                self.top = (self.top + 1) % self.max_size
                self.queue[self.top] = value
        else:
            raise IndexError('Queue is full')
    
    def dequeue(self):
        if not self.isEmpty():
            value_to_return = self.queue[self.start]
            if self.start == self.top:
                self.queue[self.start] = None
                self.start = self.top = -1
            else:
                self.queue[self.start] = None
                self.start = (self.start + 1) % self.max_size
                
            return value_to_return
        else:
            raise IndexError('Queue is empty')
    
    def peek(self):
        if not self.isEmpty():
            return self.queue[self.start]
        else:
            raise IndexError('Queue is empty')
    
    def delete(self):
        self.items = [None] * self.max_size
        self.start = self.top = -1
