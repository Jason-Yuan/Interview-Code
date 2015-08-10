##############################################################################################################################
# Ideas: Rrecursively choose the middle num in the array as root and choose root for leftchild and rightchild
# Time Complexity: O(n)
# Space Complexity: O(n)
##############################################################################################################################

class Node:
    """Implement a node class which has 3 attributes: leftChild, rightChild and value"""
    def __init__(self, val):
        self.value = val
        self.leftChild = None
        self.rightChild = None

    def inorder(self):
    	if self:
    		if self.leftChild:
    			self.leftChild.inorder()
    		print (str(self.value))
    		if self.rightChild:
    			self.rightChild.inorder()

def arrayToBinaryTree(L):
	if len(L) == 0:
		return None

	if len(L) == 1:
		return Node(L[0])

	mid = len(L) / 2
	root = Node(L[mid])
	root.leftChild = arrayToBinaryTree(L[:mid])
	root.rightChild = arrayToBinaryTree(L[mid+1:])

	return root

##############################################################################################################################

def main():
	array = [1, 2, 3, 4, 5, 6, 7, 8, 9]

	BTree = arrayToBinaryTree(array)

	BTree.inorder()

if __name__ == '__main__':
	main()