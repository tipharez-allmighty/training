class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

    def __repr__(self):
        return f"(Value={self.value}, Next={self.next})"


class MinStack:
    def __init__(self):
        self.stack = None
        self.min_values = None

    def __repr__(self):
        return f"(Min_value={self.min_values.value if self.min_values else None}, stack={self.stack})"

    def isEmpty(self):
        return self.stack == None

    def push(self, value):
        if not self.min_values or value <= self.min_values.value:
            self.min_values = Node(value=value, next=self.min_values)
        value_to_push = Node(value=value)
        if self.isEmpty():
            self.stack = value_to_push
        else:
            value_to_push.next = self.stack
            self.stack = value_to_push

    def pop(self):
        if self.isEmpty():
            raise IndexError("Stack is Empty")
        value_to_return = self.stack.value
        if value_to_return == self.min_values.value:
            self.min_values = self.min_values.next
        if self.stack.next == None:
            self.stack = None
        else:
            self.stack = self.stack.next
        return value_to_return

    def top(self):
        if self.isEmpty():
            raise IndexError("Stack is Empty")
        return self.stack.value

    def getMin(self):
        if self.isEmpty():
            raise IndexError("Stack is Empty")
        return self.min_values.value
