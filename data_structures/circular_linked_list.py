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
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

    def __repr__(self):
        next_value = self.next.value if self.next is not None else None
        return f"Node(value={self.value}, next={next_value})"


class CLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __repr__(self):
        temp_node = self.head
        result = ""
        count = 0
        while count != self.length:
            result += f"Node({temp_node.value})"

            if temp_node.next is not self.head:
                result += " -> "

            temp_node = temp_node.next

            count += 1

        return f"CLinkedList({result}, length={self.length})"

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            new_node.next = new_node
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.tail.next = new_node
            self.tail = new_node

        self.length += 1

    def prepend(self, value):
        new_node = Node(value)

        if self.length == 0:
            new_node.next = new_node
            self.head = new_node
            self.tail = new_node

        else:
            new_node.next = self.head
            self.head = new_node
            self.tail.next = self.head

        self.length += 1

    def insert(self, value, index):
        if index < 0 or index > self.length:
            raise IndexError("Index is out of range")

        new_node = Node(value)

        if index == 0:
            if self.length == 0:
                new_node.next = new_node
                self.head = new_node
                self.tail = new_node
            else:
                new_node.next = self.head
                self.head = new_node
                self.tail.next = new_node
        elif index == self.length:
            new_node.next = self.head
            self.tail.next = new_node
            self.tail = new_node
        else:
            count = 0
            temp_node = self.head
            while count != index - 1:
                temp_node = temp_node.next
                count += 1
            new_node.next = temp_node.next
            temp_node.next = new_node

        self.length += 1

    def traverse(self):
        current = self.head
        while current:
            print(current)
            current = current.next
            if current == self.head:
                break

    @empty_check
    def search(self, target):
        current = self.head
        nodes_to_return = []
        while True:
            if current.value == target:
                nodes_to_return.append(current)
            current = current.next
            if current == self.head:
                break

        return nodes_to_return

    @empty_check
    def get(self, index):
        if index < 0 or index >= self.length:
            raise IndexError("Index is out of range")

        current = self.head
        count = 0

        while count != index:
            current = current.next
            if current == self.head:
                break
            count += 1
        return current

    def set_value(self, index, value):
        if index < 0 or index >= self.length:
            raise IndexError("Index is out of range")

        current = self.head
        count = 0

        while count != index:
            current = current.next
            count += 1

        current.value = value

    @empty_check
    def popfirst(self):
        node_to_pop = None
        if self.length == 1:
            node_to_pop = self.head
            self.head = None
            self.tail = None
        else:
            node_to_pop = self.head
            self.head = self.head.next
            self.tail.next = self.head
        self.length -= 1
        return node_to_pop

    @empty_check
    def pop(self):
        node_to_pop = None
        if self.length == 1:
            node_to_pop = self.head
            self.head = None
            self.tail = None
        else:
            current = self.head

            while current.next != self.tail:
                current = current.next

            node_to_pop = self.tail
            current.next = self.head
            self.tail = current
        self.length -= 1
        return node_to_pop
    
    @empty_check
    def remove(self, index):
        if index < 0 or index >= self.length:
            raise IndexError("Index is out of range")
        if self.length == 1 and index == 0:
            self.head = None
            self.tail = None
        elif index == 0:
            self.head = self.head.next
            self.tail.next = self.head
        else:
            count = 0
            prev_node = self.head
            while count != index - 1:
                prev_node = prev_node.next
                count += 1
            prev_node.next = prev_node.next.next
            if index == self.length - 1:
                self.tail = prev_node
        
        self.length -= 1
    
    @empty_check
    def delete_by_value(self, value):
        if self.head.value == value:
            if self.head == self.tail:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next
                self.tail.next = self.head
        else:
            prev = self.head
            while prev.next.value != value:
                prev = prev.next
                
            node_to_delete = prev.next
            if node_to_delete == self.tail:
                self.tail = prev
            prev.next = prev.next.next

        self.length -= 1
        
    @empty_check
    def split_list_return_nodes(self):
        if self.head.next == self.head:
            return self.head
        
        slow = self.head
        fast = self.head
        while fast.next != self.head and fast.next.next != self.head:
            slow = slow.next
            fast = fast.next.next
        
        if fast.next.next == self.head:
            fast = fast.next
        
        head1 = self.head
        head2 = slow.next
        
        fast.next = slow.next
        
        slow.next = self.head
        
        return head1, head2
    
    @empty_check            
    def split_list_return_lists(self):
        if self.length == 0:
            return None, None
 
        mid = (self.length + 1) // 2

 
        first_list = CLinkedList()
        second_list = CLinkedList()
 
        current = self.head
        
        count = 0
        while count < mid:
            first_list.append(current.value)
            current = current.next
            count += 1
        
        first_list.tail.next = first_list.head

        while count < self.length:
            second_list.append(current.value)
            current = current.next
            count += 1
        
        return first_list, second_list

    @empty_check
    def is_sorted(self):
        if self.length == 1:
            return True
        
        current = self.head
        while current.next != self.head:
            if current.value > current.next.value:
                return False
            current = current.next
            
        return True

    def insert_into_sorted(self, data):
        new_node = Node(data)
        if not self.head:
            new_node.next = new_node
            self.head = new_node
            
        if self.head.data <= data:
            tail_node = self.head
            while tail_node.next != self.head:
                tail_node = tail_node.next
            
            new_node.next = self.head
            tail_node.next = new_node
            return
        
        current = self.head
        next_to_current = self.head.next
        while current.next != self.head:
            if current.data < data and next_to_current.data >= data:
                new_node.next = next_to_current
                current.next = new_node
                return
            else:
                current = current.next
                next_to_current = next_to_current.next
        
        new_node.next = self.head
        current.next = new_node
    
    @empty_check    
    def josephus_circle(self, step):
        if self.head == self.tail:
            return self.head
        
        current = self.head
        while self.length > 1:
            count = 1
            while count != step:
                current = current.next
                count += 1
            self.delete_by_value(current.value)
            current = current.next
                
        return current   
        
    def delete_all(self):
        self.head = None
        self.tail = None
        self.length = 0
