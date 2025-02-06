class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next
    
    def __repr__(self):
        return f'(value={self.value}, next={self.next})'

class Stack:
    def __init__(self):
        self.stack = None
    
    def __repr__(self):
        current = self.stack
        result = []
        while current:
            result.append(str(current.value))
            current = current.next
            
        return '\n'.join(result)
    
    def push(self, value):
        self.stack = Node(value, self.stack)
    
    def isEmpty(self):
        return self.stack is None        
    
    def pop(self):
        if not self.isEmpty():
            node_to_pop = self.stack
            self.stack = self.stack.next

            return node_to_pop.value
        else:
            raise IndexError('Stack is empty')
    
    def peek(self):
        if not self.isEmpty():
            return self.stack.value
        else:
            raise IndexError('Stack is empty')
