rom dataclasses import dataclass, field

@dataclass
class Heap:
    arr: list = field(default_factory=list)
    
    def _swap(self, i, j):
        self.arr[i], self.arr[j] = self.arr[j], self.arr[i]

    def _buildHeap(self, n, i): # O(logn)
        parent = i
        left = 2*i + 1
        right = 2*i + 2
        
        if left < n and self.arr[parent] < self.arr[left]:
            parent = left
        if right < n and self.arr[parent] < self.arr[right]:
            parent = right
        if parent != i:
            self._swap(i, parent)
            self._buildHeap(n, parent)

    def heapify(self, n=None):
        if n is None:
            n = len(self.arr)
        i = n//2 - 1   
        for k in range(i,-1,-1):
            self._buildHeap(n, k)
    
    def getMax(self):
        return self.arr[0] if len(self.arr) > 0 else None
    
    def heapPush(self, element_to_push): # O(logn)
        self.arr.append(element_to_push)
        self._bubbleUp()
    
    def heapExtractMax(self):
        self._swap(0, len(self.arr) - 1)
        max_value = self.arr.pop(len(self.arr) - 1)
        self._bubbleDown()
        return max_value

    def update_by_element(self, old_element, new_element): # O(n)
        if old_element in self.arr:
            index = self.arr.index(old_element)
            self.update_by_index(new_element, index)
        else:
            return 'Element has not been found'
    def update_by_index(self, new_element, index): # O(logn)
        old_element = self.arr[index]
        self.arr[index] = new_element
        if new_element > old_element:
            self._bubbleUp(index)
        if new_element < old_element:
            self._bubbleDown(index)
                        
    def _bubbleUp(self, node=None): # O(logn)
        n = len(self.arr)
        if node is None:
            node = n - 1
        parent = (node - 1) // 2
        while node != 0 and self.arr[node] > self.arr[parent]:
            self._swap(node, parent)
            node = parent
            parent = (node - 1) // 2
    
    def _bubbleDown(self, node=None): # O(logn)
        n = len(self.arr)
        if node is None:
            node = 0
        left = 2*node + 1
        right = 2*node + 2
        while True:
            left = 2*node + 1
            right = 2*node + 2
            largest = node
            if left < n and self.arr[node] < self.arr[left]:
                largest = left
            if right < n and self.arr[node] < self.arr[right]:
                largest = right
            
            if largest != node:
                self._swap(node, largest)
                node = largest
            else:
                break    
             
    def heapSort(self):
        n = len(self.arr)
        self.heapify(n)
        
        for i in range(n - 1, 0, -1):
            self._swap(0, i)
            self._buildHeap(i, 0)
        
        return self.arr
