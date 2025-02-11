class PlateStacks:
    def __init__(self, capacity):
        self.capacity = capacity
        self.stacks = []
    
    def __repr__(self):
        return str(self.stacks)
    
    def get_stack(self):
        stack_number = 0
        while stack_number <= len(self.stacks):
            if stack_number == len(self.stacks):
                self.stacks.append([])
                break
            if len(self.stacks[stack_number]) == self.capacity:
                stack_number +=1
            else:
                break
        return stack_number
    
    def isEmpty(self):
        return not self.stacks
            
    def push(self, value):
        stack_to_push = self.get_stack()
        self.stacks[stack_to_push].append(value)
        
    def pop(self):
        if self.isEmpty():
            raise IndexError('Entire Line of Stacks is Empty')
        value_to_return = self.stacks[-1].pop()
        if not self.stacks[-1]:
            self.stacks.pop(-1)
        return value_to_return

    def popAtStack(self, index):
        if index < len(self.stacks) and index >= 0:
            value_to_return = self.stacks[index].pop()
            if not self.stacks[index]:
                self.stacks.pop(index)
            
            return value_to_return
        else:
            raise IndexError('There is No Stack for this Index')
