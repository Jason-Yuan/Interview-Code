# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head or k == 0:
            return head
        
        # find the tail
        tail = head
        len = 1
        while tail.next != None:
            tail = tail.next
            len += 1
        if k % len == 0:
            return head
            
        # find the rotate place
        slow = fast = head
        for i in range(k % len):
            fast = fast.next
        while fast.next != None:
            fast = fast.next
            slow = slow.next
            
        tail.next = head
        head = slow.next
        slow.next = None
        return head