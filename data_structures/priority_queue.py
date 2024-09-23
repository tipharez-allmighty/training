from dataclasses import dataclass, field
from heap import Heap

@dataclass
class PriorityQueue:
    arr: list=field(default_factory=list)
    heap: Heap=field(init=False, repr=False)
    
    def __post_init__(self):
        self.heap = Heap(self.arr)
        self.heap.heapify()
    
    def get_max(self):
        return self.heap.getMax()
    
    def deque(self):
        return self.heap.heapExtractMax()
    
    def enque(self, element):
        self.heap.heapPush(element)
    
    def change_priority(self, old_element, new_element):
        self.heap.update_by_element(old_element, new_element)
    
    def change_priority_by_undex(self, new_element, index):
        self.heap.update_by_index(self, new_element, index)
    
    def is_empty(self):
        return len(self.heap.arr) == 0
        
       
arr = [3, 1, 4, 1, 5, 9, 2, 6, 4,34,7,68,145,]

pq = PriorityQueue(arr)
print(pq)
pq.enque(9)
pq.change_priority(5,105)
pq.change_priority(2,103)
print(pq, sep='\n')
pq.deque()
print(pq, pq.get_max(), pq.is_empty(), sep='\n')
