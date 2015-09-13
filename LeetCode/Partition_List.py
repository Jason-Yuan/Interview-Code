# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        leftDummy = ListNode(0)
        rightDummy = ListNode(0)
        left, right = leftDummy, rightDummy
        
        while head != None:
            if head.val < x:
                left.next = head
                left = left.next
            else:
                right.next = head
                right = right.next
            head = head.next
            
        left.next = rightDummy.next
        right.next = None
        
        return leftDummy.next