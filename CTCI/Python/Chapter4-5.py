# import the dependent packages
import sys
sys.path.append('../../Tree and Tree Algorithm')
from BST import *

##############################################################################################################################
# Method 1
# Ideas: Check if it is valid recursively, min < left < node < right < max
# Time Complexity: O(n)
# Space Complexity: O(logn)
##############################################################################################################################

def isBST1(root, min=-float("inf"), max=float("inf")):
	if root is None:
		return True
	elif root.leftChild == None and root.rightChild == None:
		return root.value > min and root.value < max
	elif root.leftChild == None:
		return isBST1(root.rightChild, root.value, max) and root.value > min
	elif root.rightChild == None:
		return isBST1(root.leftChild, min, root.value) and root.value < max
	return isBST1(root.leftChild, min, root.value) and isBST1(root.rightChild, root.value, max)

##############################################################################################################################
# Method 2
# Ideas: Convert the binary tree to a array, check if the array is accending order
# Time Complexity: O(n)
# Space Complexity: O(n)
##############################################################################################################################

def isBST2(root):
	res = []
	inOrderToArray(root, res)
	for i in range(1, len(res)):
		if res[i-1] > res[i]:
			return False
	return True

def inOrderToArray(node, array):
	if node:
		if node.leftChild:
			inOrderToArray(node.leftChild, array)
		array.append(node.value)
		if node.rightChild:
			inOrderToArray(node.rightChild, array)

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

    print isBST1(bst.root)
    print isBST2(bst.root)

if __name__ == '__main__':
	main()