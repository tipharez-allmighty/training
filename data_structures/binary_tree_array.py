from queue_linked_list import Queue

class BinaryTree:
    __slots__ = ('array', 'last_index', 'size')
    def __init__(self, size):
        self.array = size * [None]
        self.last_index = 0
        self.size = size
    
    def insertNode(self, value):
        if self.last_index + 1 == self.size:
            raise Exception('The Binary Tree is full')
        self.array[self.last_index + 1] = value
        self.last_index += 1
    
    def searchNode(self, value):
        for i in range(1, len(self.array)):
            if self.array[i] == value:
                return self.array[i]
        return None

    def preOrderTraversal_rec(self, index=1):
        if index > self.last_index:
            return
        print(self.array[index])
        self.preOrderTraversal_rec(index * 2)
        self.preOrderTraversal_rec((index * 2) + 1)

    def inOrderTraversal_rec(self, index=1):
        if index > self.last_index:
            return
        self.inOrderTraversal_rec(index * 2)
        print(self.array[index])
        self.inOrderTraversal_rec((index * 2) + 1)        

    def postOrderTraversal_rec(self, index=1):
        if index > self.last_index:
            return
        self.inOrderTraversal_rec(index * 2)
        self.inOrderTraversal_rec((index * 2) + 1)  
        print(self.array[index])
        
    def preOrderTraversal_iter(self):
        current_index = 1
        if self.array[current_index] == None:
            return None
        stack = [current_index]
        while stack:
            current_index = stack.pop()
            print(self.array[current_index])
            if ((current_index * 2) + 1) <= self.last_index and self.array[(current_index * 2) + 1]:
                stack.append((current_index * 2) + 1)
            if (current_index * 2) <= self.last_index and self.array[current_index * 2]:
                stack.append(current_index * 2)

    def inOrderTraversal_iter(self):
        current_index = 1
        if self.array[current_index] == None:
            return None
        stack = []
        while stack or current_index <= self.last_index:
            while current_index <= self.last_index:
                stack.append(current_index)
                current_index = current_index * 2
            current_index = stack.pop()
            print(self.array[current_index])
            current_index = (current_index * 2) + 1

    def postOrderTraversal_iter(self):
        current_index = 1
        if self.array[current_index] == None:
            return None
        stack = [current_index]
        result = []
        while stack:
            current_index = stack.pop()
            result.append(current_index)
            if (current_index * 2) <= self.last_index and self.array[current_index * 2]:
                stack.append(current_index * 2)                 
            if ((current_index * 2) + 1) <= self.last_index and self.array[(current_index * 2) + 1]:
                stack.append((current_index * 2) + 1)
        while result:
            print(self.array[result.pop()])
    
    def levelOrderTraversal(self):
        current_index = 1
        if self.array[current_index] == None:
            return None     
        queue = Queue()
        queue.enqueue(current_index)
        while not queue.isEmpty():
            current_index = queue.dequeue()
            print(self.array[current_index])
            if (current_index * 2) <= self.last_index and self.array[current_index * 2]:
                queue.enqueue(current_index * 2)                 
            if ((current_index * 2) + 1) <= self.last_index and self.array[(current_index * 2) + 1]:
                queue.enqueue((current_index * 2) + 1)

    def deleteNode(self, value):
        if self.last_index == 0:
            raise Exception('Tree Binary tree is Empty')
        current_index = 1
        if self.array[current_index] == None:
            return None

        for i in range(1, self.last_index + 1):
            if self.array[i] == value:
                self.array[i], self.array[self.last_index] = self.array[self.last_index], None
                self.last_index -= 1

    def delete(self):
        self.array = None
        self.last_index = None
        self.size = 0
