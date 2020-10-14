
class Node(object):
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None
        

class BST(object):    
    def insert(self, parent, key):
        if not parent:
            return Node(key)
        else:
            parent.left = self.insert(parent.left, key) if key < parent.data else parent.left
            parent.right = self.insert(parent.right, key) if key > parent.data else parent.right
        return parent

    def printIN(self, parent):
        if parent:
            self.printIN(parent.left)
            print("{0} ".format(parent.data), end="")
            self.printIN(parent.right)

    def printPRE(self, parent):
        if parent:
            print("{0} ".format(parent.data), end="")
            self.printIN(parent.left)
            self.printIN(parent.right)

    def printPOST(self, parent):
        if parent:
            self.printIN(parent.left)
            self.printIN(parent.right)
            print("{0} ".format(parent.data), end="")



tree_A = BST()
root = None

root = tree_A.insert(root, 5)
root = tree_A.insert(root, 8)
root = tree_A.insert(root, 30)
root = tree_A.insert(root, 12)
root = tree_A.insert(root, 27)
root = tree_A.insert(root, 1)
root = tree_A.insert(root, 7)

print("In-Order Traversal of the constructed BST:")
tree_A.printIN(root)
print()

print("Pre-Order Traversal:")
tree_A.printPRE(root)
print()

print("Post-Order Traversal:")
tree_A.printPOST(root)
print()