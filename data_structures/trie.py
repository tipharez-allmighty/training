class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_of_string = False
    
    def __repr__(self):
        return f'{self.children}, {self.end_of_string}'
    
    def __bool__(self):
        return bool(self.children)

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word: str):
        current = self.root
        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]
        current.end_of_string = True
    
    def search(self, word):
        current = self.root
        for char in word:
            if char not in current.children:
                return False
            current = current.children[char]
        return current.end_of_string

def deleteString(root: TrieNode, word, index=0):
    char = word[index]
    current_node = root.children.get(char)
    delete = False
    if len(current_node.children) > 1:
        deleteString(current_node, word, index + 1)
        return False
    if index == len(word) - 1:
        if len(current_node.children) >= 1:
            current_node.end_of_string = False
            return False
        else:
            root.children.pop(char)
            return True
    if current_node.end_of_string == True:
        deleteString(current_node, word, index + 1)
        return False
    delete = deleteString(current_node, word, index + 1)
    if delete is True:
        root.children.pop(char)
        return True
    else:
        return False
