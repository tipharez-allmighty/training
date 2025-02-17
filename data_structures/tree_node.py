class TreeNode:
    def __init__(self, data, children=None):
        self.data = data
        self.children = children if children is not None else []
    
    def __repr__(self, level=0):
        result = " " * level + f'{self.data}\n'
        for child in self.children:
            result += child.__repr__(level + 1)
        return result
    
    def add_child(self, node: "TreeNode"):
        if isinstance(node, TreeNode):
            self.children.append(node)
        else:
            raise TypeError('Wrong node type, only tree bodes can be added.')
