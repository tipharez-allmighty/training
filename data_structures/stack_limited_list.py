class Stack:
    def __init__(self, max_size: int=0):
        self.stack = []
        self.max_size = max_size
            
    def __repr__(self):
        values = [str(value) for value in reversed(self.stack)]
        return "\n".join(values)
    
    def isEmpty(self):
        return len(self.stack) == 0

    def isFull(self):
        return len(self.stack) == self.max_size
    
    def push(self, value):
        if len(self.stack) < self.max_size:
            self.stack.append(value)
        else:
            raise AttributeError('Stack is full')
            
    def pop(self):
        if not self.isEmpty():
            return self.stack.pop()
        else:
            raise AttributeError('Stack is empty')
    
    def peak(self):
        if not self.isEmpty():
            return self.stack[-1]
        else:
            raise AttributeError('Stack is empty')
    
    def delete(self):
        self.stack = []
