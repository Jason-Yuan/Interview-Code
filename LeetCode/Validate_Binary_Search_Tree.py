# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.helper(root)
        
    def helper(self, root, min=-float("inf"), max=float("inf")):
	    if root is None:
		    return True
	    elif root.left == None and root.right == None:
		    return root.val > min and root.val < max
	    elif root.left == None:
		    return self.helper(root.right, root.val, max) and root.val > min
	    elif root.right == None:
		    return self.helper(root.left, min, root.val) and root.val < max
	    return self.helper(root.left, min, root.val) and self.helper(root.right, root.val, max)