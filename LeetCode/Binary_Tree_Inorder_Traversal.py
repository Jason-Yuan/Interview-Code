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
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack = Stack()
        result = []
        current = root
        while current != None or stack.size() != 0:
            # push all the left node in to stack start from root
            while current != None:
                stack.push(current)
                current = current.left
            current = stack.pop();
            result.append(current.val);
            current = current.right;
        return result


# Method 2 Traverse
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ret = []
        self.RecInOrderTraversal(root, ret)
        return ret
        
    def RecInOrderTraversal(self, root, result):
        if root != None: # skip None or Leaf
            self.RecInOrderTraversal(root.left, result)
            result.append(root.val)
            self.RecInOrderTraversal(root.right, result)


# Method 3 Divide & Conquer
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        if root == None:
            return result
        result.append(root.val)
        
        # divide
        left = self.inorderTraversal(root.left)
        right = self.inorderTraversal(root.right)
        
        # conquer
        return left + result + right