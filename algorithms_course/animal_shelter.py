from typing import Literal

class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next
    
    def __repr__(self):
        return f'(value={self.value}, next={self.next})'
    
class AnimalShelter:
    def __init__(self):
        self.queue = None

    def __str__(self):
        return str(self.queue)
    
    def enqueue(self, pet: Literal['dog', 'cat']):
        new_element = Node(pet)
        if not self.queue:
            self.queue = new_element
        else:
            current = self.queue
            while current.next:
                current = current.next
            current.next = new_element
    
    def isEmpty(self):
        return not self.queue
    
    def dequeue(self, pet: Literal['dog', 'cat', 'any']):
        if self.isEmpty():
            raise Exception('The Animal Shelter is Empty')
        
        value_to_return = None
        if pet == 'any':
            value_to_return = self.queue.value
            self.queue = self.queue.next
        else:
            current = self.queue
            prev = None
            while current:
                if current.value == pet:
                    value_to_return = current.value                    
                    if prev:
                        prev.next = current.next
                    else:
                        self.queue = current.next
                    break
                prev = current
                current = current.next
        
        if not value_to_return:
            raise Exception(f'Unfortunately, no more {pet}s left in The Shelter')
        return value_to_return

            