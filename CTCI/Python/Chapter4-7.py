# import the dependent packages
import sys
sys.path.append('../../Tree and Tree Algorithm')
from BST import *

##############################################################################################################################
# Ideas:  Check if two node has commom ancestor, if not check their parrent recursively
# Time Complexity: O(n2)
# Space Complexity: O(logn)
##############################################################################################################################

def findLCA(p, q, root):
	if root == None:
		return None
	if p == root.value or q == root.value:
		return root

	left = findLCA(p, q, root.leftChild)
	right = findLCA(p, q, root.rightChild)
	if left and right:
		return root
	elif left:
		return left
	else:
		return right

##############################################################################################################################

def main():
    # initialize a binary search tree
    bst = BST()

    bst.insert(7)
    bst.insert(3)
    bst.insert(8)
    bst.insert(5)
    bst.insert(2)
    bst.insert(12)

    # the tree is like 
    #         7
    #        / \
    #       3   8
    #      / \  /
    #     2  5 12

    print "LCA of 2 and 12 is: ", findLCA(2, 12, bst.root).value
    print "LCA of 2 and 5 is: ", findLCA(2, 5, bst.root).value

if __name__ == '__main__':
	main()