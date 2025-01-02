class EmptyLinkedListError(Exception):
    """Raised when an operation is attempted on an empty linked list."""
    pass

def empty_check(func):
    def wrapper(self, *args, **kwargs):
        if self.head is None:
            raise EmptyLinkedListError("Linked list is empty")
        return func(self, *args, **kwargs)

    return wrapper

def mergeTwoSortedLists(list1:LinkedList, list2: LinkedList) -> Node:
    result = LinkedList()
    
    if list1.length == 0 and list2.length == 0:
        return result.head
    
    current1 = list1.head
    current2 = list2.head
    
    while current1 is not None or current2 is not None:
        if current1 is None:
            result.append(current2.key)
            current2 = current2.next
        elif current2 is None:
            result.append(current1.key)
            current1 = current1.next
        elif current1.key <= current2.key:
            result.append(current1.key)
            current1 = current1.next
        else:
            result.append(current2.key)
            current2 = current2.next
    
    return result

class Node:
    def __init__(self, key):
        self.key = key
        self.next = None

    def __repr__(self):
        next_key = self.next.key if self.next is not None else None
        return f"Node(key={self.key}, next={next_key})"


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __repr__(self):
        temp_node = self.head
        result = ""

        while temp_node is not None:
            result += f"Node({temp_node.key})"

            if temp_node.next is not None:
                result += " -> "

            temp_node = temp_node.next

        return f"LinkedList({result}, length={self.length})"

    @empty_check
    def traverse(self):
        current = self.head

        while current is not None:
            print(current)
            current = current.next

    @empty_check
    def search(self, value):
        current = self.head
        index = 0
        while current is not None:
            if current.key == value:
                return current, index
            current = current.next
            index += 1

    @empty_check
    def search_all(self, value):
        current = self.head
        result = []

        while True:
            if current.key == value:
                result.append(current)
            current = current.next

            if current == None:
                return result

    @empty_check
    def get_by_index(self, index):
        if index >= self.length or index < 0:
            raise ValueError("Index is out of range")

        current = self.head
        count = 0

        while True:
            if count == index:
                return current

            current = current.next
            count += 1

    def append(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node

        else:
            self.tail.next = new_node
            self.tail = new_node

        self.length += 1

    def prepend(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node

        else:
            new_node.next = self.head
            self.head = new_node

        self.length += 1

    def insert(self, value, index):
        if index > self.length or index < 0:
            raise ValueError("Index is out of range")

        new_node = Node(value)
        temp_node = self.head

        if self.head is None:
            self.head = new_node
            self.tail = new_node

        else:
            if index == 0:
                new_node.next = self.head
                self.head = new_node

            elif index == self.length:
                self.tail.next = new_node
                self.tail = new_node

            else:
                for _ in range(index - 1):
                    temp_node = temp_node.next

                new_node.next = temp_node.next
                temp_node.next = new_node

        self.length += 1

    @empty_check
    def set_value(self, index, value):
        if index >= self.length or index < 0:
            raise ValueError("Index is out of range")

        current_node = self.get_by_index(index)
        current_node.key = value

    @empty_check
    def popfirst(self):
        node_to_pop = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next

        self.length -= 1
        return node_to_pop

    @empty_check
    def pop(self):
        node_to_pop = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            current = self.head
            while current.next != self.tail:
                current = current.next

            current.next = None
            self.tail = current

        self.length -= 1
        return node_to_pop

    @empty_check
    def remove_by_index(self, index):
        if index >= self.length or index < 0:
            raise ValueError("Index is out of range")

        if index == 0:
            self.head = self.head.next
            if self.length == 1:
                self.tail = None

        else:
            prev_node = self.get_by_index(index=index - 1)
            prev_node.next = prev_node.next.next

            if index == self.length - 1:
                self.tail = prev_node
        self.length -= 1

    def delete_all(self):
        self.head = None
        self.tail = None
        self.length = 0

    @empty_check
    def reversed(self):
        if self.length == 1:
            return
        
        prev_node = None
        current_node = self.head
        
        while current_node:
            temp_node = current_node.next
            current_node.next = prev_node
            prev_node = current_node
            current_node = temp_node
        
        self.tail = self.head
        self.head = prev_node
        
    @empty_check
    def find_middle(self):
        if self.length == 1:
            return self.head
        
        slow = self.head
        fast = self.head
        
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        
        return slow
    
    @empty_check
    def remove_duplicates(self):
        if self.length == 1:
            return self.head
        
        seen_value = set()
        current = self.head
        seen_value.add(current.key)
        
        while current.next:
            if current.next.key in seen_value:
                current.next = current.next.next
                self.length -= 1
                
            else:
                seen_value.add(current.next.key)
                current = current.next
                
        self.tail = current
