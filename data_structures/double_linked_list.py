class EmptyLinkedListError(Exception):
    """Raised when an operation is attempted on an empty linked list."""
    pass

def empty_check(func):
    def wrapper(self, *args, **kwargs):
        if self.head is None:
            raise EmptyLinkedListError("Linked list is empty")
        return func(self, *args, **kwargs)

    return wrapper

class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None
        
    
    def __repr__(self):
        prev_value = self.prev.value if self.prev else None
        next_value = self.next.value if self.next else None
        return f'Node(prev={prev_value}, value={self.value}, next={next_value})'

class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def __repr__(self):
        temp_node = self.head
        result = ""

        while temp_node is not None:
            result += str(temp_node)

            if temp_node.next is not None:
                result += " <-> "

            temp_node = temp_node.next

        return f"LinkedList({result}, length={self.length})"
    
    def append(self, value):
        new_node = Node(value=value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        
        self.length += 1
    
    def prepend(self, value):
        new_node = Node(value=value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        
        self.length += 1
        
    @empty_check
    def traverse(self):
        current = self.head
        while current:
            print(current)
            current = current.next
            
    def traverse_reverse(self):
        current = self.tail
        while current:
            print(current)
            current = current.prev          
    
    @empty_check        
    def search(self, target):
        result = []
        current = self.head
        while current:
            if current.value == target:
                result.append(current)
            current = current.next
        
        return result

    @empty_check
    def get_by_index(self, index):
        if index < 0 or index >= self.length:
            raise IndexError('Index is out of range')
        
        middle = self.length // 2
        if index <= middle:            
            count = 0
            current = self.head
            while count != index:
                current = current.next
                count += 1
        else:
            count = self.length - 1
            current = self.tail
            while count != index:
                current = current.prev
                count -= 1
                
        return current

    @empty_check
    def set(self, index, value):
        if index < 0 or index >= self.length:
            raise IndexError('Index is out of range')
        
        middle = self.length // 2
        if index <= middle:
            count = 0        
            current = self.head
            while count != index:
                current = current.next
                count += 1
        else:
            count = self.length - 1
            current = self.tail
            while count != index:
                current = current.prev
                count -= 1            
            
        current.value = value
    
    def insert(self, index, value):
        if index < 0 or index > self.length:
            raise IndexError('Index is out of range')
        
        new_node = Node(value=value)
        if index == 0:
            if self.head:
                new_node.next = self.head
                self.head.prev = new_node
                self.head = new_node
            else:
                self.head = new_node
                self.tail = new_node
        elif index == self.length:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        else:
            middle = self.length // 2
            if index <= middle:
                count = 0
                current = self.head
                while count != index:
                    current = current.next
                    count += 1
            else:
                count = self.length - 1
                current = self.tail
                while count != index:
                    current = current.prev
                    count -= 1
                    
            new_node.prev = current.prev
            new_node.next = current
            current.prev.next = new_node
            current.prev = new_node
        
        self.length += 1
    
    @empty_check
    def popfirst(self):
        node_to_pop = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            new_head = self.head.next
            new_head.prev = None
            self.head = new_head
        
        self.length -= 1
        return node_to_pop
    
    @empty_check
    def pop(self):
        node_to_pop = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            new_tail = self.tail.prev
            new_tail.next = None
            self.tail = new_tail
        
        self.length -= 1
        return node_to_pop
    
    @empty_check
    def remove(self, index):
        if index < 0 or index >= self.length:
            raise IndexError('Index is out of range')
        
        if self.length == 1 and index == 0:
            self.head = None
            self.tail = None
        else:
            middle = self.length // 2
            if index <= middle:
                count = 0
                current = self.head
                while count != index:
                    current = current.next
                    count += 1
            else:
                count = self.length - 1
                current = self.tail
                while count != index:
                    current = current.prev
                    count -= 1
            
            if current == self.head:
                self.head = self.head.next
                self.head.prev = None
            elif current == self.tail:
                self.tail = self.tail.prev
                self.tail.next = None
            else:
                prev_node = current.prev
                next_node = current.next
                prev_node.next = next_node
                next_node.prev = prev_node
        
        self.length -= 1
