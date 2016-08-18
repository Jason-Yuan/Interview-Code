# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False
        if self.helper(root, 0, sum) == True:
            return True
        return False
        
    def helper(self, root, subSum, sum):
        if root.left == None and root.right == None:
            if subSum + root.val == sum:
                return True
        if root.left and self.helper(root.left, subSum + root.val, sum):
            return True
        if root.right and self.helper(root.right, subSum + root.val, sum):
            return True