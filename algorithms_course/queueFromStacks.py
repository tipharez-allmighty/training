class StacksQueue:
    def __init__(self):
        self.stack_1 = []
        self.stack_2 = []
    
    def __repr__(self):
        return str(self.stack_1)
    
    def isEmpty(self):
        return not self.stack_1
    
    def enqueue(self, value):
        self.stack_1.append(value)
    
    def dequeue(self):
        if self.isEmpty():
            raise IndexError('Queue is empty')
        while self.stack_1:
            self.stack_2.append(self.stack_1.pop())
        value_to_return = self.stack_2.pop()
        while self.stack_2:
            self.stack_1.append(self.stack_2.pop())
            
        return value_to_return
    
    def peek(self):
        return self.stack_1[0] if self.stack_1 else None