class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

    def __repr__(self):
        return f"Node(key={self.key}, value={self.value}, next={self.next})"

ERROR_MESSAGE = "Given key {key} is not present in Hash Table"

class HashTable:
    def __init__(self, size):
        self.size = size
        self.array = [None] * size
    
    def __repr__(self):
        result = "{"
        first = True
        for node in self.array:
            if node is not None:
                current = node
                while current:
                    if not first:
                        result += ', '
                    first = False
                    result += f'{current.key}: {current.value}'
                    current = current.next
        result += '}'
        return result

    def __getitem__(self, key):
        index = self._hash(key)
        if self.array[index] is None:
            raise KeyError(ERROR_MESSAGE.format(key))
        else:
            current = self.array[index]
            while current:
                if current.key == key:
                    return current.value
                current = current.next
            raise KeyError(ERROR_MESSAGE.format(key))
    
    def __iter__(self):
        for node in self.array:
            current = node
            while current:
                yield current.key, current.value
                current = current.next
                        
    def _hash(self, key):
        return hash(key) % self.size
    
    def insert(self, key, value):
        index = self._hash(key)
        node_to_insert = Node(key=key, value=value)
        if self.array[index] is None:
            self.array[index] = node_to_insert
        else:
            current = self.array[index]
            while current:
                if current.key == key:
                    current.value = value
                    return
                if current.next is None:
                    current.next = node_to_insert
                    return
                current = current.next
    
    def pop(self, key):
        if not self.array:
            raise KeyError(ERROR_MESSAGE.format(key))
        
        index = self._hash(key)
        current = self.array[index]
        prev = None
        while current:
            if current.key == key:
                value_to_pop = current.value
                if not prev:
                    self.array[index] = current.next
                else:
                    prev.next = current.next
                return value_to_pop
            prev = current
            current = current.next
            
        raise KeyError(ERROR_MESSAGE.format(key))
