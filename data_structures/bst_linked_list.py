from queue_linked_list import Queue

class BSTNode:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None
    
    def __repr__(self, level=0, prefix="Root: "):
        ret = " " * (level * 4) + prefix + str(self.value) + "\n"
        if self.left:
            ret += self.left.__repr__(level + 1, "L--- ")
        if self.right:
            ret += self.right.__repr__(level + 1, "R--- ")
        return ret

def insertNode_rec(root_node, value):
    if root_node.value == None:
        root_node.value = value
    elif value <= root_node.value:
        if root_node.left is None:
            root_node.left = BSTNode(value)
        else:
            insertNode_rec(root_node.left, value)
    else:
        if root_node.right is None:
            root_node.right = BSTNode(value)
        else:
            insertNode_rec(root_node.right, value)

def insertNode_iter(root_node, value):
    if root_node.value == None:
        root_node.value = value
        return
    
    current = root_node
    while True:
        if value <= current.value:
            if current.left is None:
                current.left = BSTNode(value)
                break
            else:
                current = current.left
        else:
            if current.right is None:
                current.right = BSTNode(value)
                break
            else:
                current = current.right        

def inOrderTraversal(root_node: BSTNode):
    if root_node is None:
        return None
    inOrderTraversal(root_node.left)
    print(root_node)
    inOrderTraversal(root_node.right)

def LevelOrderTraversal(rootNode: BSTNode):
    queue = Queue()
    queue.enqueue(rootNode)
    while not queue.isEmpty():
        current = queue.dequeue()
        print(current)
        if current.left:
            queue.enqueue(current.left)
        if current.right:
            queue.enqueue(current.right)

def searchNode_rec(root_node: BSTNode, value):
    if root_node == None:
        return None
    elif root_node.value == value:
        return root_node
    elif value < root_node.value:
        return searchNode_rec(root_node.left, value)
    else:
        return searchNode_rec(root_node.right, value)

def searchNode_iter(root_node: BSTNode, value):
    if root_node.value == None:
        return None    
    current = root_node
    while current:
        if value == current.value:
            return current
        elif value < current.value:
            current = current.left
        else:
            current = current.right
    return current

def minValue(rootNode: BSTNode):
    current = rootNode
    while current.left:
        current = current.left
    return current

def deleteNode(root_node: BSTNode, value):
    if root_node == None:
        return None
    if value < root_node.value:
        root_node.left = deleteNode(root_node.left, value)
    elif value > root_node.value:
        root_node.right = deleteNode(root_node.right, value)
    else:
        if root_node.left is None:
            temp = root_node.right
            root_node = None
            return temp
        if root_node.right is None:
            temp = root_node.left
            root_node = None
            return temp
        
        temp = minValue(root_node.right)
        root_node.value = temp.value
        root_node.right = deleteNode(root_node.right, temp.value)

def deleteNode_iter(root_node: BSTNode, value):
    parent = None
    current = root_node
    
    while current and current.value != value:
        parent = current
        if value < current.value:
            current = current.left
        else:
            current = current.right
    
    if not current:
        return None
    
    if not current.right and not current.left:
        if not parent:
            root_node = None
        if parent.left == current:
            parent.left = None
        else:
            parent.right = None
    
    elif not current.left or not current.right:
        child = current.left if current.left else current.right
        if not parent:
            root_node = child
            return
        else:
            if parent.left == current:
                parent.left = child
                return
            else:
                parent.right = child
                return
    
    else:
        min_node_parent = current
        min_node = current.right
        while min_node.left:
            min_node_parent = min_node
            min_node = min_node.left
            
        current.value = min_node.value
        if min_node.right:
            min_node_parent.left = min_node.right
        else:
            min_node_parent.left = None
        
def deleteBST(root_node: BSTNode):
    root_node.value = None
    root_node.left = None
    root_node.right = None
