##############################################################################################################################
#      Project:                  Binary Search Tree
#      Definition:               1. Binary Tree, which means each node has two child
#                                2. Each elements(keys) are comparble
#                                3. Each elements(keys) are unique
#                                4. Left node < Parent node < Right node
###############################################################################################################################

class Node:
    """Implement a node class which has 3 attributes: leftChild, rightChild and value"""
    def __init__(self, val):
        self.value = val
        self.leftChild = None
        self.rightChild = None
        
    def insert(self, data):
        if self.value == data:
            return False
        elif data < self.value:
            if self.leftChild:
                return self.leftChild.insert(data)
            else:
                self.leftChild = Node(data)
                return True
        else: # data > self.value
            if self.rightChild:
                return self.rightChild.insert(data)
            else:
                self.rightChild = Node(data)
                return True
                
    def find(self, data):
        if(self.value == data):
            return True
        elif data < self.value:
            if self.leftChild:
                return self.leftChild.find(data)
            else:
                return False
        else: # data > self.value
            if self.rightChild:
                return self.rightChild.find(data)
            else:
                return False

    def preorder(self):
        if self:
            print (str(self.value))
            if self.leftChild:
                self.leftChild.preorder()
            if self.rightChild:
                self.rightChild.preorder()

    def postorder(self):
        if self:
            if self.leftChild:
                self.leftChild.postorder()
            if self.rightChild:
                self.rightChild.postorder()
            print (str(self.value))

    def inorder(self):
        if self:
            if self.leftChild:
                self.leftChild.inorder()
            print (str(self.value))
            if self.rightChild:
                self.rightChild.inorder()

class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root:
            return self.root.insert(data)
        else:
            self.root = Node(data)
            return True

    def find(self, data):
        if self.root:
            return self.root.find(data)
        else:
            return False
            
    def preorder(self):
        print("Pre-Order")
        self.root.preorder()
        
    def postorder(self):
        print("Post-Order")
        self.root.postorder()
            
    def inorder(self):
        print("In-Order")
        self.root.inorder()

##############################################################################################################################

def main():
    # initialize a binary search tree
    bst = BST()

    bst.insert(3)
    bst.insert(5)
    bst.insert(2)
    bst.insert(7)
    bst.insert(12)
    bst.insert(8)

    # print the tree inorder, preorder and postorder
    bst.inorder()
    bst.preorder()
    bst.postorder()

if __name__ == '__main__':
        main()	