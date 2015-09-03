# Definition for a  binary tree node
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
        
class BSTIterator(object):
    def __init__(self, root):
        self.q=[]
        while root:
            self.q.append(root)
            root=root.left

    # @return a boolean, whether we have a next smallest number
    def hasNext(self):
        if not self.q:return False
        return True

    # @return an integer, the next smallest number
    def next(self):
        cur = self.q.pop()
        node = cur.right
        while node:
            self.q.append(node)
            node=node.left
        return cur.val
        

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())