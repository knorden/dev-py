# PROJECT: LEARNING PYTHON BY WRITING A BST
# AUTHOR: KARL NORDEN

# Class definition:
class BSN(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BST(object):
    #def constructTree(self, r, size):
    def insert(self, root, key):
        
        if not root:
            return BSN(key)
        elif key < root.data:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

