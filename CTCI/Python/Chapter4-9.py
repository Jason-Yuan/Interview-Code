# import the dependent packages
import sys
sys.path.append('../../Tree and Tree Algorithm')
from BST import *

##############################################################################################################################
# Ideas:  Check if two node has commom ancestor, if not check their parrent recursively
# Time Complexity: O(nlogn)
# Space Complexity: O(h)
##############################################################################################################################

def findPath(root, target, path=None, depth=0):
	if root == None:
		return
	if path == None:
		path = []

	if len(path) > depth:
		path[depth] = root.value
	else:
		path.append(root.value)

	temp = 0
	for i in range(depth, -1, -1):
		temp += path[i]
		if temp == target:
			printPath(path, i, depth)
	findPath(root.leftChild, target, path, depth+1)
	findPath(root.rightChild, target, path, depth+1)


def printPath(path, s, e):
	for i in range(s, e+1):
		print path[i],
	print ""

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

    findPath(bst1.root, 8)

if __name__ == '__main__':
	main()