# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {string[]}
    def binaryTreePaths(self, root):
        if not root:
            return []
        res = []
        self.helper(root, [], res)
        return res
        
    def helper(self, root, path, res):
        if root.left is None and root.right is None:
            res.append("".join(path + [str(root.val)]))
            return
        if root.left:
            self.helper(root.left, path + [str(root.val)+"->"], res)
        if root.right:
            self.helper(root.right, path + [str(root.val)+"->"], res)
        