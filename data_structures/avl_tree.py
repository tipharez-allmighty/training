from queue_linked_list import Queue
import bst_linked_list as bst

class AVLNode(bst.BSTNode):
    def __init__(self, value):
        super().__init__(value)
        self.height = 1


def getHeight(root_node: AVLNode):
    if not root_node:
        return 0
    return root_node.height

def rightRotate(disbalanced_node: AVLNode):
    new_root = disbalanced_node.left
    disbalanced_node.left = disbalanced_node.left.right
    new_root.right = disbalanced_node
    
    disbalanced_node.height = 1 + max(getHeight(disbalanced_node.left),
                                      getHeight(disbalanced_node.right))
    new_root.height = 1 + max(getHeight(new_root.left), getHeight(new_root.right))
    return new_root

def leftRotate(disbalanced_node: AVLNode):
    new_root = disbalanced_node.right
    disbalanced_node.right = disbalanced_node.right.left
    new_root.left = disbalanced_node

    disbalanced_node.height = 1 + max(getHeight(disbalanced_node.left),
                                      getHeight(disbalanced_node.right))
    new_root.height = 1 + max(getHeight(new_root.left), getHeight(new_root.right))
    return new_root

def getBalance(root_node):
    if not root_node:
        return 0
    return getHeight(root_node.left) - getHeight(root_node.right)

def insertNode(root_node: AVLNode, value):
    if not root_node:
        return AVLNode(value)
    elif value < root_node.value:
        root_node.left = insertNode(root_node.left, value)
    else:
        root_node.right = insertNode(root_node.right, value)

    root_node.height = 1 + max(getHeight(root_node.left),
                               getHeight(root_node.right))
    
    balance = getBalance(root_node)
    if balance > 1 and value < root_node.left.value:
        return rightRotate(root_node)
    if balance > 1 and value > root_node.left.value:
        root_node.left = leftRotate(root_node.left)
        return rightRotate(root_node)
    if balance < -1 and value > root_node.right.value:
        return leftRotate(root_node)
    if balance < -1 and value < root_node.right.value:
        root_node.right = rightRotate(root_node.right)
        return leftRotate(root_node)
    return root_node

def getMinValue(root_node: AVLNode):
    if not root_node or not root_node.left:
        return root_node
    return getMinValue(root_node.left)

def deleteNode(root_node, value):
    if not root_node:
        return root_node
    elif value < root_node.value:
        root_node.left = deleteNode(root_node.left, value)
    elif value > root_node.value:
        root_node.right = deleteNode(root_node.right, value)
    else:
        if not root_node.left:
            temp = root_node.right
            root_node = None
            return temp
        elif not root_node.right:
            temp = root_node.left
            root_node = None
            return temp
        temp = getMinValue(root_node.right)
        root_node.value = temp.value
        root_node.right = deleteNode(root_node.right, temp.value)
    balance = getBalance(root_node)
    if balance > 1 and getBalance(root_node.left) >= 0:
        return rightRotate(root_node)
    if balance < -1 and getBalance(root_node.right) <= 0:
        return leftRotate(root_node)
    if balance > 1 and getBalance(root_node.left) < 0:
        root_node.left = leftRotate(root_node.left)
        return rightRotate(root_node)
    if balance < -1 and getBalance(root_node.right) > 0:
        root_node.right = rightRotate(root_node.right)
        return leftRotate(root_node)
    return root_node

def deleteTree(root_node: AVLNode):
    root_node.value = None
    root_node.right = None
    root_node.left = None