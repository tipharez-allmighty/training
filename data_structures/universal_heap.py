from typing import Literal

class Heap:
    def __init__(self, size):
        self.max_size = size + 1
        self.array = [None] * self.max_size
        self.heap_size = 0

    def __repr__(self):
        return f'{self.array}'

    def __len__(self):
        return self.heap_size
        
    def __iter__(self):
        for i in self.array[1:self.heap_size + 1]:
            yield i
    
    def peek(self):
        return self.array[1]
    
    def _swap(self, i, j):
        self.array[i], self.array[j] = self.array[j], self.array[i]
        
    def _heapifyInsert(self, index,
                       heap_type: Literal['min', "max"] = 'min'):
        parent_index = int(index/2)
        if index <= 1:
            return
        if heap_type == "min":
            if self.array[index] < self.array[parent_index]:
                self._swap(index, parent_index)
                self._heapifyInsert(parent_index, heap_type=heap_type)
        elif heap_type == "max":
            if self.array[index] > self.array[parent_index]:
                self._swap(index, parent_index)        
                self._heapifyInsert(parent_index, heap_type=heap_type)
    
    def _heapifyDelete(self, index,
                       heap_type: Literal['min', 'max'] = 'min'):
        root = index
        left = 2 * index
        right = 2 * index + 1
        
        if left > self.heap_size:
            return
        if heap_type == "min":
            smallest = left
            if right <= self.heap_size and self.array[right] < self.array[smallest]:
                smallest = right
            if self.array[smallest] < self.array[root]:   
                self._swap(smallest, root)
                self._heapifyDelete(smallest, heap_type=heap_type)
        elif heap_type == "max":
            largest = left
            if right <= self.heap_size and self.array[right] > self.array[largest]:
                largest = right
            if self.array[largest] > self.array[root]:   
                self._swap(largest, root)
                self._heapifyDelete(largest, heap_type=heap_type)
                
    def insert(self, value, heap_type: Literal['min', 'max'] = 'min'):
        if self.heap_size + 1 >= self.max_size:
            raise IndexError('Heap is Full')
        else:
            self.heap_size += 1
            self.array[self.heap_size] = value
            self._heapifyInsert(index=self.heap_size, heap_type=heap_type)
    
    def extract(self, heap_type: Literal['min', 'max'] = 'min'):
        if self.heap_size == 0:
            raise IndexError('Heap is Empty')
        else:
            value_to_extract = self.array[1]
            self._swap(1, self.heap_size)
            self.array[self.heap_size] = None
            self.heap_size -= 1
            self._heapifyDelete(index=1, heap_type=heap_type)
            return value_to_extract
    
    def delete(self):
        self.array = [None] * self.max_size
        self.heap_size = 0
