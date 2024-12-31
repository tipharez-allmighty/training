class Node:
    def __init__(self, key):
        self.key = key
        self.next = None

    def __repr__(self):
        return f"Node(key={self.key}, next={self.next})"


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __repr__(self):
        temp_node = self.head
        result = ""

        while temp_node is not None:
            result += str(temp_node.key)

            if temp_node.next is not None:
                result += " -> "

            temp_node = temp_node.next

        return f"LinkedList({result}, length={self.length})"

    def traverse(self):
        current = self.head
        
        while current is not None:
            current = current.next
    
    def search(self, value):
        current = self.head
        index = 0
        while current is not None:
            if current.key == value:
                return current, index
            current = current.next
            index +=1

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
                for i in range(index - 1):
                    temp_node = temp_node.next

                new_node.next = temp_node.next
                temp_node.next = new_node

        self.length += 1
