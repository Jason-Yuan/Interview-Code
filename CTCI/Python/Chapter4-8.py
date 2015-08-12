# import the dependent packages
import sys
sys.path.append('../../Tree and Tree Algorithm')
from BST import *

##############################################################################################################################
# Ideas:  Check if two node has commom ancestor, if not check their parrent recursively
# Time Complexity: O(n2)
# Space Complexity: O(logn)
##############################################################################################################################

def isSubtree(root1, root2):
	if root2 == None:
		return True
	elif root1 == None:
		return False
	elif root1.value == root2.value:
		if isTreeIdentical(root1, root2):
			return True
	else:
		return isSubtree(root1.leftChild, root2) or isSubtree(root1.rightChild, root2)

def isTreeIdentical(root1, root2):
	if root1 == root2 == None:
		return True
	elif root1.value == root2.value:
		return isTreeIdentical(root1.leftChild, root2.leftChild) and isTreeIdentical(root1.rightChild, root2.rightChild)
	else:
		return False

##############################################################################################################################

def main():
    # initialize a binary search tree
    bst1 = BST()
    bst1.insert(7)
    bst1.insert(3)
    bst1.insert(8)
    bst1.insert(5)
    bst1.insert(2)
    bst1.insert(12)

    # the tree is like 
    #         7
    #        / \
    #       3   8
    #      / \  /
    #     2  5 12

    bst2 = BST()
    bst2.insert(3)
    bst2.insert(2)
    bst2.insert(5)

    # the tree is like 
    #       3   
    #      / \  
    #     2   5 

    bst3 = BST()
    bst3.insert(3)
    bst3.insert(1)
    bst3.insert(9)

    print "is tree2 a subtree of tree1? ", isSubtree(bst1.root, bst2.root)
    print "is tree3 a subtree of tree1? ", isSubtree(bst1.root, bst3.root)

if __name__ == '__main__':
	main()