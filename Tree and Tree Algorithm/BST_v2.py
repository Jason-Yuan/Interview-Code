##############################################################################################################################
#      Project:                  Binary Search Tree
#      Definition:               1. Binary Tree, which means each node has two child
#                                2. Each elements(keys) are comparble
#                                3. Each elements(keys) are unique
#                                4. Left node < Parent node < Right node
###############################################################################################################################

class Node:
    """A Tree Node with 3 attributes: leftChild, rightChild and value"""
    def __init__(self):
        self.value = None
        self.leftChild = None
        self.rightChild = None

class BST(object):
    """Implement a Binary Search Tree class"""
    def __init__(self):
        self.root = Node()

    def insertRecur(self, node, value):
        if node.value is None:
            node.value = value
        elif value < node.value:
            node.leftChild = node.leftChild or Node()
            self.insertRecur(node.leftChild, value)
        else:
            node.rightChild = node.rightChild or Node()
            self.insertRecur(node.rightChild, value)

    def find(self, node, value):
        if node is None:
            return False
        elif node.value == value:
            return True
        elif value < node.value:
            return self.find(node.leftChild, value)
        else:
            return self.find(node.rightChild, value)

    def inOrderRecur(self, node):
        if node:
            self.inOrderRecur(node.leftChild)
            print str(node.value)
            self.inOrderRecur(node.rightChild)

    def preOrderRecur(self, node):
        if node:
            print str(node.value)
            self.preOrderRecur(node.leftChild)
            self.preOrderRecur(node.rightChild)  

    def postOrderRecur(self, node):
        if node:
            self.postOrderRecur(node.leftChild)
            self.postOrderRecur(node.rightChild) 
            print str(node.value)   

    def Insert(self, value):
        self.insertRecur(self.root, value)

    def Find(self, value):
        return self.find(self.root, value)

    def InOrder(self):
        print "In-Order"
        self.inOrderRecur(self.root)

    def PreOrder(self):
        print "Pre-Order"
        self.preOrderRecur(self.root)

    def PostOrder(self):
        print "Post-Order"
        self.postOrderRecur(self.root)

##############################################################################################################################

def main():
    # initialize a binary search tree
    bst = BST()

    bst.Insert(3)
    bst.Insert(5)
    bst.Insert(2)
    bst.Insert(7)
    bst.Insert(12)
    bst.Insert(8)

    # print the tree inorder, preorder and postorder
    bst.InOrder()
    bst.PreOrder()
    bst.PostOrder()
    print "Dose 7 exist in the tree? ", bst.Find(7)
    print "Dose 8 exist in the tree? ", bst.Find(8)
    print "Dose 5 exist in the tree? ", bst.Find(5)
    print "Dose 2 exist in the tree? ", bst.Find(2)
    print "Dose 100 exist in the tree? ", bst.Find(100)

if __name__ == '__main__':
        main()  