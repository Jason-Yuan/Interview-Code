##############################################################################################################################
# Ideas: Two Cases:   1. if the node has right child => in the right sub tree, find the left most child
#                     2. else, find its parent, notice!!! the current node should be the left child of 
#                        its parent, otherwise keep finding ancestors
# Time Complexity: O(logn)
# Space Complexity: O(1)
##############################################################################################################################

def inOrderNext(node):
	if node.rightChild is not None:
		res = node.rightChild
		while res.leftChild is not None:
			res = res.leftChild
		return res
	else:
		# this problem assume there is a link to the current node parent
		res = node.parent
		while res is not None:
			if res.leftChild == node:
				break
			else:
				node = res
				res = node.parent
		return res