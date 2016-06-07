# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if nums:
            return self.buildTree(nums, 0, len(nums) - 1)
        return None
        
    def buildTree(self, nums, start, end):
        if start > end:
            return None
        root = TreeNode(nums[(start + end) / 2])
        root.left = self.buildTree(nums, start, (start + end) / 2 - 1)
        root.right = self.buildTree(nums, (start + end) / 2 + 1, end)
        return root