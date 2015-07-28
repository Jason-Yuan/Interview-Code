# import the dependent packages
import sys
sys.path.append('../../Tree and Tree Algorithm')
from BST import *

##############################################################################################################################
# Ideas: Rrecursively iterate each node of the tree and calculate the max height/ min height 
# Time Complexity: O(n)
# Space Complexity: O(h) (h is height of tree)
##############################################################################################################################

def IsBalancedTree(tree):
	return (MaxDepth(tree.root) - MinDepth(tree.root) <= 1)

def MaxDepth(node):
	if node is None:
		return 0
	else:
		return (1 + max(MaxDepth(node.leftChild), MaxDepth(node.rightChild)))

def MinDepth(node):
	if node is None:
		return 0
	else:
		return (1 + min(MinDepth(node.leftChild), MinDepth(node.rightChild)))

##############################################################################################################################

def mian():
	mytree = BST()

	bst.insert(3)
	bst.insert(5)
	bst.insert(2)
	bst.insert(7)
	bst.insert(12)
	bst.insert(8)

	print "Is the tree balanced? ", IsBalancedTree(bst)

if __name__ == '__main__':
        main()	