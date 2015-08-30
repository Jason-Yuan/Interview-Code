# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Method 1 Iteratively
class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)
        
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack = Stack()
        result = []
        if root == None:
            return result
        else:
            stack.push(root)
            while stack.size() != 0:
                parent = stack.pop()
                result.append(parent.val)
                if parent.right:
                    stack.push(parent.right)
                if parent.left:
                    stack.push(parent.left)
        return result


# Method 2 Traverse
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ret = []
        self.RecPreOrderTraversal(root, ret)
        return ret
        
    def RecPreOrderTraversal(self, root, result):
        if root != None: # skip None or Leaf
            result.append(root.val)
            self.RecPreOrderTraversal(root.left, result)
            self.RecPreOrderTraversal(root.right, result)


# Method 3 Divide & Conquer
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        if root == None:
            return result
        result.append(root.val)
        
        # divide
        left = self.preorderTraversal(root.left)
        right = self.preorderTraversal(root.right)
        
        # conquer
        return result + left + right