from typing import Any
from queue_linked_list import Queue

class TreeNode:
    def __init__(self, value: Any):
        self.value = value
        self.left: "TreeNode" | None  = None
        self.right: "TreeNode" | None = None
    
    def __repr__(self):
        return (f'left={self.left.value if self.left else None} <- value={self.value} ->'
                f'right={self.right.value if self.right else None}')

new_node = TreeNode(1)
new_node.left = TreeNode(2)
new_node.left.left = TreeNode(4)
new_node.left.right = TreeNode(5)
new_node.right = TreeNode(3)
new_node.right.left = TreeNode(6)
new_node.right.right = TreeNode(7)

def preOrderTraversal_rec(rootNode: TreeNode):
    if not rootNode:
        return
    print(rootNode)
    preOrderTraversal_rec(rootNode.left)
    preOrderTraversal_rec(rootNode.right)

def preOrderTraversal_iter(rootNode: TreeNode):
    stack = [rootNode]
    while stack:
        current_node = stack.pop()
        print(current_node)
        if current_node.right:
            stack.append(current_node.right)
        if current_node.left:
            stack.append(current_node.left)

def inOrderTraversal_rec(rootNode: TreeNode):
    if not rootNode:
        return
    inOrderTraversal_rec(rootNode.left)
    print(rootNode)
    inOrderTraversal_rec(rootNode.right)

def inOrderTraversal_iter(rootNode: TreeNode):
    stack = []
    current = rootNode
    while stack or current:
        while current:
            stack.append(current)
            current = current.left
        current = stack.pop()
        print(current)
        current = current.right

def postOrderTraversal_rec(rootNode: TreeNode):
    if not rootNode:
        return
    postOrderTraversal_rec(rootNode=rootNode.left)
    postOrderTraversal_rec(rootNode=rootNode.right)
    print(rootNode)

def postOrderTraversal_iter(rootNode: TreeNode):
    stack = [rootNode]
    output = []
    while stack:
        current = stack.pop()
        output.append(current)
        if current.left:
            stack.append(current.left)
        if current.right:
            stack.append(current.right)
    while output:
        print(output.pop())

def LevelOrderTraversal(rootNode: TreeNode):
    queue = Queue()
    queue.enqueue(rootNode)
    while not queue.isEmpty():
        current = queue.dequeue()
        print(current)
        if current.left:
            queue.enqueue(current.left)
        if current.right:
            queue.enqueue(current.right)

def search_by_value(rootNode: TreeNode, value):
    queue = Queue()
    queue.enqueue(rootNode)
    while not queue.isEmpty():
        current = queue.dequeue()
        if current.value == value:
            return current
        if current.left:
            queue.enqueue(current.left)
        if current.right:
            queue.enqueue(current.right)

def insert_node(rootNode: TreeNode, new_node: TreeNode):
    if rootNode.value is None:
        rootNode = new_node
        return
    
    queue = Queue()
    queue.enqueue(rootNode)
    while not queue.isEmpty():
        current = queue.dequeue()
        if current.left:
            queue.enqueue(current.left)
        else:
            current.left = new_node
            return rootNode
        if current.right:
            queue.enqueue(current.right)
        else:
            current.right = new_node
            return rootNode
    
def find_deepest_node(rootNode: TreeNode):
    queue = Queue()
    queue.enqueue(rootNode)
    while not queue.isEmpty():
        current = queue.dequeue()
        if current.left:
            queue.enqueue(current.left)
        if current.right:
            queue.enqueue(current.right)
    return current.value

def delete_deepest_node(rootNode: TreeNode, deepest_node_value):
    queue = Queue()
    queue.enqueue(rootNode)
    while not queue.isEmpty():
        current = queue.dequeue()
        if current.left:
            queue.enqueue(current.left)
            if current.left.value == deepest_node_value:
                current.left = None
                return rootNode
        if current.right:
            queue.enqueue(current.right)
            if current.right.value == deepest_node_value:
                current.right = None
                return rootNode
    return rootNode

def delete_node(rootNode: TreeNode, value):
    if not rootNode:
        raise IndexError('The tree is empty')
    deepest_node_value = find_deepest_node(rootNode=rootNode)
    delete_deepest_node(rootNode=rootNode,deepest_node_value=deepest_node_value)
    queue = Queue()
    queue.enqueue(rootNode)
    while not queue.isEmpty():
        current = queue.dequeue()
        if current.left:
            queue.enqueue(current.left)
            if current.left.value == value:
                current.left.value = deepest_node_value
                return rootNode
        if current.right:
            queue.enqueue(current.right)
            if current.right.value == value:
                current.right.value = deepest_node_value
                return rootNode
    return rootNode  
    
def delete_tree(root_node: TreeNode):
    root_node.left = None
    root_node.right = None
    root_node.value = None
    return root_node
