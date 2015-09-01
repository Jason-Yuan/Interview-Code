# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def peek(self):
        return self.items[-1]
        
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        result = [[root.val]]
        
        queue = Queue()
        queue.enqueue(root)
        flag = False
        while not queue.isEmpty():
            temp = []
            size = queue.size()
            for i in range(size):
                current = queue.dequeue()
                if current.left != None:
                    if flag:
                        temp.append(current.left.val)
                    else:
                        temp.insert(0, current.left.val)
                    queue.enqueue(current.left)
                if current.right != None:
                    if flag:
                        temp.append(current.right.val)
                    else:
                        temp.insert(0, current.right.val)
                    queue.enqueue(current.right)
            flag = not flag
            if temp != []:
                result.append(temp)
                
        return result