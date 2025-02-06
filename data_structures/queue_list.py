class Queue:
    def __init__(self):
        self.queue = []
    
    def __repr__(self):
        values = [str(value) for value in self.queue]
        return ' '.join(values)

    def isEmpty(self):
        return len(self.queue) == 0
    
    def enqueue(self, value):
        self.queue.append(value)
    
    def dequeue(self):
        if not self.isEmpty():
            value_to_return = self.queue[0]
            self.queue.remove(value_to_return)
            return value_to_return
        else:
            raise IndexError('Queue is empty')
    
    def peek(self):
        if not self.isEmpty():
            return self.queue[0]
        else:
            raise IndexError('Queue is empty')
    
    def delete(self):
        self.queue = []
