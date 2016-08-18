# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        res = []
        if not root:
            return res
        self.helper(root, [], 0, sum, res)
        return res
        
    def helper(self, root, path, subSum, sum, res):
        if root.left == None and root.right == None:
            if subSum + root.val == sum:
                res.append(path + [root.val])
        if root.left:
            self.helper(root.left, path + [root.val], subSum + root.val, sum, res)
        if root.right:
            self.helper(root.right, path + [root.val], subSum + root.val, sum, res)