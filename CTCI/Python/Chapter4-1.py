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

def main():
	mytree = BST()

	mytree.insert(3)
	mytree.insert(5)
	mytree.insert(2)
	mytree.insert(7)
	mytree.insert(12)
	mytree.insert(8)

	print "Is the tree balanced? ", IsBalancedTree(mytree)

if __name__ == '__main__':
        main()	