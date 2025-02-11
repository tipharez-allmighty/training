def isStackCheck(func):
    def wrapper(self, stack, *args, **kwargs):
        if stack < 0 or stack > self.num_stacks:
            raise IndexError(f'There is not stack {stack}')
        return func(self, stack, *args, **kwargs)
    return wrapper

class ThreeStacks:
    def __init__(self, stack_size):
        self.num_stacks = 3
        self.stack_size = stack_size
        self.array = [None] * stack_size*self.num_stacks
        self.sizes = [0] * self.num_stacks
    
    @isStackCheck
    def isFull(self, stack):
        return self.sizes[stack] == self.stack_size
    
    @isStackCheck
    def isEmpty(self, stack):
        return self.sizes[stack] == 0
    
    @isStackCheck
    def top_element(self, stack):
        return stack * self.stack_size + self.sizes[stack] - 1
    
    def push(self, value, stack):
        if self.isFull(stack):
            raise IndexError('The Stack is Full')
        self.sizes[stack] += 1
        self.array[self.top_element(stack)] = value
    
    def pop(self, stack):
        if self.isEmpty(stack):
            raise IndexError('The Stack is Empty')
        value = self.array[self.top_element(stack)]
        self.array[self.top_element(stack)] = None
        self.sizes[stack] -= 1
        return value
