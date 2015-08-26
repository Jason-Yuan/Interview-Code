# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {TreeNode}
    def invertTree(self, root):
        if root == None:
            return 
        queue = [root]
        while len(queue) != 0:
            current = queue.pop()
            # swap the leftchild and rightchild
            current.left, current.right = current.right, current.left
            if current.left:
                queue.insert(0, current.left)
            if current.right:
                queue.insert(0, current.right)
        return root