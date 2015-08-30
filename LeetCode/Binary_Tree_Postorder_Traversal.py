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
        prev = None
        current = root
        
        if root == None:
            return result
            
        stack.push(root)
        while stack.size() != 0:
            current = stack.peek();
            if prev == None or prev.left == current or prev.right == current: # traverse down the tree
                if current.left != None:
                    stack.push(current.left)
                elif current.right != None:
                    stack.push(current.right)
            elif current.left == prev: # traverse up the tree from the left
                if current.right != None:
                    stack.push(current.right)
            else: # traverse up the tree from the right
                result.append(current.val)
                stack.pop()
            prev = current

        return result


# Method 2 Traverse
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ret = []
        self.RecPostOrderTraversal(root, ret)
        return ret
        
    def RecPostOrderTraversal(self, root, result):
        if root != None: # skip None or Leaf
            self.RecPostOrderTraversal(root.left, result)
            self.RecPostOrderTraversal(root.right, result)
            result.append(root.val)


# Method 3 Divide & Conquer
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        if root == None:
            return result
        result.append(root.val)
        
        # divide
        left = self.postorderTraversal(root.left)
        right = self.postorderTraversal(root.right)
        
        # conquer
        return left + right + result