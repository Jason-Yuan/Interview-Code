# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        maxSum, _ = self.helper(root)
        return maxSum
        
    def helper(self, root):
        if not root:
            return -sys.maxint, 0
            
        left = self.helper(root.left)
        right = self.helper(root.right)
        maxPath = max(left[0], right[0], left[1] + root.val + right[1])
        singlePath = max(left[1] + root.val, right[1] + root.val, 0)
        return maxPath, singlePath