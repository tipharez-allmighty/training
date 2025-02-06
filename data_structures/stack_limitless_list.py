class Stack:
    def __init__(self):
        self.stack = []
    
    def __repr__(self):
        values = [str(value) for value in reversed(self.stack)]
        return "\n".join(values)
    
    def isEmpty(self):
        return len(self.stack) == 0
    
    def push(self, value):
        self.stack.append(value)
    
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
