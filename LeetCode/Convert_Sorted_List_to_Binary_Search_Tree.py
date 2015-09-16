# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.current = None
        
    def getListLength(self, head):
        size = 0
        while head:
            size += 1
            head = head.next
        return size
        
    def sortedListToBSTHelper(self, size):
        if size <= 0:
            return None

        left = self.sortedListToBSTHelper(size / 2)
        root = TreeNode(self.current.val)
        self.current = self.current.next
        right = self.sortedListToBSTHelper(size - 1 - size / 2)

        root.left = left
        root.right = right

        return root
        
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        self.current = head
        size = self.getListLength(head)

        return self.sortedListToBSTHelper(size)